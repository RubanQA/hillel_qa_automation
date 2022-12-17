# сть фрагмент текста, состоящий из предложений.
# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным
# или восклицательным знаком (или несколькими такими знаками). Слова состоят только из латинских букв, разделяются
# отделяются пробелами или запятыми с пробелами. Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.

import re

text = """Hello, cocroach. And where it is? Who, can - Do it?! Or vice versa!? Yes, it's difficult... Claro..
Hola..."""
pattern = "([A-Z][a-z]*)|[.!?] ([A-Z][a-z]*)|\n([A-Z][a-z]*)"

def generate_sentence(text: str) -> str:

    pattern = '([A-Z][a-zA-Z]*),?\s?.*?[?.!]+'
    re_obj = re.compile(pattern)
    res = re_obj.findall(text)
    res2 = ''
    for i, word in enumerate(res):
        if i == 0:
            res2 += word + ' '
        else:
            res2 += word.lower() + ' '
    res2 = res2.strip() + '.'
    return res2
print(generate_sentence(text))
