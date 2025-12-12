from typing import List

def stripNoise(text: str) -> str:
    # write your code here ^_^
    cleanText = ""
    punctuation = ["#", "@", "%", "!", "-", "_", "…"]
    for char in text:
        print("char:", char)
        if char not in punctuation:
            cleanText += char
            print("cleanText:", cleanText)

    return str(cleanText)

stripNoise("___")