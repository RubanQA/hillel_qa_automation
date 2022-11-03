# 1. Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'
word = input('Enter your word: ').casefold()
print('+' if word == word[:: -1] and word.isalpha() else '-')

# 2. Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
text = input('Enter text: ').casefold()
f_word = input('Enter a search word: ').casefold()
if len(f_word) <= 0:
    print("Please, try enter search word!")
elif f_word in text:
    print("YES")
else:
    print("NO")

# 3. Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www',
# иначе добавить в конец строки 'zzz'.
word = input('Enter your word: ').casefold()
if word.startswith('abc'):
    word = word.replace('abc', 'www')
else:
    word += 'zzz'
print(word)

# 4. Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
text = input('Enter text: ')
for i in text:
    if i.isdigit():
        text = text.replace(i, '')
print(text)

# 5. Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
# что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"
email = input('Enter your email: ')
if len(email) >= 3 and '@' in email and '.' in email and " " not in email:
    print("YES")
else:
    print("NO")