import re

#print(re.match)
#print(re.search)
#print(re.findall)
#print(re.sub)

# [] можно указать множество подходящих символов
pattern = r"abc"
string = "babcd"
match_object = re.match(pattern, string)
print(match_object)
match_object = re.search(pattern, string)
print(match_object)

pattern = r"a[abc]c"
string = "aac"
match_object = re.match(pattern, string)
print(match_object)
