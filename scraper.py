import  requests
from bs4 import BeautifulSoup

# s223667

## Analiza struktury opinni w serwisie [Ceneo.pl]

|Składowa|Selektor|Zmienna|
|--------|--------|-------|
|opinia|div.js_product.review|review|
|identyfikator opinni|\[data-entry-id\]|review_id|
|autor|span.user-post__author-name|author|
|rekomandacja|span.user-post_author-recomendation > em|recomendation|
|liczba gwiazdek|span.user-post_score-count|stars|
|treść|div.user-post_text|content|
|data wystawienia|span.user-post_published > time:nth-child(1)\[datetime\]|publish_date|
|data zakupu|span.user-post_published > time:nth-child(2)\[datetime\]|purchase_date|
|dla ilu przydatna|button.vote-yes > span <br>button.vote-yes[data-total-vote] <br>span[id|usefull|
|dla ilu nieprzydatna|useless||
|lista zalet|div.review-feature_tittle--positives ~ review feature_item |Positives|
|lista wad|div.review-feature_tittle--negatives ~ review feature_item |cons|
||||

url = "https://www.ceneo.pl/95365253;pla?se=YxWbm1iqQxdyrhZALD2q02WnsAqEsNg5&shop=146599625&gclid=EAIaIQobChMIz5SOvanU9gIVM0aRBR1U1Qi3EAQYASABEgI1O_D_BwE"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

print(page_dom.prettify())
#pretiffy robi nam wcięcia