import re


def find_rhetorical_devices(text):
    devices = {
        'Сравнения': len(re.findall(r'\bкак\b|\bсловно\b|\bбудто\b', text)),
        'Олицетворения': len(re.findall(r'\b[А-Яа-я]+ [А-Яа-я]+ся\b', text)),
        'Прилагательные в сравнительной степени': len(re.findall(r'\b[А-Яа-я]+(ее|ей|ше)\b', text))
    }
    return devices


def find_borrowed_words(text, borrowed_words):
    words = text.split()
    found_borrowed = [word for word in words if word.lower() in borrowed_words]
    return found_borrowed


def load_borrowed_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            borrowed_words = [line.strip() for line in file]
        return borrowed_words
    except FileNotFoundError:
        return f"\nОшибка: Файл '{filename}' не найден. Проверьте путь к файлу."
