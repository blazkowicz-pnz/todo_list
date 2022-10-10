FROM python:3.9-slim

WORKDIR /app/todolist

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=/app/todolist

RUN groupadd --system service && useradd --system -g service api

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY todo_list ./
COPY core ./
COPY entrypoint.sh ./
COPY manage.py ./

USER api

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]