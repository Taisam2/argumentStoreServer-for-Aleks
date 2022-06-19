FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip==21.2.4 pip-tools==6.2.0
COPY requirements.txt /app/requirements/
RUN pip install -r requirements/requirements.txt

COPY index.py docker-entrypoint.sh wait-for-it.sh /app/
COPY argument_store /app/argument_store

EXPOSE 8080

# ENTRYPOINT [ "/app/docker-entrypoint.sh" ]

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8080", "index:app"]