import argparse
import os
import requests

class Core(object):
  def __init__(self):
    pass

  def make_folder(channel_id) -> None:
    if not os.path.exists(f"./{channel_id}"):
      os.mkdir(f"./{channel_id}")

  def download_file(url: str, file_name: str, file_type: str, output_dir: str, quiet: bool) -> None:
    with open(f"{output_dir}/{file_name}.{file_type}", "wb") as f:
      file = requests.get(url).content
      f.write(file)
      if quiet == False:
        print(f"Downloaded {file_name}.{file_type}, ≈{round(len(file) * 0.001, 1)} KB")

  def build_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = 'Discord self-bot tools.', epilog = 'Made by NightFeather')
    parser.add_argument('--token', "-t", required=True, nargs=1, type=str, help='user token (not bearer token)')

    tool_parsers = parser.add_subparsers(dest="tool", title = 'Tools')

    change_hypesquad_parser = tool_parsers.add_parser('change-hypesquad', help='change hypesquad house directly without filling out the form')
    change_hypesquad_parser.add_argument('--house-id', "-i", required=True, choices=[1, 2, 3], nargs=1, type=int, help='hypersquad guild id [1: Bravery, 2: Brilliance, 3: Balance]')

    fetch_images_parser = tool_parsers.add_parser('backup-media', help='backup medias from channel (only available if you are able to access the channel)')
    fetch_images_parser.add_argument('--channel-id', "-c", required=True, nargs=1, type=str, help='discord channel id')
    fetch_images_parser.add_argument('--output-dir', "-o", required=False, nargs=1, type=str, help='output directory')
    fetch_images_parser.add_argument('--quiet', "-q", required=False, action='store_true', help='quiet mode')

    fetch_emojis_parser = tool_parsers.add_parser('fetch-emoji', help='fetch emojis from guild (only available if you are able to access the guild)')
    fetch_emojis_parser.add_argument('--guild-id', "-g", required=True, nargs=1, type=str, help='discord guild id')
    fetch_emojis_parser.add_argument('--output-dir', "-o", required=False, nargs=1, type=str, help='output directory')
    fetch_emojis_parser.add_argument('--quiet', "-q", required=False, action='store_true', help='quiet mode')

    fetch_stickers_parser = tool_parsers.add_parser('fetch-sticker', help='fetch stickers from guild (only available if you are able to access the guild)')
    fetch_stickers_parser.add_argument('--guild-id', "-g", required=True, nargs=1, type=str, help='discord guild id')
    fetch_stickers_parser.add_argument('--output-dir', "-o", required=False, nargs=1, type=str, help='output directory')
    fetch_stickers_parser.add_argument('--quiet', "-q", required=False, action='store_true', help='quiet mode')

    return parser.parse_args()