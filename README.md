# NotSoEasyPref

## Objectifs :

- Agréger les créneaux de rendez-vous que proposent la préfecture de Seine-Maritime aux étrangers toutes les X heures
- Présenter dans une page web les créneaux dispos pour faciliter le travail des professionnels
- Notifier une mise à disponibilité de la démarche souhaitée

# Développement

## Roadmap

- [x] **BETA** ~ script ne fonctionnant que sur une seule démarche, _proof of concept_
- [x] **V1** ~ implémentation pour que le script s'effectue sur toutes les démarches
- [x] **V2** ~ optimisation du script et de la manière d'exporter les données pour le déploiement sur un serveur
- [ ] **V3** ~ implémentation d'un système de notification
- [ ] **V4** ~ implémentation des données dans un espace web

## Les démarches supportées

Actuellement, le script vérifie les disponibilités de la Préfecture de la Seine-Maritime pour les motifs suivants :
- [Dépôt de la demande d'un premier titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50382/0)
- [Dépôt de la demande de renouvelement d'un titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50389/0)
- [Retrait d'un titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50420/0)
- [Retrait d'un récépissé](https://www.seine-maritime.gouv.fr/booking/create/50416/0)
- [Retrait d'un document de voyage (Document de Circulation pour Etrangers Mineurs, Titre de Voyage pour Réfugié ou Titre de Voyage)](https://www.seine-maritime.gouv.fr/booking/create/51406/0)
- [Régularisation du séjour](https://www.seine-maritime.gouv.fr/booking/create/47116/0)

## Installation

Étape par étape à venir.
1. Installer un [interpréteur Python](https://www.python.org/downloads/) et le navigateur de votre choix. Ici, j'utilise [Mozilla Firefox](https://www.mozilla.org/fr/firefox/new/)
2. Installer le paquet [Selenium](https://selenium-python.readthedocs.io/installation.html) selon votre système d'exploitation. Récupérez également le WebDriver correspondant à votre navigateur Internet (j'inclus geckodriver, celui pour Firefox)

# Crédits

## Bibliothèques

- **Selenium** : tout repose sur cet outil formidable. [Pour en savoir plus](https://github.com/SeleniumHQ/Selenium).

## Licence

Ce script est sous **licence GNU GPL3** : https://www.gnu.org/licenses/gpl-3.0.html

**Si vous souhaitez modifier ce projet, vous devez rendre l'entiereté de votre code source disponible et faire référence au *copyright*. Vous devez également publier votre travail sous la même licence.**
>*Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.*
