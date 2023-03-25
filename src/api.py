from requests import Session
from urllib.parse import quote
import random
import json
import os
import re

BASE_URL = "https://wojakparadise.net"


def getList(session: Session, type: str, value: str) -> json:
    """Raw json request
    Can be: category, tag, ws
    Category and tag requires value but ws doesn't
    """

    if ((type == "category" or type == "tag") and value != ""):
        slug = f"/{type}/req/{quote(value)}"
    elif type == "ws":
        slug = "/ws/req"
    else:
        print(f"{value} is not a valid value \
                Valid values are: category, tag, ws")
        return

    response = session.get(f"{BASE_URL}{slug}")

    return response.json()


def download(session: Session, wJson: list):
    for item in wJson:
        id = item['id']
        name = item['name']
        name = ''.join(filter(str.isalnum, name))

        response = session.get(f"{BASE_URL}/wojak/{id}/img", stream=True)
        fout_path = f"wojak/{name}.png"

        if (os.path.isfile(fout_path)):
            fout_path = fout_path.replace('.png', f"{random.randint(0,10000)}.png")


        with open(fout_path, 'wb') as fout:
            for chunk in response:
                fout.write(chunk)
            print(f"Image path: {fout_path}")
