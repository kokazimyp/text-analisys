import sqlite3


def create_tables(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS texts 
                      (id INTEGER PRIMARY KEY, content TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS word_frequencies 
                      (id INTEGER PRIMARY KEY, word TEXT, frequency INTEGER, text_id INTEGER,
                       FOREIGN KEY(text_id) REFERENCES texts(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sentence_analysis 
                      (id INTEGER PRIMARY KEY, sentence_type TEXT, count INTEGER, text_id INTEGER,
                       FOREIGN KEY(text_id) REFERENCES texts(id))''')

    conn.commit()
    conn.close()
