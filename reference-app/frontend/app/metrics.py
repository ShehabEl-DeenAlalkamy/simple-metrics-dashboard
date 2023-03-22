from app import metrics
from app.utils.helpers import get_host

from flask import request


def _init(app):
    metrics._default_labels = {'host': get_host()}

    metrics.init_app(app)

    metrics.info('app_info', 'Frontend Service',
                 version='2.1.1', major='2', minor='1')

    metrics.register_default(
        metrics.counter(
            'frontend_service_http_request_by_path', 'Request count by request paths',
            labels={'path': lambda: request.path, 'method': lambda: request.method,
                    'status': lambda resp: resp.status_code}, initial_value_when_only_static_labels=False
        )
    )
