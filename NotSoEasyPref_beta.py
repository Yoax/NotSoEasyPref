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

# Début du script
print(
    "\n---\nn0750345ypr3f : un script pour (sur)veiller l'accès aux droits des étrangers\n~~~~~~~~\n"
    "Patientez 1 minute ! Ne fermez pas Firefox, le petit robot travaille dur !\n"
    "Quand la fenêtre de Firefox se fermera, vous aurez un petit message !\n\n"
)

# Initialisation du WebDriver
driver = webdriver.Firefox()
driver.get("https://www.seine-maritime.gouv.fr/booking/create/50389/0")

# Récupération et formatage de la date et de l'heure pour l'export
heure = datetime.now().strftime("%H:%M:%S")
jour = date.today().strftime("%m/%d/%y")

# Coche le bouton d'acceptation
elem = driver.find_element(By.NAME, "condition")
elem.send_keys(Keys.SPACE)

# Appuie sur le bouton pour aller à la page suivante
elem = driver.find_element(By.NAME, "nextButton")
elem.send_keys(Keys.SPACE)

# Récupère et compare le texte issu de la requête JQuery du serveur
time.sleep(20) # nécessaire pour éviter que cette action se lance avant que la seconde page ait chargée (améliorable)
elem = driver.find_element(By.ID, "FormBookingCreate").text
if elem == "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement.":
    disponibilite = 0
else:
    disponibilite = 1

# Ferme le WebDriver et, par extension, Firefox
driver.close()

# Ajoute les résultats du parsing à un fichier csv pour par la suite manipuler les données simplement
fichier = open("step1Stats" + ".csv", "a")
fichier.write(str(jour) + "," + str(heure) + "," + str(disponibilite) + "\n")

print("TERMINÉ AVEC BRIO !（＾ω＾)\n---\n")
