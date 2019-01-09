#!/usr/bin/python

import redis

try:
        r = redis.Redis(
            host='127.0.0.1',
            port=6379,
            db=0)

        print(r.ping())
        print('Connected!')

        print("Creating Key first_name")
        r.hset("person:0", "first_name", "Rami")
        print("Creating Key last_name")
        r.hset("person:0", "last_name", "Edouard")
        # now print the hset
        print(r.hgetall("person:0"))
except Exception as ex:
        print('Error:', ex)
        exit('Failed to connect, terminating.')
