FROM python:3.8.8

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VERSION=1.1.4 \
  POETRY_VIRTUALENVS_IN_PROJECT=1

RUN apt-get update && \
  apt-get install -y --no-install-recommends curl=7.64.* && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

ENV PATH="${PATH}:~/.poetry/bin"

# Install Python dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
WORKDIR /service/recommendations

RUN poetry run python -m grpc_tools.protoc -I ../protobufs --python_out=. \
  --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
