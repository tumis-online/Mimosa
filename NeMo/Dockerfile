FROM nemo:latest

WORKDIR src/

COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src/ .

CMD [ "python", "-m" , "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]