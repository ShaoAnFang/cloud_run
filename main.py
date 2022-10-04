import os
import json
import random
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route('/GGWP', methods=['GET'])
def test():
    return "GGWP"

#AVgle API
@app.route('/avgle', methods=['GET'])
def darkAnan():
    AVGLE_LIST_COLLECTIONS_API_URL = 'https://api.avgle.com/v1/videos/{}'

    randomPagesNumber = random.randint(0,1195)
    #page 1195,有60片,其他都50
    #print randomPageNumber
    if randomPagesNumber != 1195:
        #0~49選不重複的7個數字
        randomVideoNumbers = random.sample(range(0, 49), 5)
    else:
        randomVideoNumbers = random.sample(range(0, 59), 5)

    res = requests.get(AVGLE_LIST_COLLECTIONS_API_URL.format(randomPagesNumber))
    res.encoding='utf8'
    #print(res.json())
    videos = []
    videos = res.json()['response']['videos']
    
    videoRandom = []
    for x in randomVideoNumbers:
        videoRandom.append(videos[x])
    
    return json.dumps(videoRandom)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
