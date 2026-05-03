# 🤝 Contributing

## 🛠️ Tech Stack

* **Frontend:** [11ty](https://www.11ty.dev/) + [Pico.css](https://www.picocss.com) + Vanilla JavaScript
* **Backend:** [Firebase](https://firebase.google.com/) (Auth + Firestore + Storage)
* **Hosting:** Netlify
* **Package Manager:** pnpm

---

## 🚀 Getting Started Locally

### 1. Fork & Clone

* Click the **'Fork'** button on the main repository.
* Clone **your fork** to your local machine:
```bash
    git clone https://github.com/YOUR_USERNAME/CareBridge.git
    cd CareBridge
    git remote add upstream https://github.com/omar-hossam/CareBridge.git
```

### 2. Install Dependencies

Make sure you have [pnpm](https://pnpm.io/installation) installed.

```bash
pnpm install
```

### 3. Firebase Setup

1. Create a Firebase project at [console.firebase.google.com](https://console.firebase.google.com)
2. Enable **Authentication** (Email/Password), **Firestore**, and **Storage**
3. Copy your Firebase config into `_data/firebase.js`

### 4. Run Development Server

```bash
pnpm dev # Runs 11ty on localhost:8080
```

---

## 🏗️ Development Workflow

Always work on a branch. Never code directly on `main`.

1. **Sync with the team:**
```bash
    git checkout main
    git pull upstream main
```

2. **Create your task branch:**
```bash
    git checkout -b feature/your-task-name
```

3. **Code & Test:** Ensure the app runs without errors using `pnpm dev`.

4. **Push to your fork** using **Conventional Commits**:
```bash
    git add .
    git commit -m "feat: implement user donation history"
    git push origin feature/your-task-name
```

5. **Submit Your Work:**
    - Go to [omar-hossam/CareBridge](https://github.com/omar-hossam/CareBridge)
    - Click **"Compare & Pull Request"**
    - Briefly describe your changes and tag a teammate for review

---

## 📐 Project Architecture

### Frontend (11ty + Pico.css + JS)

* **Components:** Reusable UI elements go in `_components/`
* **Pages:** Main views go in `content/`
* **Layout:** Main layout is in `_includes/base.njk`
* **Styling:** Use Pico.css built-in variables for consistency, custom CSS goes in `css/`
* **JS:** Each page has its own module in `js/`. Firebase is initialized once in `base.njk` and exposed via `window.db`, `window.auth`, `window.storage`

### Backend (Firebase)

* **Auth:** Email/Password via Firebase Authentication
* **Database:** Firestore with 2 collections — `users` and `requests`
* **Storage:** Firebase Storage for hospital documents (legal PDF, logo, photos)
* **Security:** Firestore rules enforce role-based access — never rely on frontend-only checks

### Auth & Roles

| Role | Access |
| :--- | :--- |
| `donor` | Browse and fund requests |
| `individual` | Submit personal aid requests |
| `hospital` | Submit patient requests (requires admin approval) |
| `admin` | Approve/reject hospital applications |

Route protection is handled by `/js/guard.js` — every protected page imports and awaits it before running any logic.

---

## 📜 Coding Standards

* **No frameworks** — vanilla JS modules only, keep it lightweight
* **Firebase on `window`** — never re-initialize Firebase in page scripts, use `window.db`, `window.auth`, `window.storage`
* **Guard every route** — import `guard.js` in every protected page JS file
* **Privacy always** — never display patient real names, photos, or IDs anywhere in the UI
* **Error handling** — always wrap Firebase calls in `try/catch` and show user-friendly messages
* **Conventional Commits** — `feat:`, `fix:`, `docs:`, `style:`, `refactor:`

---

## 💬 Communication

If you're stuck or want to discuss a feature, open an Issue in the repository or reach out on our Discord. Happy coding! 🚀
