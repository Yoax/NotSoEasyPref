# NotSoEasyPref
https://aministration.fr

Ce projet n'est en aucun cas une volonté de nuire à la Préfecture de Seine-Maritime et ce qu'elle représente. Je souhaite faliciter l'accès aux droits des usagers étrangers pour modérer les frustrations (tant des usagers que des professionnels) engendrées par le système actuel. Ainsi, il est, selon moi, nécessaire de mettre en place cette suite d'outil pour permettre la transparance.

Je suis joignable par [mail](mailto:aministrateur@aministration.fr).

## Objectifs :

- Agréger les créneaux de rendez-vous que proposent la préfecture de Seine-Maritime aux étrangers à une fréquence fixe
- Permettre d'analyser les mouvement via un graphique pour identifier, s'il y en a, des motifs récurrents dans les courbes
- Notifier une mise à disponibilité de la démarche souhaitée

# Développement
## Roadmap

- [x] **BETA** ~ script ne fonctionnant que sur une seule démarche, _proof of concept_
- [x] **V1** ~ implémentation pour que le script s'effectue sur toutes les démarches
- [x] **V2** ~ optimisation du script et de la manière d'exporter les données pour le déploiement sur un serveur
- [ ] **V3** ~ implémentation des données dans un espace web
- [ ] **V4** ~ implémentation d'un système de notification

## Les démarches supportées

Actuellement, le script vérifie les disponibilités de la Préfecture de la Seine-Maritime pour les motifs suivants :
- [Dépôt de la demande d'un premier titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50382/0)
- [Dépôt de la demande de renouvelement d'un titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50389/0)
- [Retrait d'un titre de séjour](https://www.seine-maritime.gouv.fr/booking/create/50420/0)
- [Retrait d'un récépissé](https://www.seine-maritime.gouv.fr/booking/create/50416/0)
- [Retrait d'un document de voyage (Document de Circulation pour Etrangers Mineurs, Titre de Voyage pour Réfugié ou Titre de Voyage)](https://www.seine-maritime.gouv.fr/booking/create/51406/0)
- [Régularisation du séjour](https://www.seine-maritime.gouv.fr/booking/create/47116/0)

Toutes les 15 minutes, NotSoEasyPref est exécuté par une tâche CRON. Le reste suit.
# Crédits
## Bibliothèques

- **Selenium** : tout repose sur cet outil formidable. [Pour en savoir plus](https://github.com/SeleniumHQ/Selenium).
- **bokeh** : interprétation graphique dynamique simple d'apprentissage (la preuve, j'ai réussi). [Pour en savoir plus](https://bokeh.org/)

## Licence

Ce script est sous **licence GNU GPL3** : https://www.gnu.org/licenses/gpl-3.0.html

**Si vous souhaitez modifier ce projet, vous devez rendre l'entiereté de votre code source disponible et faire référence au *copyright*. Vous devez également publier votre travail sous la même licence.**
>*Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.*
