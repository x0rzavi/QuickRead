FROM python:alpine

WORKDIR /app

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}

COPY . /app/

ENTRYPOINT ["./gunicorn.sh"]
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:8080/ || exit 1