#!/usr/bin/env python3
"""

"""
from functools import wraps
import redis
import uuid
from typing import Any, Union, Optional, Callable


def call_history(method: Callable) -> Callable:
    """
    """
@wraps(method)
def wrapper(self, *Args, **kwargs) -> Any:
    """
    """
    input_list_key = f"{method.__qualname__}:inputs"
    output_list_key = f"{method.__qualname__}:outputs"
    if isinstance(self._redis, redis.Redis):
        self._redis.rpush(input_list_key, str(args))
    
    output = method(self, *args, **kwargs)
    if isinstance(self._redis.Redis):
        self._redis.rpush(output_list_key, output)
    return output
return wrapper

def count_calls(method Callable) -> Callable:
     """
     """
     @wraps(method)
def wrappers(self, *args, **kwargs) -> Any:
    """
    """
    if instance(self._redis, redis.Redis):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def replay(fn: callable) -> None:
    """

    """
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    func_name = fn.__qualname__
    input_list_key = "{}:inputs".format(func_name)
    output_list_key = "{}:outputs".format(func_name)
    func_call_count = 0
    if redis_store.exists(func_name) != 0:
        func_call_count = int(redis_store.get(func_name))
    print("{} was called {} times:".format(func_name, func_call_count))
    inputs = redis_store.lrange(input_list_key, 0, -1)
    outputs = redis_store.lrange(output_list_key, 0, -1)
    for inp, out in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            inp.decode("utf-8"),
            out,
        ))
    return None


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

    @call_history
    @count_calls
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
            if fn is not None:
                data = fn(data)
            return data

    def get_str(self, key: str) -> Optional[str]:
        """
        """
        return self.get(key, lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        """
        # use get with a conversion function to retrieve an integer
        return self.get(key, lambda x: int(x))


