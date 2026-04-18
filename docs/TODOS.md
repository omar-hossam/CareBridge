# 🏥 Hospital-Donor Connection Platform - TODOs

## 🎯 Project Vision

A direct, low-friction platform where donors pay hospital bills for patients in need. 
**Tech Stack:** Flask (Backend), SQLite (Database), HTMX (Dynamic UI), Pico.css (Styling).

---

## 🏗️ Phase 1: Core Infrastructure (The "Bones")

- [ ] **Database Initialization:** Finalize `models.py` with Donors, Hospitals, Admins and Donations.
- [ ] **Auth System:**
    - [ ] Create **Sign Up** (with Role selection: Donor vs. Hospital).
    - [ ] Create **Login/Logout** logic.
- [ ] **Role-Based Access:** Ensure Donors can't see Hospital Admin pages.

---

## 📄 Phase 2: Page Implementation (The "Body")

### 1. Public Pages (Trust Building)

- [ ] **Home Page:** Hero section + "How it works" + HTMX-powered "Total Lives Impacted" counter.
- [ ] **Hospital Directory:** A list of hospitals. 
    - *HTMX Feature:* Search bar that filters hospitals without refreshing the page.
- [ ] **FAQ/Transparency Page:** Simple static info on fund safety.

### 2. Donor Dashboard (The "Giver")

- [ ] **My Impact:** Total amount donated and history.
- [ ] **Donation Flow:** - [ ] Select Hospital/Case.
    - [ ] Input Amount.
    - [ ] Integration with Stripe (Test Mode) or a Mock Payment button for local dev.
- [ ] **Receipts:** Generate a simple HTML view of past donations.

### 3. Hospital Portal (The "Receiver")

- [ ] **Profile Setup:** Hospital name, location, and verification status.
- [ ] **Fund Requests:** A form to post "Needs" (e.g., "Need $500 for Emergency Surgery").
- [ ] **Wallet View:** See total funds received and pending payouts.

---

## ⚡ Phase 3: The HTMX "Magic" (The "Experience")

- [ ] **Inline Editing:** Allow hospitals to edit their profile details without page reloads.
- [ ] **Live Search:** Search for hospitals/cases in real-time as the donor types.
- [ ] **Dynamic Forms:** Show "Success" messages or "Error" alerts inside the same page after donating.
- [ ] **Infinite Scroll:** For the Hospital Directory or Donation History.

---

## 🛡️ Phase 4: Security & Polish (The "Shield")

- [ ] **Data Validation:** Use `WTForms` or manual checks to ensure donation amounts are > 0.
- [ ] **Password Hashing:** Ensure `Werkzeug` is hashing all passwords.
- [ ] **Anonymization:** Logic to hide patient names from public views.
- [ ] **Environment Variables:** Move `SECRET_KEY` and DB paths to a `.env` file.

---

## 🚀 Phase 5: Local Testing & Prep

- [ ] **Mock Data script:** Create a `seed.py` file to fill the SQLite DB with fake hospitals and donors for testing.
- [ ] **Team Review:** Test the full flow: *Donor Sign Up -> Browse Hospital -> Donate -> Hospital sees funds.*

---

## 🛠️ How to Work Smoothly

1. **Model First:** Don't write UI until the `models.py` for that feature is solid.
2. **HTMX Routes:** All HTMX routes should return **HTML fragments** (partial files), **not full pages OR JSON to prevent unexpected errors**.
3. **Commit often:** Even though it's local, keep your code versioned.

---

## Final Tip

- It's okay to make mistakes, we are learning and enjoying :)
- Don't focus on making something perfect, make it work then if you can make it pretty
