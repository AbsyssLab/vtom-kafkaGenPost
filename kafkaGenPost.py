#!/usr/bin/env python3
"""
Kafka GenPost script for VTOM: publish a message.

Positional parameters:
  $1  bootstrap_servers
  $2  topic
  $3  message
  $4  key                 optional
  $5  security_protocol   optional (default: PLAINTEXT)
  $6  sasl_mechanism      optional
  $7  username            optional
  $8  password            optional
  $9  ssl_cafile          optional

Exit codes:
  0 = message published
  1 = error
"""

import logging
import sys

from kafka import KafkaProducer
from kafka.serializer import DefaultSerializer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    stream=sys.stdout,
    force=True,
)

# === Argument validation ===
if len(sys.argv) < 4:
    logging.error(
        "Usage: python kafkaGenPost.py <bootstrap_servers> <topic> <message> "
        "[key] [security_protocol] [sasl_mechanism] [username] [password] [ssl_cafile]"
    )
    sys.exit(1)

BOOTSTRAP_SERVERS = sys.argv[1]
TOPIC = sys.argv[2]
MESSAGE = sys.argv[3]
KEY = sys.argv[4] if len(sys.argv) > 4 else ""
SECURITY_PROTOCOL = sys.argv[5] if len(sys.argv) > 5 and sys.argv[5] else "PLAINTEXT"
SASL_MECHANISM = sys.argv[6] if len(sys.argv) > 6 else ""
USERNAME = sys.argv[7] if len(sys.argv) > 7 else ""
PASSWORD = sys.argv[8] if len(sys.argv) > 8 else ""
SSL_CAFILE = sys.argv[9] if len(sys.argv) > 9 else ""


def build_producer():
    """Build a configured KafkaProducer."""
    config = {
        "bootstrap_servers": [
            item.strip() for item in BOOTSTRAP_SERVERS.split(",") if item.strip()
        ],
        "security_protocol": SECURITY_PROTOCOL or "PLAINTEXT",
        "acks": "all",
        "retries": 3,
        "key_serializer": DefaultSerializer(),
        "value_serializer": DefaultSerializer(),
    }

    if SASL_MECHANISM:
        config["sasl_mechanism"] = SASL_MECHANISM
    if USERNAME:
        config["sasl_plain_username"] = USERNAME
    if PASSWORD:
        config["sasl_plain_password"] = PASSWORD
    if SSL_CAFILE:
        config["ssl_cafile"] = SSL_CAFILE

    return KafkaProducer(**config)


# === Main execution ===
producer = None
try:
    logging.info("Starting Kafka GenPost publish")
    logging.info(f"Servers           : {BOOTSTRAP_SERVERS}")
    logging.info(f"Topic             : {TOPIC}")
    logging.info(f"Key               : {'(none)' if KEY == '' else '(provided)'}")
    logging.info("Message           : (not displayed)")
    logging.info(f"Security protocol : {SECURITY_PROTOCOL}")

    logging.info("Connecting to Kafka broker...")
    producer = build_producer()
    logging.info("Successfully connected to Kafka")

    logging.info("Publishing message...")
    future = producer.send(
        TOPIC,
        value=MESSAGE,
        key=KEY if KEY != "" else None,
    )
    metadata = future.get(timeout=10)
    producer.flush()

    logging.info(
        f"Message published (partition={metadata.partition}, "
        f"offset={metadata.offset})"
    )
    logging.info("Result: OK (code 0)")
    sys.exit(0)

except Exception as exc:
    logging.error(f"Error during execution: {exc}")
    sys.exit(1)

finally:
    if producer is not None:
        logging.info("Closing Kafka producer")
        producer.close()
