import re

pattern = r"(\w+)-\1"
string = "test-test chow-chow"
match = re.match(pattern, string)
print(match)

duplicates = re.sub(pattern, r"\1", string)
print(duplicates)