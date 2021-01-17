from translate import Translator
translator= Translator(from_lang=input("Enter Source Language\n"),to_lang=input("Enter Destination Language\n"))
try:
    translation = translator.translate(input("Enter Text\n"))
    print(translation)
except:
    print("Connection Error Retry")