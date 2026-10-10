"""
HealBotPro – Database layer

Authentication is handled entirely by Firebase.
This module is kept as a placeholder for any future SQLite/PostgreSQL
extensions (e.g., consultation audit logs, usage analytics).

If you add local persistence, initialize SQLModel here:

    from sqlmodel import SQLModel, create_engine, Session
    engine = create_engine("sqlite:///./healbot.db")
    SQLModel.metadata.create_all(engine)
"""

# No local DB is active in the current Firebase-only auth setup.
# Future: extend with consultation logs, rate-limit counters, etc.
