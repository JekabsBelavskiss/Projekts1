def ievadit_ienakumus_un_izdevumus():
    ienakumi = float(input("Ievadiet uzņēmuma ienākumus: "))
    izdevumi = float(input("Ievadiet uzņēmuma izdevumus: "))
    return ienakumi, izdevumi

def aprekikins(ienakumi, izdevumi, nlikme):
    pelna = ienakumi - izdevumi
    nodoklis = pelna * (nlikme / 100)
    neto_pelna = pelna - nodoklis
    return pelna, nodoklis, neto_pelna

def programma():
    for _ in range(1): 
        ienakumi, izdevumi = ievadit_ienakumus_un_izdevumus()

        if izdevumi > ienakumi:
            print("Kļūda: Izdevumi nevar būt lielāki par ienākumiem.")
        else:
            nlikme = float(input("Ievadiet nodokļu (%): "))
            pelna, nodoklis, neto_pelna = aprekikins(ienakumi, izdevumi, nlikme)
            print(f"Peļņa pēc nodokļiem: {neto_pelna:.2f} EUR")
            print(f"Nodokļi: {nodoklis:.2f} EUR")
            print(f"Bruto peļņa: {pelna:.2f} EUR")

programma()
