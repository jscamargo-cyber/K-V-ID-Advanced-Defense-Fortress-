
🛡️ Proyecto K-VØID: Laboratorio de Detección y Respuesta (SIEM/EDR)

Esta es la versión final optimizada para tu README.md. He integrado los datos técnicos del reporte con las instrucciones de replicación en un formato de alto impacto para reclutadores.
🛡️ Proyecto K-VØID: Laboratorio de Detección y Respuesta (SIEM/EDR)

Este repositorio contiene las herramientas ofensivas y defensivas utilizadas para simular un entorno de Security Operations Center (SOC) profesional basado en Wazuh y contenedores Docker. El proyecto demuestra el ciclo completo de un incidente: desde la ejecución del vector de ataque hasta la ingesta de telemetría y el análisis de cumplimiento normativo.
🚀 Componentes del Repositorio

    ataque_recon.py: Script de Python para simular escaneos de red y vectores de fuerza bruta.

    k-void-blocker.py: Script de respuesta automática diseñado para mitigar amenazas en tiempo real.

    ossec.conf: Configuración optimizada del agente Wazuh para monitoreo de integridad (FIM) y recolección de logs.

    evidencia_recon.json: Muestra de telemetría capturada durante las fases de ataque para análisis forense.

📊 Resultados y Telemetría SOC (Análisis del Incidente)

A través de este laboratorio se logró una visibilidad profunda del comportamiento del atacante, documentada en los reportes adjuntos:

    Ingesta de Datos: 174 alertas procesadas en 60 minutos, con picos de actividad correlacionados a las ráfagas de ataque.

    Mapeo MITRE ATT&CK: Identificación precisa de tácticas de Defense Evasion:

        T1078 (Valid Accounts): 6 eventos detectados.

        T1548.003 (Sudo and Sudo Caching): 6 eventos de elevación de privilegios.

    Auditoría de Cumplimiento: Monitoreo automatizado de requisitos PCI DSS:

        10.2.5: Registro de accesos a componentes del sistema (21 eventos).

        10.6.1: Revisión de logs de seguridad para todos los componentes (14 eventos).

🛠️ Instrucciones de Replicación

Siga estos pasos para desplegar el laboratorio en cualquier entorno Linux basado en Debian/Ubuntu:
1. Despliegue del Wazuh Manager

Instale la infraestructura central mediante contenedores Docker (Single-node):
Bash

curl -sL https://db.browser.wazuh.com/install.sh | bash

2. Configuración del Entorno Ofensivo

Es fundamental aislar las dependencias del script de ataque en un entorno virtual:
Bash

python3 -m venv venv
source venv/bin/activate
pip install requests  # Dependencia para el simulador de reconocimiento

3. Ejecución del Ataque y Monitoreo

Una vez que el agente esté activo y reportando al Manager (ver estado en el Dashboard), ejecute el vector de ataque:
Bash

python3 ataque_recon.py [172.20.2.13]

🎯 Conclusión del Proyecto

Este laboratorio valida la eficacia de Wazuh como herramienta de visibilidad centralizada. La capacidad de detectar manipulaciones en el archivo de sudoers y ataques de fuerza bruta en tiempo real permite a los analistas de SOC ejecutar medidas de contención proactivas, reduciendo significativamente el tiempo de exposición (Mean Time to Repair - MTTR) ante incidentes críticos.
