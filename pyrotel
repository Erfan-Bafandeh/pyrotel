from .util import message
from colorama import Fore
import requests
from subprocess import getoutput as cmd

# dev by Erfan-Bafandeh - persian py

lib_name = "pyrotel"

print("Loading . .")

version = requests.get(f"https://pypi.org/pypi/{lib_name}/json").json()["info"]["version"]

libs = cmd("pip freeze").split("\n")

for i in range(len(libs)):
    info = libs[i].split("==")
    if info[0] == lib_name:
        last_version = info[1]
if last_version != version:
    print(f"""
you have a new update !

lib name: {Fore.LIGHTCYAN_EX}{lib_name}{Fore.RESET}
version: {Fore.LIGHTCYAN_EX}{last_version}{Fore.RESET}
new vesion: {Fore.LIGHTCYAN_EX}{version}{Fore.RESET}
""")

print(f"""
Welcome to {lib_name} {Fore.LIGHTCYAN_EX}{version}{Fore.RESET} library.

dev by {Fore.LIGHTYELLOW_EX}Erfan Bafandeh.{Fore.RESET}
""")

class Client:

    def __init__(self, token: str, timeout: float = 10, debug_mode: bool = True) -> None:
        self.token = token
        self.timeout = timeout
        self.debug_mode = debug_mode

    def request(self, method: str, json: dict = {}, files: dict = {}) -> dict:
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        if json != {} and files != {}:
            response = requests.post(url=url, data=json, files=files).json()
        elif json != {}:
            response = requests.post(url=url, data=json).json()
        elif files != {}:
            response = requests.post(url=url, files=files).json()
        else:
            response = requests.post(url=url).json()
        if response["ok"]:
            return response
        else:
            if self.debug_mode:
                print(f"""This is an error message from {Fore.LIGHTCYAN_EX}pyrotel{Fore.RESET} lib:
{Fore.LIGHTRED_EX}{method}{Fore.RESET} method has a bug.

description: {response["description"]}
note: if you can't debug this error, you can send a message to pyrotel lib support in telegram massenger.
support: {Fore.LIGHTCYAN_EX}t.me/ppy_sup{Fore.RESET}""")
            return response

    def on_message(self):
        '''Use this method to receive updates
        Example:
            from balepy import Client

            client = Client('token', timeout=10)
            def main():
                for update in client.on_message():
                    print(update.text)

            main()
        '''
        payload: dict = {
            'offset': -1, 'limit': 100
        }
        while True:
            update = self.request('getupdates', json=payload)
            payload['offset'] = 1
            if (update != None) and (update['ok']) and (update['result'] != []):
                break

        payload['offset'] = update['result'][len(update['result'])-1]['update_id'] + 1
        payload['limit'] = 1
        while True:
            responce = self.request('getupdates', json=payload)
            if responce != None and responce['result'] != []:
                payload['offset'] += 1
                yield message(responce['result'][0])

    async def get_updates(self) -> dict:
        return self.request("getupdates")

    async def set_webhook(self, url: str) -> dict:
        payload = {
            "url":url
        }
        return self.request("setwebhook", json=payload)

    async def delete_webhook(self) -> dict:
        return self.request("deletewebhook")

    async def get_webhookinfo(self) -> dict:
        return self.request("getwebhookinfo")

    async def send_message(self, 
                           chat_id: int, 
                           text: str, 
                           disable_notification: bool = False, 
                           reply_markup: dict = "", 
                           reply_to_message_id: int = 0,
                           message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id, 
            "text":text, 
            "reply_markup":reply_markup, 
            "reply_to_message_id":reply_to_message_id, 
            "disable_notification":disable_notification,
            "message_thread_id":message_thread_id
        }
        return self.request("sendmessage", json=payload)

    async def send_photo(self, 
                         chat_id: int,
                         file: bytes,
                         caption: str = "",
                         has_spoiler: bool = False,
                         disable_notification: bool = False, 
                         reply_markup: dict = "",
                         reply_to_message_id: int = 0,
                         message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id,
            "caption":caption,
            "has_spoiler":has_spoiler,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        files = {
            "photo":open(file, "rb")
        }
        return self.request("sendphoto", json=payload, files=files)

    async def send_audio(self, 
                         chat_id: int,
                         file: bytes,
                         caption: str = "",
                         disable_notification: bool = False, 
                         reply_markup: dict = "",
                         reply_to_message_id: int = 0,
                         message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id,
            "caption":caption,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        files = {
            "audio":open(file, "rb")
        }
        return self.request("sendaudio", json=payload, files=files)

    async def send_document(self, 
                         chat_id: int,
                         file: bytes,
                         caption: str = "",
                         disable_notification: bool = False, 
                         reply_markup: dict = "",
                         reply_to_message_id: int = 0,
                         message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id,
            "caption":caption,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        files = {
            "document":open(file, "rb")
        }
        return self.request("senddocument", json=payload, files=files)

    async def send_video(self, 
                         chat_id: int,
                         file: bytes,
                         caption: str = "",
                         has_spoiler: bool = False,
                         disable_notification: bool = False, 
                         reply_markup: dict = "",
                         reply_to_message_id: int = 0,
                         message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id,
            "caption":caption,
            "has_spoiler":has_spoiler,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        files = {
            "video":open(file, "rb")
        }
        return self.request("sendvideo", json=payload, files=files)

    async def send_voice(self, 
                         chat_id: int,
                         file: bytes,
                         caption: str = "",
                         disable_notification: bool = False, 
                         reply_markup: dict = "",
                         reply_to_message_id: int = 0,
                         message_thread_id: int = 0) -> dict:
        payload = {
            "chat_id":chat_id,
            "caption":caption,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        files = {
            "voice":open(file, "rb")
        }
        return self.request("sendvoice", json=payload, files=files)

    async def send_contact(self,
                           chat_id: int,
                           phone_number: str,
                           first_name: str,
                           last_name: str = "",
                           disable_notification: bool = False,
                           reply_markup: dict = "",
                           reply_to_message_id: int = 0,
                           message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "phone_number":phone_number,
            "first_name":first_name,
            "last_name":last_name,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        return self.request("sendcontact", json=payload)

    async def send_dice(self,
                        chat_id: int,
                        emoji: str = "",
                        disable_notification: bool = False,
                        reply_markup: dict = "",
                        reply_to_message_id: int = 0,
                        message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "emoji":emoji,
            "disable_notification":disable_notification,
            "reply_markup":reply_markup,
            "reply_to_message_id":reply_to_message_id,
            "message_thread_id":message_thread_id
        }
        return self.request("senddice", json=payload)

    async def get_user_profiles(self,
                                user_id: int):
        payload = {
            "user_id":user_id
        }
        return self.request("getUserProfilePhotos", json=payload)

    async def ban_chat_member(self,
                              chat_id: int,
                              user_id: int,
                              revoke_messages: bool = False):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id,
            "revoke_messages":revoke_messages
        }
        return self.request("banchatmember", json=payload)

    async def unban_chat_member(self,
                              chat_id: int,
                              user_id: int,
                              only_if_banned: bool = False):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id,
            "only_if_banned":only_if_banned
        }
        return self.request("unbanchatmember", json=payload)

    async def restrict_chat_member(self,
                                   chat_id: int,
                                   user_id: int,
                                   permissions: dict):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id,
            "permissions":permissions
        }
        return self.request("restrictChatMember", json=payload)

    async def promote_chat_member(self,
                                  chat_id: int,
                                  user_id: int,
                                  is_anonymous: bool = False,
                                  can_delete_messages: bool = False,
                                  can_restrict_members: bool = False,
                                  can_promote_members: bool = False,
                                  can_invite_users: bool = True,
                                  can_change_info: bool = False,
                                  can_pin_messages: bool = True):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id,
            "is_anonymous":is_anonymous,
            "can_delete_messages":can_delete_messages,
            "can_restrict_members":can_restrict_members,
            "can_promote_members":can_promote_members,
            "can_invite_users":can_invite_users,
            "can_change_info":can_change_info,
            "can_pin_messages":can_pin_messages
        }
        return self.request("promoteChatMember", json=payload)

    async def set_admin_custom_title(self,
                                     chat_id: int,
                                     user_id: int,
                                     custom_title: str):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id,
            "custom_title":custom_title
        }
        return self.request("setChatAdministratorCustomTitle", json=payload)

    async def ban_chatsender(self,
                             chat_id: int,
                             sender_chat_id: int):
        payload = {
            "chat_id":chat_id,
            "sender_chat_id":sender_chat_id
        }
        return self.request("banChatSenderChat", json=payload)

    async def unban_chatsender(self,
                             chat_id: int,
                             sender_chat_id: int):
        payload = {
            "chat_id":chat_id,
            "sender_chat_id":sender_chat_id
        }
        return self.request("unbanChatSenderChat", json=payload)

    async def set_chat_permissions(self,
                                   chat_id: int,
                                   permissions: dict):
        payload = {
            "chat_id":chat_id,
            "permissions":permissions
        }
        return self.request("setChatPermissions", json=payload)

    async def get_chat_link(self,
                            chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("exportChatInviteLink", json=payload)

    async def create_invite_link(self,
                                 chat_id: int,
                                 name: str,
                                 expire_date: int = 99999999999999999,
                                 member_limit: int = 99999,
                                 creates_join_request: bool = False):
        payload = {
            "chat_id":chat_id,
            "name":name,
            "expire_date":expire_date,
            "member_limit":member_limit,
            "creates_join_request":creates_join_request
        }
        return self.request("createChatInviteLink", json=payload)

    async def edit_invite_link(self,
                                 chat_id: int,
                                 invite_link: str,
                                 name: str,
                                 expire_date: int = 99999999999999999,
                                 member_limit: int = 99999,
                                 creates_join_request: bool = False):
        payload = {
            "chat_id":chat_id,
            "name":name,
            "invite_link":invite_link,
            "expire_date":expire_date,
            "member_limit":member_limit,
            "creates_join_request":creates_join_request
        }
        return self.request("editChatInviteLink", json=payload)

    async def remove_invite_link(self,
                                 chat_id: int,
                                 invite_link: str):
        payload = {
            "chat_id":chat_id,
            "invite_link":invite_link
        }
        return self.request("revokeChatInviteLink", json=payload)

    async def accept_chat_join_request(self,
                                       chat_id: int,
                                       user_id: int):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id
        }
        return self.request("approveChatJoinRequest", json=payload)

    async def cancel_chat_join_request(self,
                                       chat_id: int,
                                       user_id: int):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id
        }
        return self.request("declineChatJoinRequest", json=payload)

    async def set_chat_photo(self,
                             chat_id: int,
                             file: bytes):
        payload = {
            "chat_id":chat_id
        }
        files = {
            "photo":open(file, "rb")
        }
        return self.request("setChatPhoto", json=payload, files=files)

    async def delete_chat_photo(self,
                                chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("deleteChatPhoto", json=payload)

    async def set_chat_title(self,
                             chat_id: int,
                             title: str):
        payload = {
            "chat_id":chat_id,
            "title":title
        }
        return self.request("setChatTitle", json=payload)

    async def set_chat_description(self,
                                   chat_id: int,
                                   description: str):
        payload = {
            "chat_id":chat_id,
            "description":description
        }
        return self.request("setChatDescription", json=payload)

    async def pin_message(self,
                          chat_id: int,
                          message_id: int,
                          disable_notification: bool = False):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id,
            "disable_notification":disable_notification
        }
        return self.request("pinChatMessage", json=payload)

    async def unpin_message(self,
                            chat_id: int,
                            message_id: int):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id
        }
        return self.request("unpinChatMessage", json=payload)

    async def unpin_all_messages(self,
                                 chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("unpinAllChatMessages", json=payload)

    async def leave_chat(self,
                         chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("leaveChat", json=payload)

    async def get_chat_admins(self,
                              chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("getChatAdministrators", json=payload)

    async def get_chat_member_count(self,
                                    chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("getChatMemberCount", json=payload)

    async def get_chat_member_info(self,
                                   chat_id: int,
                                   user_id: int):
        payload = {
            "chat_id":chat_id,
            "user_id":user_id
        }
        return self.request("getChatMember", json=payload)

    async def create_forum_topic(self,
                                chat_id: int,
                                name: str):
        payload = {
            "chat_id":chat_id,
            "name":name
        }
        return self.request("createForumTopic", json=payload)

    async def close_forum_topic(self,
                                chat_id: int,
                                message_thread_id: int):
        payload = {
            "chat_id":chat_id,
            "message_thread_id":message_thread_id
        }
        return self.request("closeForumTopic", json=payload)

    async def open_forum_topic(self,
                               chat_id: int,
                               message_thread_id: int):
        payload = {
            "chat_id":chat_id,
            "message_thread_id":message_thread_id
        }
        return self.request("reopenForumTopic", json=payload)

    async def delete_forum_topic(self,
                                 chat_id: int,
                                 message_thread_id: int):
        payload = {
            "chat_id":chat_id,
            "message_thread_id":message_thread_id
        }
        return self.request("deleteForumTopic", json=payload)

    async def unpin_all_topic_messages(self,
                                       chat_id: int,
                                       message_thread_id: int):
        payload = {
            "chat_id":chat_id,
            "message_thread_id":message_thread_id
        }
        return self.request("unpinAllForumTopicMessages", json=payload)

    async def edit_general_forum_topic(self,
                                       chat_id: int,
                                       name: str):
        payload = {
            "chat_id":chat_id,
            "name":name
        }
        return self.request("editGeneralForumTopic", json=payload)

    async def close_general_forum_topic(self,
                                       chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("closeGeneralForumTopic", json=payload)

    async def open_general_forum_topic(self,
                                       chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("reopenGeneralForumTopic", json=payload)

    async def hide_general_forum_topic(self,
                                       chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("hideGeneralForumTopic", json=payload)

    async def unhide_general_forum_topic(self,
                                         chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("unhideGeneralForumTopic", json=payload)

    async def unpin_general_topic_messages(self,
                                           chat_id: int):
        payload = {
            "chat_id":chat_id
        }
        return self.request("unpinAllGeneralForumTopicMessages", json=payload)

    async def set_my_name(self,
                              name: str):
        payload = {
            "name":name
        }
        return self.request("SetMyName", json=payload)

    async def get_my_name(self):
        return self.request("GetMyName")

    async def set_my_description(self,
                              description: str):
        payload = {
            "description":description
        }
        return self.request("SetMyDescription", json=payload)

    async def get_my_description(self):
        return self.request("GetMyDescription")

    async def set_my_short_description(self,
                              short_description: str):
        payload = {
            "short_description":short_description
        }
        return self.request("SetMyShortDescription", json=payload)

    async def get_my_short_description(self):
        return self.request("GetMyShortDescription")

    async def edit_message_text(self,
                                chat_id: int,
                                message_id: int,
                                text: str,
                                reply_markup: dict = ""):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id,
            "text":text,
            "reply_markup":reply_markup
        }
        return self.request("editMessageText", json=payload)

    async def edit_message_caption(self,
                                chat_id: int,
                                message_id: int,
                                caption: str,
                                reply_markup: dict = ""):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id,
            "caption":caption,
            "reply_markup":reply_markup
        }
        return self.request("editMessageCaption", json=payload)

    async def edit_message_caption(self,
                                chat_id: int,
                                message_id: int,
                                reply_markup: dict = ""):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id,
            "reply_markup":reply_markup
        }
        return self.request("editMessageReplyMarkup", json=payload)

    async def delete_message(self,
                             chat_id: int,
                             message_id: int):
        payload = {
            "chat_id":chat_id,
            "message_id":message_id
        }
        return self.request("deleteMessage", json=payload)

    async def delete_messages(self,
                             chat_id: int,
                             message_ids: int):
        payload = {
            "chat_id":chat_id,
            "message_ids":message_ids
        }
        return self.request("deleteMessages", json=payload)

    async def forward_message(self,
                              chat_id: int,
                              from_chat_id: int,
                              message_id: int,
                              disable_notification: bool = False,
                              message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "from_chat_id":from_chat_id,
            "message_id":message_id,
            "disable_notification":disable_notification,
            "message_thread_id":message_thread_id
        }
        return self.request("forwardMessage", json=payload)

    async def forward_messages(self,
                              chat_id: int,
                              from_chat_id: int,
                              message_ids: dict,
                              disable_notification: bool = False,
                              message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "from_chat_id":from_chat_id,
            "message_ids":message_ids,
            "disable_notification":disable_notification,
            "message_thread_id":message_thread_id
        }
        return self.request("forwardMessages", json=payload)

    async def copy_message(self,
                              chat_id: int,
                              from_chat_id: int,
                              message_id: int,
                              disable_notification: bool = False,
                              caption: str = "",
                              reply_markup: dict = "",
                              message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "from_chat_id":from_chat_id,
            "message_id":message_id,
            "disable_notification":disable_notification,
            "caption":caption,
            "reply_markup":reply_markup,
            "message_thread_id":message_thread_id
        }
        return self.request("copyMessage", json=payload)

    async def copy_messages(self,
                              chat_id: int,
                              from_chat_id: int,
                              message_ids: str,
                              disable_notification: bool = False,
                              remove_caption: bool = False,
                              message_thread_id: int = 0):
        payload = {
            "chat_id":chat_id,
            "from_chat_id":from_chat_id,
            "message_ids":message_ids,
            "disable_notification":disable_notification,
            "remove_caption":remove_caption,
            "message_thread_id":message_thread_id
        }
        return self.request("copyMessages", json=payload)

    async def getme(self) -> dict:
        return self.request("getme")
