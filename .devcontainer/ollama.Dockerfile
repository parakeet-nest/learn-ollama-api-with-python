FROM ollama/ollama:0.4.1

RUN <<EOF
/bin/sh -c "\
    /bin/ollama serve & \
    sleep 1 && \
    ollama pull granite3-moe:1b"
EOF

ENTRYPOINT ["/bin/ollama"]
EXPOSE 11434
CMD ["serve"]
