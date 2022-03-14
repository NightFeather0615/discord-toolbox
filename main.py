import requests
import argparse
import os, sys
import apnggif


class Core(object):
  def __init__(self):
    pass

  def make_folder(channel_id):
    if not os.path.exists(f"./{channel_id}"):
      os.mkdir(f"./{channel_id}")

  def download_image(url: str, file_name: str, file_type: str, output_dir: str, quiet: bool):
    with open(f"{output_dir}/{file_name}.{file_type}", "wb") as f:
      image = requests.get(url).content
      f.write(image)
      if quiet == False:
        print(f"Downloaded {file_name}.{file_type}, ~{round(len(image) * 0.001, 1)} KB")

  def build_parser():
    parser = argparse.ArgumentParser(description = 'Discord self-bot tools.', epilog = 'Made by NightFeather')

    tool_parsers = parser.add_subparsers(help='Tools', dest="tool")
    tool_parsers.required = True

    fetch_images_parser = tool_parsers.add_parser('fetch-images', help='fetch images from channel (only available if you are able to access the channel)')
    fetch_images_parser.add_argument('--token', "-t", required=True, nargs=1, type=str, help='user token (not bearer token)')
    fetch_images_parser.add_argument('--channel-id', "-c", required=True, nargs=1, type=str, help='discord channel ID')
    fetch_images_parser.add_argument('--output-dir', "-o", required=False, nargs=1, type=str, help='output directory')
    fetch_images_parser.add_argument('--quiet', "-q", required=False, action='store_true', help='quiet mode')

    fetch_stickers_parser = tool_parsers.add_parser('fetch-stickers', help='fetch stickers from guild (only available if you are able to access the guild)')
    fetch_stickers_parser.add_argument('--token', "-t", required=True, nargs=1, type=str, help='user token (not bearer token)')
    fetch_stickers_parser.add_argument('--guild-id', "-g", required=True, nargs=1, type=str, help='discord guild ID')
    fetch_stickers_parser.add_argument('--output-dir', "-o", required=False, nargs=1, type=str, help='output directory')
    fetch_stickers_parser.add_argument('--quiet', "-q", required=False, action='store_true', help='quiet mode')

    return parser.parse_args()

class Discord(object):
  def __init__(self):
    pass

  def fetch_user(token: str):
    user_data = requests.get("https://discord.com/api/users/@me", headers = {"Authorization": token}).json()
    if user_data.get('code') == 0:
      print("HTTP Error: 401 Unauthorized, invalid token")
      return None
    else:
      print(f"\nLogin success\nUser: {user_data['username']}#{user_data['discriminator']}\nID: {user_data['id']}\n")
      return user_data

class ImageFetcher(object):
  def __init__(self):
    pass

  def fetch_images(channel_id: str, token: str, output_dir: str, quiet: bool, before: str = None):
    if output_dir == None:
      Core.make_folder(f"./{channel_id}")
      output_dir = f"./{channel_id}"
    url = f"https://discord.com/api/channels/{channel_id}/messages" + ("" if before is None else f"?before={before}")
    messages = requests.get(url, headers = {"Authorization": token}).json()
    for message in messages:
      if message["attachments"] != []:
        for attachment in message["attachments"]:
          if attachment["content_type"].startswith("image/"):
            file_name = str(hash(message["id"] + message["timestamp"] + attachment["url"])).replace("-", "")
            Core.download_image(attachment["url"], file_name, "png", output_dir, quiet)
    if len(messages) == 50:
      ImageFetcher.fetch_images(channel_id, token, output_dir, quiet, messages[-1]["id"])
    else:
      print("Fetching complete.")


class StickersFetcher(object):
  def __init__(self):
    pass

  def fetch_stickers(guild_id: str, token: str, output_dir: str, quiet: bool):
    if output_dir == None:
      Core.make_folder(f"./{guild_id}")
      output_dir = f"./{guild_id}"
    url = f"https://discord.com/api/guilds/{guild_id}/stickers"
    stickers = requests.get(url, headers = {"Authorization": token}).json()
    for sticker in stickers:
      sticker_url = f"https://media.discordapp.net/stickers/{sticker['id']}.png"
      Core.download_image(sticker_url, sticker['id'], "png", output_dir, quiet)
      if sticker['format_type'] == 2:
        apnggif.apnggif(png = f"./{output_dir}/{sticker['id']}.png", gif = f"./{output_dir}/{sticker['id']}.gif")
        os.remove(f"./{output_dir}/{sticker['id']}.png")
        print(f"Converted {sticker['id']}.png to {sticker['id']}.gif")
    print("\nFetching complete.")

def main():
  args = Core.build_parser()
  if Discord.fetch_user(args.token[0]) != None:
    print("Starting...\n")
    if args.tool == "fetch-images":
      ImageFetcher.fetch_images(args.channel_id[0], args.token[0], args.output_dir, args.quiet)
    if args.tool == "fetch-stickers":
      StickersFetcher.fetch_stickers(args.guild_id[0], args.token[0], args.output_dir, args.quiet)

if "__main__" == __name__:
  main()