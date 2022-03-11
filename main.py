import requests
import time
import os, sys

user_token = input("[User Token (not Bearer token)]\n$ ")
channel_id = input("[Channel ID]\n$ ")

def main():
  fetch_user(user_token)

def fetch_user(user_token: str):
  os.system('cls' if os.name == 'nt' else 'clear')
  url = "https://discord.com/api/users/@me"
  user_data = requests.get(url, headers = {"Authorization": user_token})
  user_data = user_data.json()
  print(f"[Logged in as user]\n - ID: {user_data['id']}\n - Username: {user_data['username']}\n - Discriminator: {user_data['discriminator']}")
  check_is_continue()

def check_is_continue():
  print("\n[Warning]\n - This program use self-bot to fetch image, which aginest Discord ToS, are you sure you want to continue? (y/n)")
  while True:
    choice = input(f"$ ")
    if choice.lower() == "y":
      try:
        os.mkdir(f"./Fetched-Channels/{channel_id}")
      except FileExistsError:
        pass
      fetch_images(channel_id)
      break
    elif choice.lower() == "n":
      sys.exit()
    else:
      print("[Error]\n - Invalid input")

def fetch_images(channel_id: str, before: str = None):
  url = "https://discord.com/api/channels/" + (f"{channel_id}/messages" if before is None else f"{channel_id}/messages?before={before}")
  data = requests.get(url, headers = {"Authorization": user_token})
  data = data.json()
  download_image(data)
  if len(data) == 50:
    fetch_images(channel_id, data[-1]["id"])
  else:
    print("\n[Program exits]\n - No more messages content attachments to fetch.")
    sys.exit()

def download_image(data):
  for message in data:
    if message["attachments"] != []:
      print("")
      print(f"[Fetched message]\n - ID: {message['id']}\n - Attachments: {len(message['attachments'])}")
      for attachment in message["attachments"]:
        if attachment["content_type"].startswith("image/"):
          print("")
          file_name = str(hash(message["id"] + message["timestamp"] + attachment["url"])).replace("-", "")
          with open(f"./Fetched-Channels/{channel_id}/{file_name}.png", "wb") as f:
            raw_image = requests.get(attachment["url"])
            file_size = round(raw_image.content.__sizeof__() * 0.001, 1)
            print(f"[Download Image]\n - Name: {file_name}.png\nSize: ~{file_size} KB")
            f.write(raw_image.content)

if "__main__" == __name__:
  main()