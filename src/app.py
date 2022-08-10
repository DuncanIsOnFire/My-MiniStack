import time
import prometheus_client

from flask import Response, Flask

from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter

site = Flask( __name__ )

metrics = []
metrics.append( Counter( 'python_request_count', 'Total processed requests' ) )

@site.route('/')
def hello_world():
    metrics[0].inc()
    return 'Hello World'

@site.route("/metrics")
def app_metrics():
    resp = []
    for v in metrics:
        resp.append( prometheus_client.generate_latest(v) )
    return Response( resp, mimetype = "text/plain")
    return "<br>".join( resp )

if __name__ == '__main__':
    site.run()
