

## Future Plans
- plan to find better tts engine
- modify functionality to be more user-friendly
- slim down code used from ao3 api to necessary bits only

## Bugs to Fix
- fictional email addresses are being filtered by cloudflare (but not fictional phone numbers) -- need to modify parser code
- certain text-based page breaks are said verbatim -- find way to recognize & purge page breaks like that
- can't read text in embedded images -- need to modify parser code & implement optical character recognition for images


## Credits
- uses [gTTS](https://github.com/pndurette/gTTS)
- This project uses Armando Flores's [Ao3_API](https://github.com/ArmindoFlores/ao3_api)