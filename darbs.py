def ievade():
    ienakumi = float(input("Ievadiet uzņēmuma ienākumus: "))
    izdevumi = float(input("Ievadiet uzņēmuma izdevumus: "))
    return ienakumi, izdevumi

def aprekikins(ienakumi, izdevumi, nlikme):
    pelna = ienakumi - izdevumi
    nodoklis = pelna * (nlikme / 100)
    netopelna = pelna - nodoklis
    return pelna, nodoklis, netopelna

def programma():
    for _ in range(1): 
        ienakumi, izdevumi = ievade()

        if izdevumi > ienakumi:
            print("Kļūda: Izdevumi nevar būt lielāki par ienākumiem.")
        else:
            nlikme = float(input("Ievadiet nodokļu (%): "))
            pelna, nodoklis, netopelna = aprekikins(ienakumi, izdevumi, nlikme)
            print(f"Peļņa pēc nodokļiem: {netopelna:.2f} EUR")
            print(f"Nodokļi: {nodoklis:.2f} EUR")
            print(f"Bruto peļņa: {pelna:.2f} EUR")

programma()
