FROM python:3.10.8

# set a directory for the app
WORKDIR app

COPY . /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5001

# run the command
CMD ["python", "./main.py"]