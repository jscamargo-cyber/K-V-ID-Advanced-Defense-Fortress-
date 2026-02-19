Centro de investigación técnica dedicado a la orquestación de Defensa Activa, Hardening de sistemas y respuesta ante incidentes. Este laboratorio utiliza un stack contenedorizado para la detección proactiva de amenazas mediante el análisis de telemetría y logs en tiempo real.

K-VØID | Advanced Defense Fortress 🛡️

"Mastering the system from the core to the void."

K-VØID es un ecosistema de investigación técnica enfocado en la Defensa Activa, el Hardening de infraestructuras críticas y la orquestación de seguridad bajo el marco DevSecOps. Este laboratorio implementa un clúster de monitoreo avanzado capaz de procesar telemetría en tiempo real y detectar tácticas ofensivas complejas.
🛠️ Arquitectura del Sistema

El despliegue se basa en una infraestructura de microservicios robusta:

    Motor de Indexación: Almacenamiento y búsqueda de eventos de seguridad a alta velocidad.

    Wazuh Manager: Cerebro del SIEM encargado del análisis de logs y correlación de alertas.

    Dashboard K-VØID: Interfaz analítica para la visualización de incidentes y cumplimiento de normativas.

    Agentes de Host: Despliegue en endpoints para monitoreo de integridad de archivos (FIM) y detección de intrusiones.

🚀 Capacidades Implementadas

    Detección de Tácticas MITRE ATT&CK: Identificación automática de comportamientos maliciosos como Disable or Modify Tools y reconocimiento de red.

    Gestión Segura de Infraestructura: Implementación de certificados SSL/TLS para la comunicación cifrada entre nodos y agentes.

    Validación de Reglas Personalizadas: Correlación exitosa de eventos tras la ejecución de ataques simulados con scripts de Python.

📂 Estructura del Proyecto
Bash

├── core-siem/          # Orquestación Docker & Configuraciones SSL
├── agent-configs/      # Políticas de monitoreo y reglas FIM
├── rulesets/           # Detecciones personalizadas para MITRE
└── evidence/           # Capturas de telemetría y reportes de incidentes

📊 Evidencia de Operación

Durante las pruebas de estrés, el sistema procesó 231 eventos críticos en un periodo de 30 minutos, logrando una visibilidad total sobre los vectores de ataque simulados.
🛡️ Roadmap de Investigación

    Módulo K-VØID | Kernel: Implementación de reglas de auditoría de llamadas al sistema (syscalls).

    Integración Threat Intel: Sincronización automática con feeds de Shodan y VirusTotal.

    Respuesta Automática: Scripts en Python para bloqueo reactivo de IPs maliciosas detectadas por el SIEM.

Desarrollado por: Sebastian Camargo

Ingeniero en Seguridad de la Información (E) | Especialista en Hacking Ético y DevSecOps.
