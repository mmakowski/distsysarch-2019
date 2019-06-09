distributed primality checker

Use:

* Kubernetes
* gRPC
* Redis

x python/go/rust/haskell


## User Interface

* `prime check <number>` -- check if a number is prime
* `prime max` -- check max known contiguous prime
* `prime list` -- list all known contiguous primes


## Architecture

* command line sends the prime to an available checker (find out if K8 helps with that)
* all known contiguous primes are cached in Redis
* there are two types of workers:
    * checker:
        * check division by all known contiguous primes (read from redis)
        * if max known contiguous prime is less than sqrt input then try division by all numbers up to sqrt of input
    * siever: runs Eratosthenes sieve algorithm, populating the cache with subsequent contiguous primes 


## Implementations

### Python

Not organised very well, all worker and client code are lumped together in a single directory structure with a single pipenv environment. It makes it easier to share the protocol code and ensure correct libraries are present in each image, but in a real project these application should be better separated, and perhaps have protocol published as a pip package.


## Good numbers to check

* 982451651432521 (min divisor: 19127491)
* 9824516514325212377 (prime close to the representation limit, takes ~10 mins to check naively)
