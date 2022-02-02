# pull official base image
FROM node:16.13.2

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY --chown=node:node package.json .
RUN npm install

COPY --chown=node:node . .
USER node
# install app dependencies
COPY package*.json ./

#RUN npm install

# add app
COPY . .

EXPOSE 3000

# start app
CMD [ "npm", "start" ]