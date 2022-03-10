import requests
import time
import logging

user_token = input("User Token (mfa): ")
channel_id = input("Channel ID: ")
folder_path = input("Folder: ")

logging.basicConfig(level = logging.INFO,
                    format = '[%(asctime)s] [%(levelname)s] %(message)s',
                    datefmt = '%Y/%m/%d %I:%M:%S')

def main():
  data = requests.get(f"https://discord.com/api/channels/{channel_id}/messages", headers = {"Authorization": user_token})
  data = data.json()
  for message in data:
    logging.info(f"Message: {message['id']} | Timestamp: {message['timestamp']} | Attachments: {len(message['attachments'])}")
    for attachment in message["attachments"]:
      if attachment["content_type"].startswith("image/"):
        file_name = hash(message["id"] + message["timestamp"] + attachment["url"])
        with open(f"./{folder_path}/{file_name}.png", "wb") as f:
          f.write(requests.get(attachment["url"]).content)
  logging.info("Sleep for 30 seconds to avoid rate limit...")
  time.sleep(30)
  continue_fetch_images(data[-1]["id"])

def continue_fetch_images(before: str):
  data = requests.get(f"https://discord.com/api/channels/{channel_id}/messages?before={before}", headers = {"Authorization": user_token})
  data = data.json()
  for message in data:
    logging.info(f"Message: {message['id']} | Timestamp: {message['timestamp']} | Attachments: {len(message['attachments'])}")
    for attachment in message["attachments"]:
      if attachment["content_type"].startswith("image/"):
        file_name = hash(message["id"] + message["timestamp"] + attachment["url"])
        with open(f"./{folder_path}/{file_name}.png", "wb") as f:
          f.write(requests.get(attachment["url"]).content)
  logging.info("Sleep for 30 seconds to avoid rate limit...")
  time.sleep(30)
  if len(data) == 50:
    continue_fetch_images(data[-1]["id"])
  else:
    logging.info("No more image to fetch.")

if "__main__" == __name__:
  main()