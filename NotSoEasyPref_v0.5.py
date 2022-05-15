"""
Copyright 2021 Yoan POUZET
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
jour = date.today().strftime("%m_%d_%y") ###format MM/JJ/AA - ce format aide à s'organiser dans des fichiers car il permet de trier alphabétiquement et chronologiquement en un clic
heure = datetime.now().strftime("%H_%M_%S") ###format HH:MM:SS

# Lancement du WebDriver sans tête et ouverture du CSV
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
fichier = open("rapport" + ".csv", "a")

# Script
print(
    "n0750345ypr3f : un script pour (sur)veiller l'accès aux droits des étrangers"
    "\nExécution le " + str(jour) + " à " + str(heure) +
    "\n~~~~~~~~"
    "\nPatientez 10 minutes ! Ne fermez pas le terminal, le petit robot travaille dur !"
    "\n~~~~~~~~"
)

for i in dictionnaireDemarches:
    ## Nouveau tour
    nomDemarche = str(i)
    urlDemarche = str(dictionnaireDemarches.get(i))
    driver.get(urlDemarche)
    heure = datetime.now().strftime("%H_%M_%S") ###format HH_MM_SS
    print("\n" + nomDemarche + " : " + str(heure))

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
        print("il n'y a plus de disponibilité")

    else:
        disponibilite = 1
        print("DES CRENEAUX SONT DISPOS !!!")
        
        ## Enregistre le code source de la page
        fichierHTML = open("HTML/" + nomDemarche + "-" + str(jour) + "-" + str(heure) + ".html", "x")
        codeHTML = driver.page_source
        fichierHTML.write(codeHTML)
        fichierHTML.close()

    fichier.write("\n" + str(jour) + "," + str(heure) + "," + nomDemarche + "," + str(disponibilite))

# Et c'est terminé !
driver.close()
fichier.close()
print(
    "~~~~~~~~"
    "\nTERMINÉ AVEC BRIO !（＾ω＾)"
    "\n~~~~~~~~"
)
