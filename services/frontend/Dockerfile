# Use Node.js as the base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy all app files
COPY . .

# Expose port 3000 and start the React development server
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
