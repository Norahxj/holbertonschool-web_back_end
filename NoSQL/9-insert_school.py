#!/usr/bin/env python3
"""This module provides a function to insert a school document."""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection and return its _id."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
