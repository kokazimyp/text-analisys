from collections import Counter, defaultdict
import re
import matplotlib.pyplot as plt
import spacy

nlp = spacy.load("ru_core_news_sm")


def plot_word_frequency(text, top_n):
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(top_n)
    words, counts = zip(*most_common)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='pink')
    plt.title("Частотность слов")
    plt.xlabel("Ось X: Слова")
    plt.ylabel("Ось Y: Частота")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()


def plot_sentence_types(text):
    sentences = re.findall(r'[^.!?]+[.!?]', text)

    question_count = 0
    exclamation_count = 0
    statement_count = 0

    for sentence in sentences:
        if sentence.endswith('?'):
            question_count += 1
        elif sentence.endswith('!'):
            exclamation_count += 1
        else:
            statement_count += 1

    if sum([question_count, exclamation_count, statement_count]) == 0:
        print("Ошибка: в тексте нет предложений для анализа.")
        return

    labels = ['Вопросительные', 'Восклицательные', 'Утвердительные']
    sizes = [question_count, exclamation_count, statement_count]

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['pink', 'mediumvioletred', 'hotpink'])
    plt.title("Доля типов предложений")
    plt.axis('equal')
    plt.grid(True)
    plt.show()


def plot_word_length_distribution_bywords(text):
    words = text.split()
    word_lengths = [len(word) for word in words]

    plt.figure(figsize=(10, 6))
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 2), edgecolor='black', color='pink')
    plt.xlabel('Длина слова')
    plt.ylabel('Количество слов')
    plt.title('Распределение длины слов')
    plt.xticks(range(1, max(word_lengths) + 1))
    plt.grid(axis='y')
    plt.show()


def plot_average_sentence_length(text):
    pattern = r'\b(\d+\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    avg_sentence_lengths = []

    for i, chapter in enumerate(chapters):
        sentences = re.split(r'[.!?]', chapter)
        sentences = [s for s in sentences if s.strip()]

        avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)

        avg_sentence_lengths.append(avg_sentence_length)

    plt.figure(figsize=(10, 5))
    plt.plot(avg_sentence_lengths, label='Средняя длина предложений', color='pink', marker='o')
    plt.xlabel('Глава')
    plt.ylabel('Средняя длина предложений')
    plt.title('Средняя длина предложений по главам')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_character_frequency(text):
    char_counts = Counter(text.lower())
    chars, counts = zip(*char_counts.items())
    plt.bar(chars, counts, color='pink')
    plt.xlabel('Символы')
    plt.ylabel('Частота')
    plt.title('Частота символов в тексте')
    plt.grid(axis='y')
    plt.show()


def plot_word_length_distribution(text):
    words = text.split()
    lengths = [len(word) for word in words]

    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=range(1, max(lengths) + 2), align='left', rwidth=0.8, color='pink')
    plt.title("Распределение длины слов")
    plt.xlabel("Ось X: Длина слова")
    plt.ylabel("Ось Y: Частота")
    plt.xticks(range(1, max(lengths) + 1))
    plt.grid(axis='y')
    plt.show()


def plot_verb_tenses(text):
    doc = nlp(text)
    tenses = {'прошедшее': 0, 'настоящее': 0, 'будущее': 0}

    for token in doc:
        if token.pos_ == "VERB":
            morph = token.morph
            if "Tense=Past" in morph:
                tenses['прошедшее'] += 1
            elif "Tense=Pres" in morph:
                tenses['настоящее'] += 1
            elif "Tense=Fut" in morph:
                tenses['будущее'] += 1

    labels = tenses.keys()
    counts = tenses.values()

    plt.bar(labels, counts, color='pink')
    plt.xlabel('Время глагола')
    plt.ylabel('Количество')
    plt.title('Использование глаголов по временам')
    plt.grid(axis='y')
    plt.show()


def plot_unique_words_dynamics(text, window_size=100):
    words = text.split()
    unique_ratios = []
    unique_words = set()
    for i in range(0, len(words), window_size):
        window = words[i:i + window_size]
        unique_words.update(window)
        unique_ratios.append(len(unique_words) / (i + window_size))
    plt.plot(unique_ratios, marker='o', color='pink')
    plt.xlabel('Окна текста')
    plt.ylabel('Пропорция уникальных слов')
    plt.title('Динамика уникальных слов')
    plt.grid(True)
    plt.show()


def plot_pos_distribution(text, window_size=1000):
    doc = nlp(text)
    pos_counts = {'существительные': [], 'глаголы': [], 'прилагательные': []}
    words = [token.text for token in doc]
    for i in range(0, len(words), window_size):
        window = words[i:i + window_size]
        counts = {'существительные': 0, 'глаголы': 0, 'прилагательные': 0}
        for word in window:
            token = nlp(word)[0]
            if token.pos_ == "NOUN":
                counts['существительные'] += 1
            elif token.pos_ == "VERB":
                counts['глаголы'] += 1
            elif token.pos_ == "ADJ":
                counts['прилагательные'] += 1
        total = sum(counts.values())
        if total > 0:
            for key in pos_counts:
                pos_counts[key].append(counts[key] / total)
    colors = {'существительные': 'hotpink', 'глаголы': 'deeppink', 'прилагательные': 'pink'}
    for key, values in pos_counts.items():
        plt.plot(values, label=key, color=colors[key])
    plt.xlabel('Окна текста')
    plt.ylabel('Доля')
    plt.title('Доля частей речи')
    plt.grid(True)
    plt.legend()
    plt.show()


def plot_word_length_distribution_subplot(text):
    words = text.split()
    word_lengths = [len(word) for word in words]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.hist(word_lengths, bins=range(1, 21), edgecolor='black', color='pink')
    plt.xlabel('Длина слова')
    plt.ylabel('Количество слов')
    plt.title('Распределение длины слов')
    plt.grid(axis='y')
    plt.xticks(range(1, 21))

    plt.subplot(1, 2, 2)
    short_words = len([word for word in words if 1 <= len(word) <= 4])
    medium_words = len([word for word in words if 5 <= len(word) <= 8])
    long_words = len([word for word in words if len(word) >= 9])
    sizes = [short_words, medium_words, long_words]
    labels = ['1-4 символа', '5-8 символов', '9+ символов']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['pink', 'mediumvioletred', 'hotpink'])
    plt.title('Доли слов разной длины')

    plt.tight_layout()
    plt.show()


def plot_word_frequency_length_subplot(text):
    words = text.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(10)
    common_words, common_counts = zip(*most_common)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.bar(common_words, common_counts, color='pink')
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.title('Топ-10 самых частых слов')
    plt.grid(axis='y')
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    word_lengths = [len(word) for word in words]
    plt.hist(word_lengths, bins=range(1, max(word_lengths) + 1), edgecolor='black', color='pink')
    plt.xlabel('Длина слова')
    plt.ylabel('Количество слов')
    plt.title('Распределение длины слов')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def plot_vowel_consonant_distribution(text):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    consonant_count = sum(1 for char in text.lower() if char in consonants)
    labels = ['Гласные', 'Согласные']
    counts = [vowel_count, consonant_count]
    plt.bar(labels, counts, color='pink')
    plt.xlabel('Тип букв')
    plt.ylabel('Количество')
    plt.title('Частотность гласных и согласных')
    plt.grid(axis='y')
    plt.show()


def plot_word_initial_distribution(text):
    initial_counts = defaultdict(int)
    for word in text.split():
        if word:
            initial_counts[word[0].lower()] += 1
    letters, counts = zip(*sorted(initial_counts.items()))
    plt.bar(letters, counts, color='pink')
    plt.xlabel('Начальная буква')
    plt.ylabel('Количество слов')
    plt.title('Распределение слов по начальным буквам')
    plt.grid(axis='y')
    plt.show()


def plot_digit_frequency(text):
    digits = [char for char in text if char.isdigit()]
    digit_counts = Counter(digits)
    digits, counts = zip(*digit_counts.items())
    plt.bar(digits, counts, color='pink')
    plt.xlabel('Цифры')
    plt.ylabel('Частота')
    plt.title('Частота использования цифр')
    plt.grid(axis='y')
    plt.show()


def plot_word_sentence_comparison(text):
    pattern = r'\b(\d+)\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    word_counts = []
    sentence_counts = []

    for i, chapter in enumerate(chapters):
        words = chapter.split()
        sentences = re.split(r'[.!?]', chapter)
        sentences = [s for s in sentences if s.strip()]

        word_counts.append(len(words))
        sentence_counts.append(len(sentences))

    plt.figure(figsize=(10, 5))
    plt.plot(word_counts, label='Слова', color='hotpink', marker='o')
    plt.plot(sentence_counts, label='Предложения', color='pink', linestyle='--', marker='s')
    plt.xlabel('Глава')
    plt.ylabel('Количество')
    plt.title('Сравнение слов и предложений по главам')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_word_sentence_length_comparison(text):
    if not text.strip():
        print("Ошибка: текст пустой.")
        return

    pattern = r'\b(\d+)\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    avg_word_lengths = []
    avg_sentence_counts = []

    for i, chapter in enumerate(chapters):
        words = chapter.split()
        sentences = re.split(r'[.!?]', chapter)
        sentences = [s for s in sentences if s.strip()]
        avg_word_length = sum(len(word) for word in words) / len(words)
        avg_sentence_count = len(sentences)
        avg_word_lengths.append(avg_word_length)
        avg_sentence_counts.append(avg_sentence_count)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(avg_word_lengths, label='Средняя длина слов', color='pink', marker='o')
    plt.xlabel('Глава')
    plt.ylabel('Средняя длина слов')
    plt.title('Средняя длина слов по главам')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.bar(range(1, len(avg_sentence_counts) + 1), avg_sentence_counts, color='hotpink')
    plt.xlabel('Глава')
    plt.ylabel('Количество предложений')
    plt.title('Количество предложений по главам')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def plot_pos_proportion(text):
    pattern = r'\b(\d+)\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    pos_proportions = {'существительные': [], 'глаголы': [], 'прилагательные': []}
    pos_counts = {'существительные': [], 'глаголы': [], 'прилагательные': []}

    for i, chapter in enumerate(chapters):
        doc = nlp(chapter)
        counts = {'существительные': 0, 'глаголы': 0, 'прилагательные': 0}

        for token in doc:
            if token.pos_ == "NOUN":
                counts['существительные'] += 1
            elif token.pos_ == "VERB":
                counts['глаголы'] += 1
            elif token.pos_ == "ADJ":
                counts['прилагательные'] += 1

        total = sum(counts.values())

        for key in pos_proportions:
            pos_proportions[key].append(counts[key] / total if total > 0 else 0)
            pos_counts[key].append(counts[key])

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    colors = {'существительные': 'hotpink', 'глаголы': 'deeppink', 'прилагательные': 'pink'}
    for key, values in pos_proportions.items():
        plt.plot(values, label=key, marker='o', color=colors[key])
    plt.xlabel('Глава')
    plt.ylabel('Доля')
    plt.title('Пропорции частей речи по главам')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    x = range(1, len(pos_counts['существительные']) + 1)
    width = 0.2
    plt.bar([i - width for i in x], pos_counts['существительные'], width=width, label='Существительные',
            color='hotpink')
    plt.bar(x, pos_counts['глаголы'], width=width, label='Глаголы', color='deeppink')
    plt.bar([i + width for i in x], pos_counts['прилагательные'], width=width, label='Прилагательные', color='pink')
    plt.xlabel('Глава')
    plt.ylabel('Количество')
    plt.title('Абсолютная частота частей речи по главам')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def plot_punctuation_frequency(text):
    pattern = r'\b(\d+)\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    comma_counts = []
    period_counts = []
    exclamation_counts = []

    for i, chapter in enumerate(chapters):
        comma_counts.append(chapter.count(','))
        period_counts.append(chapter.count('.'))
        exclamation_counts.append(chapter.count('!'))

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(comma_counts, label='Запятые', color='pink', marker='o')
    plt.plot(period_counts, label='Точки', color='hotpink', marker='s')
    plt.plot(exclamation_counts, label='Восклицательные знаки', color='deeppink', marker='^')
    plt.xlabel('Глава')
    plt.ylabel('Частота')
    plt.title('Частота знаков препинания по главам')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    total_counts = [sum(comma_counts), sum(period_counts), sum(exclamation_counts)]
    labels = ['Запятые', 'Точки', 'Восклицательные знаки']
    plt.bar(labels, total_counts, color=['pink', 'hotpink', 'deeppink'])
    plt.xlabel('Знаки препинания')
    plt.ylabel('Общее количество')
    plt.title('Общее количество знаков препинания')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def plot_verb_tenses_comparison(text, window_size=100):
    doc = nlp(text)
    words = [token.text for token in doc]
    tenses = {'прошедшее': [], 'настоящее': [], 'будущее': []}
    total_verbs = []

    for i in range(0, len(words), window_size):
        window = words[i:i + window_size]
        counts = {'прошедшее': 0, 'настоящее': 0, 'будущее': 0}

        for word in window:
            token = nlp(word)[0]
            if token.pos_ == "VERB":
                morph = token.morph
                if "Tense=Past" in morph:
                    counts['прошедшее'] += 1
                elif "Tense=Pres" in morph:
                    counts['настоящее'] += 1
                elif "Tense=Fut" in morph:
                    counts['будущее'] += 1

        total = sum(counts.values())
        if total > 0:
            for tense in tenses:
                tenses[tense].append(counts[tense] / total * 100)  # Процентное содержание
        else:
            for tense in tenses:
                tenses[tense].append(0)

        total_verbs.append(sum(counts.values()))

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    for tense, values in tenses.items():
        colors = {'прошедшее': 'hotpink', 'настоящее': 'deeppink', 'будущее': 'pink'}
        plt.plot(values, label=tense, marker='o', color=colors[tense])
    plt.xlabel('Окна текста')
    plt.ylabel('Процентное содержание')
    plt.title('Процентное содержание времен глаголов')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    total_counts = {tense: sum(values) for tense, values in tenses.items()}
    plt.bar(total_counts.keys(), total_counts.values(), color=['hotpink', 'deeppink', 'pink'])
    plt.xlabel('Время глагола')
    plt.ylabel('Абсолютная частота')
    plt.title('Абсолютная частота времен глаголов')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()


def get_keywords_from_user():
    keywords_input = input("Введите ключевые слова через запятую: ")
    keywords = [keyword.strip() for keyword in keywords_input.split(",")]
    return keywords


def plot_keyword_dynamics(text, keywords, window_size=100):
    words = text.split()
    num_windows = (len(words) // window_size) + 1
    keyword_counts = {keyword: [0] * num_windows for keyword in keywords}

    for i in range(num_windows):
        start = i * window_size
        end = start + window_size
        window = words[start:end]

        for keyword in keywords:
            keyword_counts[keyword][i] = window.count(keyword)

    cmap = plt.cm.Reds_r
    num_colors = max(1, len(keywords))
    colors = [cmap(i / (num_colors - 1)) for i in range(num_colors)]

    plt.figure(figsize=(10, 6))
    for i, (keyword, counts) in enumerate(keyword_counts.items()):
        plt.plot(counts, label=keyword, color=colors[i % len(colors)], marker='o')

    plt.xlabel('Окна текста')
    plt.ylabel('Количество появлений')
    plt.title('Динамика появления ключевых слов')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_complex_simple_words(text, threshold=8):
    pattern = r'\b(\d+)\s+глава\b'
    chapters = re.split(pattern, text)
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    complex_word_counts = []
    simple_word_counts = []

    for i, chapter in enumerate(chapters):
        words = chapter.split()
        complex_words = [word for word in words if len(word) > threshold]
        simple_words = [word for word in words if len(word) <= threshold]

        complex_word_counts.append(len(complex_words))
        simple_word_counts.append(len(simple_words))

    total_words = [complex + simple for complex, simple in zip(complex_word_counts, simple_word_counts)]
    complex_percent = [complex / total * 100 if total > 0 else 0 for complex, total in
                       zip(complex_word_counts, total_words)]
    simple_percent = [simple / total * 100 if total > 0 else 0 for simple, total in
                      zip(simple_word_counts, total_words)]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(complex_percent, label='Сложные слова', color='pink', marker='o')
    plt.plot(simple_percent, label='Простые слова', color='deeppink', marker='s')
    plt.xlabel('Глава')
    plt.ylabel('Процентное содержание')
    plt.title('Процентное содержание слов по главам')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.bar(range(1, len(chapters) + 1), complex_word_counts, label='Сложные слова', color='pink')
    plt.bar(range(1, len(chapters) + 1), simple_word_counts, label='Простые слова', color='deeppink',
            bottom=complex_word_counts)
    plt.xlabel('Глава')
    plt.ylabel('Количество слов')
    plt.title('Абсолютная частота слов по главам')
    plt.legend()
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()
