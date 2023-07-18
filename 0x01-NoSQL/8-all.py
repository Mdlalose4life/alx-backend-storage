#!/usr/bin/env python3
"""
A Python function that lists all documents in a collection:

Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


import pymongo


def list_all(mongo_collection):
    """ Return lists all documents in a collection """
    if not mongo_collection:
        return []
    documents = mongo_collection.find()
    return [document for document in documents]
