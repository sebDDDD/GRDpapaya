#!/usr/bin/env python3
import urllib.request
import json

def sntp_client():
    try:
        url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Bogota"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        print('Respuesta recibida de: timeapi.io')
        print('\tHora =', data['dateTime'])
        print('\tZona horaria =', data['timeZone'])
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    sntp_client()
    