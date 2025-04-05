# Use Node.js as the base image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy all app files
COPY . .

# Expose port 3000 and start the React development server
EXPOSE 3000

# Fix for crypto issue and add necessary environment variable for Vite
ENV CHOKIDAR_USEPOLLING=true

# Use --no-sandbox to avoid any errors related to headless environments
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
