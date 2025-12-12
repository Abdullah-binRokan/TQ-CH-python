from typing import List

def stripNoise(text: str) -> str:
    # write your code here ^_^
    cleanText = ""
  
    for char in text:
        print("char:", char)
        if char.isalpha() or char.isdigit() :
            cleanText += char
            print("cleanText:", cleanText)

    return str(cleanText)

stripNoise("Att@ck#2024!!")