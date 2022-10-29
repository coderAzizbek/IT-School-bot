import logging
from aiogram.types import Message, ReplyKeyboardRemove
from googletrans import Translator
import requests
import json
from loader import dp
from keyboards.default.ask import Homepage

app_id = "b3d51d5c"
app_key = "44cb194845fbb877d2587a4f8b538222"
language = "en-gb"

translator = Translator()

logging.basicConfig(level=logging.INFO)

@dp.message_handler(text_contains="Speak English")
async def speak_english(message: Message):
    await message.answer("So'z yuboring", reply_markup=Homepage)


def GetDifinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()

    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definition = []
    for sense in senses:
        definition.append(f"👉 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definition)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output


@dp.message_handler()
async def translate(message: Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        if lang == 'en':
            dest = 'uz'
        elif lang == 'ru':
            dest = 'uz'
        else:
            dest = 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text
        lookup = GetDifinitions(word_id)
        if lookup:
            await message.reply(f"Word:{word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi 😞")
