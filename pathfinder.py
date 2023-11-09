#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:30:24 PM EDT 2023 
author: Ryan Hildebrandt, github.com/ryancahildebrandt
"""
# imports
import chromadb
import json
import os

def entry_text_parser(entry, text_key):
    docs = []
    ids = []
    s_counter = 1
    for s in entry[text_key].split("."):
        docs.append(f"{entry['name']}: {s}")
        ids.append(f"{entry['id']}_text_{s_counter}")
        s_counter += 1

    out = [docs, ids]
    return out

def simple_entry_parser(entry, key, value):
    docs = []
    ids = []
    k_text = key.replace("_", " ")
    ids.append(f"{entry['id']}_{key}")
    if value not in ["", {}, [], None, "-"]:
        docs.append(f"{entry['name']}'s {k_text} is {value}")
    else:
        docs.append(f"{entry['name']} does not have a {k_text}")
    out = [docs, ids]
    return out

def append_entries(docs, ids, entry_docs, entry_ids):
    for d in entry_docs:
        docs.append(d)
    for i in entry_ids:
        ids.append(i)

docs = []
ids = []
all_data = []
all_keys = []

keys_to_skip = [
    "exclude_from_search",
    "id",
    "summary",
    "text"
    ]

acronyms = {
    "ac" : "armor_class",
    "hp" : "hit_points",
    "hp_raw" : "hit_points_raw",
    "npc" : "non_player_character",
    "pfs" : "pathfinder_society"
}

for file in os.listdir("data/archives-of-nethys-scraper/parsed/"):
    with open(f"data/archives-of-nethys-scraper/parsed/{file}") as f:
        d = json.load(f)
        for entry in d:
            all_data.append(entry)

for entry in all_data:
    for key in entry.keys():
        all_keys.append(key)
        if "markdown" in key:
            if key not in keys_to_skip:
                keys_to_skip.append(key)

for entry in all_data:
    entry_temp = {}
    for key, value in entry.items():
        if key in acronyms.keys():
            entry_temp[acronyms[key]] = entry[key]
    entry.update(entry_temp)

for entry in all_data:
    for key, value in entry.items():
        if key not in keys_to_skip:
            entry_docs, entry_ids = simple_entry_parser(entry, key, value)
            append_entries(docs, ids, entry_docs, entry_ids)
            if key == "summary":
                entry_docs, entry_ids = entry_text_parser(entry, "summary")
                append_entries(docs, ids, entry_docs, entry_ids)
            if key == "text":
                entry_docs, entry_ids = entry_text_parser(entry, "text")
                append_entries(docs, ids, entry_docs, entry_ids)
            if key == "url":
                value = f"https://2e.aonprd.com{value}"

collection = initialize_collection("pathfinder2e")
batched_load(collection, docs, ids, 100)
