## pyrotel 0.9.0v

<h3 align="center">pyrotel is a library for telegram bots.</h3>

> ## Install and Update:
```python
pip install pyrotel
```

> ## START:
```python
from pyrotel import Client

app = Client("API_TOKEN")

async def bot():
	for msg in app.on_message():
		if msg.text == "/start":
			app.send_message(msg.chat_id, "hello my dear.\nwelcome to my bot :)", reply_to_message_id=msg.message_id)

```

> ## Social Media:
<a href="https://t.me/persian_py">TELEGRAM</a><br>
<a href="https://github.com/Erfan-Bafandeh/pyrotel">GITHUB</a>
