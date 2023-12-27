FROM python:3.10.8

# set a directory for the app
WORKDIR app

COPY * /app/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 8501

# run the comma"nd
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py"]