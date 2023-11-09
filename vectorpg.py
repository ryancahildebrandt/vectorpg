#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 05:25:33 PM EDT 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
from utils import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--collection_name", type = str, help = "Collection name to connect to")
parser.add_argument("-n", "--n_results", type = int, help = "Number of results to return with each query", default = 3)
args = parser.parse_args()

collection = initialize_collection(args.collection_name)
print(f"Connected to collection {args.collection_name}, containing {collection.count()} records")
print(f"Type 'quit' or 'exit' to terminate")

while True:
	inp = input("Query: ")
	if inp in ["quit", "exit"]:
		break
	query = inp
	results = collection.query(query_texts = query, n_results = args.n_results)
	print(f"Query: {query}")
	print("Results:")
	for i in results["documents"][0]:
		print(f"- {i}")
	print("---")