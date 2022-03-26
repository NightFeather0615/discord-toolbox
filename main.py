import sys
from module.Core import Core
from module.Discord import Discord
from module.EmojiFetcher import EmojiFetcher
from module.MediaFetcher import MediaFetcher
from module.StickerFetcher import StickerFetcher

ascii_title = u"""
 _____   _                       _   _______          _ _               
 |  __ \(_)                     | | |__   __|        | | |              
 | |  | |_ ___  ___ ___  _ __ __| |    | | ___   ___ | | |__   _____  __
 | |  | | / __|/ __/ _ \| '__/ _` |    | |/ _ \ / _ \| | '_ \ / _ \ \/ /
 | |__| | \__ \ (_| (_) | | | (_| |    | | (_) | (_) | | |_) | (_) >  < 
 |_____/|_|___/\___\___/|_|  \__,_|    |_|\___/ \___/|_|_.__/ \___/_/\_\\

                                                    Made by NightFeather                                         
"""

warning = "\n[WARNING]\nThis tool using self-bot, which is against Discord ToS, use at your own risk\n"

def main() -> None:
  print(ascii_title)
  print(warning)
  args = Core.build_parser()
  if Discord.fetch_user(args.token[0]) != None:
    if args.tool != None:
      print(f"[Info]\nStarting {args.tool}...\n")
      if args.tool == 'change-hypesquad':
        Discord.change_hypesquad_house(args.token[0], args.house_id[0])
      elif args.tool == "backup-media":
        MediaFetcher.fetch_media(args.channel_id[0], args.token[0], args.output_dir, args.quiet)
      elif args.tool == "fetch-sticker":
        StickerFetcher.fetch_sticker(args.guild_id[0], args.token[0], args.output_dir, args.quiet)
      elif args.tool == "fetch-emoji":
        EmojiFetcher.fetch_emoji(args.guild_id[0], args.token[0], args.output_dir, args.quiet)

if "__main__" == __name__:
  main()
  sys.exit(0)