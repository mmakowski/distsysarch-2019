.PHONY: docker

all: protocol/prime_pb2.py protocol/prime_pb2_grpc.py

docker:
	pipenv lock -r > requirements.txt
	docker build . -f docker/checker/Dockerfile -t isharine/dsa-python-checker:0.0.1
	rm requirements.txt

protocol/prime_pb2.py: protocol/prime.proto
	python -m grpc_tools.protoc -I. --python_out=. protocol/prime.proto

protocol/prime_pb2_grpc.py: protocol/prime.proto
	python -m grpc_tools.protoc -I. --grpc_python_out=. protocol/prime.proto

clean:
	rm protocol/*.py

