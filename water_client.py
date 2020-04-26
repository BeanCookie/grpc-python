from __future__ import print_function
import logging

import grpc

import water_pb2
import water_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = water_pb2_grpc.WaterCompanyStub(channel)
        response = stub.BuyWater(water_pb2.WaterRequest(price=14.5))
    print("WaterCompany client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()