# Clause UI Mockups – React Frontend

This folder contains the UI components and app logic for submitting and interacting with clause suggestions.

---

## Components

- `ClauseSubmitForm.jsx` – Form to submit new clauses to the backend API
- `ClauseSuggestionBox.jsx` – Simple component to accept or reject sample clauses
- `App.jsx` – Page wrapper that renders both components
- `index.jsx` – React entry point

---

## Running the App (from desktop)

### Option 1 – Using Vite (recommended)
```bash
npm create vite@latest clause-ui --template react
cd clause-ui
npm install
npm run dev
