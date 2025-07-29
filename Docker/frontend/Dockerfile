# Use the official Nginx base image
FROM nginx:latest

# Remove the default index.html if present
RUN rm -f /usr/share/nginx/html/index.html

# Copy your custom index.html to Nginx’s web root
COPY index.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

