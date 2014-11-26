#!/usr/bin/env python -*- coding: utf-8 -*-

import io
from threading import Thread
from Queue import Queue

import google_ngram_downloader as goograms
from google_ngram_downloader import readline_google_store as read_goograms

def store_ngrams(n):
    fname, url, records = next(read_goograms(ngram_len=5))
    with io.open('googram.'+str(n), 'wb') as fout:
        record = 'r'
        while record:
            record = next(records)
            print>>fout, record
    return n
            
def wrapper(func, arg, queue):
  """" Wrapper class for multi-threaded functions """
  queue.put(func(arg))
            
q1, q2 = Queue(), Queue()
Thread(target=wrapper, args=(store_ngrams, 1, q1)).start()
Thread(target=wrapper, args=(store_ngrams, 2, q2)).start()
q1.get(); q2.get()

q3, q4 =  Queue(), Queue()
Thread(target=wrapper, args=(store_ngrams, 3, q3)).start()
Thread(target=wrapper, args=(store_ngrams, 4, q4)).start()
q3.get(); q4.get()

q5 = Queue()
Thread(target=wrapper, args=(store_ngrams, 5, q5)).start()
q5.get() 