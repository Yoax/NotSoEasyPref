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

jour = date.today().strftime("%m/%d/%y") ###format MM/JJ/AA - ce format aide à s'organiser dans des fichiers car il permet de trier alphabétiquement et chronologiquement en un clic

# Lancement du WebDriver
driver = webdriver.Firefox()

# Script
print(
    "\n~~~~~~~~\n"
    "n0750345ypr3f : un script pour (sur)veiller l'accès aux droits des étrangers"
    "\n~~~~~~~~\n"
    "Patientez 5 minutes ! Ne fermez pas Firefox, le petit robot travaille dur !\n"
    "Quand la fenêtre de Firefox se fermera, ce sera terminé !"
    "\n~~~~~~~~\n"
)

for i in dictionnaireDemarches:
    ## Nouveau tour
    nomDemarche = str(i)
    urlDemarche = str(dictionnaireDemarches.get(i))
    driver.get(urlDemarche)
    heure = datetime.now().strftime("%H:%M:%S") ###format HH:MM:SS

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
        print(nomDemarche, " : il n'y a plus de disponibilité")
    else:
        disponibilite = 1
        print(nomDemarche, " : DES CRENEAUX SONT DISPOS !!!")
        
    fichier = open("rapport" + ".csv", "a")
    fichier.write(str(jour) + "," + str(heure) + "," + nomDemarche + "," + str(disponibilite) + "\n")

# Et c'est terminé !
driver.close()
print(
    "\n~~~~~~~~\n"
    "TERMINÉ AVEC BRIO !（＾ω＾)"
    "\n~~~~~~~~\n"
)
