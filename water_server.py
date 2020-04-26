from concurrent import futures
import logging
import grpc

import water_pb2
import water_pb2_grpc

class WaterCompany(water_pb2_grpc.WaterCompanyServicer):

    def BuyWater(self, request, context):
        return water_pb2.WaterReply(message='Buy water, %.1f!' % request.price)

    def BuyStreamWater(self, request, context):
        for i in range(100):
            yield water_pb2.WaterReply(message='Buy water, %d!' % i)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    water_pb2_grpc.add_WaterCompanyServicer_to_server(WaterCompany(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()