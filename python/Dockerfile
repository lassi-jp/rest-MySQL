FROM uselagoon/python-3.10

WORKDIR /usr/src/python

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .
CMD [ "python3", "main.py" ]
