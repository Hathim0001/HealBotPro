# Troubleshooting

## Backend

### ValueError: Firebase app already initialized
The app auto-initialises on startup. This error appears if the lifespan function
runs twice (e.g., Uvicorn --reload with two workers). Wrap init in a try/except — already done in main.py.

### groq.RateLimitError
Groq free-tier limits: ~30 req/min. Add a short syncio.sleep(1) between pipeline steps, or upgrade to Groq's paid tier.

### Neo4j ServiceUnavailable
- Check the AuraDB instance is running (free tier pauses after inactivity)
- Verify NEO4J_URI uses 
eo4j+s:// (not olt://)

### Pinecone PineconeApiException: 404 Not Found
- The index name in PINECONE_INDEX doesn't match the actual index
- Ensure dimensions=384 and metric=cosine

### PDF extraction returns None
- The PDF may be scanned (image-only) — OCR is not currently supported
- Try a text-layer PDF exported from Word/Google Docs

---

## Frontend

### Blank page on Vercel
- Check browser console for VITE_API_BASE missing
- Ensure environment variables are set in Vercel dashboard (not just .env)

### Firebase uth/invalid-api-key
- The VITE_FIREBASE_API_KEY env var is missing or wrong
- For local dev, create rontend/.env with all VITE_FIREBASE_* values

### CORS error from browser
- The backend llow_origins is ["*"] — if you're still getting CORS, check your API Gateway CORS settings (AWS API Gateway has its own CORS layer)
