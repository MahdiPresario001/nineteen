FROM prom/prometheus:latest

COPY config/prometheus-config.yaml /etc/prometheus/prometheus.yml

CMD [ "--config.file=/etc/prometheus/prometheus.yml", \
     "--storage.tsdb.path=/prometheus", \
     "--storage.tsdb.retention.time=7d", \
     "--web.console.libraries=/usr/share/prometheus/console_libraries", \
     "--web.console.templates=/usr/share/prometheus/console" ]
