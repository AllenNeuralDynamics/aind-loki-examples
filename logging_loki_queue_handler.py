# This example is taken from the python-logging-loki documentation
# This is a non-blocking logging method which uses lokis wrapper around the standard 
# queue handler.

import logging.handlers
import logging_loki
from multiprocessing import Queue


handler = logging_loki.LokiQueueHandler(
    Queue(-1),
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(...)
