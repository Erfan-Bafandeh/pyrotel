## Start Handler

```python
from pyrotel import Client
import asyncio
import sys

app = Client("API_TOKEN")

async def bot():
	for msg in app.on_message():
			await app.send_message(msg.chat_id, "hello my dear.\nwelcome to my bot :)")

if __name__ == "__main__":
	asyncio.run(bot())
```
