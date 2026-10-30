---
name: readme
description: >-
  Genera y estandariza la documentación de alta ingeniería 'Enterprise Paper-Grade v5.0' (iContext Federation Protocol v5.0) del repositorio activo
  creando simultáneamente README.md (Inglés) y README_ES.md (Español). Combina lenguaje corporativo de vanguardia
  (propuesta de valor estratégica, ROI, TCO, gobernanza) con rigor de paper científico (formulación matemática en
  LaTeX, diagramas ASCII, métricas bimodales inyectadas desde .context/icontext_bus.json y citación BibTeX) sin incluir rutas locales absolutas.
  Compatible con ecosistemas de IA: Google, Anthropic, OpenAI, Cursor y Copilot.
  Se activa al ejecutar /readme o al solicitar la estandarización o generación de READMEs.
---

# Workflow Obligatorio: Generación de Enterprise Paper-Grade v5.0 READMEs Duales (`/readme`)

> **DIRECTIVA FUNDAMENTAL DE SEGURIDAD, PORTABILIDAD Y COMPATIBILIDAD MULTI-AI (v5.0):**
> 1. **PROHIBIDO INCORPORAR RUTAS LOCALES ABSOLUTAS:** Queda terminantemente prohibido incluir rutas locales del sistema de archivos (ej. `C:\...`, `D:\...`, `file:///...`, `/home/...`). Toda ruta o referencia DEBE ser estrictamente relativa a la raíz del repositorio (`README.md`, `src/`, `config/`, `docs/`, `skills/`, etc.) y cumplir con la topología canónica `all-lowercase` (`01_seed/`, `02_foundation/`, `tools/`).
> 2. **GENERACIÓN DUAL SIMULTÁNEA Y ATOMICIDAD:** El agente DEBE generar siempre dos archivos en la raíz del repositorio:
>    - `README.md`: Versión maestra en idioma inglés técnico y corporativo internacional.
>    - `README_ES.md`: Versión completa en idioma español técnico riguroso y corporativo.
> 3. **HEADER DE CONMUTACIÓN DE IDIOMA RELATIVO:** La cabecera de ambos archivos debe incluir el selector de idioma con enlaces puramente relativos:
>    - En `README.md`: `**Language:** [English](README.md) | [Español](README_ES.md)`
>    - En `README_ES.md`: `**Idioma:** [English](README.md) | [Español](README_ES.md)`
> 4. **FEDERACIÓN iCONTEXT v5.0 (CAPA L3):**
>    - Antes de escanear el repositorio desde cero, consumir `./.context/icontext_bus.json` (si existe) para inyectar métricas verificadas en la Sección 4 (`Empirical Performance & Benchmarks`): cobertura AST de `ThinkingSeed` (`l1_thinkingseed.ast_coverage_pct`), puntuación y eficiencia espectral FPAI de `MetricsThinking` (`l2_metricsthinking.global_score`, `fpai_pf_spectral`) y presupuesto de tokens de `iDirectory` (`l0_idirectory.active_tokens`).
>    - Al finalizar la generación, actualizar el estado `l3_ireadme` en `./.context/icontext_bus.json` (`parity_score: 1.0`, `zero_local_paths: true`, `zero_emojis: true`, `latex_balanced: true`).

---

## Principios Estéticos y de Diseño Técnico (Enterprise Paper-Grade v5.0 Standard)

1. **ZERO EMOJIS & TONO INSTITUCIONAL DE VANGUARDIA:**
   Queda estrictamente prohibido el uso de emojis, iconos informales, exclamaciones o muletillas conversacionales. El tono debe ser denso, asertivo, formal y de alta ingeniería (estilo IEEE Transactions / ACM Systems + Enterprise Architecture Review).

2. **LENGUAJE CORPORATIVO ESTRATÉGICO Y TECH-APPEAL:**
   La documentación debe ser atractiva tanto para ingenieros de software líderes como para ejecutivos de tecnología (VP Engineering, CTO, Enterprise Architects):
   - **Tensión Operacional & Coste de Inacción:** Cuantificar el problema de negocio, la fricción técnica o el riesgo de deriva/deuda técnica que el repositorio resuelve.
   - **Propuesta de Valor Estratégico:** Explicar el impacto en términos de reducción de TCO (Total Cost of Ownership), retorno de inversión (ROI), aceleración de Time-to-Market, mitigación de riesgos de cumplimiento (Compliance) y resiliencia de la plataforma.
   - **Tesis Arquitectónica:** Presentar la solución técnica basada en patrones probados de ingeniería (Clean Architecture, Event-Driven, Medallion, Agentic Core, iContext Federation Protocol v5.0).

3. **FORMULACIÓN MATEMÁTICA FORMAL EN $\LaTeX$:**
   Cualquier algoritmo, optimización, econometría, función de pérdida, transformación de datos, balance de carga, invariante de consistencia o cota computacional DEBE expresarse con nomenclatura formal de *paper* científico utilizando notación KaTeX/LaTeX estándar (`$$...$$` para bloques independientes y `$...$` para expresiones en línea). Vincular explícitamente las variables matemáticas con los módulos de código ejecutables.

4. **TOPOLOGÍA ARQUITECTÓNICA EN CAJAS ASCII:**
   Diseñar diagramas de arquitectura en cajas monospaciadas ASCII/Unicode limpias, simétricas y legibles. Explicitar la separación de capas: Planos de Control (*Control Plane*), Planos de Datos/Analítica (*Data Plane*), contratos de datos, pasarelas y almacenamiento. No utilizar Mermaid por defecto salvo solicitud explícita del usuario.

5. **BADGES MONOCROMÁTICOS / SOBRIOS DE ALTO IMPACTO:**
   Utilizar badges de Shields.io con estilo `flat-square` o `for-the-badge`, en paleta neutra y sobria (`#1a1a1a`, `#2b2b2b`, `#34495e`, `#4b5563`, `#000000`).

6. **MATRIZ DE RENDIMIENTO Y BENCHMARKS BIMODAL:**
   La tabla de benchmark debe presentar métricas en dos dimensiones complementarias:
   - **Métricas de Ingeniería de Sistemas:** Latencia (p50/p95/p99), throughput de procesamiento, concurrencia, huella de memoria.
   - **Métricas de Negocio y Gobernanza (iContext Bus):** Tasa de fuga de rutas (0.0%), índice de sincronización ($\Phi = 1.0$), cobertura AST de contratos, eficiencia espectral FPAI ($PF_{\text{spectral}}$) o ahorro de cómputo/tokens.

7. **DEVEX DETERMINISTA ("PLUG & PLAY / LLEGAR E INSTALAR"):**
   Instrucciones de despliegue y ejecución reproducibles en una sola línea, preparadas para pipelines de CI/CD automatizados y auditorías de invariantes.

---

## Procedimiento Paso a Paso para el Agente

### Paso 1: Reconocimiento Integral y Consumo del Bus iContext v5.0
Inspecciona el repositorio activo priorizando los artefactos de federación:
1. **Bus de Federación y Satélite L0:** Leer `./.context/icontext_bus.json`, `./.context/tree.json` y `./.context/contracts_ast.json` (si existen) para obtener topología `all-lowercase`, firmas públicas y telemetría verificada.
2. **ADN Arquitectónico L1:** Consultar `./01_seed/seed-*-master.md` (o vía `python FWengine.py seed --toc`) para extraer el propósito estratégico, invariantes y modelos de datos.
3. **Telemetría Forense L2:** Consultar `./artifacts/plans/metricsthinking/MetricsThinking.json` (si existe) para incorporar métricas reales de calidad, seguridad y acoplamiento AST.
4. **Manifiestos y Suites de Pruebas:** Revisar `pyproject.toml`, `package.json`, `Cargo.toml` y `tests/`.

### Paso 2: Generación Dual Simultánea (`README.md` y `README_ES.md`)
Generar ambos archivos con las 8 secciones canónicas exactas, inyectando las insignias / escudos de estado (badges) de las metodologías iContext activas en la cabecera:
1. `## 1. Executive Abstract` / `## 1. Resumen Ejecutivo`
2. `## 2. System Architecture & Topology` / `## 2. Arquitectura y Topología del Sistema`
   - **Subsección Obligatoria de Gobernanza Federada:** Dentro de esta sección, incluir la subsección `### Federated Governance & Context Engineering (iContext v5.0)` (en inglés) / `### Gobernanza Federada & Context Engineering iContext v5.0` (en español), resumiendo cuáles de los 4 proyectos canónicos (`iDirectory`, `ThinkingSeed`, `MetricsThinking`, `iReadme`) se encuentran incorporados en el repositorio y detallando brevemente su función de optimización atencional y control agéntico.
3. `## 3. Mathematical Formulation & Analytical Engines` / `## 3. Formulación Matemática y Motores Analíticos`
4. `## 4. Empirical Performance & Benchmarks` / `## 4. Rendimiento Empírico y Benchmarks`
5. `## 5. Repository Structure & Artifacts` / `## 5. Estructura del Repositorio y Artefactos` (usando estrictamente directorios en minúsculas: `01_seed/`, `02_foundation/`, `tools/`, `scripts/`, `tests/`)
6. `## 6. Execution & Verification Protocol` / `## 6. Protocolo de Ejecución y Verificación`
7. `## 7. Domain Glossary` / `## 7. Glosario de Dominio`
8. `## 8. Academic & Engineering References` / `## 8. Referencias Académicas y de Ingeniería` (con cita BibTeX).

### Paso 3: Verificación de Invariantes y Certificación L3
Valida que:
1. Ningún archivo contenga rutas absolutas de disco (`C:\`, `D:\`, `file:///`, `/home/`) ni directorios legacy en mayúsculas (`001_Seed`, `02_Foundation`, `Tools`).
2. Cero emojis en ambos documentos.
3. Las delimitaciones de KaTeX/LaTeX (`$$` y `$`) estén perfectamente balanceadas.
4. Las 8 secciones canónicas estén presentes en el orden exacto ($\Phi = 1.0$).
5. Si el repositorio dispone de `scripts/init_readme.py` o `tests/test_invariants.py`, ejecutar `pytest` para certificar el cumplimiento y actualizar `l3_ireadme` en `.context/icontext_bus.json`.
