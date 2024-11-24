from voiture import Voiture
from citroen import Citroen
from cb import CB


class CitroenDs(Voiture, Citroen):
    def __init__(self):
        Voiture.__init__(self)
        Citroen.__init__(self)
        self.modele = "DS moderne (>2000)"
        self._option_payante_ds_01 = False
        self._option_payante_ds_02 = False
        self._option_payante_ds_03 = False
        self.__option_calculateur_ds_01 = False
        self.__option_calculateur_ds_02 = False
        self.__option_calculateur_ds_03 = False
        self.start_options()
        self.cb = CB()

    def __del__(self):
        print("Suppression de la voiture")

    def start_options(self):
        if _option_payante_ds_01:
            print("GPS activé")
        if _option_payante_ds_02:
            print("Anti dépassement lignes blanches activé")
        if _option_payante_ds_03:
            print("Freinage urgence activé")

        if __option_calculateur_ds_01:
            print("Puissance moteur: 120 cv")
        elif __option_calculateur_ds_02:
            print("Puissance moteur: 150 cv")
        elif __option_calculateur_ds_03:
            print("Puissance moteur: 180 cv")


if __name__ == "__main__":
    ma_ds = CitroenDs()
    print(ma_ds.marque)
    print(ma_ds.modele)
    print(ma_ds.type_suspension)
    print(ma_ds.statut_moteur())
    ma_ds.start_moteur()
    print(ma_ds.statut_moteur())