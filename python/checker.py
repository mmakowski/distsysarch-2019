from redis import Redis

from protocol import prime_pb2, prime_pb2_grpc


PRIMES = 'primes'


class PrimeCheckerServicer(prime_pb2_grpc.PrimeCheckerServicer):
    def IsPrime(self, request, context):
        # TODO
        return prime_pb2.IsPrimeResponse(isPrime=True)
