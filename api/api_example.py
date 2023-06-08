from pprint import pprint
from requests import get

responce = get("https://newsapi.org/v2/everything?q=apple&from=2023-06-07&to=2023-06-07&sortBy=popularity&apiKey=6e3d876e28c6486e9d44d47b0276045d")

apple_data = responce.json()

yazar = input('yazar ismi giriniz: ')
for i in apple_data.get("articles"):
    if i.get('author') == yazar:
        pprint(i)


