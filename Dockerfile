FROM ubuntu:14.04
MAINTAINER Your Name "jason.cook@microsoft.com"
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
COPY . /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]