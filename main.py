import os
import json
import requests
import dotenv
import pyperclip
dotenv.load_dotenv()

coins = ['bitcoin', 'ethereum']
currency = 'usd'

prices = {}

for coin in coins:
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}'
    response = requests.get(url, timeout=10)
    data = response.json()
    prices[coin] = data[coin][currency]
    

json_data = json.dumps(prices)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + os.getenv('PINATA_JWT'),
}

response = requests.post(
    'https://api.pinata.cloud/pinning/pinJSONToIPFS', data=json_data, headers=headers, timeout=10)

if response.status_code == 200:
    ipfs_data = response.json()
    ipfs_hash = ipfs_data['IpfsHash']
    print(f"File pinned successfully! IPFS hash: {ipfs_hash}")
    pyperclip.copy(ipfs_hash)
    print("IPFS hash copied to clipboard.")
else:
    print(
        f"Error pinning file to IPFS: {response.status_code} - {response.text}")
