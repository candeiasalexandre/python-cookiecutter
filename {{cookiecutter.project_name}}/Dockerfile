##
## Build
FROM python:{{cookiecutter.python_version}} AS build

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
ENV PATH="/etc/poetry/bin:${PATH}"

WORKDIR /code
COPY ./pyproject.toml ./pyproject.toml
COPY ./poetry.lock ./poetry.lock

RUN poetry config virtualenvs.in-project true  && \
    poetry install


COPY {{cookiecutter.__project_name_snake}} {{cookiecutter.__project_name_snake}}
COPY Makefile Makefile
RUN poetry install --only-root

RUN make build

##
## Release
FROM python:{{cookiecutter.python_version}}-slim AS release

WORKDIR /app

COPY --from=build /code/dist /app/dist

RUN pip install --no-cache-dir --upgrade -r dist/requirements.txt && \
    pip install --no-cache-dir --no-dependencies dist/*.whl && \
    rm -rf dist

CMD ["{{cookiecutter.__project_name_kebab}}", "--help"]
    