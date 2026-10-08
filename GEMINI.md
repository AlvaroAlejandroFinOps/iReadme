# Reglas de Gobernanza y Documentación: Ecosistema iReadme

Este archivo establece las directrices de ingeniería y documentación institucional para el proyecto **iReadme** y sus componentes.

## 1. Estándar de Documentación Enterprise Paper-Grade v2.0
Cualquier generación o actualización de los archivos `README.md` y `README_ES.md` debe cumplir estrictamente con el estándar definido en `skills/readme/SKILL.md` y la skill global `/readme`:

1. **Aislamiento de Rutas (Portabilidad Total):**
   - Queda estrictamente prohibido incluir rutas locales absolutas del sistema operativo (como `C:\...`, `D:\...`, `file:///...`, `/home/...`).
   - Todas las referencias a carpetas, scripts y archivos deben ser relativas a la raíz del repositorio (`src/`, `config/`, `docs/`, `skills/`, `tests/`, etc.).
   - El header de conmutación de idioma debe utilizar enlaces relativos limpios:
     - En `README.md`: `**Language:** [English](README.md) | [Español](README_ES.md)`
     - En `README_ES.md`: `**Idioma:** [English](README.md) | [Español](README_ES.md)`

2. **Rigor Estético y Formal:**
   - **Zero Emojis:** Prohibido el uso de emojis, iconos informales o muletillas conversacionales. Tono denso, asertivo e institucional (estilo IEEE Transactions / ACM Systems + Enterprise Architecture Review).
   - **LaTeX Formal:** Expresar cualquier modelo matemático, optimización, invariante de consistencia o cálculo algorítmico mediante fórmulas LaTeX estándar (`$$...$$` y `$...$`).
   - **Topología ASCII:** Los diagramas de arquitectura deben representarse en cajas monospaciadas ASCII/Unicode limpias y simétricas, diferenciando explícitamente el plano de control (*Control Plane*) del plano de datos/analítica (*Data/Analytical Plane*).
   - **Badges Sobrios de Alto Impacto:** Utilizar badges monocromáticos o en tonos neutros (`#1a1a1a`, `#2b2b2b`, `#34495e`, `#4b5563`, `#000000`) reflejando motor, arquitectura, estándar, ecosistema multi-IA y suite de verificación.

3. **Narrativa Corporativa de Vanguardia y Atractivo Tech:**
   - **Tríada del Resumen Ejecutivo:**
     1. *Tensión Operacional & Coste de Inacción:* Cuantificar la fricción técnica, riesgo de deriva o deuda del sistema.
     2. *Propuesta de Valor Estratégico:* Ahorro de TCO, ROI de ingeniería, aceleración de Time-to-Market y gobernanza auditable.
     3. *Tesis Arquitectónica:* Resolución técnica mediante principios de ingeniería de sistemas de alto desempeño.
   - **Matriz de Rendimiento Bimodal:** Combinar métricas de ingeniería de sistemas (latencia p50/p95/p99, throughput, memoria) con KPIs de negocio y gobernanza (fuga de rutas 0.0%, paridad de secciones 1.0, SLA compliance).
   - **Compatibilidad Universal Multi-IA ("Plug & Play"):** Documentar y garantizar soporte para Google Antigravity, Anthropic Claude Code, OpenAI ChatGPT/Codex y Cursor IDE.

4. **Paridad Dual de Idiomas:**
   - Mantener siempre sincronizadas las versiones en inglés (`README.md`) y español (`README_ES.md`) con las 8 secciones canónicas de ingeniería.

5. **Estructura Canónica de 8 Secciones:**
   - `## 1. Executive Abstract / Resumen Ejecutivo`
   - `## 2. System Architecture & Topology / Arquitectura y Topología del Sistema`
   - `## 3. Mathematical Formulation & Analytical Engines / Formulación Matemática y Motores Analíticos`
   - `## 4. Empirical Performance & Benchmarks / Rendimiento Empírico y Benchmarks`
   - `## 5. Repository Structure & Artifacts / Estructura del Repositorio y Artefactos`
   - `## 6. Execution & Verification Protocol / Protocolo de Ejecución y Verificación`
   - `## 7. Domain Glossary / Glosario de Dominio`
   - `## 8. Academic & Engineering References / Referencias Académicas y de Ingeniería` (incluyendo BibTeX citation).
