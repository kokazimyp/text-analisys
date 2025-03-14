import re


def clean_text(text, remove_punctuation=False, replace_yo=True):
    if remove_punctuation:
        text = re.sub(r'[,.!?;:\'\"()-«»–]', '', text)
    if replace_yo:
        text = text.replace('ё', 'е')

    text = re.sub(r'\s+', ' ', text).strip()

    return text


def manage_stop_words(stop_words, action, word):

    if action == 'add':
        stop_words.append(word)
        print(f"\nСлово {word} добавлено")
        return stop_words

    if action == 'remove':
        if word in stop_words:
            print("\nСтоп слово", word, "удалено.")
            stop_words.remove(word)
            return stop_words
        
        print(f"\nСлово {word} не найдено в стоп-листе!")
        return stop_words
    
    print(f"\nДействие {action} не распознано!")
    return stop_words


def remove_stop_words(text, stop_words):

    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)
