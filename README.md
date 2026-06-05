# najma-saba_final  

**Electronic Voting System** – A Django‑based web application that enables secure, tamper‑proof elections using a lightweight blockchain implementation.

---

## Overview  

`najma-saba_final` is a prototype electronic voting platform built with Python/Django. It demonstrates how a blockchain can be leveraged to store votes immutably while providing a familiar web interface for administrators, candidates, and voters. The project includes:

* A full Django project (`Electronic_Voting_system`) with configured ASGI/WSGI entry points.  
* An `elections` app that contains the core voting logic, models, forms, admin integration, and a simple blockchain implementation (`elections/blockchain.py`).  
* Sample assets (e.g., candidate images) and migration scripts to set up the database schema.  

The repository is intended for educational purposes and as a starting point for more robust, production‑ready voting solutions.

---

## Features  

| ✅ | Feature |
|---|---------|
| **Secure voting** | Votes are recorded on a custom blockchain, making them cryptographically linked and resistant to tampering. |
| **Admin dashboard** | Django admin interface to manage candidates, voters, and view the blockchain ledger. |
| **Candidate management** | CRUD operations for candidate profiles, including image uploads (`candidates/bl.jpg`). |
| **Voter authentication** | Simple voter model with profile linking; can be extended with real authentication mechanisms. |
| **Blockchain explorer** | View each block’s hash, previous hash, timestamp, and stored vote data via the web UI. |
| **REST‑ready** | ASGI/WSGI configuration ready for deployment behind servers such as Daphne, Uvicorn, or Gunicorn. |
| **Extensible architecture** | Clear separation between Django app (`elections`) and blockchain logic, making future enhancements straightforward. |

---

## Tech Stack  

| Layer | Technology |
|-------|------------|
| **Language** | Python 3.9+ |
| **Web Framework** | Django 4.x (ASGI & WSGI support) |
| **Database** | SQLite (default) – can be swapped for PostgreSQL, MySQL, etc. |
| **Blockchain** | Custom Python implementation (`elections/blockchain.py`) |
| **Front‑end** | Django templates + Bootstrap (optional) |
| **IDE** | VS Code (settings stored in `.vscode/settings.json`) |
| **Version Control** | Git (GitHub) |

---

## Installation  

> **Prerequisite:** Python 3.9 or newer installed on your system.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/najma-saba_final.git
cd najma-saba_final

# 2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt   # If a requirements file is not present, install Django manually:
pip install Django==4.*

# 4️⃣ Apply database migrations
python manage.py migrate

# 5️⃣ (Optional) Create a