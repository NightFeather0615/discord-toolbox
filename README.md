# discord-toolbox
a simple Discord self-bot tools combination package

# Available tools
* backup-images
* fetch-emojis
* fetch-stickers

## backup-images
Quick example:  
`python3 main.py backup-images --channel-id 456574854780912354 --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--channel-id|-c|True|Discord channel ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|

## fetch-emojis
Quick example:  
`python3 main.py fetch-emojis --guild-id 456574854780912354 --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--guild-id|-g|True|Discord guild ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|

## fetch-stickers
Quick example:  
`python3 main.py fetch-stickers --guild-id 456574854780912354 --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--guild-id|-g|True|Discord guild ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|
