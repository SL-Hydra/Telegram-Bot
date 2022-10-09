from telethon import TelegramClient, events

# api_id and api_hash from https://my.telegram.org/apps
api_id = '9940370'
api_hash = 'fc46bff15accdce77e023c4701210c28'

client = TelegramClient('user', api_id, api_hash).start()

# This message can contain any text, links, and emoji:
message = "Hello! Thank you for contacting me 👍\nI'll be back soon and reply to your message."

@client.on(events.NewMessage())
async def handler(event):
	sender = await event.get_input_sender()
  # file="11.png" is attached image, its optional parameter
	await client.send_message(sender, message, file="icon.png")

client.run_until_disconnected()

