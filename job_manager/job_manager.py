from flask import Flask, request
from job_task import count_words, celery_app
from celery.result import AsyncResult
import json

app = Flask(__name__)

@app.route('/count', methods = ['POST'])
def countWords():
    try:
        print("count words", flush=True)
        data = request.get_json()
        print(data, flush=True)
        dataText = data['text']
        print(dataText, flush=True)
        result = count_words.delay(dataText)
        return json.dumps({"id": result.id})
    except:
        return json.dumps({"message":"provide input with text as key"}),204

@app.route('/get_result/<id>', methods = ['GET'])
def get_count_words_url(id):

    res = AsyncResult(id.strip(), app=celery_app)
    count = -1
    if res.status == "SUCCESS":
        count = res.get()
    if count < 0:
        return json.dumps({"message":"this id does not exist"}),200
    else:
        return json.dumps({"count": count})
    
    

