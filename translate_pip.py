from translate import Translator

translator = Translator(to_lang="de")
translation = translator.translate("Hello, my name is Ogata. I'm from brazil. I'm a student.")
print(translation)