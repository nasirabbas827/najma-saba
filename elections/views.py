from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from .forms import Voterform
from django.contrib.auth import login, logout
from django.contrib import messages 
from .forms import Voterchangeform
from .models import Election


def home(request):
    return render(request, 'dashboard.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = Voterform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = Voterform()
    return render(request, 'signup.html', {'form': form})




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = Voterchangeform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  
    else:
        form = Voterchangeform(instance=request.user)
    
    return render(request, 'update_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})

@login_required
def view_elections(request):
    elections = Election.objects.all()
    return render(request, 'view_elections.html', {'elections': elections})

from django.shortcuts import render, get_object_or_404
from .models import Candidate

def view_candidates(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    candidates = Candidate.objects.filter(election=election)
    return render(request, 'view_candidates.html', {'candidates': candidates, 'election': election})


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Vote
from .blockchain import Blockchain, Block
import time


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Election, Candidate, Vote
from .blockchain import Block, Blockchain  # Assuming you have a blockchain module

@login_required
def cast_vote(request, election_id, candidate_id):
    election = get_object_or_404(Election, pk=election_id)
    candidate = get_object_or_404(Candidate, pk=candidate_id)

    # Check if the election is ongoing
    if election.status != 'ongoing':
        return HttpResponse("Voting is not allowed. The election is not currently ongoing.")

    # Check if the user has already voted in this election
    if Vote.objects.filter(user=request.user, election=election).exists():
        return HttpResponse("You have already voted in this election.")  # Simple HttpResponse for already voted case

    # Get the latest vote in the same election to determine the previous hash
    latest_vote = Vote.objects.filter(election=election).order_by('-id').first()
    previous_hash = latest_vote.block_hash if latest_vote else None

    # Generate a new block for each vote and update the block hash
    block_data = f"{request.user.username}{candidate.name}{election.name}"
    new_block = Block(len(Blockchain().chain), previous_hash, int(time.time()), block_data)
    new_block.mine_block(Blockchain().difficulty)
    block_hash = new_block.hash

    # Save the vote
    new_vote = Vote.objects.create(user=request.user, election=election, candidate=candidate, block_hash=block_hash, previous_hash=previous_hash)

    # Include blockchain information in the response
    response_message = f"Your vote has been cast successfully. The block hash for your vote is: {block_hash}"
    return HttpResponse(response_message)


from django.shortcuts import render
from django.http import HttpResponse
from .models import Election, Candidate, Vote
from collections import Counter

def election_results(request):
    # Get all completed elections
    completed_elections = Election.objects.filter(status='completed')

    if not completed_elections:
        return HttpResponse("No completed elections to show results.")

    election_results_data = []

    for election in completed_elections:
        candidates = Candidate.objects.filter(election=election)
        votes = Vote.objects.filter(election=election)

        # Count votes for each candidate
        candidate_votes = Counter(vote.candidate for vote in votes)

        # Prepare data for rendering
        election_data = {
            'election': election,
            'candidates': candidates,
            'results': candidate_votes.most_common(),  # List of (candidate, vote_count) tuples
        }

        election_results_data.append(election_data)

    return render(request, 'election_results.html', {'election_results_data': election_results_data})
