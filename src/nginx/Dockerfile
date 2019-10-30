# Use the stable nginx image
FROM nginx:stable

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/