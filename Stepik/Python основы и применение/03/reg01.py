import re

pattern = r"a[abc]c"
string = "abc, acc, aac"
all_inclusion = re.findall(pattern, string)
print(all_inclusion)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)