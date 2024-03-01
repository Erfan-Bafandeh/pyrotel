## Quick Start

```pyhton
from pyrotel import Client
import asyncio
import sys

app = Client("API_TOKEN")

async def bot():
	for msg in app.on_message():
		if msg.text == "/start":
			await app.send_message(msg.chat_id, "hello my dear.\nwelcome to my bot :)")
		elif msg.text == "/stop":
		    await app.send_message(msg.chat_id, "good bye !")
		    sys.exit()

if __name__ == "__main__":
	asyncio.run(bot())
```
