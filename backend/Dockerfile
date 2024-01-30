FROM python:3.11

RUN mkdir /fastapi_records

WORKDIR /fastapi_records

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY  pyproject.toml poetry.lock /fastapi_records/

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

COPY . /fastapi_records

WORKDIR /fastapi_records/backend

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=127.0.0.1:8000