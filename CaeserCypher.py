def translate(text, offset) -> str:
    num = [(ord(c.lower()) - 97 + offset) % 26 + 97 if not c == " " else 32 for c in text]
    return "".join([chr(n) for n in num])


text = "Esp njmpcnspq td nzzvtyr fa l dezcx"
for i in range(26):
    print(translate(text, i) + '!')
