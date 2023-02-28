ASCII_UPPER_A = 65
ASCII_LOWER_Z = 122
ASCII_LOWER_A = 97


def cipher(text, offset) -> str:
    # old method:
    # num = [(ord(c.lower()) - 97 + offset) % 26 + 97 if 97 <= ord(c.lower()) <= 122 else ord(c) for c in text]
    # return ''.join([chr(n) for n in num])

    def shift(char) -> str:
        if ASCII_LOWER_A <= ord(char.lower()) <= ASCII_LOWER_Z:
            start = ASCII_LOWER_A if char.islower() else ASCII_UPPER_A
            char = chr((ord(char) - start + offset) % 26 + start)
        return char
    return ''.join([shift(char) for char in text])


t = "What? Text that you will never be able to read? 1mp0551bl3!"
o = 15
print(f"The text '{t}' was translated by {o} characters to produce '{cipher(t, o)}'.")
