# This example is taken from the python-logging-loki documentation
# This is a non-blocking example of logging based on using the standard queueing method in the
# standard library.

import logging.handlers
import logging_loki
from multiprocessing import Queue


queue = Queue(-1)
handler = logging.handlers.QueueHandler(queue)
handler_loki = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)
logging.handlers.QueueListener(queue, handler_loki)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(...)
