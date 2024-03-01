## send_message

```python
app.send_message(chat_id, text)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification


## send_photo

```python
app.send_photo(chat_id, file)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, caption, has_spoiler


## send_audio

```python
app.send_audio(chat_id, file)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, caption


## send_document

```python
app.send_document(chat_id, file)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, caption


## send_video

```python
app.send_video(chat_id, file)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, caption, has_spoiler


## send_voice

```python
app.send_voice(chat_id, file)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, caption


## send_contact

```python
app.send_contect(chat_id, phone_number, first_name)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, last_name


## send_dice

```python
app.send_dice(chat_id)
```
optional inputs: reply_markup, reply_to_message_id, message_thread_id, disable_notification, emoji


## get_user_profiles

```python
app.get_user_profiles(user_id)
```
optional inputs: 


## ban_chat_member

```python
app.ban_chat_member(chat_id, user_id)
```
optional inputs: revoke_messages


## unban_chat_member

```python
app.unban_chat_member(chat_id, user_id)
```
optional inputs: only_if_banned


## restrict_chat_member

```python
app.restrict_chat_member(chat_id, user_id)
```
optional inputs: permissions


## promote_chat_member

```python
app.promote_chat_member(chat_id, user_id)
```
optional inputs: is_anonymous, can_delete_messages, can_restrict_members, can_promote_members, can_invite_users, can_change_info, can_pin_messages


## set_admin_custom_title

```python
app.unban_chat_member(chat_id, user_id, custom_title)
```
optional inputs: 


## ban_chatsender

```python
app.ban_chatsender(chat_id, sender_chat_id)
```
optional inputs: 


## unban_chatsender

```python
app.unban_chatsender(chat_id, sender_chat_id)
```
optional inputs: 


## set_chat_permissions

```python
app.set_chat_permissions(chat_id, permissions)
```
optional inputs: 


## get_chat_link

```python
app.get_chat_link(chat_id)
```
optional inputs: 


## edit_invite_link

```python
app.edit_invite_link(chat_id, invite_link, name)
```
optional inputs: expire_date, limit_member, creates_join_request


## remove_invite_link

```python
app.remove_invite_link(chat_id, invite_link)
```
optional inputs: 


## accept_chat_join_request

```python
app.accept_chat_join_request(chat_id, user_id)
```
optional inputs: 


## remove_chat_join_request

```python
app.remove_chat_join_request(chat_id, user_id)
```
optional inputs: 


## set_chat_photo

```python
app.set_chat_photo(chat_id, file)
```
optional inputs: 


## delete_chat_photo

```python
app.delete_chat_photo(chat_id)
```
optional inputs: 


## set_chat_title

```python
app.set_chat_title(chat_id, title)
```
optional inputs: 
