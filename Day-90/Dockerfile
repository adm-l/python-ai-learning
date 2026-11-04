FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
RUN pip install --no-cache-dir .
RUN useradd --create-home --uid 10001 appuser && mkdir -p /data && chown -R appuser:appuser /app /data
USER appuser
ENV ORDER_API_DB=/data/orders.db
EXPOSE 8000
CMD ["uvicorn", "order_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
