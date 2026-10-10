# Deployment Guide

## Frontend ? Vercel

1. Install Vercel CLI: 
pm i -g vercel
2. From rontend/:
   `ash
   vercel --prod
   `
3. Set environment variables in the Vercel dashboard:
   - VITE_API_BASE ? your API Gateway URL
   - VITE_FIREBASE_API_KEY etc.

The ercel.json in rontend/ handles SPA routing rewrites automatically.

## Backend ? AWS Lambda

The backend uses [Mangum](https://mangum.io/) to run FastAPI on AWS Lambda.

### Deploy steps (using AWS Console or SAM CLI)

1. Package your code:
   `ash
   pip install -r requirements.txt -t package/
   cp *.py package/
   cp *.json package/   # Firebase Admin SDK JSON
   cd package && zip -r ../healbot.zip .
   `
2. Upload healbot.zip to your Lambda function.
3. Set the handler to main.handler.
4. Set all environment variables from .env in Lambda ? Configuration ? Environment variables.
5. Attach an API Gateway (HTTP API) trigger.

### Runtime

- Python 3.11
- Memory: 512 MB recommended (Groq calls are fast; Neo4j/Pinecone add ~200ms)
- Timeout: 30 seconds

### Cold Start Mitigation

Enable Lambda provisioned concurrency if cold starts exceed 3s.

## Health Check

After deploying, hit GET / — it should return {"status":"ok"}.
