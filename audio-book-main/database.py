import sqlite3

def init_db(db_path="Documents.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        type TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        text TEXT NOT NULL,
        FOREIGN KEY (document_id) REFERENCES documents(id)
    )''')

    conn.commit()
    return conn

def save_document(conn, document):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO documents (title, author, type)
        VALUES (?, ?, ?)
    ''', (document.title, document.author, document.__class__.__name__))

    doc_id = cursor.lastrowid
    sections = document.process_content()

    for section in sections:
        cursor.execute('''
            INSERT INTO sections (document_id, title, text)
            VALUES (?, ?, ?)
        ''', (doc_id, section["title"], section["text"]))

    conn.commit()

def get_documents(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM documents")
    return cursor.fetchall()

def get_sections(conn, doc_id):
    cursor = conn.cursor()
    cursor.execute("SELECT title, text FROM sections WHERE document_id = ?", (doc_id,))
    return cursor.fetchall()