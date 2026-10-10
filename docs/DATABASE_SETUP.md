# Neo4j & Pinecone Setup Guide

## Neo4j AuraDB (Free Tier)

1. Sign up at [console.neo4j.io](https://console.neo4j.io)
2. Create a free AuraDB instance (choose the **Free** tier)
3. Download the connection credentials file — it contains NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD
4. Set these in your .env file

### Loading the Medical Knowledge Graph

The graph contains Disease ? Symptom relationships used in Step 2 of the pipeline.
Run the graph loader (not included in this public repo) or import your own Cypher dataset:

`cypher
// Example node creation
CREATE (d:Disease {name: 'Dengue Fever'})
CREATE (s:Symptom {name: 'High Fever'})
CREATE (s2:Symptom {name: 'Joint Pain'})
CREATE (d)-[:HAS_SYMPTOM]->(s)
CREATE (d)-[:HAS_SYMPTOM]->(s2)
`

### Querying Symptoms

The backend uses this pattern:
`cypher
MATCH (s:Symptom)-[:HAS_SYMPTOM]-(d:Disease)-[:HAS_SYMPTOM]-(related:Symptom)
WHERE s.name IN 
RETURN DISTINCT d.name AS disease, collect(DISTINCT related.name) AS related_symptoms
LIMIT 10
`

---

## Pinecone (Starter / Free Tier)

1. Sign up at [app.pinecone.io](https://app.pinecone.io)
2. Create an index with:
   - **Dimensions**: 384 (matches ll-MiniLM-L6-v2)
   - **Metric**: cosine
   - **Name**: healbot-index (or update PINECONE_INDEX in .env)
3. Copy your API key to .env as PINECONE_API_KEY

### Namespace Strategy

| Namespace | Purpose |
|-----------|---------|
| medical-docs | Clinical reference documents (RAG) |
| user-{uid} | Per-patient medical history |

Patient history is namespaced by Firebase UID to ensure data isolation.
