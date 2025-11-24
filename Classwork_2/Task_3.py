text = input("Введите текст: ")

number_of_sentences = text.count(".")
print(f"Количество предложений: {number_of_sentences}")

number_of_words = len(text.split())
print(f"Количество слов: {number_of_words}")

punctuation_marks = ["!", "?", ",", "."]
number_of_marks = 0
for mark in text:
    if mark in punctuation_marks:
        number_of_marks += 1
print(f"Количество знаков препинания: {number_of_marks}")