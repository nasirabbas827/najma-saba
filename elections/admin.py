from django.contrib import admin
from .models import Election, Candidate , Vote

class VoteAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'candidate', 'election', 'block_hash' , 'previous_hash')

# Register your models with the custom admin class
admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote, VoteAdmin)
