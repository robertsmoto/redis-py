from __future__ import annotations
import logging
import os
import redis

logger = logging.getLogger('custom.logger')

class Redis:
    """Redis query helper class."""

    def __init__(self, db: int):
        self.host = os.getenv('REDIS_HOST', '')
        self.conn = redis.Redis(
                host=os.getenv('REDIS_HOST', ''),
                port=int(os.getenv('REDIS_PORT', '0')),
                db=db,
                password=os.getenv('REDIS_PASS', '')
                )

    def __repr__(self):
        return self.conn

    def printconn(self):
        print("## connection -->", self.conn)

