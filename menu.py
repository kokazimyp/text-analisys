from text_loader import load_text
from text_cleaner import clean_text, manage_stop_words
from text_analyzer import find_anagrams, find_palindromes, find_words_by_pattern, sentence_analysis
from frequency_analyzer import count_characters, count_words, count_sentences, average_word_length, \
    average_sentence_length
from visualization import plot_word_frequency, plot_sentence_types, plot_word_length_distribution, \
    plot_average_sentence_length, plot_character_frequency, plot_verb_tenses, plot_unique_words_dynamics, \
    plot_pos_distribution, plot_vowel_consonant_distribution, plot_word_length_distribution_subplot, \
    plot_word_frequency_length_subplot, plot_word_initial_distribution, plot_digit_frequency, \
    plot_word_sentence_comparison, plot_word_sentence_length_comparison, plot_pos_proportion, \
    plot_punctuation_frequency, plot_verb_tenses_comparison, plot_keyword_dynamics, get_keywords_from_user, \
    plot_complex_simple_words, plot_word_length_distribution_bywords
from database_manager import save_text_to_db, save_word_frequencies, save_sentence_analysis
from advanced_analyzer import find_rhetorical_devices, find_borrowed_words, load_borrowed_words
from create_database import create_tables
from tabulate import tabulate


def show_menu():
    print("\n╔════════════════════════════════════════╗")
    print("╠═════════════════ Меню ═════════════════╣")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Создать базу данных                 ║")
    print("╠════════════════════════════════════════╣")
    print("║ 2. Загрузить текст                     ║")
    print("╠════════════════════════════════════════╣")
    print("║ 3. Очистить текст                      ║")
    print("╠════════════════════════════════════════╣")
    print("║ 4. Управление стоп-словами             ║")
    print("╠════════════════════════════════════════╣")
    print("║ 5. Поиск анаграмм                      ║")
    print("╠════════════════════════════════════════╣")
    print("║ 6. Поиск палиндромов                   ║")
    print("╠════════════════════════════════════════╣")
    print("║ 7. Поиск слов по шаблону               ║")
    print("╠════════════════════════════════════════╣")
    print("║ 8. Частотный анализ                    ║")
    print("╠════════════════════════════════════════╣")
    print("║ 9. Визуализация данных                 ║")
    print("╠════════════════════════════════════════╣")
    print("║ 10. Сохранить результаты в базу данных ║")
    print("╠════════════════════════════════════════╣")
    print("║ 11. Расширенный анализ текста          ║")
    print("╠════════════════════════════════════════╣")
    print("║ 12. Анализ типов предложений           ║")
    print("╠════════════════════════════════════════╣")
    print("║ 13. Выход                              ║")
    print("╚════════════════════════════════════════╝")


def main():
    text = None
    stop_words = []
    cleaned_text = None
    cleaned_text_without_punctuation = None
    keyword = []
    text_id = None
    db_path = 'text_analysis.db'

    while True:
        show_menu()
        choice = input("\nВыберите опцию: ")

        if choice == '1':
            create_tables(db_path)
            print("\nБаза данных создана")
            continue

        if choice == '2':
            file_path = input("\nВведите путь к файлу: ")
            text = load_text(file_path)
            if text:
                print("\nТекст успешно загружен.")
            else:
                print("\nОшибка при загрузке текста.")

        elif choice == '3':
            if text:
                cleaned_text = clean_text(text)
                cleaned_text_without_punctuation = clean_text(text, remove_punctuation=True)
                print("\nТекст очищен.")
            else:
                print("\nСначала загрузите текст.")

        elif choice == '4':
            if text:
                action = input("\nВведите действие (add/remove): ")
                word = input("\nВведите слово: ")
                stop_words = manage_stop_words(stop_words, action, word)
            else:
                print("Сначала загрузите текст.")

        elif choice == '5':
            if cleaned_text_without_punctuation:
                anagrams = find_anagrams(cleaned_text_without_punctuation)
                print(tabulate(anagrams, tablefmt="rounded_grid"))
            else:
                print("\nСначала очистите текст.")

        elif choice == '6':
            if cleaned_text:
                palindromes = find_palindromes(cleaned_text)
                table_data = [[word] for word in palindromes]

                print("\nНайденные палиндромы:")
                print(tabulate(table_data, headers=["Палиндром"], tablefmt="rounded_grid", stralign="center"))
            else:
                print("\nСначала очистите текст.")

        elif choice == '7':
            if cleaned_text:
                pattern = input("\nВведите регулярное выражение для поиска: ")
                matches = find_words_by_pattern(cleaned_text, pattern)
                table = [[match] for match in matches]
                print("\nНайденные слова по шаблону:")
                print(tabulate(table, headers=["Слова"], tablefmt="rounded_grid"))
            else:
                print("\nСначала очистите текст.")

        elif choice == '8':
            if cleaned_text:
                stats = [
                    ["Количество символов", f"{count_characters(cleaned_text):,}"],
                    ["Количество слов", f"{count_words(cleaned_text):,}"],
                    ["Количество предложений", f"{count_sentences(cleaned_text):,}"],
                    ["Средняя длина слов", f"{average_word_length(cleaned_text):.2f}"],
                    ["Средняя длина предложений", f"{average_sentence_length(cleaned_text):.2f}"]
                ]

                print(tabulate(stats, tablefmt="rounded_grid", numalign="right", stralign="left"))
            else:
                print("\nСначала очистите текст.")

        elif choice == '9':
            if cleaned_text:
                print("\n╔══════════════════════════════════════════════════════════════════════╗")
                print("╠═════════════════════════ Меню визуализации ══════════════════════════╣")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 1. Гистограмма частотности слов                                      ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 2. Круговая диаграмма типов предложений                              ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 3. Гистограмма распределения слов по длине                           ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 4. График средней длины предложений по главам                        ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 5. Столбчатая диаграмма частоты символов                             ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 6. График распределения длины слов в тексте                          ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 7. График использования глаголов по временам                         ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 8. График динамики уникальных слов                                   ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 9. График долей частей речи                                          ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 10. График анализ распределения и частотности слов с разной длиной   ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 11. График частотности слов и их длина                               ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 12. График анализа гласных и согласных                               ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 13. График распределения слов по начальным буквам                    ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 14. График частоты использования цифр                                ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 15. График сравнительного анализа слов и предложений                 ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 16. График сравнительного анализа длины слов и предложений           ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 17. График пропорций частей речи                                     ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 18. График частоты знаков препинания                                 ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 19. График использования времен глаголов                             ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 20. График динамики ключевых слов                                    ║")
                print("╠══════════════════════════════════════════════════════════════════════╣")
                print("║ 21. График частотности сложных и простых слов                        ║")
                print("╚══════════════════════════════════════════════════════════════════════╝")
                viz_choice = input("\nВыберите тип визуализации: ")
                if viz_choice == '1':
                    top_n = int(input("\nВведите количество самых частоных слов для визуализации: "))
                    plot_word_frequency(cleaned_text_without_punctuation, top_n)
                elif viz_choice == '2':
                    plot_sentence_types(cleaned_text)
                elif viz_choice == '3':
                    plot_word_length_distribution_bywords(cleaned_text)
                elif viz_choice == '4':
                    plot_average_sentence_length(cleaned_text)
                elif viz_choice == '5':
                    plot_character_frequency(cleaned_text)
                elif viz_choice == '6':
                    plot_word_length_distribution(cleaned_text)
                elif viz_choice == '7':
                    plot_verb_tenses(cleaned_text)
                elif viz_choice == '8':
                    plot_unique_words_dynamics(cleaned_text)
                elif viz_choice == '9':
                    plot_pos_distribution(cleaned_text)
                elif viz_choice == '10':
                    plot_word_length_distribution_subplot(cleaned_text)
                elif viz_choice == '11':
                    plot_word_frequency_length_subplot(cleaned_text)
                elif viz_choice == '12':
                    plot_vowel_consonant_distribution(cleaned_text)
                elif viz_choice == '13':
                    plot_word_initial_distribution(cleaned_text_without_punctuation)
                elif viz_choice == '14':
                    plot_digit_frequency(cleaned_text)
                elif viz_choice == '15':
                    plot_word_sentence_comparison(cleaned_text)
                elif viz_choice == '16':
                    plot_word_sentence_length_comparison(cleaned_text)
                elif viz_choice == '17':
                    plot_pos_proportion(cleaned_text)
                elif viz_choice == '18':
                    plot_punctuation_frequency(cleaned_text)
                elif viz_choice == '19':
                    plot_verb_tenses_comparison(cleaned_text)
                elif viz_choice == '20':
                    keyword = get_keywords_from_user()
                    plot_keyword_dynamics(cleaned_text, keyword)
                elif viz_choice == '21':
                    plot_complex_simple_words(cleaned_text)
                else:
                    print("\nНеверный выбор.")
            else:
                print("\nСначала очистите текст.")

        elif choice == '10':
            if cleaned_text:
                text_id = save_text_to_db(cleaned_text)
                save_word_frequencies(cleaned_text_without_punctuation, text_id)
                save_sentence_analysis(cleaned_text, text_id)
                print("\nРезультаты сохранены в базу данных.")
            else:
                print("\nСначала очистите текст.")

        elif choice == '11':
            if cleaned_text:
                print("\n╔════════════════════════════════════════╗")
                print("║ 1. Анализ риторических приемов         ║")
                print("╠════════════════════════════════════════╣")
                print("║ 2. Анализ заимствованных слов          ║")
                print("╚════════════════════════════════════════╝")
                advanced_choice = input("\nВыберите тип анализа: ")
                if advanced_choice == '1':
                    print("\n")
                    found_devices = find_rhetorical_devices(cleaned_text)
                    table_data = [[device, count] for device, count in found_devices.items()]

                    print(tabulate(table_data, tablefmt="rounded_grid",
                                   numalign="right", stralign="left"))

                elif advanced_choice == '2':
                    borrowed_words_path = input("\nВведите путь к файлу с заимствованными словами:")
                    borrowed_words = load_borrowed_words(borrowed_words_path)
                    if isinstance(borrowed_words, str):
                        print(borrowed_words)
                    else:
                        found_borrowed = find_borrowed_words(cleaned_text, borrowed_words)

                        if found_borrowed:
                            table_data = [[word] for word in found_borrowed]
                            print("\nНайденные заимствованные слова:")
                            print(tabulate(table_data, tablefmt="rounded_grid", stralign="center"))
                        else:
                            print("\nЗаимствованных слов не найдено.")
                else:
                    print("\nНеверный выбор.")
            else:
                print("\nСначала очистите текст.")

        elif choice == '12':
            if cleaned_text:
                analize_result = sentence_analysis(cleaned_text)

                table_data = [[type, value] for type, value in
                              analize_result.items()]  # Преобразуем словарь в список для таблицы

                print("\nРезультат анализа:")
                print(tabulate(table_data, headers=["Тип", "Количество"], tablefmt="rounded_grid", numalign="right",
                               stralign="left"))
            else:
                print("\nСначала очистите текст.")

        elif choice == '13':
            print("\n╔══════════════════════╗")
            print("║ Выход из программы.  ║")
            print("╚══════════════════════╝")
            break

        else:
            print("\nНеверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
