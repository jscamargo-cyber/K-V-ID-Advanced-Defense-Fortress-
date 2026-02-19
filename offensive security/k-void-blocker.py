import sys
import os
import json

# Leer la alerta desde el stdin (Wazuh la envía así)
def main():
    alert_input = sys.stdin.read()
    alert = json.loads(alert_input)
    
    # Extraer la IP del atacante (suponiendo que viene del log de recon)
    # Para pruebas locales usaremos la IP de origen del evento
    src_ip = alert.get('data', {}).get('srcip', '127.0.0.1')
    
    print(f"[!] K-VØID detectó ataque desde {src_ip}. Iniciando bloqueo...")
    
    # Comando para bloquear la IP (Ejemplo con iptables en Linux)
    # En Windows usarías 'netsh advfirewall firewall add rule...'
    os.system(f"sudo iptables -A INPUT -s {src_ip} -j DROP")
    
    print(f"[+] IP {src_ip} bloqueada con éxito.")

if __name__ == "__main__":
    main()
