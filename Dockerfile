FROM python:3.9-slim as layer_python

WORKDIR /core

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# RUN apt-get update \
#     && apt-get -y install gcc

RUN apt-get update \
    && apt-get -y install gcc libpq-dev \
    && apt-get clean


RUN python -m venv /env
RUN /env/bin/pip install --upgrade pip
RUN /env/bin/pip install -r /requirements.txt




FROM layer_python as layer_dependencies

COPY . /app
COPY ./scripts /scripts
COPY --from=layer_python /env /env


EXPOSE 8000

RUN adduser --disabled-password --no-create-home app \
    && mkdir -p /vol/web/static \
    && mkdir -p /vol/web/media \
    && chown -R app:app /vol \
    && chmod -R 755 /vol \
    && chmod -R +x /app/scripts \
    && chown -R app:app /app

ENV PATH="/scripts:/env/bin:$PATH"

USER app

CMD ["/app/scripts/run.sh"]