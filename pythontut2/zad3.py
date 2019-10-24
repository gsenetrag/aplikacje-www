def deleteLetterFromText(text, _letter):
    textWithoutLetter = ''
    for letter in text:
        if letter != _letter:
            textWithoutLetter += letter
    return textWithoutLetter


text = "qwertyton"
print(deleteLetterFromText(text,'t'))