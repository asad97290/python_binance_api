from binance.client import Client

# Replace with your API key and secret
api_key = '<api_key>'
secret_key = '<secret_key>'

# Create a Binance client
client = Client(api_key, secret_key)

# Define transfer parameters
coin = 'USDT'  # Asset to transfer
amount = 16     # Amount to transfer
address = '0x6B7C5e4cf26Cd4291f5E5Af43a3bEdB242183B46'  # Address to which you are sending SOL
network='ETH'
# Transfer SOL
try:
    result = client.withdraw(coin=coin, amount=amount, address=address, network=network,name='Withdraw')
    print("Transfer successful:", result)
except Exception as e:
    print("An error occurred:", e)



