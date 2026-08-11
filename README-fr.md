# Connecteur Kafka GenPost
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](../../LICENSE.md)&nbsp;
[![fr](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Le connecteur publie un message sur un topic Kafka depuis Visual TOM.

# Disclaimer
Aucun support ni garanties ne seront fournis par Absyss SAS pour ce projet et fichiers associes. L'utilisation est a vos propres risques.

Absyss SAS ne peut etre tenu responsable des dommages causes par l'utilisation d'un des fichiers mis a disposition dans ce depot Github.

Il est possible de faire appel a des jours de consulting pour l'implementation.

# Preacquis

  * Visual TOM 7.3.2 ou plus
  * Python 3.x ou plus
  * Acces a un cluster / topic Kafka
  * Installer les packages python requis avec pip: `pip install -r requirements.txt`

# Consignes
  * Windows :
    * Placer le fichier `kafkaGenPost.py` dans le repertoire `%ABM_BIN%` (ou votre repertoire de scripts)
    * Declarer la queue / application custom sur l'agent (voir guide administrateur)

  * Linux/Unix :
    * Placer le fichier `kafkaGenPost.py` dans le repertoire `$TOM_ADMIN` (ou votre repertoire de scripts)
    * Declarer la queue / application custom sur l'agent (voir guide administrateur)

  * Créer dans Visual TOM une "Ressource Générique" avec la définition suivante ou importer le fichier KafkaGenPost.xml:
   ```
   vtimport -x -f KafkaGenPost.xml
   ```
   ![Custom application screenshot](screenshots/kafkaGenPost.png?raw=true)

Le script retourne des codes de sortie specifiques :
- `0` : Message publie avec succes
- `1` : Erreur de publication / connexion / validation

Description des parametres:
  * `Param 1` BOOTSTRAP_SERVERS : serveurs Kafka (requis), ex: `localhost:9092`
  * `Param 2` TOPIC : nom du topic (requis)
  * `Param 3` MESSAGE : contenu a publier (requis)
  * `Param 4` KEY : cle Kafka optionnelle
  * `Param 5` SECURITY_PROTOCOL : optionnel (`PLAINTEXT` / `SASL_SSL` / `SSL`, defaut `PLAINTEXT`)
  * `Param 6` SASL_MECHANISM : mecanisme SASL optionnel (ex: `PLAIN`)
  * `Param 7` USERNAME : utilisateur SASL optionnel
  * `Param 8` PASSWORD : mot de passe SASL optionnel
  * `Param 9` SSL_CAFILE : chemin optionnel du certificat CA

Protegez les parametres avec des guillemets `""` (surtout s'ils contiennent des espaces ou caracteres speciaux).

Le connecteur fournit une journalisation avec :
- Horodatage
- Niveaux de log (INFO, WARNING, ERROR)
- Statut de publication (partition / offset)
- Contenu du message jamais affiche dans les logs

Exemple de sortie de log :
```
2026-08-07 11:04:12,298 | INFO | Starting Kafka GenPost publish
2026-08-07 11:04:12,298 | INFO | Servers           : localhost:9092
2026-08-07 11:04:12,298 | INFO | Topic             : demo-topic
2026-08-07 11:04:12,298 | INFO | Key               : (none)
2026-08-07 11:04:12,298 | INFO | Message           : (not displayed)
2026-08-07 11:04:12,310 | INFO | Successfully connected to Kafka
2026-08-07 11:04:12,320 | INFO | Message published (partition=0, offset=14)
2026-08-07 11:04:12,320 | INFO | Result: OK (code 0)
```

# Licence
Ce projet est sous licence Apache 2.0. Voir le fichier [LICENCE](LICENSE) pour plus de details.

# Code de conduite
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)
Absyss SAS a adopte le [Contributor Covenant](CODE_OF_CONDUCT.md) en tant que Code de Conduite et s'attend a ce que les participants au projet y adherents egalement. Merci de lire le [document complet](CODE_OF_CONDUCT.md) pour comprendre les actions qui seront ou ne seront pas tolerees.
