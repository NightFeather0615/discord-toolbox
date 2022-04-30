import requests
import os, sys
import apnggif
from .Core import Core

class StickerFetcher(object):
  def __init__(self):
    pass

  def fetch_sticker(guild_id: str, token: str, output_dir: str, quiet: bool) -> None:
    url = f"https://discord.com/api/guilds/{guild_id}/stickers"
    stickers = requests.get(url, headers = {"Authorization": token}).json()

    if isinstance(stickers, dict) and stickers.get('code'):
      print(f"[Fetch Failed]\nError {stickers['code']}: {stickers['message']}")
      sys.exit(1)

    if output_dir == None:
      output_dir = f"./sticker/{guild_id}"
      Core.make_folder("./sticker")
      Core.make_folder(f"./sticker/{guild_id}")

    for sticker in stickers:
      sticker_url = f"https://media.discordapp.net/stickers/{sticker['id']}.png"
      Core.download_file(sticker_url, sticker['id'], "png", output_dir, quiet)

      if sticker['format_type'] == 2:
        apnggif.apnggif(png = f"./{output_dir}/{sticker['id']}.png", gif = f"./{output_dir}/{sticker['id']}.gif")
        os.remove(f"./{output_dir}/{sticker['id']}.png")
        print(f"Converted {sticker['id']}.png to gif")
      elif sticker['format_type'] == 3:
        print("Convert failed, unsupported format: Lottie")

    print(f"\n[Fetch Complete]\nDownloaded {len(stickers)} sticker(s)")