# 🤝 Contributing

## 🛠️ Tech Stack Focus

* **Backend:** Flask (Application Factory Pattern)
* **Database:** SQLite with Flask-SQLAlchemy
* **Frontend:** HTMX for dynamic updates + Pico.css

---

## 🚀 Getting Started Locally

### 1. Fork & Clone

* Click the **'Fork'** button on the main repository.
* Clone **your fork** to your local machine (run that onetime only!):
    ```bash
    git clone https://github.com/YOUR_USERNAME/donation-platform.git
    
    cd donation_platform
    
    git remote add upstream https://github.com/care-bridge/platform.git
    ```

2.  **Set up Virtual Environment & Install modules:** `python make.py init && python make.py setup`

3.  **Run:** `python make.py run`
    
### The Feature Workflow (Do this for every task!)

Always work on a branch. Never code directly on main.

1. Sync with the team:

```bash
git checkout main
git pull upstream main
```

2. Create your task branch: `git checkout -b feature/your-task-name`

3. Code THEN Test THEN Run: `python make.py test && python make.py run`

4. Lint your code when done: `python make.py lint`

5. Push to your fork:

use **Conventional Commits** but keep it simple and easy for you, don't over engineer, make it simple like that:

```bash
git add .
git commit -m "feat: implement models.py"
git push origin feature/your-task-name
```

6. Submit Your Work:

- Go to the original repository on GitHub.
- Click "Compare & Pull Request".
- Briefly describe your changes and tag a teammate for a quick review.

7. Read *Coding Standards below*

---

## 🏗️ Development Workflow

### 1. Database Changes

If you need to change the data structure:

* Modify `app/models.py`.

### 2. Adding Routes

* **Don't** add routes to `app.py`.
* **Do** add them to the appropriate Blueprint in `app/routes/` (e.g., `auth.py`, `donations.py`).
* Register new Blueprints in `app/__init__.py`.

### 3. Frontend & HTMX

* We aim for a Single Page Application (SPA) feel without heavy JavaScript.
* Use HTMX attributes (`hx-get`, `hx-post`, `hx-target`) to swap HTML fragments.
* Store small, reusable snippets (for HTMX) in `app/templates/partials/`.
* Reusable components in `app/templates/macros.html` using flask's built-in feature `macros`

---

## 📜 Coding Standards

* **Python styling:** Very important to run `python make.py lint` 
* **Docstrings:** Briefly explain the purpose of new routes or models.
* **Privacy:** Always anonymize patient data in the UI.
* **DON'T EDIT make.py file!**

---

## 💬 Communication

If you're stuck or want to discuss a new feature, reach out to us on our Discord Group or open an Issue in the repository. Happy coding! 🚀
