# This example is taken from the python-loki-logging documentation
# This code is blocking and so latency and outages to the loki server can impact performance and ux

# Important toi note is that the tags fields in the "extra" keyword will be represented in the labels column 
# of the loki webpage.  This column can also be later parsed into seperate columns.

import logging
import logging_loki


handler = logging_loki.LokiHandler(
    url="https://my-loki-instance/loki/api/v1/push", 
    tags={"application": "my-app"},
    auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("my-logger")
logger.addHandler(handler)
logger.error(
    "Something happened", 
    extra={"tags": {"service": "my-service"}},
)
