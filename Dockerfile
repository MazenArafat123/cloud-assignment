FROM python:alpine
WORKDIR /app
COPY pythoncode.py .
COPY random_paragraphs.txt .
RUN pip install nltk
CMD ["python","pythoncode.py"]