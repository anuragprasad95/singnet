from sn_agent.tests.test_service_adapter import test_perform_services
from sn_agent.ontology import setup_ontology

import logging

log = logging.getLogger('test')
log.setLevel(logging.DEBUG)

format = logging.Formatter('[L:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', datefmt = '%d-%m-%Y %H:%M:%S')
log_handler = logging.StreamHandler()
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(format)
log.addHandler(log_handler)

log.debug('Starting test')


class MockApp(dict):
    def __init__(self):
        self['log'] = log
        pass

app = MockApp()
setup_ontology(app)

test_perform_services(app)