FROM python:3.7-buster
# Install ODBC drivers
RUN apt-get update
RUN apt-get install -y gcc unixodbc-dev nano
# Set the working direction
WORKDIR /app

# Add requirements and install
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update -y
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools libssl1.1 libssl-dev

COPY . .

RUN pip install -r /app/requirements.txt

CMD ["python3", "-u", "master_orchestrator.py"]
#ENTRYPOINT [/entry_points/point.sh]