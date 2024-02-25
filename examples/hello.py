from pyrotel import *

api_token = ""
admins = [0, 1, 2, 3, 4]

bot = client(api_token)

for i in admins:
  bot.send_message(i, "hello my admin")
