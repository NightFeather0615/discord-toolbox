import requests
import sys
from .Core import Core

class EmojiFetcher(object):
  def __init__(self):
    pass

  def fetch_emoji(guild_id: str, token: str, output_dir: str, quiet: bool) -> None:
    url = f"https://discord.com/api/guilds/{guild_id}/emojis"
    emojis = requests.get(url, headers = {"Authorization": token}).json()

    if isinstance(emojis, dict) and emojis.get('code'):
      print(f"[Fetch Failed]\nError {emojis['code']}: {emojis['message']}")
      sys.exit(1)

    if output_dir is None:
      output_dir = f"./emoji/{guild_id}"
      Core.make_folder("./emoji")
      Core.make_folder(f"./emoji/{guild_id}")

    for emoji in emojis:
      file_type = "png" if emoji['animated'] == False else "gif"
      emoji_url = f"https://cdn.discordapp.com/emojis/{emoji['id']}.{file_type}"
      file_name = f"{emoji['id']} - {emoji['name']}"
      Core.download_file(emoji_url, file_name, file_type, output_dir, quiet)

    print(f"\n[Fetch Complete]\nDownloaded {len(emojis)} emoji(s)")