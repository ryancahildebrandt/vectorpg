#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:36:58 PM EST 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
from utils import *

#https://basicfantasy.org/download.cgi/Basic-Fantasy-RPG-Rules-r107.pdf
docs, ids = load_documents_from_pdf("data/Basic-Fantasy-RPG-Rules-r107.pdf")
collection = initialize_collection("basicr107")
batched_load(collection, docs, ids, 100)