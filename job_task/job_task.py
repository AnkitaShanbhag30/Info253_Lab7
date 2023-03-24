import os
from celery import Celery
# import requests
from collections import Counter
# from bs4 import BeautifulSoup
import re
import nltk
import time

broker_url  = os.environ.get("CELERY_BROKER_URL"),
res_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery_app = Celery(name           = 'job_task',
                    broker         = broker_url,
                    result_backend = res_backend)
print(celery_app, flush=True)

@celery_app.task
def count_words(dataText):
    try:
        print(dataText, flush=True)
        r = dataText
        print(r, flush=True)
    except:
        return 0

    if r:
        # text processing
        print(dataText, flush=True)
        tokens = nltk.word_tokenize(dataText)
        text = nltk.Text(tokens)
        # remove punctuation, count raw words
        nonPunct = re.compile('.*[A-Za-z].*')
        words_count = len([w for w in text if nonPunct.match(w)])
        # words_count = len(r.split())
        time.sleep(words_count)
        return words_count
    
    return 0