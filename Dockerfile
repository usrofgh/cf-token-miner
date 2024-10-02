ARG PYTHON_IMAGE=python:3.12.5

FROM ${PYTHON_IMAGE} AS library_installer
WORKDIR /app/
COPY poetry.lock pyproject.toml ./

RUN sudo apt-get update && sudo apt-get install tesseract-ocr && sudo apt-get install libtesseract-dev && \
    pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev &&  \
    rm -rf /tmp/poetry_cache

FROM ${PYTHON_IMAGE}-slim AS runtime
ENV PATH=/app/.venv/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY --from=library_installer /app/.venv ./.venv
RUN ls -a
COPY src ./src
