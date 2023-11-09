#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:37:29 PM EST 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
from utils import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type = str, help = "PDF file to load from")
parser.add_argument("-c", "--collection_name", type = str, help = "Collection name to load to")
args = parser.parse_args()

docs, ids = load_documents_from_pdf(args.file)
collection = initialize_collection(args.collection_name)
batched_load(collection, docs, ids, 100)