#!/usr/bin/env python3

import http.client
import urllib.parse
import json
import os

URL = "app.limacharlie.io"
API_KEY = os.getenv('LC_KEY')
OID = os.getenv('OID')

def generateJwt(oid, api_key):
    """
    Code for generating a JWT key.
    """
    try:
        if not api_key:
            raise ValueError("API key not set.")

        params = urllib.parse.urlencode({
            "oid": oid,
            "secret": api_key,
        })

        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        conn = http.client.HTTPSConnection(URL, timeout=5)
        conn.request("POST", "/jwt", params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()

        if response.status != 200:
            raise Exception(f"Failed to refresh the JWT: {response.status}")

        parsed_data = json.loads(data)
        token = parsed_data["jwt"]
        return token

    except Exception as e:
        print(f"Failed to refresh the JWT: {e}")
        return False

def main():
    """
    Main entry.
    """

    jwt_key = generateJwt(OID, API_KEY)
    print(jwt_key)

if __name__ == '__main__':
    main()