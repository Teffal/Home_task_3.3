# -*- coding: utf-8 -*-
import requests


def translate_text(text, language):
    API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.' \
              'a95fd4bfde5c1794fa433453956bd261eae80152'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': API_KEY,
        'lang': language,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    with open('RU.txt', 'w', encoding='utf-8')as f:
        f.write(' '.join(response.get('text')))


def open_file(file_name):
    with open(file_name + '.txt', encoding='utf-8') as f:
        translate_text(f.read(), file_name.lower()+'-ru')

if __name__ == "__main__":
    file_name = input('Enter file name: ')
    open_file(file_name)
