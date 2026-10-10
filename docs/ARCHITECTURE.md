# HealBotPro – Architecture Overview

## System Components

`
+---------------------------------------------------------+
¦                        Frontend                         ¦
¦  React + Vite · Firebase Auth · Tailwind CSS            ¦
¦                                                         ¦
¦  Landing ? Auth ? IntakeChat ? Report / History         ¦
+---------------------------------------------------------+
                        ¦ HTTPS (REST)
+-----------------------?---------------------------------+
¦                    FastAPI Backend                       ¦
¦  Python 3.11 · Mangum (AWS Lambda adapter)              ¦
¦                                                         ¦
¦  /intake/turn  ?  MediAssist (Groq LLaMA-3 70B)         ¦
¦  /consult      ?  4-step diagnostic pipeline            ¦
¦  /tts          ?  edge-tts (Microsoft Neural)           ¦
¦  /upload       ?  PDF ? Pinecone                        ¦
+---------------------------------------------------------+
       ¦                              ¦
+------?------+              +--------?--------+
¦   Neo4j     ¦              ¦    Pinecone     ¦
¦  AuraDB     ¦              ¦  Vector Store   ¦
¦  (Graph DB) ¦              ¦  (RAG / History)¦
+-------------+              +-----------------+
`

## Data Flow

1. **Authentication** – Firebase handles user sign-up/login; the backend verifies tokens via irebase-admin.
2. **Intake** – The frontend sends conversation turns to /intake/turn. MediAssist (LLaMA-3 70B on Groq) asks follow-up questions until it outputs [INTAKE_COMPLETE].
3. **Consultation** – /consult runs the 4-step pipeline:
   - extract_symptoms_with_llm – lightweight 8B model parses symptoms
   - pass_1_neo4j_graph_search – traverses medical knowledge graph
   - pass_2_pinecone_rag_retrieval – fetches relevant clinical documents + user history
   - generate_consultation_report – 70B model writes a structured doctor's brief
4. **TTS** – /tts streams MP3 audio back for the voice call interface.

## Deployment

- **Backend**: AWS Lambda + API Gateway (via Mangum)
- **Frontend**: Vercel (static build, 
pm run build)
- **Databases**: Neo4j AuraDB Free + Pinecone Starter
