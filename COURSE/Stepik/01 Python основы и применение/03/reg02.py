import re
# [] -- можно указать множество подходящих символов
# . ^ $ * + ? {} [] \ | () --метасимволы
# \d -- [0-9] -- цифры
# \D -- [^0-9] -- не цифры
# \s -- [ \t\n\r\f\v] -- пробельные символы
# \S -- [^ \t\n\r\f\v] --
# \w -- [a-zA-Z0-9_] -- буквы + цифры + _
# \W -- [a-zA-Z0-9_] --

pattern = r" english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)