# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 2.x     | ? Yes    |
| 1.x     | ? No     |

## Reporting a Vulnerability

Please **do not** open a public GitHub Issue for security vulnerabilities.

Instead, email the maintainers directly (see profile). Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (optional)

We aim to respond within **48 hours** and release a patch within **7 days** for critical issues.

## Security Practices

- Firebase ID tokens are verified server-side on every protected request via irebase-admin
- Patient data stored in Pinecone is namespaced by Firebase UID — users cannot access each other's history
- API keys are stored as environment variables and never hardcoded
- The .gitignore explicitly excludes Firebase Admin SDK JSON files
- CORS is currently set to llow_origins=["*"] for development — **restrict this in production** to your frontend domain
