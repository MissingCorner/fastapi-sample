FROM python:3.11-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY portal /app
WORKDIR /app
CMD ["unicorn", "-w 4", "main:app"]
