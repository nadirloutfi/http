import requests

token_url = "https://orcastarkiller.authentication.cert.sap.hana.ondemand.com/oauth/token"

# client ID
client_id = 'sb-ppro-procserver-sac-orcastarkiller!t2319'

# client certificate and private key
cert = ('cert/certificate-cf.txt', 'cert/key-cf.txt')

# headers and payload
headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
payload = { 'grant_type': 'client_credentials', 'client_id': client_id }

response = requests.post(token_url, headers=headers, data=payload, cert=cert)

if response.ok:
    print("Access token: ", response.json().get('access_token'))
else:
    print("Error: ", response.content)