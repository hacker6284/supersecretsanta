#!/usr/bin/env python
# Function which makes IFTTT requests for the webhooks applet

import requests


def ifttt(name, value1, value2, value3, key):
    """Make an ifttt webhooks call on hook *name* with value payloads.
    Pass secret key as last argument
    """

    payload = {'value1': value1, 'value2': value2, 'value3': value3}
    requests.post("https://maker.ifttt.com/trigger/{}/with/key/{}".format(
        name, key), data=payload)
