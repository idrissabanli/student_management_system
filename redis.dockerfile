FROM redis:4.0.11

ENV REDIS_PASSWORD glqJ1z5Ume5xTgOr

CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]
