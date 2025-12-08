file_name_1 = "text_1.txt"
content = "Съешь ещё этих мягких французских булок,\nда выпей же чаю."

with open(file_name_1, 'w', encoding='utf-8') as file:
    file.write(content)

file_name_2 = "text_2.txt"
content_2 = "Питончики."

with open(file_name_2, 'w', encoding='utf-8') as file:
    file.write(content_2)
with open(file_name_2, 'r', encoding='utf-8') as file:
    content_2 = file.read()

choice = input("""Введите название файла, который необходимо открыть.
Доступные варианты:
text_1.txt
text_2.txt:
""")

word_count = 0
if choice == 'text_1.txt':
    with open(file_name_1, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        words = file.read().split()
        word_count = len(words)
        print(num_lines)
        print(word_count)
        print(words)
