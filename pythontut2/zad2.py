def dataFunction(data_text):
    slownik = dict({
        "length":len(data_text),
        "letters": set(data_text),
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    })
    return slownik


text = "heheszki"
print(dataFunction(text)["length"])
print(dataFunction(text)["letters"])
print(dataFunction(text)["big_letters"])
print(dataFunction(text)["small_letters"])