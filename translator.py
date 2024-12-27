from deep_translator import GoogleTranslator

def translate(text, lang):
    translated = GoogleTranslator(source='auto', target=lang)
    result = translated.translate(text)
    print(result)

translate(text=input("Text: "), lang=input("Select language: "))