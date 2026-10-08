---
name: readme
description: >-
  Genera y estandariza la documentación de alta ingeniería 'Enterprise Paper-Grade' del repositorio activo
  creando simultáneamente README.md (Inglés) y README_ES.md (Español). Combina lenguaje corporativo de vanguardia
  (propuesta de valor estratégica, ROI, TCO, gobernanza) con rigor de paper científico (formulación matemática en
  LaTeX, diagramas ASCII, métricas bimodales y citación BibTeX) sin incluir rutas locales absolutas. Compatible con
  ecosistemas de IA: Google, Anthropic, OpenAI, Cursor y Copilot.
  Se activa al ejecutar /readme o al solicitar la estandarización o generación de READMEs.
---

# Workflow Obligatorio: Generación de Enterprise Paper-Grade READMEs Duales (`/readme`)

> **DIRECTIVA FUNDAMENTAL DE SEGURIDAD, PORTABILIDAD Y COMPATIBILIDAD MULTI-AI:**
> 1. **PROHIBIDO INCORPORAR RUTAS LOCALES ABSOLUTAS:** Queda terminantemente prohibido incluir rutas locales del sistema de archivos (ej. `C:\...`, `D:\...`, `file:///...`, `/home/...`). Toda ruta o referencia DEBE ser estrictamente relativa a la raíz del repositorio (`README.md`, `src/`, `config/`, `docs/`, `skills/`, etc.) o descriptores genéricos del entorno.
> 2. **GENERACIÓN DUAL SIMULTÁNEA:** El agente DEBE generar siempre dos archivos en la raíz del repositorio:
>    - `README.md`: Versión maestra en idioma inglés técnico y corporativo internacional.
>    - `README_ES.md`: Versión completa en idioma español técnico riguroso y corporativo.
> 3. **HEADER DE CONMUTACIÓN DE IDIOMA RELATIVO:** La cabecera de ambos archivos debe incluir el selector de idioma con enlaces puramente relativos:
>    - En `README.md`: `**Language:** [English](README.md) | [Español](README_ES.md)`
>    - En `README_ES.md`: `**Idioma:** [English](README.md) | [Español](README_ES.md)`
> 4. **COMPATIBILIDAD UNIVERSAL AGENTIC:** Este estándar es interoperable entre ecosistemas de IA: Google Antigravity / Gemini CLI, Anthropic Claude Code, OpenAI ChatGPT / Codex, Cursor IDE y GitHub Copilot.

---

## Principios Estéticos y de Diseño Técnico (Enterprise Paper-Grade Standard)

1. **ZERO EMOJIS & TONO INSTITUCIONAL DE VANGUARDIA:**
   Queda estrictamente prohibido el uso de emojis, iconos informales, exclamaciones o muletillas conversacionales. El tono debe ser denso, asertivo, formal y de alta ingeniería (estilo IEEE Transactions / ACM Systems + Enterprise Architecture Review).

2. **LENGUAJE CORPORATIVO ESTRATÉGICO Y TECH-APPEAL:**
   La documentación debe ser atractiva tanto para ingenieros de software líderes como para ejecutivos de tecnología (VP Engineering, CTO, Enterprise Architects):
   - **Tensión Operacional & Coste de Inacción:** Cuantificar el problema de negocio, la fricción técnica o el riesgo de deriva/deuda técnica que el repositorio resuelve.
   - **Propuesta de Valor Estratégico:** Explicar el impacto en términos de reducción de TCO (Total Cost of Ownership), retorno de inversión (ROI), aceleración de Time-to-Market, mitigación de riesgos de cumplimiento (Compliance) y resiliencia de la plataforma.
   - **Tesis Arquitectónica:** Presentar la solución técnica basada en patrones probados de ingeniería (Clean Architecture, Event-Driven, Medallion, Agentic Core, Microservicios desacoplados).

3. **FORMULACIÓN MATEMÁTICA FORMAL EN $\LaTeX$:**
   Cualquier algoritmo, optimización, econometría, función de pérdida, transformación de datos, balance de carga, invariante de consistencia o cota computacional DEBE expresarse con nomenclatura formal de *paper* científico utilizando notación KaTeX/LaTeX estándar (`$$...$$` para bloques independientes y `$...$` para expresiones en línea). Vincular explícitamente las variables matemáticas con los módulos de código ejecutables.

4. **TOPOLOGÍA ARQUITECTÓNICA EN CAJAS ASCII:**
   Diseñar diagramas de arquitectura en cajas monospaciadas ASCII/Unicode limpias, simétricas y legibles. Explicitar la separación de capas: Planos de Control (*Control Plane*), Planos de Datos/Analítica (*Data Plane*), contratos de datos, pasarelas y almacenamiento. No utilizar Mermaid por defecto salvo solicitud explícita del usuario.

5. **BADGES MONOCROMÁTICOS / SOBRIOS DE ALTO IMPACTO:**
   Utilizar badges de Shields.io con estilo `flat-square` o `for-the-badge`, en paleta neutra y sobria (negros, pizarra, grises oscuros: `#1a1a1a`, `#2b2b2b`, `#34495e`, `#4b5563`, `#000000`). Los badges deben reflejar:
   - Estado del Motor (*Engine*)
   - Estándar (*Enterprise Paper-Grade v2.0*)
   - Ecosistema Multi-IA (*Multi-AI: Google | Claude | OpenAI | Cursor*)
   - Nivel de Arquitectura / Tier
   - Suite de Verificación (*Invariants 100% Passed*)
   - Licencia

6. **MATRIZ DE RENDIMIENTO Y BENCHMARKS BIMODAL:**
   La tabla de benchmark debe presentar métricas en dos dimensiones complementarias:
   - **Métricas de Ingeniería de Sistemas:** Latencia (p50/p95/p99), throughput de procesamiento, concurrencia, huella de memoria.
   - **Métricas de Negocio y Gobernanza:** Tasa de fuga de rutas (0.0%), índice de sincronización ($\Phi = 1.0$), cumplimiento de SLAs corporativos, tasa de deriva de datos o ahorro de cómputo/tokens.

7. **DEVEX DETERMINISTA ("PLUG & PLAY / LLEGAR E INSTALAR"):**
   Instrucciones de despliegue y ejecución reproducibles en una sola línea, preparadas para pipelines de CI/CD automatizados y auditorías de invariantes.

---

## Procedimiento Paso a Paso para el Agente

### Paso 1: Reconocimiento Integral y Extracción de Hechos del Workspace
Inspecciona metódicamente el repositorio activo para extraer la evidencia física (*Ground Truth*):
1. **Manifiestos de Dependencias & Runtime:** (`pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, `pom.xml`, etc.) para determinar runtime, stack y librerías.
2. **Arquitectura y Gobernanza:** (`GEMINI.md`, `CLAUDE.md`, `AGENTS.md`, `01_seed/`, `02_Foundation/`, `docs/`) para entender el propósito estratégico, las restricciones y las entidades del dominio.
3. **Módulos de Código y Algoritmos:** (`src/`, `lib/`, `core/`, `cloud_jobs/`, `data_generation/`) para identificar motores analíticos, flujos de datos y lógica algorítmica para modelar en LaTeX.
4. **Suites de Pruebas & Invariantes:** (`tests/`, `specs/`) para estructurar la sección de verificación y protocolos de calidad.
5. **Infraestructura & Contratos:** (`infrastructure/`, `schemas/`, `Dockerfile`, Terraform, etc.) para identificar planos de despliegue y contratos de datos.

### Paso 2: Modelado de Arquitectura, Formulación LaTeX y Matriz Bimodal
- Sintetiza la tensión de negocio y la propuesta de valor estratégico en prosa ejecutiva.
- Diseña el diagrama ASCII de topología del sistema con límites claros de control y datos.
- Modela matemáticamente los algoritmos, invariantes o transformaciones clave en $\LaTeX$.
- Construye la matriz de benchmarking combinando KPIs de negocio/gobernanza y métricas de sistemas.

### Paso 3: Generación del Archivo Maestro `README.md` (Inglés)
Escribe el archivo `README.md` en la raíz del repositorio con la siguiente estructura canónica obligatoria:

```markdown
# [SYSTEM_ACRONYM]: [High-Impact Enterprise Subtitle]

**Language:** [English](README.md) | [Español](README_ES.md)

[![Engine](https://img.shields.io/badge/Engine-[Name]-1a1a1a?style=flat-square)](#)
[![Standard](https://img.shields.io/badge/Standard-Enterprise%20Paper--Grade%20v2.0-2b2b2b?style=flat-square)](#)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Multi--AI%20%28Google%20%7C%20Claude%20%7C%20OpenAI%20%7C%20Cursor%29-34495e?style=flat-square)](#)
[![Architecture](https://img.shields.io/badge/Architecture-[Pattern]-4b5563?style=flat-square)](#)
[![Verification](https://img.shields.io/badge/Verification-Invariants%20100%25-000000?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-[License]-1a1a1a?style=flat-square)](#)

---

## 1. Executive Abstract

[Paragraph 1: Operational Friction & Business Tension. Detailed breakdown of industry/system friction, operational cost of inaction, compliance vulnerability, or technical debt.]

[Paragraph 2: Strategic Value Proposition & Enterprise Impact. Quantitative and qualitative value delivery: TCO reduction, SLA guarantees, ROI acceleration, cross-functional developer velocity, and rigorous platform governance.]

[Paragraph 3: Architectural Thesis & Technical Resolution. Clear formulation of how the system resolves the tension through proven engineering paradigms, deterministic guarantees, and multi-AI portability.]

---

## 2. System Architecture & Topology

[High-precision ASCII box diagram depicting Control Plane, Ingestion/Gateway, Analytical Engines, Data Contracts, Storage Subsystems, and Observability.]

```
+---------------------------------------------------------------------------------+
|                              [SYSTEM TOPOLOGY]                                  |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------+     +-----------------------+     +---------------------+
|     Control Plane     | --> |   Analytical Kernel   | --> | Output / Deliverable|
+-----------------------+     +-----------------------+     +---------------------+
```

---

## 3. Mathematical Formulation & Analytical Engines

### 3.1. [Engine / Subsystem A Formulation]
[Rigorous mathematical formulation using KaTeX/LaTeX, defining sets, objective functions, optimization targets, and operational invariants.]

$$\mathcal{L}(\theta) = \sum_{i=1}^{M} \omega_i \cdot \psi(x_i) + \lambda \|\theta\|^2$$

[Explicit mapping of variables to software components and operational bounds.]

### 3.2. [Engine / Subsystem B Formulation & Computational Bounds]
[Complexity bounds and formal system invariants.]

$$\mathcal{O}(N \log N), \quad \Phi(\mathcal{S}_{A}, \mathcal{S}_{B}) = 1.0$$

---

## 4. Empirical Performance & Benchmarks

| Dimension | Metric | Baseline | Target Standard | Observed (Production / Twin) |
|:----------|:-------|:---------|:----------------|:-----------------------------|
| **Systems** | Latency (p99) | ... | < 100 ms | ... |
| **Systems** | Throughput | ... | > 1,000 req/s | ... |
| **Systems** | Memory Footprint | ... | < 256 MB | ... |
| **Governance**| Path Leakage Rate | 15.0% | 0.0% | 0.0% |
| **Governance**| Parity Score ($\Phi$)| 0.70 | 1.00 | 1.00 |
| **Business** | TCO Savings / Efficiency| Baseline | +45% | +52.4% |

---

## 5. Repository Structure & Artifacts

[Annotated ASCII tree detailing directory responsibilities following Clean Architecture / DDD, including AI agent configurations.]

```
[repo-name]/
├── .gitignore                  # Git exclusion policy definition
├── AGENTS.md                   # Universal open AI agent specification
├── CLAUDE.md                   # Anthropic Claude Code & Desktop integration
├── GEMINI.md                   # Google Antigravity & Gemini CLI governance
├── OPENAI.md                   # OpenAI ChatGPT / Codex project prompt
├── .cursorrules                # Cursor IDE contextual rule specification
├── skills/                     # Canonical Agent Skills distribution directory
│   └── [skill_name]/
│       └── SKILL.md            # Universal agent skill definition
├── scripts/                    # Automation entry points & CLI tooling
├── src/                        # Core application & domain modules
└── tests/                      # Verification suite & invariant tests
```

---

## 6. Execution & Verification Protocol

### 6.1. Universal 1-Click Installation ("Plug & Play")
[Deterministic, copy-pasteable commands for single-command installation across AI platforms.]

### 6.2. Pipeline Execution & Runtime Entry Points
[Deterministic execution commands for pipelines, background jobs, or CLI entry points.]

### 6.3. Verification Suite & Invariant Tests
[Testing commands, coverage assertions, and data contract validations.]

---

## 7. Domain Glossary

* **[Term A]:** Formal, unambiguous definition bridging distributed systems and business value.
* **[Term B]:** Formal, unambiguous definition.

---

## 8. Academic & Engineering References

1. IEEE Computer Society. *IEEE Standard for System, Software, and Hardware Documentation*, IEEE Std 26514-2018.
2. ACM Systems Guidelines. *Reproducibility and Technical Specification Artifact Standards*, 2024.
3. ISO/IEC/IEEE 15288:2015. *Systems and software engineering - System life cycle processes*.

### BibTeX Citation

```bibtex
@software{system_acronym_year,
  author = {[Author/Organization]},
  title = {[System Name]: [High-Impact Enterprise Subtitle]},
  year = {[Year]},
  url = {[Repository URL]}
}
```
```

### Paso 4: Generación del Archivo `README_ES.md` (Español)
Escribe el archivo `README_ES.md` en la raíz del repositorio manteniendo idéntica topología, ecuaciones $\LaTeX$, diagramas ASCII, tablas de benchmarks y estructura canónica de 8 secciones, traduciendo con máxima fidelidad técnica la prosa al español corporativo y técnico formal.

Estructura obligatoria de `README_ES.md`:
- Título y subtítulo en español formal.
- Header: `**Idioma:** [English](README.md) | [Español](README_ES.md)`
- `## 1. Resumen Ejecutivo` (Tensión Operativa, Propuesta de Valor Estratégica, Tesis Arquitectónica).
- `## 2. Arquitectura y Topología del Sistema`
- `## 3. Formulación Matemática y Motores Analíticos`
- `## 4. Rendimiento Empírico y Benchmarks`
- `## 5. Estructura del Repositorio y Artefactos`
- `## 6. Protocolo de Ejecución y Verificación`
- `## 7. Glosario de Dominio`
- `## 8. Referencias Académicas y de Ingeniería` (con cita BibTeX).

### Paso 5: Verificación de Invariantes y Certificación
Valida que:
1. Ningún archivo contenga rutas absolutas de disco (`C:\`, `D:\`, `file:///`, `/home/`).
2. Cero emojis en ambos documentos.
3. Las delimitaciones de KaTeX/LaTeX (`$$` y `$`) estén perfectamente balanceadas.
4. Las 8 secciones canónicas estén presentes en el orden exacto.
5. Los selectores relativos de idioma sean recíprocos y funcionales.
