FROM ultrafunk/undetected-chromedriver:latest

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

RUN mkdir /app
ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "bot.py"]
