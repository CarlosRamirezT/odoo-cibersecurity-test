import os
import requests
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

secure_mode = os.getenv("SECURE_MODE") == "true"
url = "http://nginx:80" if secure_mode else "http://odoo:8069"
usernames = ["admin", "user", "odoo"]  # Nombres de usuario de prueba
passwords = ["admin", "12345", "password", "odoo"]  # Contraseñas de prueba

_logger.info(f'SECURE_MODE: {secure_mode}, using url: {url}')

def attempt_login(username, password):
    try:
        response = requests.post(url, data={"login": username, "password": password})
        if "Odoo" not in response.text:  # Si no contiene 'Odoo', puede que el login sea exitoso
            _logger.info(f"url: {url}, Login exitoso con usuario: {username} y contraseña: {password}")
        else:
            _logger.info(f"url: {url}, Fallido para usuario: {username} y contraseña: {password}")
    except Exception as e:
        _logger.error(f"url: {url}, Error: {e}")

# Ejecutar múltiples solicitudes de prueba

with ThreadPoolExecutor(max_workers=10) as executor:
    for username in usernames:
        for password in passwords:
            _logger.info(f"Probando usuario: {username} y contraseña: {password}")
            executor.submit(attempt_login, username, password)
