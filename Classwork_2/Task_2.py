text = input("Введите текст: ")

count_of_words = 0
for word in text.split():
    count_of_words += 1
print(f"Количество слов: {count_of_words}")

list_of_symbols = ["!", "?", ".", ","]
count_of_symbols = 0
for symbol in text:
    if symbol in list_of_symbols:
        count_of_symbols += 1
print(f"Количество символов: {count_of_symbols}")

vowels = "аеёиоуыэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
count_of_vowels = 0
count_of_consonants = 0
for vowel in text:
    if vowel in vowels:
        count_of_vowels += 1
print(f"Количество гласных: {count_of_vowels}")
for consonant in text:
    if consonant in consonants:
        count_of_consonants += 1
print(f"Количество согласных: {count_of_consonants}")

longest_word_length = 0
longest_word = ""
for word in text.split():
    if len(word) > longest_word_length:
        longest_word_length = len(word)
        longest_word = word
print(f"Самое длинное слово: {longest_word}")