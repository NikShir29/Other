file_name_1 = "text_1.txt"
content = "Съешь ещё этих мягких французских булок,\nда выпей же чаю.\n "
with open(file_name_1, 'w', encoding='utf-8') as file:
    file.write(content)

file_name_2 = "text_2.txt"
content_2 = "Питончики.\n "
with open(file_name_2, 'w', encoding='utf-8') as file:
    file.write(content_2)

choice = input("""Введите название файла, который необходимо открыть.
Доступные варианты:
text_1.txt
text_2.txt:
""")

if choice in ['text_1.txt', 'text_2.txt']:
    filename = file_name_1 if choice == 'text_1.txt' else file_name_2
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_lines = len(lines)
            empty_lines = sum(1 for line in lines if line.strip() == '')
            non_empty_lines = total_lines - empty_lines

            file.seek(0)
            content = file.read()
            word_count = len(content.split())
            char_count = len(content)

            print(f"Файл: {choice}")
            print(f"Общее количество строк: {total_lines}")
            print(f"Пустых строк: {empty_lines}")
            print(f"Непустых строк: {non_empty_lines}")
            print(f"Количество слов: {word_count}")
            print(f"Количество символов: {char_count}")

            choice_save = input("Сохранить анализ в новый файл? Y/N: ")
            if choice_save in ['Y', 'y']:
                with open("report.txt", 'w', encoding='utf-8') as report_file:
                    report_file.write(f"""
    Файл: {choice}
    Общее количество строк: {total_lines}
    Пустых строк: {empty_lines}
    Непустых строк: {non_empty_lines}
    Количество слов: {word_count}
    Количество символов: {char_count}""")
                print("Работа успешно завершена.")
            elif choice_save in ['N', 'n']:
                print("Работа успешно завершена.")
    except PermissionError:
        print(f"Ошибка: Нет прав на запись в файл {filename}")
    except IOError as e:
        print(f"Ошибка ввода-вывода при создании файла {filename}: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка при создании файла {filename}: {e}")
else:
    print("Файл не найден.")
