from collections import Counter
import sqlite3
import re


def save_text_to_db(text, db_path='text_analysis.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO texts (content) VALUES (?)''', (text,))
    text_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return text_id


def save_word_frequencies(text, text_id, db_path='text_analysis.db'):
    words = text.split()
    word_counts = Counter(words)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for word, frequency in word_counts.items():
        cursor.execute('''INSERT INTO word_frequencies (word, frequency, text_id) 
                          VALUES (?, ?, ?)''', (word, frequency, text_id))
    conn.commit()
    conn.close()


def save_sentence_analysis(text, text_id, db_path='text_analysis.db'):
    sentences = re.findall(r'[^.!?]+[.!?]', text, re.DOTALL)
    sentences = [s for s in sentences if s.strip()]

    types = {'повествовательные': 0, 'вопросительные': 0, 'восклицательные': 0}
    for sentence in sentences:
        if sentence.endswith('.'):
            types['повествовательные'] += 1
        elif sentence.endswith('?'):
            types['вопросительные'] += 1
        elif sentence.endswith('!'):
            types['восклицательные'] += 1

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    for sentence_type, count in types.items():
        cursor.execute('''INSERT INTO sentence_analysis (sentence_type, count, text_id) 
                          VALUES (?, ?, ?)''', (sentence_type, count, text_id))
    conn.commit()
    conn.close()