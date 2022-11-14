aantal_mensen = 4 
aantal_minuten_in_VR = 45
prijs_in_VR_per_vijf_min = 0.37
prijs_per_persoon_speelhal = 7.45

totale_prijs = (aantal_minuten_in_VR / 5) * prijs_in_VR_per_vijf_min * aantal_mensen + prijs_per_persoon_speelhal * aantal_mensen
float = totale_prijs
format_float = "{:.2f}".format(float)

print ("Dit geweldige dagje uit met " + str(aantal_mensen) + " menesen in de Speelhal met " + str(aantal_minuten_in_VR) + " minuten VR kost je maar " + format_float + " euro")