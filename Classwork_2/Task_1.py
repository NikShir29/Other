text = input("Введите текст: ")
banned_words = input("Введите список запрещенных слов через пробел: ").lower()
banned_list = banned_words.split()
text_list = text.split()
new_text = None

for word in text_list:
    if word.lower() in banned_list:
        new_text = text.replace(word, "***")
        text = new_text

if new_text:
    print(new_text)
else:
    print(text)