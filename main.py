import requests

endpoint = " https://opsin.ch.cam.ac.uk/opsin/cyclopropane.png"

response = requests.get(endpoint)

if response.status_code == 200:
    with open("image.png", "wb") as f:
        f.write(response.content)
else:
    print("")
