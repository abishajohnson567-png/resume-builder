import json
import sqlite3
import os
from datetime import datetime

DB_PATH = "resumes.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            data TEXT NOT NULL,
            photo TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_resume(name, data, photo=None):
    conn = get_db()
    now = datetime.now().isoformat()
    cursor = conn.execute(
        "INSERT INTO resumes (name, data, photo, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        (name, json.dumps(data), photo, now, now)
    )
    resume_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return resume_id

def update_resume(resume_id, name, data, photo=None):
    conn = get_db()
    now = datetime.now().isoformat()
    conn.execute(
        "UPDATE resumes SET name=?, data=?, photo=?, updated_at=? WHERE id=?",
        (name, json.dumps(data), photo, now, resume_id)
    )
    conn.commit()
    conn.close()

def get_resume(resume_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM resumes WHERE id=?", (resume_id,)).fetchone()
    conn.close()
    if row:
        result = dict(row)
        result["data"] = json.loads(result["data"])
        return result
    return None

def get_all_resumes():
    conn = get_db()
    rows = conn.execute("SELECT id, name, created_at, updated_at FROM resumes ORDER BY updated_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_resume(resume_id):
    conn = get_db()
    conn.execute("DELETE FROM resumes WHERE id=?", (resume_id,))
    conn.commit()
    conn.close()
