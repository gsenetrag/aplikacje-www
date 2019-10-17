studenci = [
    {"nrIndex":144441,"Imie":"Zdzisiu","Nazwisko":"Wszywka"},
    {"nrIndex":144442,"Imie":"Jacek","Nazwisko":"Kaczmarski"},
    {"nrIndex":144443,"Imie":"Alex","Nazwisko":"Kwaśniewski"},
    ]

studenci.append({
    "nrIndex":144444,
    "Imie":"Adam",
    "Nazwisko":"Malysz",
    "Wiek":23,
    "Email":"malysz@wp.pl",
    "RokUrodzenia":1996,
    "Adres":"Malysza 45"
    })

studenci.append({
    "nrIndex":144445,
    "Imie":"Juzef",
    "Nazwisko":"Pilsudski",
    "Wiek":18,
    "Email":"ziuk@wp.pl",
    "RokUrodzenia":2000,
    "Adres":"Al. Pilsudskiego 44"
    })

for student in studenci:
    print(student["Imie"])