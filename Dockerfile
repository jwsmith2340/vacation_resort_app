
FROM python:3.13

WORKDIR /opt/vacation_resort_app

COPY ./requirements.txt /opt/vacation_resort_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /opt/vacation_resort_app/requirements.txt

COPY ./app /opt/vacation_resort_app

CMD ["fastapi", "run", "main.py", "--port", "80"]