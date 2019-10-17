data = [
    {"kraj":"Polska","sklad":
        {
            "trener":{"imie":"Jerzy","nazwisko":"Brzęczek"},
            "zawodnicy":(
                {"nr":9,"imie":"Robert","nazwisko":"Lewandowski","ilosc_bramek":10},
                {"nr":7,"imie":"Arkadiusz","nazwisko":"Milik","ilosc_bramek":5},
                {"nr":1,"imie":"Wojciech","nazwisko":"Szczesny","ilosc_bramek":0}
            )
        }
    },
    {
        "ksiazka":
        {
            "tytul":"Harry Potter fabryka czekolady",
            "autor":"J. K. Mikke"
        }
    }
]



print(
    data[0]["sklad"]["zawodnicy"][0]["imie"] + " "
    + data[0]["sklad"]["zawodnicy"][0]["nazwisko"]
    + " jest zawodnikiem z "
    + data[0]["kraj"][0:5] + "i "
    + "i czyta książkę pod tytułem \""
    + data[1]["ksiazka"]["tytul"] + "\" "
    + "autorstwa " + data[1]["ksiazka"]["autor"] + "go"
    )