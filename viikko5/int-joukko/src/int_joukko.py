class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int):
            raise TypeError("Kapasiteetin on oltava kokonaisluku")
        if kapasiteetti < 0:
            raise ValueError("Negatiivinen kapasiteetti")
        self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int):
            raise TypeError("Kasvatuskoon on oltava kokonaisluku")
        if kasvatuskoko < 0:
            raise ValueError("Negatiivinen kasvatuskoko")
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        for alkio in self.lukujono:
            if alkio == luku:
                return True
        return False

    def kopioi_lista(self, kopioi, kopio):
        for i, luku in enumerate(kopioi):
            kopio[i] = luku

    def to_int_list(self):
        lista = self._luo_lista(self.alkioiden_lkm)
        for i in range(0, self.alkioiden_lkm):
            lista[i] = self.lukujono[i]

        return lista

    def laajenna(self):
        uusi_lukujono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(self.lukujono, uusi_lukujono)
        self.lukujono = uusi_lukujono

    def lisaa(self, luku):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = luku
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm += 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.lukujono[-1] != 0:
                self.laajenna()

            return True
        return False

    def poista(self, luku):
        kohta = -1
        for i, alkio in enumerate(self.lukujono):
            if luku == alkio:
                kohta = i
                self.lukujono[kohta] = 0
                break

        if kohta == -1:
            return False

        for i in range(kohta, self.alkioiden_lkm - 1):
            self.lukujono[i] = self.lukujono[i + 1]
            self.lukujono[i + 1] = 0

        self.alkioiden_lkm -= 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    @staticmethod
    def yhdiste(lista1, lista2):
        yhdiste = IntJoukko()

        for luku in lista1.to_int_list():
            yhdiste.lisaa(luku)

        for luku in lista2.to_int_list():
            yhdiste.lisaa(luku)

        return yhdiste

    @staticmethod
    def leikkaus(lista1, lista2):
        leikkaus = IntJoukko()
        luvut = {}

        for luku in lista1.to_int_list():
            luvut[luku] = 1

        for luku in lista2.to_int_list():
            try:
                luvut[luku]
                leikkaus.lisaa(luku)
            except:
                continue

        return leikkaus

    @staticmethod
    def erotus(lista1, lista2):
        erotus = IntJoukko()

        for luku in lista1.to_int_list():
            erotus.lisaa(luku)

        for luku in lista2.to_int_list():
            erotus.poista(luku)

        return erotus

    def __str__(self):
        match self.alkioiden_lkm:
            case 0:
                return "{}"
            case 1:
                return "{" + str(self.lukujono[0]) + "}"
            case _:
                return str(set(self.to_int_list()))
