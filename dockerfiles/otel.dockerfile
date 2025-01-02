FROM otel/opentelemetry-collector-contrib:0.106.1

COPY config/otel-config.yaml /etc/otelcol-contrib/config.yaml

CMD ["--config=/etc/otelcol-contrib/config.yaml"]
