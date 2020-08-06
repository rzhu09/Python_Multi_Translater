#Raymond Zhu || 5_31_2020

from googletrans import Translator
import pandas as pd
import inflect

def int_checker(num): #check if there is a number value in the string given
    try:
        temp = int(num)
        return True
    except ValueError:
        return False

translator = Translator() #main translator variable

text_to_translate = input("Text to Translate is: ") #grab user input on string to translate
language = translator.detect(text_to_translate).lang #figure out what langauge of the string is

inf_engine = inflect.engine() #begin the engine of converting string to numbers using the inflect library

text_array = "" #text holder for manipulation

for i in text_to_translate.split(' '): #grab every word in the given input
    if int_checker(i): #if there is a valid num to convert go here
        temp = inf_engine.number_to_words(i) #convert the num to english first
        temp_word = translator.translate(temp, dest = language).text #convert back the num to it's origin of language
        text_array += temp_word + ' ' #append the written out num in text to the text holder

    else: #else if the data is not a num just append it
        text_array += i + ' '

text_to_translate = text_array #make the text to translate equal to the manipulated string

number_of_lang = input("How many different translations do you want? ")

arr_of_lang = []

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

language_ = []
codes_ = []

for i in LANGUAGES:
    language_.append(LANGUAGES[i])
    codes_.append(i)

df = pd.DataFrame(codes_, language_,['Codes']) #create a new data frame for better visual

print("")
print("Example: English, input code 'en'")
print("List of Language Codes to choose from: ")
print("")

with pd.option_context('display.max_rows', None, 'display.max_columns', None): #display entire data frame
    print(df)

print("")


for i in range(int(number_of_lang)):
    temp = input('What is language {i} ? '.format(i = i+1))
    arr_of_lang.append(temp)

print("")

df2 = pd.read_csv('first_scrape.csv')

#df3 finds all the countries that have the official language equal to that of the user input
df3 = sorted(df2[df2['Official language'].apply(lambda val: LANGUAGES[language].upper() in str(val).upper())]['Country'].value_counts().index.tolist())

for i in arr_of_lang: #print out all the translated versions of the input in the lanaguages the user wanted
    print("'{}'".format(text_to_translate) + ' in {lan} is: '.format(lan = LANGUAGES[i].upper()) + translator.translate(text_to_translate, dest = i).text)

print("")

print("Fun Fact, the language {L} is an official language in : {d}".format(L = LANGUAGES[language].upper(), d = df3))