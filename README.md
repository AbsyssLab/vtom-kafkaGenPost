# Kafka GenPost Connector
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](../../LICENSE.md)&nbsp;
[![en](https://img.shields.io/badge/lang-fr-red.svg)](README-fr.md)

This connector publishes a message to a Kafka topic from Visual TOM.

# Disclaimer
No support or warranties will be provided by Absyss SAS for this project and associated files. Use is at your own risk.

Absyss SAS cannot be held responsible for damages caused by the use of any files made available in this Github repository.

Consulting days can be requested for implementation.

# Prerequisites

  * Visual TOM 7.3.2 or higher
  * Python 3.x or higher
  * Access to a Kafka cluster / topic
  * Install required python packages with pip: `pip install -r requirements.txt`

# Instructions
  * Windows :
    * Place the file `kafkaGenPost.py` in the `%ABM_BIN%` directory (or your scripts directory)
    * Declare the queue / custom application on the agent (see administrator guide)

  * Linux/Unix :
    * Place the file `kafkaGenPost.py` in the `$TOM_ADMIN` directory (or your scripts directory)
    * Declare the queue / custom application on the agent (see administrator guide)

  * Create a "Generic Resource" in Visual TOM with the following definition or import the KafkaGenPost.xml file:
   ```
   vtimport -x -f KafkaGenPost.xml
   ```
   ![Custom application screenshot](screenshots/kafkaGenPost.png?raw=true)

The script returns specific exit codes:
- `0`: Message published successfully
- `1`: Publish / connection / validation error

Parameter descriptions:
  * `Param 1` BOOTSTRAP_SERVERS : Kafka bootstrap servers (required), e.g. `localhost:9092`
  * `Param 2` TOPIC : Kafka topic name (required)
  * `Param 3` MESSAGE : Message payload to publish (required)
  * `Param 4` KEY : Optional Kafka message key
  * `Param 5` SECURITY_PROTOCOL : Optional (`PLAINTEXT` / `SASL_SSL` / `SSL`, default `PLAINTEXT`)
  * `Param 6` SASL_MECHANISM : Optional SASL mechanism (e.g. `PLAIN`)
  * `Param 7` USERNAME : Optional SASL username
  * `Param 8` PASSWORD : Optional SASL password
  * `Param 9` SSL_CAFILE : Optional CA certificate path

Protect parameters with double quotes `""` (especially if they contain spaces or special characters).

The connector provides logging with:
- Timestamps
- Log levels (INFO, WARNING, ERROR)
- Publish status (partition / offset)
- Message payload never displayed in logs

Example log output:
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


# License
This project is licensed under Apache 2.0. See the [LICENSE](LICENSE) file for more details.

# Code of Conduct
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)
Absyss SAS has adopted the [Contributor Covenant](CODE_OF_CONDUCT.md) as a Code of Conduct and expects project participants to adhere to it as well. Please read the [complete document](CODE_OF_CONDUCT.md) to understand which actions will or will not be tolerated.
