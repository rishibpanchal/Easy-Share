This is a small Flask-based file/text sharing app that creates short room codes where users can upload files and share text snippets.

Quick facts
- Minimal Flask app in `app.py`.
- Static assets in `static/` and templates in `templates/`.
- Runtime storage (uploads, texts) is kept out of the repo and listed in `.gitignore`.

Setup

1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

Run locally

```powershell
# Set a port if desired; set FLASK_DEBUG=1 to enable debug mode
$env:PORT=5000; $env:FLASK_DEBUG=1; python app.py
```

Notes for GitHub
- The `uploads/` and `texts/` folders are runtime storage — they are ignored by `.gitignore` to avoid committing user data.
- A `.gitkeep` placeholder is added so the directories exist in the repo if needed.

Recommended next steps
- Add a license if you want to open-source the project.
- Add a small `Procfile` or Dockerfile if deploying to a platform.
