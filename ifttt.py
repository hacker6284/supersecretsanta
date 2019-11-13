import requests

def ifttt(name, value1, value2, value3, key):
    payload = { 'value1' : value1, 'value2' : value2, 'value3' : value3}
    requests.post("https://maker.ifttt.com/trigger/%s/with/key/%s"%(name, key), data=payload)
