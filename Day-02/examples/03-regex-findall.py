import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

pattern = r'\d+'
text= "There are 120 apples and 45 oranges in shop"
matches = re.findall(pattern, text)
print(matches)