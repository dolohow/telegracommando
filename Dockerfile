FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY telegracommando.py .
COPY commands.d .

VOLUME /config
VOLUME /usr/src/app/commands.d

ENTRYPOINT ["python", "telegracommando.py"]
CMD ["--config", "/config/telegracommando.ini"]
