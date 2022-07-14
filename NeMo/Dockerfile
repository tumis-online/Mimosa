FROM nvcr.io/nvidia/nemo:22.04

WORKDIR /
RUN pip -V
RUN which python
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY src/ .
RUN echo "Test"
CMD [ "python", "-m" , "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]