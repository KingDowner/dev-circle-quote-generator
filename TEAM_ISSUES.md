# Suggested GitHub Issues

Create the following four issues in your repository (Issues → New issue). Members can claim one each.

## 1. Improve the HTML layout (beginner)
**Goal:** Improve `templates/index.html` so the quote card is accessible and easy to understand. Keep existing IDs `quote-text`, `quote-author`, and `new-quote` because the JavaScript needs them.
**Done when:** Heading, quote text, attribution, and button display cleanly on desktop and mobile.

## 2. Polish styling and responsiveness (beginner)
**Goal:** Improve `static/style.css` with hover states, small-screen spacing, and a readable visual hierarchy.
**Done when:** Site looks good and button is usable on a narrow phone screen and desktop; focus state remains visible.

## 3. Connect the button to Flask (beginner/intermediate)
**Goal:** In `static/script.js`, use `fetch('/api/quote')` on click. Read the JSON, update the quote and author, and show an error if the request fails.
**Done when:** Pressing the button updates the page from the API without a reload; errors do not crash the page.

## 4. Return random quotes from Python (beginner/intermediate)
**Goal:** In `app.py`, create a list of at least 5 quotes and select one with Python's `random.choice` when `/api/quote` is requested.
**Done when:** API returns JSON with `text` and `author`, and repeated calls can return different quotes.
