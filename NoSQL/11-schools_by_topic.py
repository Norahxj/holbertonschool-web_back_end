#!/usr/bin/env python3
"""This module provides a function to find schools by topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
