FROM node

WORKDIR /app

ADD package.json /tmp/package.json
RUN cd /tmp && yarn --pure-lockfile
RUN cd /app && ln -s /tmp/node_modules
