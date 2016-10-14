FROM mhart/alpine-node

RUN apk add --update python python-dev gfortran py-pip && \
  easy_install-2.7 pip && \
  pip install --upgrade pip && \
  pip install bs4 && \
  apk del python-dev gfortran py-pip && \
  rm -rf /var/cache/apk/*

WORKDIR /app

ADD node_modules node_modules
ADD pun.py .
ADD pun-server.js .
ADD settings.json .

# Expose node port
EXPOSE 80

# Run node
CMD [ "node", "pun-server.js" ]
