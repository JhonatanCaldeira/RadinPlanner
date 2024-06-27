FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r /backend/requirements.txt

COPY . /backend

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
