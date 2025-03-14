from collections import defaultdict
import re


def sentence_analysis(text):
    sentences = re.findall(r'[^.!?]+[.!?]', text, re.DOTALL)
    sentences = [s for s in sentences if s.strip()]

    types = {'Повествовательные': 0, 'Вопросительные': 0, 'Восклицательные': 0}
    for sentence in sentences:
        if sentence.endswith('.'):
            types['Повествовательные'] += 1
        elif sentence.endswith('?'):
            types['Вопросительные'] += 1
        elif sentence.endswith('!'):
            types['Восклицательные'] += 1

    return types

from collections import defaultdict

def find_anagrams(text):
    words = text.split()
    anagrams = defaultdict(list)

    for word in words:
        if len(word) >= 3:
            lower_word = word.lower()
            sorted_word = ''.join(sorted(lower_word))
            anagrams[sorted_word].append(lower_word)

    unique_anagrams = [list(set(group)) for group in anagrams.values() if len(set(group)) > 1]

    return unique_anagrams


def find_palindromes(text):
    words = text.split()
    palindromes = {word for word in words if word == word[::-1] and len(word) >= 3}
    return sorted(palindromes)


def find_words_by_pattern(text, pattern):
    return re.findall(pattern, text)

