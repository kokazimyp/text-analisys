import re


def count_characters(text):
    return len(text)


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    sentence_endings = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s')

    sentences = sentence_endings.split(text)

    sentences = [s for s in sentences if s.strip()]

    return len(sentences)


def average_word_length(text):
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def average_sentence_length(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s for s in sentences if s.strip()]
    if not sentences:
        return 0
    total_words = sum(len(s.split()) for s in sentences)
    return total_words / len(sentences)

