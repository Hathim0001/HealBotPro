# Local Development Setup

## Prerequisites

| Tool | Version |
|------|---------|
| Python | 3.11+ |
| Node.js | 18+ |
| npm / pnpm | latest |

## Backend Setup

`ash
cd backend
python -m venv .venv

# Activate venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
cp ../.env.example .env
# Fill in your API keys in .env
`

Place your Firebase Admin SDK JSON (downloaded from Firebase Console ? Project Settings ? Service Accounts) inside the ackend/ folder.

`ash
python main.py
# API running at http://localhost:8002
# Docs at http://localhost:8002/docs
`

## Frontend Setup

`ash
cd frontend
npm install

# Create frontend env
echo "VITE_API_BASE=http://localhost:8002" > .env

npm run dev
# App running at http://localhost:5173
`

## Common Issues

### irebase_admin JSON not found
Make sure the Firebase service account JSON file is inside the ackend/ directory (not the project root).

### Neo4j connection refused
Check that your NEO4J_URI uses the 
eo4j+s:// scheme (AuraDB requires TLS).

### Pinecone 404 on upsert
Ensure the index was created with dimension=384 and metric cosine.
