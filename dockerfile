FROM python:3.11-alpine

WORKDIR /code

RUN apk add --update --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./QR_Code_Gen/Qr_generator.py" ]