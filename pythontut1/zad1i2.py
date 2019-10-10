lorem = "Czym jest Lorem Ipsum? Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

def zad2(text, a, b):
    i = 0
    j = 0
    for z in text:
        if b == z:
            i = i+1

        if a == z:
            j = j+1
    return [i,j]

#zad 2
imie = "Grzegorz"
nazwisko = "Senetra"
wyn1 = str(zad2(lorem,nazwisko[2],imie[1])[0])
wyn2 = str(zad2(lorem,nazwisko[2],imie[1])[1])
print("W tekście jest "+wyn1+" liter "+nazwisko[2]+" oraz "+wyn2+" liter "+imie[1])



