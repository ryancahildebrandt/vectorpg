#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:24:52 PM EST 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
import itertools
import chromadb
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re

def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := list(itertools.islice(it, n)):
        yield batch

def initialize_collection(name):
	client = chromadb.PersistentClient("data/db")
	out = client.get_or_create_collection(name = name, metadata={"hnsw:space": "cosine"})
	return out

def batched_load(collection, docs, ids, n):
	batched_ids = batched(ids, n)
	batched_docs = batched(docs, n)
	counter = 0
	for id, doc in zip(batched_ids, batched_docs):
		collection.add(documents = doc, ids = id)
		counter += 1
		print(f"{counter}/{int(len(ids)/n)+1}")

def load_documents_from_pdf(path):
	docs = []
	ids = []
	counter = 0
	for page_layout in extract_pages(path):
		for index, element in enumerate(page_layout):
			if isinstance(element, LTTextContainer):
				doc = re.sub("[\s]+", " ", element.get_text())
				docs.append(doc)
				ids.append(str(counter))
				counter += 1
	out = [docs, ids]
	return out
