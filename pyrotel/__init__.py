# REQUESTS
from requests import post
# COLORAMA
from colorama import  Fore
# START MESSAGE
print(f"""
Wellcome to pyrotel {Fore.LIGHTCYAN_EX}0.1.3v{Fore.RESET} library.

dev by {Fore.LIGHTYELLOW_EX}Erfan Bafandeh.{Fore.RESET}
""")

# DEF
def ifa(update):
	upc = str(update).count("callback")
	if upc == 0:
		return True
	elif upc != 0:
		return False

# BOT CLASS FOR GET YOUR BOT TOKEN
class client:
	# GET TOKEN
	def __init__(self, token:str, app="telegram"):
		if app == "telegram":
			self.api = "api.telegram.org"
			self.app = app
		if app == "bale":
			self.api = "tapi.bale.ai"
			self.app = app
		self.token = token
	# UPDATE
	# GET UPDATES
	def get_updates(self):
		return post(url=f"https://{self.api}/bot{self.token}/getupdates").json()
	# GET LAST UPDATE
	def get_last_update(self):
		return post(url=f"https://{self.api}/bot{self.token}/getupdates").json()["result"][-1]
	# MESSAGE
	# SEND MESSAGE
	def send_message(self, chat_id:int, text:str, reply_markup="", disable_notification=False):
		return post(url=f"https://{self.api}/bot{self.token}/sendmessage", json={"chat_id":chat_id, "text":text, "reply_markup":reply_markup, "disable_notification":disable_notification}).json()
	# EDIT MESSAGE
	def edit_message(self, chat_id:int, message_id:int, text:str, reply_markup=""):
		return post(url=f"https://{self.api}/bot{self.token}/editmessagetext", json={"chat_id":chat_id, "message_id":message_id, "text":text, "reply_markup":reply_markup}).json()
	# DELETE MESSAGE
	def delete_message(self, chat_id:int, message_ids:list):
		if self.app == "telegram":
			return post(url=f"https://{self.api}/bot{self.token}/deletemessages", json={"chat_id":chat_id, "message_ids":message_ids}).json()
		elif self.app == "bale":
			return post(url=f"https://{self.api}/bot{self.token}/deletemessage", json={"chat_id":chat_id, "message_id":message_ids}).json()
	def forward_message(self, chat_id:int, from_chat_id:int, message_ids:list, disable_notification=False):
		if self.app == "telegram":
			return post(url=f"https://{self.api}/bot{self.token}/forwardmessages", json={"chat_id":chat_id,"from_chat_id":from_chat_id , "message_ids":message_ids, "disable_notification":disable_notification}).json()
		elif self.app == "bale":
			return post(url=f"https://{self.api}/bot{self.token}/forwardmessage", json={"chat_id":chat_id,"from_chat_id":from_chat_id , "message_id":message_ids, "disable_notification":disable_notification}).json()
	# USERS
	# GET ME
	def getme(self):
		a = post(url=f"https://{self.api}/bot{self.token}/getme")
		a = a.json()
		return a
	# GET CHAT
	def get_chat(self, chat_id:int):
		a = post(url=f"https://{self.api}/bot{self.token}/getchat?chat_id={chat_id}")
		a = a.json()
		return a
	# SETWEBHOOK
	def setwebhook(self, url):
		return post(url=f"hhtps://{self.api}/bot{self.token}/setwebhook", json={"url":url}).json()
	# OPTIONS
	def keyboard(self, keys, resize_keyboard=True, one_time_keyboard=False):
		return {"keyboard":keys, "resize_keyboard":resize_keyboard, "one_time_keyboard":one_time_keyboard}
	def remove_keyboard(self):
		return {"remove_keyboard":True}
# MESSAGE CLASS FOR IMPORT DATA WITH UPDATES
class message:
	# GET UPDATE FOR IMPORT
	def __init__(self, update):
		if ifa(update):
			self.text = update["message"]["text"]
			self.message_id = update["message"]["message_id"]
			self.chat_id = update["message"]["chat"]["id"]
			self.first_name = update["message"]["chat"]["first_name"]
		else:
			self.text = update["callback_query"]["data"]
			self.message_id = update["callback_query"]["message"]["message_id"]
			self.chat_id = update["callback_query"]["from"]["id"]
			self.first_name = update["callback_query"]["from"]["first_name"]
