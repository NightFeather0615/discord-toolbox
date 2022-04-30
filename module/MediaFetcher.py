import requests
import sys
from .Core import Core

class MediaFetcher(object):
  def __init__(self):
    pass

  def fetch_media(channel_id: str, token: str, output_dir: str, quiet: bool, before: str = None) -> None:
    url = f"https://discord.com/api/channels/{channel_id}/messages" + ("" if before is None else f"?before={before}")
    messages = requests.get(url, headers = {"Authorization": token}).json()

    if isinstance(messages, dict) and messages.get('code'):
      print(f"[Backup Failed]\nError {messages['code']}: {messages['message']}")
      sys.exit(1)

    if output_dir == None:
      output_dir = f"./backup/{channel_id}/media"
      Core.make_folder("./backup")
      Core.make_folder(f"./backup/{channel_id}")
      Core.make_folder(f"./backup/{channel_id}/media")

    media_count = 0
    for message in messages:
      if message["attachments"] != []:
        media_index = 1
        for attachment in message["attachments"]:
          if attachment["content_type"].startswith(("image/", "video/", "audio/")):
            file_type = attachment["content_type"].split("/")[1]
            if file_type == "quicktime": file_type = "mov"
            file_name = f"{message['id']} - {media_index}"
            Core.download_file(attachment["url"], file_name, file_type, output_dir, quiet)
            media_count += 1
            media_index += 1

    if len(messages) == 50:
      MediaFetcher.fetch_media(channel_id, token, output_dir, quiet, messages[-1]["id"])
    else:
      print(f"\n[Backup Complete]\nDownloaded {media_count} media(s)")