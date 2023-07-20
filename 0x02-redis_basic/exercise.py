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
    
    def get(self, key: str, fn:
            Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None)\
            -> Union[str, bytes, int, float, None]:
            """

            """
            data = self._redis.get(key)
            # If no key in redit return None
            if data in None:
                return None
            # If the key is present, the execute the function
            if fn in not None:
                data = fn(data)
            return data

    def get_str(self, key:str) -> Optional[str]:
        """
        """
        return self.get(key, lamda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        """
        # use get with a conversion function to retrieve an integer
        return self.get(key, lambda x: int(x))
