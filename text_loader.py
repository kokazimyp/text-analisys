import sqlite3


def load_text(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None


def save_text_to_db(text, db_path='text_analysis.db'):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO texts (content) VALUES (?)''', (text,))
        conn.commit()
        conn.close()
        print("Текст успешно сохранен в базу данных.")
    except Exception as e:
        print(f"Ошибка при сохранении текста в базу данных: {e}")

