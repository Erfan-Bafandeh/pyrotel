# pyrotel
pyrotel is a good library for telegram bots

--------------------------------------------------

<h2>how to start client?</h2>

```python
from pyrotel import *

api_token = "TOKEN"

bot = client(api_token)
```
(optional inputs: app)

--------------------------------------------------

<h2>how to change library app to bale?</h2>

```python
bot = client("TOKEN", app="bale")
```

--------------------------------------------------

# how to use pyrotel library methods?

```python
send_message(chat_id, text)
```
this method is for send a message or send a keyboard to user.
(optional inputs: disable_notificaton, reply_markup)

--------------------------------------------------

```python
edit_message(chat_id, msg_id, text)
```
this method is for edit a message.
(optional inputs: reply_markup)

--------------------------------------------------

```python
delete_message(chat_id, message_ids)
```
this method is for delete messages.

--------------------------------------------------

```python
forward_message(chat_id, from_chat_id, message_ids)
```
this method is for forward messages.
(optional inputs: disable_notification)

--------------------------------------------------

```python
bot.setwebhook(url)
```
this method is for set webhook.

--------------------------------------------------

```python
bot.getme()
```
this method don't get values.
this method is for get bot name or ....

--------------------------------------------------

```python
bot.get_chat(chat_id)
```
this method is for get chat info

--------------------------------------------------

```python
bot.get_updates()
```
this method don't get values.
this method is for get updates from telegram or bale servers.

--------------------------------------------------

```python
bot.get_last_update()
```
this method don't get values, too.
this method is for get last update from telegram or bale servers.

--------------------------------------------------

# how to use message class?
```python
msg = message(update)

msg.text
msg.message_id
msg.chat_id
msg.first_name
```

--------------------------------------------------

# how to make a keyboard in pyrotel library?
```python
keys = [["buy", "sell"],
["support"]]
keyboard = bot.keyboard(keys)
```
this method is for make a keyboard.
(optional inputs: resize_keyboard, one_time_keyboard)

--------------------------------------------------

# how to send a keyboard?
```python
bot.send_message(msg.chat_id, "hello wellcome to my bot", reply_markup=keyboard)
```
