FROM python:3.7

RUN apt-get update 
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils




 
RUN mkdir app
ADD . /app
WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt



EXPOSE 8000






CMD ["python3", "./script.py"]   