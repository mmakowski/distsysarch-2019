import sys

import grpc
from redis import Redis

from protocol import prime_pb2, prime_pb2_grpc


PRIMES = 'primes'


def main(args: list):
    if args[1] == 'max':
        _max()
    if args[1] == 'list':
        _list()
    if args[1] == 'check':
        num = int(args[2])
        _check(num)


def _max():
    redis = _redis()
    if redis.exists(PRIMES):
        print(redis.lindex(PRIMES, redis.llen(PRIMES) - 1).decode('utf-8'))


def _list():
    redis = _redis()
    if redis.exists(PRIMES):
        for i in redis.lrange(PRIMES, 0, redis.llen(PRIMES) - 1):
            print(i.decode('utf-8'))


def _check(num: int):
    channel = grpc.insecure_channel('localhost:9000')  # TODO: needs to point to where the checker runs
    stub = prime_pb2_grpc.PrimeCheckerStub(channel)
    response = stub.IsPrime(prime_pb2.IsPrimeRequest(number=num))
    print(response)


def _redis() -> Redis:
    return Redis(host='localhost', port=6379)


if __name__ == '__main__':
    main(sys.argv)
