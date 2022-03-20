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