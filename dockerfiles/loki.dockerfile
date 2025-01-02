FROM grafana/loki:main

WORKDIR /etc/loki

COPY config/loki-config.yaml /etc/loki/config.yaml

ENTRYPOINT ["/usr/bin/loki"]
CMD ["-config.file=/etc/loki/config.yaml"]
