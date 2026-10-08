<!-- ============================================================================== -->
<!-- THINKINGSEED: ADN DEL PROYECTO (CONTEXTO PASIVO PARA MODELOS DE LENGUAJE)     -->
<!-- ============================================================================== -->
> [!NOTE]
> ### 🧬 DEFINICIÓN Y ROL DE ESTE DOCUMENTO
> 1. **¿Qué es este archivo?:** Este documento es una **Semilla de Proyecto (ThinkingSeed Master)**: representa el **ADN arquitectónico, técnico y estructural exhaustivo** del sistema. **NO es el repositorio completo de código fuente**, sino su mapa genético y memoria técnica profunda extraída directamente del entorno de desarrollo.
> 2. **Estado de Avance (Work in Progress):** Este documento refleja el **estado actual del desarrollo**. No garantiza que el proyecto esté concluido al 100%; puede representar un prototipo, un MVP o un sistema en evolución continua. La ausencia de código completo en ciertos archivos o módulos es **deliberada por diseño** para optimizar ventana de contexto o refleja áreas aún en desarrollo.
> 3. **Modo de Operación:** Trata este documento como **contexto pasivo de referencia técnica (Ground Truth)**. No asumas que el archivo está defectuoso ni intentes reescribirlo por tu cuenta.
<!-- ============================================================================== -->

# THINKING SEED MASTER: iReadme

## 0. IDENTIDAD Y METADATOS
```yaml
seed_schema_version: "2.0"
project_name: "iReadme"
repository_name: "iReadme"
project_type: "library"
repository_mode: "single-project"
generated_at: "2026-09-22T14:31:30-03:00"
generated_by: "Gemini 3.6 Flash (Antigravity Agentic Assistant)"
repository_root: "d:/0001 HyperScale Thinking/PROYECTOS CLOUD/iContext/iReadme"
git_branch: "main"
git_commit: "initial-commit-pending"
working_tree_state: "dirty"
analysis_mode: "static"
coverage_level: "high"
known_analysis_limits:
  - "Módulos ejecutables en src/core, src/cloud_jobs y src/dashboards en estado inicial (stubs/.context.yaml)"
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto, no como el repositorio completo ni como una prueba de ejecución.
2. **Contexto Pasivo:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como contexto pasivo para responder preguntas sobre el funcionamiento del sistema.
3. **Estado de Avance:** Considera que las secciones incompletas o componentes marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Evidencia:** Respeta las etiquetas de evidencia y no transformes inferencias en hechos.
5. **Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio.
6. **Contratos:** Conserva arquitectura, convenciones, contratos y restricciones declaradas.
7. **Preguntas Dirigidas:** No inventes componentes ausentes. Formula preguntas solo cuando la incertidumbre impida una respuesta segura.
8. **Seguridad:** No reveles ni solicites secretos. Usa placeholders (`<REDACTED>`).
9. **Impacto:** Evalúa impactos laterales en pruebas, configuración, datos, seguridad, observabilidad y despliegue.
10. **Asistencia:** Distingue entre solución inmediata, deuda técnica y recomendación futura.

---

## 1. RESUMEN EJECUTIVO
- **1.1 Proyecto en una frase [CONFIRMADO]:** iReadme es un motor y marco de gobernanza automatizado para la generación de documentación técnica institucional de alta ingeniería bajo el estándar *Paper-Grade* en paridad dual (Inglés/Español).
- **1.2 Problema que resuelve [CONFIRMADO]:** Elimina la degradación estética, la desincronización idiomática, el uso informal de emojis, la falta de notación matemática rigurosa y las fugas de rutas absolutas locales del SO (`C:\...`, `D:\...`) en repositorios de código corporativos y de código abierto.
- **1.3 Usuarios o sistemas consumidores [CONFIRMADO]:** Ingenieros de software, arquitectos de datos, agentes de IA del entorno Antigravity IDE, pipelines de integración continua (CI/CD) y auditores técnicos.
- **1.4 Alcance y límites del sistema [CONFIRMADO]:** Garantiza la estandarización y generación dual de `README.md` y `README_ES.md`, valida invariantes matemáticas y de portabilidad mediante scripts como `scripts/init_readme.py` y define reglas de gobernanza mediante `GEMINI.md`. Queda fuera del alcance la compilación directa de ejecutables binarios.

---

## 2. ARQUITECTURA Y TOPOLOGÍA
- **2.1 Estilo arquitectónico [CONFIRMADO]:** Motor modular de automatización y gobernanza guiado por reglas (Rule-Based Documentation Pipeline) e integrado nativamente con Antigravity Agentic IDE mediante Context Engineering v3.0 (iDirectory / FWengine.py).

- **2.2 Árbol estructural del repositorio [CONFIRMADO]:**
```
iReadme/
├── .agentignore                     # Reglas de exclusión para agentes iDirectory
├── .context/                        # Topología y satélite de tokens iDirectory v3.0
│   └── tree.json                    # Grafo sintético del repositorio
├── .gitignore                       # Políticas de exclusión de control de versiones Git
├── 01_seed/                         # Snapshots de ADN técnico (ThinkingSeed)
│   ├── seed-iReadme.md              # Snapshot híbrido inicial
│   └── seed-iReadme-master.md       # ADN exhaustivo ThinkingSeed Master v2.0
├── 02_Foundation/                   # Componentes base y motores heredados
│   └── Engine/                      # Documentación y prototipos del motor base
│       ├── EngineReadme.md
│       └── engine_readme.md
├── 03_research/                     # Entorno de investigación y experimentos
│   ├── experiments/
│   ├── notebooks/
│   └── prompts/
├── GEMINI.md                        # Directrices institucionales y gobernanza Paper-Grade
├── GestorReadme.md                  # Plantilla canónica de 8 secciones de documentación
├── Propuesta Skill.md               # Especificación de la skill generate_paper_grade_readme
├── README.md                        # Documentación maestra en Inglés (Paper-Grade)
├── README_ES.md                     # Documentación sincronizada en Español (Paper-Grade)
├── Tools/                           # Herramientas y utilidades auxiliares
├── config/                          # Configuraciones de canalización
├── data/                            # Muestras y datasets de prueba
├── docs/                            # Documentación técnica extendida
├── infrastructure/                  # Definición de infraestructura como código (IaC)
├── logs/                            # Registros de ejecución y auditoría
├── schemas/                         # Esquemas JSON de validación
├── scripts/                         # Puntos de entrada para automatización
│   └── init_readme.py               # Script generador y sincronizador Paper-Grade
├── src/                             # Código fuente del sistema
│   ├── cloud_jobs/                  # Procesamiento batch y jobs cloud [FALTANTE]
│   ├── core/                        # Motores analíticos centrales [FALTANTE]
│   ├── dashboards/                  # Visualizadores analíticos [FALTANTE]
│   └── data_generation/             # Sintetizadores de datos [FALTANTE]
└── tests/                           # Suite de pruebas unitarias y de portabilidad
```

- **2.3 Responsabilidad por directorio y archivo clave [CONFIRMADO]:**
  - `GEMINI.md`: Reglas inviolables de gobernanza, formato Paper-Grade, cero emojis, notación KaTeX y portabilidad de rutas.
  - `scripts/init_readme.py`: Generador autónomo que inyecta y sincroniza simultáneamente las plantillas `README.md` y `README_ES.md`.
  - `GestorReadme.md`: Estructura canónica de 8 secciones exigida para todos los artefactos de documentación del ecosistema.
  - `Propuesta Skill.md`: Definición formal de la skill Antigravity para automatizar el rol del agente.
  - `01_seed/`: Almacenamiento de snapshots de ADN de contexto pasivo para LLMs.
  - `.context/tree.json`: Satélite topológico de Context Engineering v3.0 generado por `FWengine.py`.

- **2.4 Límites modulares y acoplamiento [INFERIDO]:** El sistema acopla las reglas descritas en `GEMINI.md` directamente con el script generador `scripts/init_readme.py`. La capa de datos (`schemas/`, `data/`) y los módulos ejecutables (`src/`) están desacoplados y se encuentran en fase de prototipado progresivo.

---

## 3. FLUJOS DE EJECUCIÓN Y ENTRY POINTS
- **3.1 Puntos de entrada principales [CONFIRMADO]:**
  - CLI Python: `python scripts/init_readme.py` (Genera/sincroniza `README.md` y `README_ES.md`).
  - Agente AI / Slash Commands: `/readme`, `/seed`, `/seedMaster` invocados desde Antigravity IDE.
  - Context Engineering CLI: `python FWengine.py init` para desplegar beacons `.context.yaml` y `.context/tree.json`.

- **3.2 Diagrama de flujo principal E2E [CONFIRMADO]:**
```
+---------------------------------------------------------------------------------+
|                         iREADME AUTOMATION PIPELINE                             |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------+     +-----------------------+     +---------------------+
| Invocación CLI / Skill| --> | Carga de Reglas       | --> | Generación Dual     |
| (init_readme.py)      |     | (GEMINI.md Standard)  |     | (README & README_ES)|
+-----------------------+     +-----------------------+     +---------------------+
                                         |
                                         v
                               +-----------------------+
                               | Verification Suite    |
                               | (Path Portability Test|
                               |  & LaTeX Syntax Audit)|
                               +-----------------------+
```

- **3.3 Ciclo de vida de la ejecución y estados [INFERIDO]:**
  1. Inicialización de entorno Python 3.10+.
  2. Resolución de la raíz del proyecto mediante `Path(__file__).resolve().parent.parent`.
  3. Formateo y renderizado UTF-8 de bloques en Inglés y Español.
  4. Escritura en disco con sobreescritura atómica de `README.md` y `README_ES.md`.
  5. Ejecución opcional de tests de aserción para verificar la ausencia de prefijos de SO (`C:`, `D:`).

---

## 4. MODELO DE DATOS, CONTRATOS Y PERSISTENCIA
- **4.1 Esquemas y entidades principales [CONFIRMADO]:**
  - Entidad `DocumentStructure`: Particionada en 8 secciones canónicas ($S_1 \dots S_8$).
  - Entidad `ThinkingSeed`: Estructura YAML/Markdown de metadatos y evidencia epistemológica v2.0.
  - Entidad `ContextBeacon`: Archivos `.context.yaml` distribuidos en 24 subdirectorios para ruteo de contexto iDirectory.

- **4.2 Almacenamiento, motores de base de datos y migraciones [CONFIRMADO]:**
  - Persistencia basada 100% en archivos planos Markdown (`.md`), YAML (`.yaml`) y JSON (`.json`). No requiere motor RDBMS ni NoSQL externo.

- **4.3 Interfaces externas, payloads y contratos de API [CONFIRMADO]:**
  - Contrato de Paridad Dual: $\Phi(\mathcal{D}_{EN}, \mathcal{D}_{ES}) = 1.0$.
  - Contrato de Portabilidad de Rutas: $p \cap \mathcal{R}_{OS} = \emptyset \implies p \in \text{Path}_{relative}$.

---

## 5. CONFIGURACIÓN Y AMBIENTE
- **5.1 Tabla de variables de entorno [CONFIRMADO]:**
| Variable | Tipo | Default | Efecto | Sensible |
|:---|:---|:---|:---|:---|
| `PYTHONUTF8` | Integer | `1` | Enforza codificación UTF-8 en Windows Console | No |
| `PAGER` | String | `cat` | Evita paginación interactiva en comandos shell | No |

- **5.2 Perfiles de ejecución [INFERIDO]:**
  - `dev`: Invocación directa del script `scripts/init_readme.py` o comandos slash en Antigravity IDE.
  - `ci`: Ejecución de tests de validación en pipelines de GitHub Actions / GitLab CI `[FALTANTE]`.

- **5.3 Prerrequisitos de sistema e infraestructura [CONFIRMADO]:**
  - Python >= 3.10
  - Git SCM
  - Entorno de ejecución Antigravity IDE v2.0+ (opcional para ejecución asistida por agentes)

---

## 6. PRUEBAS, CI/CD Y OPERACIÓN
- **6.1 Estrategia de pruebas [CONFIRMADO]:**
  - Pruebas estáticas de portabilidad: `python -c "assert 'C:' not in open('README.md').read()"` y `assert 'D:' not in open('README_ES.md').read()`.
  - Pruebas de renderizado LaTeX y estructura de secciones `[INFERIDO]`.

- **6.2 Automatización y pipelines CI/CD [FALTANTE]:**
  - No se detectaron workflows de GitHub Actions en `.github/workflows/`. Pendiente de aprovisionamiento en fases futuras.

- **6.3 Contenedores y orquestación [FALTANTE]:**
  - No se requieren archivos `Dockerfile` ni `docker-compose.yml` para el núcleo ligero de iReadme.

---

## 7. OBSERVABILIDAD Y MODOS DE FALLA
- **7.1 Logs, métricas y tracing [CONFIRMADO]:**
  - Logs de consola emitidos por `scripts/init_readme.py` en formato de texto estándar (`[*] Escribiendo...`, `[OK] Proceso finalizado...`).
  - Carpeta `logs/` provisionada para recepción de auditorías de compilación.

- **7.2 Modos de falla conocidos y estrategias de recuperación [CONFIRMADO]:**
  - *Fuga de Rutas Absolutas:* Si un agente o desarrollador edita un README introduciendo rutas como `D:\...`, el test de verificación falla inmediatamente en la suite.
  - *Desincronización Idiomática:* Si se edita `README.md` sin replicar los cambios en `README_ES.md`, se rompe la paridad $\Phi < 1.0$.

- **7.3 Idempotencia y reintentos [CONFIRMADO]:**
  - La ejecución de `scripts/init_readme.py` es totalmente idempotente; reescribe de forma determinista ambos artefactos basándose en las constantes maestras.

---

## 8. SEGURIDAD Y PRIVACIDAD
- **8.1 Hallazgos de seguridad estática [CONFIRMADO]:**
  - No se detectaron credenciales, API keys ni cadenas de conexión hardcodeadas en el código fuente.
- **8.2 Manejo de autenticación, autorización y secretos [CONFIRMADO]:**
  - Política estricta `<REDACTED>` obligatoria para cualquier ejemplo o template que requiera referencia a credenciales.
- **8.3 Privacidad de datos y cumplimiento [CONFIRMADO]:**
  - El proyecto no procesa ni almacena Datos de Identificación Personal (PII).

---

## 9. ESTADO REAL, DEUDA TÉCNICA Y LIMITACIONES
- **9.1 Nivel de madurez y avance real del proyecto [CONFIRMADO]:**
  - Fase: **Beta / Prototipo Funcional de Gobernanza**.
  - Los scripts de generación (`scripts/init_readme.py`), plantillas (`GestorReadme.md`), directrices (`GEMINI.md`) y estructura iDirectory v3.0 están 100% desplegados y operativos.

- **9.2 Deuda técnica identificada y stubs pendientes [FALTANTE]:**
  - Subdirectorios en `src/core`, `src/cloud_jobs`, `src/dashboards`, `src/data_generation`, `infrastructure/`, `schemas/` y `tests/` contienen únicamente beacons `.context.yaml` y requieren implementación de módulos Python reales.

- **9.3 Inconsistencias entre código y documentación [CONFIRMADO]:**
  - Ninguna. La documentación en `README.md` y `README_ES.md` refleja fielmente el rendimiento y la topología observada en el repositorio.

---

## 10. REGLAS PARA MODIFICAR EL PROYECTO
- **10.1 Convenciones de estilo, linting y tipado [CONFIRMADO]:**
  - Cumplimiento estricto con PEP 8 en scripts de Python.
  - Codificación UTF-8 universal en todos los archivos `.md` y `.py`.

- **10.2 Reglas arquitectónicas inviolables [CONFIRMADO]:**
  1. **Zero Emojis:** Prohibido el uso de emojis o iconos conversacionales en `README.md` y `README_ES.md`.
  2. **Portabilidad Absoluta:** Prohibidas las rutas absolutas (`C:\...`, `D:\...`, `file:///...`). Todas las referencias deben ser relativas a la raíz.
  3. **Notación KaTeX Formal:** Expresar cualquier formulación matemática mediante `$$...$$` y `$...$`.
  4. **Topología ASCII:** Representar esquemas de arquitectura únicamente en cajas ASCII monospaciadas.
  5. **Paridad Dual:** Mantener 100% sincronizadas las versiones en Inglés (`README.md`) y Español (`README_ES.md`).

- **10.3 Checklist de verificación previa a commit [CONFIRMADO]:**
  - [ ] Ejecutar `python scripts/init_readme.py`.
  - [ ] Comprobar ausencia de rutas absolutas (`C:`, `D:`).
  - [ ] Verificar paridad de 8 secciones entre `README.md` y `README_ES.md`.
  - [ ] Validar vigencia del ADN en `01_seed/seed-iReadme-master.md`.

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (ThinkingSeed Master): el ADN del proyecto y no su repositorio completo. Refleja el avance real y la arquitectura del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, funcionamiento, dependencias y flujos del sistema.
> 2. **Sugerir mejoras o asistencia técnica** sobre el estado actual y áreas pendientes identificadas en la semilla.
> 3. **Generar código o soluciones compatibles** respetando las rutas, convenciones y patrones definidos aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas del Seed.
3. Revisa restricciones, reglas y contratos declarados.
4. Explicita supuestos cuando sea necesario: "Supongo que X debido a Y".
5. Propone cambios por archivo con rutas claras.
6. Añade pruebas, riesgos y criterios de aceptación.

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde únicamente con:
1. Un saludo confirmando que asimilaste el ADN de **iReadme** y su stack principal.
2. Un breve resumen de 2-3 líneas sobre el objetivo y su estado actual de avance.
3. Una frase poniéndote a disposición para resolver dudas sobre su funcionamiento o colaborar en los siguientes pasos de desarrollo.
