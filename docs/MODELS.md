# LLM Models Used in HealBotPro

All models run on [Groq](https://groq.com) — free tier with generous rate limits.

## Model Selection Rationale

| Step | Model | Reason |
|------|-------|--------|
| Conversational intake (MediAssist) | llama-3.3-70b-versatile | Best medical reasoning, nuanced follow-up questions |
| Symptom extraction | llama-3.1-8b-instant | Lightweight; structured JSON output is fast |
| Consultation report | llama-3.3-70b-versatile | High-quality structured clinical writing |

## Embedding Model

| Use | Model | Dimensions |
|-----|-------|-----------|
| Document & history vectorisation | ll-MiniLM-L6-v2 (via sentence-transformers) | 384 |

Runs locally inside the Lambda function — no external API call required.

## Prompt Design

### MediAssist System Prompt (Intake)
MediAssist is instructed to:
1. Greet the patient warmly
2. Ask ONE focused follow-up question per turn
3. Probe: onset, duration, severity, associated symptoms, aggravating/relieving factors, medications, allergies
4. After 4–7 turns (when sufficient), emit [INTAKE_COMPLETE] followed by a JSON patient summary

### Symptom Extraction Prompt
A lightweight structured prompt asking the 8B model to return a JSON array of canonical symptom names from free-text.

### Report Generation Prompt
Instructs the 70B model to write a structured brief with sections:
- Chief Complaint
- History of Present Illness
- Differential Diagnoses (ranked)
- Recommended Investigations
- Management Plan
- Red Flags
