FROM python:3.8-buster
RUN pip install flask
COPY sample_app.py /app/sample_app.py
EXPOSE 8080
CMD ["python", "/app/sample_app.py"]
