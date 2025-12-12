from typing import List
import string
def stripNoise(text: str) -> str:
    # write your code here ^_^
    cleanText = ""
    for char in text:
        print("char: ", char)
        if char not in string.punctuation:
            cleanText += char
            print("cleanText: ", cleanText)

    return str(cleanText)

stripNoise("___")