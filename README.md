# Flask wrapper for template/index.html

This small Flask app serves `template/index.html` and saves POSTed form submissions into `submissions.xlsx` in the project root.

Requirements
- Python 3.9+
- Install dependencies from `requirements.txt` (example for PowerShell shown below)

Quick start (PowerShell)

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/ in your browser. The form in `template/index.html` posts to `login.php` by default; this app adds a route at `/submit` and will save fields `username` and `password` to `submissions.xlsx`.

Notes
- I changed the form action in runtime by providing a route `/submit`. To have the form post to `/submit`, either edit `template/index.html` to set `action="/submit"` or use the browser developer tools to submit manually.
- For privacy/security: passwords are stored in plain text in the Excel file. Use only for testing.
