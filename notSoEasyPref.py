"""
Copyright 2022 Yoan POUZET
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or 
any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
from datetime import datetime, date

# Déclaration des variables
dictionnaireDemarches = {
    "depot_1er_TDS": "https://www.seine-maritime.gouv.fr/booking/create/50382/0",
    "renouvelement_TDS": "https://www.seine-maritime.gouv.fr/booking/create/50389/0",
    "retrait_TDS": "https://www.seine-maritime.gouv.fr/booking/create/50420/0",
    "retrait_recepisse": "https://www.seine-maritime.gouv.fr/booking/create/50416/0",
    "retrait_DCEM_TVR_TIV": "https://www.seine-maritime.gouv.fr/booking/create/51406/0",
    "regularisation_sejour": "https://www.seine-maritime.gouv.fr/booking/create/47116/0",
}
tempsAttente = 20 ###en secondes
jour = date.today().strftime("%y-%m-%d") ###format AA/MM/JJ
heure = datetime.now().strftime("%H:%M") ###format HH:MM
jourEtHeure = str(jour) + " " + str(heure)

print("NotSoEasyPref : " + jourEtHeure + "\n~\n\nPatientez 5 minutes !\n\n")

# Lancement du WebDriver sans tête
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

for i in dictionnaireDemarches:
    ## Nouveau tour
    nomDemarche = str(i)
    print("Vérification de " + nomDemarche + " en cours...")
    urlDemarche = str(dictionnaireDemarches.get(i))
    fichier = open("/home/yoan/NotSoEasyPref/Data/" + nomDemarche + ".csv", "a")
    driver.get(urlDemarche)

    ## Coche le bouton d'acceptation
    elem = driver.find_element(By.NAME, "condition")
    elem.send_keys(Keys.SPACE)

    ## Appuie sur le bouton pour aller à la page suivante
    elem = driver.find_element(By.NAME, "nextButton")
    elem.send_keys(Keys.SPACE)

    ## Récupère et compare le texte issu de la requête JQuery du serveur
    time.sleep(tempsAttente) ### nécessaire pour éviter que cette action se lance avant que la seconde page ait chargée (améliorable)
    elem = driver.find_element(By.ID, "FormBookingCreate").text
    if elem == "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement.":
        disponibilite = 0

    else:
        elem = driver.find_element(By.NAME, "nextButton")
        elem.send_keys(Keys.SPACE)
        time.sleep(tempsAttente)
        disponibilite = 0

        elem = driver.find_elements(By.XPATH, "//table/tbody/tr/td")
        for i in elem:
            if i.get_attribute("class") == "status-1 free":
                disponibilite = disponibilite + 1
            else:
                pass

    fichier.write("\n" + jourEtHeure + "," + str(disponibilite))
    fichier.close()
    print("Il y a " + str(disponibilite) + " disponibilité(s)\n")

# Et c'est terminé !
driver.close()

