import json
import  requests
from bs4 import BeautifulSoup

# s223667

## Analiza struktury opinni w serwisie [Ceneo.pl]

url = "https://www.ceneo.pl/95365253;pla?se=YxWbm1iqQxdyrhZALD2q02WnsAqEsNg5&shop=146599625&gclid=EAIaIQobChMIz5SOvanU9gIVM0aRBR1U1Qi3EAQYASABEgI1O_D_BwE"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("div.js_product-review")

all_reviews = []


for review in reviews: 

    review_id = review["data-entry-id"]

    author = review.select("span.user-post__author-name").pop(0).text.strip()

    try:
        recommendation = review.select("span.user-post__author-recomendation > em").pop(0).text
        recommendation = True if recommendation == "Polecam" else False
    except: recommendation = None
    stars = review.select("span.user-post__score-count").pop(0).text
    stars = float(stars.split("/").pop(0).replace(",","."))

    content = review.select("div.user-post__text").pop(0).get_text()

    content = content.replace("\n"," ").replace("  "," ").strip()

    publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]
    publish_date = publish_date.split("  ").pop(0)
    #print(type(publish_date))
    #print(publish_date)
    try:
        purchase_date =  review.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"]
        #print(type(purchase_date))
        #print(purchase_date)
    except IndexError: purchase_date = None

    useful = review.select("span[id^=votes-yes]").pop().text
    useful = review.select("span[id^=votes-yes]").pop().text
    useful = int(useful)

    useless = review.select("span[id^=votes-no]").pop().text
    useless = int(useful)

    #print(type(useless))
    #print(useless)

    pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
    pros = [item.text.strip() for item in pros]

    cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
    cons = [item.text.strip() for item in cons]

    #print(type(pros))
    #print(pros)

    single_review = {
        "review_id": review_id,
        "author": author,
        "recomendation": recommendation,
        "stars": stars,
        "content": content,
        "publish_date": publish_date,
        "purchase_date": purchase_date,
        "usefull": useful,
        "useless": useless,
        "pros": pros,
        "cons": cons,
    }
    all_reviews.append(single_review)
print(json.dumps(single_review, indent=4, ensure_ascii=False))
#pretiffy robi nam wcięcia