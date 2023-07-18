import sys

import elasticapm
from elasticapm.conf.constants import OUTCOME

USE_ELASTIC_APM='true'
APM_SECRET_TOKEN='AAEAAWVsYXN0aWMvZmxlZXQtc2VydmVyL3Rva2VuLTE2NjAxOTk5ODgxMzA6WlI5M1NlYVlSVUtJNkhpTVBSdE9QUQ'
APM_SERVER_URL='http://dm1-chel1.is74.ru:8200'
APM_ENVIRONMENT='production'

apm_client = elasticapm.Client(
    service_name="nuclio",
    server_url=APM_SERVER_URL,
    secret_token=APM_SECRET_TOKEN,
    environment=APM_ENVIRONMENT,
    global_labels="application=assistant",
)
elasticapm.instrument()

def my_except_hook(exctype, value, traceback):
    elasticapm.set_transaction_result(OUTCOME.FAILURE)
    elasticapm.get_client().capture_exception((exctype, value, traceback),)
    sys.__excepthook__(exctype, value, traceback)
        
sys.excepthook = my_except_hook

1 / 0