# HealBotPro – Frontend

React + Vite single-page application.

## Stack

| Library | Purpose |
|---------|---------|
| React 18 | UI framework |
| Vite 5 | Build tool & dev server |
| Firebase JS SDK | Auth (sign-up, login, ID tokens) |
| Axios | HTTP client |
| Tailwind CSS | Utility-first styling |

## Folder Structure

`
frontend/
+-- src/
¦   +-- App.jsx              ? Root: routing between Landing / Auth / Chat / Report
¦   +-- main.jsx             ? React entry point
¦   +-- index.css            ? Global styles + Tailwind imports
¦   +-- components/
¦       +-- Auth.jsx         ? Login & Register forms
¦       +-- IntakeChat.jsx   ? Conversational symptom intake (MediAssist)
¦       +-- ReportView.jsx   ? Diagnostic report display
¦       +-- HistoryModal.jsx ? Upload & encode medical history PDF
¦       +-- HistoryPage.jsx  ? View past consultations
¦       +-- CallInterface.jsx? Voice call UI with TTS
+-- index.html
+-- package.json
+-- vite.config.js
`

## Environment Variables

Create rontend/.env:
`
VITE_API_BASE=http://localhost:8002
VITE_FIREBASE_API_KEY=...
VITE_FIREBASE_AUTH_DOMAIN=...
VITE_FIREBASE_PROJECT_ID=...
`

## Available Scripts

| Command | Description |
|---------|-------------|
| 
pm run dev | Start dev server at localhost:5173 |
| 
pm run build | Production build ? dist/ |
| 
pm run preview | Preview the production build |
| 
pm run lint | Run ESLint |
