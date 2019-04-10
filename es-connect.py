#!/usr/bin/python2.7
from elasticsearch import Elasticsearch
import time

es = None
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

def check_es(): 
 if es.ping():
     print('Connection to Elasticsearch are OK')
     settings_es()
 else:
     print('No Connection to Elasticsearch, waiting 30 seconds')
     time.sleep(30)
     check_es()
 return

def settings_es():
 request_body = {
         "settings" : {
             "number_of_shards" : 1,
             "number_of_replicas": 0,
                      },
 
         'mappings': {
             'members': {
                 'properties': {
                     'Body': {'type': 'text'},
                     'ReceiptHandle': {'type': 'text'},
                     'MD5OfBody': {'type': 'text'},
                     'MD5OfMessageAttributes': {'type': 'text'},
                     'MessageId': {'type': 'text'},
                     'MessageAttributes': {'type': 'text'},
                                }
                         }
                      }
                }

 es.indices.create(index = 'ips', body = request_body)

 return
 
check_es()
