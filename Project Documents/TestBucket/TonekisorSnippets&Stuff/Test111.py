# Test111

import http.client

conn = http.client.HTTPSConnection("getqrcode.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4d5e8e361emsh29643ad0810cc45p1e9dc0jsn1aac8a8b180b",
    'X-RapidAPI-Host': "getqrcode.p.rapidapi.com"
}

conn.request("GET", "/api/getQR?forQR=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DdQw4w9WgXcQ", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))