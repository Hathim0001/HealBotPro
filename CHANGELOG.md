# Changelog

All notable changes to HealBotPro are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/).

---

## [Unreleased]

## [2.0.0] – 2026-11-01
### Added
- Conversational intake assistant (MediAssist) replacing static textarea
- /intake/turn endpoint for multi-turn symptom gathering
- Text-to-speech (/tts) via edge-tts (Microsoft Neural voices)
- Call interface component (CallInterface.jsx)
- History page with AI-generated patient summary
- PDF upload via base64 for AWS Lambda compatibility

### Changed
- Auth migrated fully to Firebase (removed SQLite user table)
- Report UI redesigned with structured sections

### Removed
- One-time dev scripts (dataset_loader, generate_cypher, etc.)
- Legacy SQLite auth endpoints

## [1.0.0] – 2026-06-15
### Added
- Initial FastAPI backend with Neo4j + Pinecone pipeline
- Symptom extraction ? graph search ? RAG retrieval ? report generation
- React frontend with basic form input
- Firebase authentication
