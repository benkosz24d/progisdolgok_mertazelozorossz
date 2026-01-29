def ora_perc(percek):
    ora = percek // 60
    perc = percek % 60
    return ora, perc


def filmek_bekerese():
    filmek = []
    for i in range(3):
        cim = input("Add meg a film címét: ")
        hossz = int(input("Add meg a film hosszát percben: "))
        filmek.append((cim, hossz))
    return filmek


filmek = filmek_bekerese()

for film in filmek:
    cim = film[0]
    percek = film[1]

    ora, perc = ora_perc(percek)
    print(cim, "hossza:", ora, "óra", perc, "perc")