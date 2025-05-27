import sqlite3
import os

def run_schema_and_seed():
    """
    Creates the database, runs schema.sql, and seeds sample data.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(base_dir, 'code-challenge.db')
    schema_path = os.path.join(base_dir, 'lib', 'db', 'schema.sql')
    from lib.db.seed import seed

    # Remove old db if exists
    if os.path.exists(db_path):
        os.remove(db_path)

    # Create new db and run schema
    conn = sqlite3.connect(db_path)
    try:
        with open(schema_path, 'r') as f:
            conn.executescript(f.read())
        conn.commit()
    finally:
        conn.close()

    # Seed data
    seed()
    print("Database setup and seeded successfully.")

if __name__ == "__main__":
    run_schema_and_seed()