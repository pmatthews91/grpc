import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub


def main() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)
    request = RecommendationRequest(
         user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
    )
    result = client.Recommend(request)

    print(result)


if __name__ == "__main__":
    main()
