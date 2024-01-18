v0.0.1
# Please Note
The primary purpose of this readme is for my own benefit, it is entirely just ramblings of a madman.

## To-Do
- find better tts engine
- modify functionality to be more user-friendly
- slim down code used from ao3 api to necessary bits only
- improve conversion speed
- look into fixing bugs

## Bugs to Fix
- fictional email addresses are being filtered by cloudflare (but not fictional phone numbers) -- need to modify parser code
- certain text-based page breaks are said verbatim -- find way to recognize & purge page breaks like that
- can't read text in embedded images -- need to modify parser code & implement optical character recognition for images

## Credits
- uses [gTTS](https://github.com/pndurette/gTTS)
- This project uses Armando Flores's [Ao3_API](https://github.com/ArmindoFlores/ao3_api)

- fic being used to test this version is [User Since](https://archiveofourown.org/works/1012337) by rageprufrock