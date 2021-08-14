from deep_translator import GoogleTranslator

eng_file = open("text_4.txt", "r")
rus_file = open("text_4_rus.txt", "w")

for line in eng_file:
    rus_file = open("text_4_rus.txt", "a")
    to_translate = (line)
    translated = GoogleTranslator(source='auto', target='ru').translate(to_translate)
    rus_file.write(translated)
    rus_file.write("\n")
eng_file.close()
rus_file.close()

