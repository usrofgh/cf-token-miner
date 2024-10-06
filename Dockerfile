ARG PYTHON_IMAGE=python:3.12.5

FROM ${PYTHON_IMAGE} AS library_installer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/
COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev

FROM ${PYTHON_IMAGE}-slim AS runtime
RUN apt-get update && \
    apt-get install -y  \
    nano wget xclip tesseract-ocr libtesseract-dev \
    xvfb xserver-xephyr tigervnc-standalone-server x11-utils gnumeric python3-tk python3-dev gnome-screenshot && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb
ENV PATH=/app/.venv/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app/
COPY --from=library_installer /app/.venv ./.venv
COPY .env .
COPY src ./src
