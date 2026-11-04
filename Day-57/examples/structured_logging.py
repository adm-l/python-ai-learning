"""JSON structured logs with stable correlation fields."""
import json
import logging


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps({
            "level": record.levelname,
            "message": record.getMessage(),
            "job_id": getattr(record, "job_id", None),
        })


def main() -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger = logging.getLogger("worker")
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info("job completed", extra={"job_id": "job-42"})


if __name__ == "__main__":
    main()
