import time
import random
import prometheus_client

from flask import Response, Flask

from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter
from prometheus_client import Histogram

site = Flask( __name__ )

metrics = []
metrics.append( Counter( 'python_request_count', 'Total processed requests' ) )
metrics.append( Histogram( 'request_latency_seconds', 'Number of seconds to process a request.' ) )

@site.route('/')
def hello_world():
    metrics[0].inc()
    start_time = time.time()
    time.sleep( random.random( ) )
    end_time = time.time() - start_time
    metrics[1].observe( end_time )
    return 'Hello World'

@site.route("/metrics")
def app_metrics():
    resp = []
    for v in metrics:
        resp.append( prometheus_client.generate_latest(v) )
    return Response( resp, mimetype = "text/plain")
#   return "<br>".join( resp )

if __name__ == '__main__':
    site.run()
