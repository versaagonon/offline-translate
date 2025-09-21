import argostranslate.translate
from langdetect import detect

while True:
    text = input("Input (input 'exit' to exit): ")
    if text.lower() == "exit":
        break
    src_lang = detect(text)
    installed_langs = argostranslate.translate.get_installed_languages()
    from_lang = next(filter(lambda l: l.code == src_lang, installed_langs))
    to_lang = next(filter(lambda l: l.code == "en", installed_langs))
    translated_text = from_lang.get_translation(to_lang).translate(text)

    print(f"Detected: {src_lang} | Output: {translated_text}")
