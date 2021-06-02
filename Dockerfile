FROM tensorflow/tensorflow:2.4.1

WORKDIR /usr/local/src/w2v

ADD requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

COPY w2v_service.py ./

EXPOSE 4088

CMD ["python3", "./w2v_service.py"]
