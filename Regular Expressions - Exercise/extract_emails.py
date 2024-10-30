import re

text = input()
pattern = re.compile(r"(^|(?<=\s))([a-z0-9]+[\w.-]*)@([a-z\-_]+)(\.[a-z]+)+\b")
emails = pattern.finditer(text)
for email in emails:
    print(email.group())

