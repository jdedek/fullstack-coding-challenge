# Use the stable nginx image
FROM nginx:stable

LABEL maintainer "Julien Dedek <jdedek@posteo.de>"

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/