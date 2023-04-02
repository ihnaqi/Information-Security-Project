# Use an official Node.js runtime as a parent image
FROM node:16.13.1

# Set the working directory to /app
WORKDIR /app

# Install Angular CLI globally
RUN npm install -g @angular/cli@12.1.1

# Copy the package.json and package-lock.json files into the container at /app
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the default port for the Angular app
EXPOSE 4200

# Start the Angular app
CMD ng serve --host 0.0.0.0
