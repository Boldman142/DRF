FROM python:3

ENV PATH /root/.local/bin:$PATH

WORKDIR /core

RUN apt-get update -y && apt-get upgrade -y

COPY . .

RUN pip install --upgrade pip

RUN python3 -m venv env

RUN ./env/bin/activate

RUN  pip install -r requirements.txt

CMD gunicorn -w 3 --chdir ./core core.wsgi --bind 0.0.0.0:8000

#COPY ./requirements.txt /core/
#
#RUN pip install -r /core/requirements.txt
#
#COPY . .
