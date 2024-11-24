class Voiture():
    def __init__(self):
        self.nombre_roues = 4
        self.nombre_fauteuils = 1
        self.moteur = False
        self.volant = True

    def start_moteur(self):
        self.moteur = True
        return self.moteur

    def stop_moteur(self):
        self.moteur = False
        return self.moteur

    def statut_moteur(self):
        return self.moteur


if __name__ == "__main__":
    ma_voiture_basique = Voiture()
    print(ma_voiture_basique.statut_moteur())
    ma_voiture_basique.start_moteur()
    print(ma_voiture_basique.statut_moteur())