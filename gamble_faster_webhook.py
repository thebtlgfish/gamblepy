import time
import random
import requests
from webhook import sendWebhook, WEBHOOK_URL

botuser = "gamblepy"

def gamble(times, min, max, wait):
	print("start gambling: \n")
	# sendWebhook(WEBHOOK_URL, "User Started Gambling: \n", botuser)
	rolls = []
	for i in range(times):
		time.sleep(wait)
		roll = random.randint(min, max)
		message = f"Rolled {roll}\n"
		rolls.append(roll)
		print(message)
		# sendWebhook(WEBHOOK_URL, message, botuser)

	return rolls

	for roll in rolls:
		sendWebhook(WEBHOOK_URL, message, botuser)

if 1 == 1:

    time.sleep(5)
    total = gamble(100, 1, 100, 5) 
    totalmessage = f"Total Rolls: {len(total)}"
    allvalues = f"All Roll Values: {total}"
    print(totalmessage)
    sendWebhook(WEBHOOK_URL, totalmessage, botuser)
    print(allvalues)
    sendWebhook(WEBHOOK_URL, allvalues, botuser)

    if total:
        average = sum(total) / len(total)
        averagemessage = f"Average Roll: {average:.2f}"
        print(averagemessage)
        sendWebhook(WEBHOOK_URL, averagemessage, botuser)

