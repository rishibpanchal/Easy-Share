# FileShare — Minimal Flask file & text sharing

FileShare is a small, single-file Flask application that creates short room codes so users can upload files and share text snippets within short-lived rooms. It is intentionally lightweight and suitable for quick demos, local sharing, or as a starting point for a more feature-rich service.

**Key features**
- Simple room-based sharing with short room codes
- File uploads stored in `uploads/` (runtime storage)
- Plain-text snippets stored in `texts/` (runtime storage)
- Minimal dependencies and single-file entrypoint (`app.py`)

Prerequisites
- Python 3.10+ recommended
- Git (optional, for cloning)

Quickstart (Windows / PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app (development):

```powershell
# Optional: set a port and enable Flask debug mode for development
$env:PORT=5000; $env:FLASK_DEBUG=1; python app.py
```

Configuration
- `PORT` — port number used by the server (default: 5000 if not set)
- `FLASK_DEBUG` — set to `1` to enable Flask debug mode in development

Project layout

- `app.py` — Flask application entrypoint
- `config.py` — configuration helpers (if present)
- `templates/` — Jinja2 templates (`index.html`, `room.html`)
- `static/` — static assets such as `style.css`
- `uploads/` — runtime file storage (ignored by git)
- `texts/` — runtime text snippet storage (ignored by git)

Notes about runtime storage
- The `uploads/` and `texts/` directories are intended for runtime data and are excluded from version control via `.gitignore`. A `.gitkeep` file may be present to ensure the directories exist in the repo.

Security & privacy
- This project is a simple demo and does not include production-grade security measures (authentication, access controls, virus scanning, rate limiting). Do not deploy publicly without adding proper safeguards.

Deployment suggestions
- For staging/production consider a WSGI server (e.g. Gunicorn or Waitress on Windows) and a reverse proxy.
- Use persistent storage (S3, disk volume) for uploads if you need durability.
- Add HTTPS, authentication, and rate limiting before exposing to the public internet.

Contributing
- Contributions are welcome. Open an issue or a pull request with a clear description of the change.

Suggested next steps
- Add a license file (e.g., `MIT` or `Apache-2.0`) if you intend to open-source the project.
- Add a `Procfile` or `Dockerfile` for simple deployment workflows.
- Add basic tests or CI for linting and formatting.

License
- Add a `LICENSE` file to indicate the project's license. No license is included by default.

If you'd like, I can also add a `LICENSE`, a small `Procfile`/`Dockerfile`, or commit these changes for you.
