#!/usr/bin/env python3
"""

"""
import redis
import uuid
from typing import Any, Union, Optional, Callable


class Cache:
    """Cache class.
    """

    def __init__(self):
        """
        Cache class constructor that initializes a Redis client instance
        and flushes the database with flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method to store data in Redis and return a key for the stored
        data.

        Args:
            data (Union[str, bytes, int, float]): The data to store. Can
            be a str, bytes, int, or float.

        Returns:
            str: A randomly generated key that can be used to retrieve
            the stored data.
        """
        # generate a random key using uuid
        keys = str(uuid.uuid4())
        # store the data in Redis using the key
        self._redis.set(keys, data)
        # return the key
        return keys
