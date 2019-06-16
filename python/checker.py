from redis import Redis

from concurrent import futures
import math
import time

import grpc

from protocol import prime_pb2, prime_pb2_grpc


PRIMES = 'primes'
PORT = 9000

class PrimeCheckerServicer(prime_pb2_grpc.PrimeCheckerServicer):
    def IsPrime(self, request, context):
        # TODO: check the redis cache
        for i in range(2, int(math.sqrt(request.number))+2):
            if request.number % i == 0:
                return prime_pb2.IsPrimeResponse(isPrime=False, divisor=i)
        return prime_pb2.IsPrimeResponse(isPrime=True)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    prime_pb2_grpc.add_PrimeCheckerServicer_to_server(PrimeCheckerServicer(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    while True:
        time.sleep(1)
