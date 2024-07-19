This repo contains the docker-compose file for standading up a grafana and loki server as well as python
examples of logging to loki with the python-loki-logging library available on pypi.

The code examples are taken from this documentation page: [python-loki-logging](https://pypi.org/project/python-logging-loki/)

Information about loki and other methods of installation can be found here:  [loki](https://grafana.com/docs/loki/latest/)

Other Notes:
- The default credentials from grafana are admin/admin
- You must enable the loki plugin on the grafana server and create a dashboard with the loki datasource.
- You can enable the loki plugin on an existing grafana service rather than run a separate grafana instance.
