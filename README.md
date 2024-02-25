# pyrotel
pyrotel is a good library for telegram bots


how to use pyrotel library methods?
--------------------------------------------------
send_message(chat_id, text)
this method is for send a message or send a keyboard to user.
(optional inputs: disable_notificaton, reply_markup)
--------------------------------------------------
edit_message(chat_id, msg_id, text)
this method is for edit a message.
(optional inputs: reply_markup)
--------------------------------------------------
delete_message(chat_id, message_ids)
this method is for delete messages.
--------------------------------------------------
forward_message(chat_id, from_chat_id, message_ids)
this method is for forward messages.
(optional inputs: disable_notification)
--------------------------------------------------
setwebhook(url)
this method is for set webhook.
--------------------------------------------------
getme()
this method don't get values.
this method is for get bot name or ....
--------------------------------------------------
get_chat(chat_id)
this method is for get chat info
--------------------------------------------------
get_updates()
this method don't get values.
this method is for get updates from telegram or bale servers.
--------------------------------------------------
```python
get_last_update()```
this method don't get values, too.
this method is for get last update from telegram or bale servers.



