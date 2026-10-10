# HealBotPro – API Reference

Base URL (local): http://localhost:8002
Base URL (production): see your API Gateway URL

All protected endpoints require:
`
Authorization: Bearer <firebase_id_token>
`

---

## Health

### GET /
Returns { "status": "ok" }. Use for uptime checks.

---

## Authentication

### POST /register
Create a new user record (Firebase UID + display name).

**Body:**
`json
{ "uid": "firebase_uid", "username": "john", "full_name": "John Doe" }
`

### POST /login
Verify a Firebase ID token and return user info.

**Body:**
`json
{ "token": "<firebase_id_token>" }
`

---

## Intake (Conversational Symptom Gathering)

### POST /intake/turn
Send one turn of the patient–MediAssist conversation.

**Body:**
`json
{
  "conversation": [
    { "role": "user", "content": "I have a headache and fever" },
    { "role": "assistant", "content": "How long have you had these symptoms?" },
    { "role": "user", "content": "About 3 days" }
  ],
  "doc_path": null
}
`

**Response:**
`json
{
  "message": "Have you taken any medication for the fever?",
  "intake_complete": false,
  "summary": null
}
`
When intake_complete is 	rue, summary contains the patient brief to pass to /consult.

---

## Consultation

### POST /consult
Run the full 4-step diagnostic pipeline.

**Body:**
`json
{
  "patient_summary": "3-day headache, fever 38.5°C, nausea...",
  "user_id": "firebase_uid",
  "doc_path": "temp_uploads/abc.pdf",
  "conversation_transcript": "Patient: I have a headache…\nMediAssist: …"
}
`

**Response:**
`json
{
  "symptoms": ["headache", "fever", "nausea"],
  "diseases": ["Viral infection", "Dengue fever"],
  "report": "## Doctor's Consultation Brief\n…"
}
`

---

## Documents & History

### POST /upload
Upload a medical PDF (multipart).

### POST /user/history
Encode patient history into Pinecone (base64 PDF body).

### GET /user/{user_id}
Check whether a patient has stored history in Pinecone.

---

## Text-to-Speech

### POST /tts
Stream MP3 audio for a text string.

**Body:**
`json
{ "text": "Hello, I am MediAssist. How can I help you today?", "lang": "en" }
`

**Response:** udio/mpeg stream
