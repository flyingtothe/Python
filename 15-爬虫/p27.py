import re

pattern = re.compile(r'\d+')

s = pattern.findall('i an 18 years ols and 185 high')
print(s)

s = pattern.finditer('i an 18 years ols and 185 high')
print(type(s))

for i in s:
    print(i.group())