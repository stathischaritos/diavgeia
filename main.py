import unirest
from elasticsearch import Elasticsearch
from queries import *
import json
import datetime


BASE_URL = "http://diavgeia.gov.gr/opendata/search.json"
INDEX = 'diavgeia'
PAGE_SIZE = 500

es = Elasticsearch()

#Find the oldest document already inside ES
try: 
    result = es.search(index=INDEX, body=QUERIES["getOldestEntry"])
    oldestDecisionDate = result["hits"]["hits"][0]["_source"]["submissionTimestamp"]
    oldestDecisionDate = datetime.datetime.fromtimestamp(float(oldestDecisionDate)/1000).strftime('%Y-%m-%d')
except:
    oldestDecisionDate = "2016-03-01"

#Build request params object
print oldestDecisionDate
params = {
    "page": 0,
    "size": PAGE_SIZE,
    "from_date": "2008-01-01",
    "to_date": oldestDecisionDate
}

total = 1000
pageNumber = 0

while pageNumber <= total:
    params["page"] = pageNumber
    response = unirest.get(BASE_URL, params=params)

    #update total pages number and current page
    total = response.body['info']['total'] / PAGE_SIZE
    pageNumber += 1

    #Index every decision inside elasticsearch
    for decision in response.body['decisions']:
        es.index(index="diavgeia", doc_type='decision', id=decision["versionId"],  body=decision)

