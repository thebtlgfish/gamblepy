import requests

with open('webhookurl', 'r') as file:
        WEBHOOK_URL = file.read().strip()

def sendWebhook(url, message, username):

    data = {
        "content": message,
        "username": username,
    }

    r = requests.post(url, json=data)
    if r.status_code == 204:
    	print("Sent Webhook Message")
    else:
    	print(f"Error Sending Message {r.status_code}")



# sendWebhook(WEBHOOK_URL, message, botuser)