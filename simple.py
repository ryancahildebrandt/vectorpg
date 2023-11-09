#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:37:29 PM EST 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
from utils import *

#https://buriedwithoutceremony.com/wp-content/uploads/2017/07/simple-world.pdf
docs, ids = load_documents_from_pdf("data/simple-world.pdf")
collection = initialize_collection("simple2017")
batched_load(collection, docs, ids, 100)