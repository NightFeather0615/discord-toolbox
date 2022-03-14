# discord-toolbox
a simple Discord self-bot tools combination package

# Available tools
* Check Token
* Change HypeSquad House
* Backup Images
* Fetch Emojis
* Fetch Stickers

## Basic Command format
`python3 main.py --token TOKEN [TOOL] [Args]`

E.g.   
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw change-hypesquad --house-id 1`

## Check Token
Quick example:  
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|

## Change HypeSquad House
Quick example:  
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw change-hypesquad --house-id 1`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--house-id|-c|True|HypeSquad house ID|

|ID|House|
|-|-|
|1|Bravery|
|2|Brilliance|
|3|Balance|

## Backup Images
Quick example:  
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw backup-images --channel-id 456574854780912354`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--channel-id|-c|True|Discord channel ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|

## Fetch Emojis
Quick example:  
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw fetch-emojis --guild-id 456574854780912354`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--guild-id|-g|True|Discord guild ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|

## Fetch Stickers
Quick example:  
`python3 main.py --token OTIASDEQDA5Mjky.YEWQEQmw.PlM2JJQWEQWEDJ7HDyhrw fetch-stickers --guild-id 456574854780912354`

|Argument|Alias|Required|Description|
|-|-|-|-|
|--token|-t|True|Discord user token (not bearer token)|
|--guild-id|-g|True|Discord guild ID|
|--output-dir|-o|False|Output directory|
|--quiet|-q|False|Quiet output|
