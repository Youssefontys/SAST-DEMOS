# Dockerfile
# Kwetsbaarheid 1: Gebruik 'latest' tag, wat onvoorspelbaar is
FROM ubuntu:latest

# Kwetsbaarheid 2: Run als 'root' is onveilig
USER root

RUN apt-get update && apt-get install -y python3

# Kwetsbaarheid 3: Poorten onnodig exposen
EXPOSE 80 443 22

CMD ["/usr/bin/python3", "app.py"]