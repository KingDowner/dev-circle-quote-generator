# The Dev Circle — Random Quote Generator

Our first collaborative coding project! Build a small web app that shows a random quote whenever someone presses a button.

## Tech stack
- HTML for structure
- CSS for styling
- JavaScript for fetching and displaying quotes
- Python + Flask for the quote API

## Run locally

1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create a virtual environment: `python -m venv .venv`
4. Activate it: macOS/Linux `source .venv/bin/activate`; Windows PowerShell `.venv\Scripts\Activate.ps1`
5. Install dependencies: `python -m pip install -r requirements.txt`
6. Run: `python app.py`
7. Open http://127.0.0.1:5000 and test the sample JSON at http://127.0.0.1:5000/api/quote

You may need to use `python3` or `py` instead of `python` on your machine.

## Files
- `app.py`: Flask routes and sample quote
- `templates/index.html`: page markup
- `static/style.css`: visual design
- `static/script.js`: button logic starter
- `requirements.txt`: Flask dependency

## Team tasks
1. **HTML:** Improve accessibility and page structure.
2. **CSS:** Add mobile polish, button hover/focus states, and consistent spacing.
3. **JavaScript:** Use `fetch('/api/quote')` to request and display the quote, with error handling.
4. **Python:** Replace the fixed sample quote with a random selection from a list of quotes.

The API and page run, but the JavaScript and randomization are intentionally incomplete to leave room for the team to build together.

## Collaboration
- Claim a GitHub Issue before starting.
- Create a branch for each task, e.g. `feature/random-quotes`.
- Commit your changes and open a pull request into `main`.
- Ask a teammate to review before merging.
- Don't commit passwords, API keys, `.env` files, or your `.venv` folder.

**Learn. Build. Collaborate. Grow.**
