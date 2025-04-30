
#Klasse Art
class Art:
    def __init__(self, art_name):
        self.art_name = art_name

    def __str__(self):
        return f"(Art: {self.art_name})"

#Klasse Tier
class Tier:
    def __init__(self, tier_name, art_name="Nicht spezifiziert"):
        self.tier_name = tier_name
        self.art_name = Art(art_name)

    def __str__(self):
        return f"{self.tier_name}"

#Klasse Pfleger
class Pfleger:
    def __init__(self, pfleger_name):
        self.pfleger_name = pfleger_name
        self.verwaltete_tiere = []

    def tier_hinzufuegen(self, verwaltetes_tier):
        self.verwaltete_tiere.append(verwaltetes_tier)

    def __str__(self):
        return f"{self.pfleger_name}"

#Klasse Fütterung
class Fuetterung:
    def __init__(self, fuetternder_pfleger, gefuettertes_tier):
        self.fuetternder_pfleger = fuetternder_pfleger
        self.gefuettertes_tier = gefuettertes_tier

    def fuetterungsprozess(self, gefuettertes_tier):
        print(f"{self.fuetternder_pfleger} hat {gefuettertes_tier.tier_name} {gefuettertes_tier.art_name} gefüttert")




#Objektdefinition der vorhandenen Tiere
simba = Tier("Simba", "Löwe")
melman = Tier("Melman", "Giraffe")

tom = Pfleger("Tom")
tom.tier_hinzufuegen(simba)
tom.tier_hinzufuegen(melman)
futterrunde1 = Fuetterung(tom, simba)
futterrunde2 = Fuetterung(tom, melman)
futterrunde1.fuetterungsprozess(simba)
futterrunde2.fuetterungsprozess(melman)
