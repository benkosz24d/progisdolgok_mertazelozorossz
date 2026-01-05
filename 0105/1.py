bevasarlo_lista = ["kenyér", "tej", "tojás"]
print("Kezdeti bevásárlólista:", bevasarlo_lista)

# Új elem hozzáadása (user input)
uj_elem = input("Adj meg egy új terméket, amit hozzá szeretnél adni: ")
bevasarlo_lista.append(uj_elem)
print("Lista frissítve:", bevasarlo_lista)


torlendo = input("Adj meg egy terméket, amit törölni szeretnél: ")

if torlendo in bevasarlo_lista:
    bevasarlo_lista.remove(torlendo)
    print(f"A(z) '{torlendo}' eltávolítva.")
else:
    print(f"A(z) '{torlendo}' nincs a listában.")

print("Aktuális lista:", bevasarlo_lista)

# Ellenőrzés (user input)
keresett = input("Melyik terméket szeretnéd ellenőrizni? ")

if keresett in bevasarlo_lista:
    print(f"A(z) '{keresett}' szerepel a bevásárlólistában.")
else:
    print(f"A(z) '{keresett}' NEM szerepel a bevásárlólistában.")