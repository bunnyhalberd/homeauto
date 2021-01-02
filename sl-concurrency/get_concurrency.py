#
# Get concurrency on agni
#

import logging
import requests
import json
from time import sleep

from llbase import llsd
import paho.mqtt.client as mqtt

endpoint = "https://api.secondlife.com/datafeeds/secondlife.xml"


def get_concurrency():

    logging.debug("using endpoint: " + endpoint)

    headers = {"Accept": "application/llsd+xml"}

    r = requests.get(endpoint, headers=headers)
    logging.debug(r.content)

    # Parse our result out of the LLSD
    code = llsd.parse_xml(r.content)

    concurrency = code["stats"]["inworld"]
    logging.info("concurrency: %d", concurrency)

    return concurrency


def publish_concurrency(concurrency):

    logging.debug("publishing %d", concurrency)

    data = {"concurrency": concurrency}

    client = mqtt.Client("SL Concurrency Thingy")

    client.connect("home.opsnlops.io", port=1883, keepalive=60, bind_address="")
    logging.debug("connected")

    client.publish("sl/concurrency", json.dumps(data))
    logging.debug("published")

    client.disconnect()
    logging.debug("disconnect")


if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
    )

    while True:
        concurrency = get_concurrency()
        publish_concurrency(concurrency)
        sleep(10)