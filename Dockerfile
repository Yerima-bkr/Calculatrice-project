FROM python:3.11
WORKDIR /yerima
COPY calculatrice.py .
CMD ["python", "calculatrice.py"]
