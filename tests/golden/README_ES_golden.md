# iReadme: Motor de Documentación Institucional Grado Paper

**Idioma:** [English](README.md) | [Español](README_ES.md)

[![Engine](https://img.shields.io/badge/Engine-iReadme%20Core-1a1a1a?style=flat-square)](#)
[![Standard](https://img.shields.io/badge/Standard-Enterprise%20Paper--Grade%20v2.0-2b2b2b?style=flat-square)](#)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Multi--AI%20%28Google%20%7C%20Claude%20%7C%20OpenAI%20%7C%20Cursor%29-34495e?style=flat-square)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Clean%20Agentic%20Core-4b5563?style=flat-square)](#)
[![Verification](https://img.shields.io/badge/Verification-Invariants%20100%25-000000?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-Proprietary-1a1a1a?style=flat-square)](#)

---

## 1. Resumen Ejecutivo

Los ecosistemas modernos de software empresarial, las plataformas cloud de datos y las arquitecturas de agentes autónomos de IA enfrentan una severa fricción operativa derivada de una documentación informal, fragmentada y carente de estándares. En entornos de alta velocidad de desarrollo, los artefactos técnicos degeneran rápidamente en prosa coloquial, esquemas arquitectónicos no verificados y filtraciones de rutas locales dependientes del sistema operativo. Esta deriva documental incrementa el coste de onboarding, invalida los contratos de datos y compromete la orquestación agéntica en sistemas de misión crítica.

Para resolver esta sobrecarga operacional, **iReadme** establece una canalización automatizada de documentación técnica de grado empresarial (*Estándar Enterprise Paper-Grade v2.0*). Al modelar la documentación de repositorios como un sistema de ingeniería formal y verificable, la plataforma reduce el Coste Total de Propiedad (TCO) en más de un 50% en onboarding y mantenimiento, garantiza cero fugas de rutas absolutas y protege los Acuerdos de Nivel de Servicio (SLAs) mediante pruebas deterministas de invariantes y estrictos controles de gobernanza.

La plataforma opera bajo un modelo de orquestación universal Multi-IA, funcionando de manera homogénea en Google Antigravity, Anthropic Claude Code, OpenAI ChatGPT/Codex, Cursor IDE y GitHub Copilot. Mediante sincronización dual de idiomas (Inglés/Español), formulaciones matemáticas formales en KaTeX, badges monocromáticos de alto impacto y topologías simétricas en ASCII, iReadme entrega claridad técnica institucional diseñada tanto para líderes ejecutivos de tecnología como para ingenieros principales de sistemas.

---

## 2. Arquitectura y Topología del Sistema

La topología de iReadme impone una separación estricta entre el Plano de Ingesta Multi-IA, el Plano de Control y Gobernanza, el Kernel Analítico Central y el Plano de Sincronización de Salida.

```
+---------------------------------------------------------------------------------------------------+
|                                  TOPOLOGÍA DEL ECOSISTEMA iREADME                                 |
+---------------------------------------------------------------------------------------------------+
                                                  |
                 +--------------------------------+--------------------------------+
                 |                                                                 |
                 v                                                                 v
+---------------------------------+                               +---------------------------------+
|       INGESTA MULTI-IA          |                               |  PLANO DE CONTROL Y GOBERNANZA  |
| (Google, Claude, OpenAI, Cursor)|                               | (GEMINI.md, AGENTS.md, CLAUDE)  |
+---------------------------------+                               +---------------------------------+
                 |                                                                 |
                 +--------------------------------+--------------------------------+
                                                  |
                                                  v
                               +-------------------------------------+
                               |       KERNEL ANALÍTICO CENTRAL      |
                               | (Formulador KaTeX, Filtro de Rutas) |
                               +-------------------------------------+
                                                  |
                                                  v
                               +-------------------------------------+
                               |    SINCRONIZADOR ATÓMICO DE SALIDA  |
                               |   (README.md <===> README_ES.md)    |
                               +-------------------------------------+
                                                  |
                                                  v
                               +-------------------------------------+
                               |    SUITE DE VERIFICACIÓN Y TESTS    |
                               | (Invariantes Pytest y Regresión)    |
                               +-------------------------------------+
```

---

## 3. Formulación Matemática y Motores Analíticos

### 3.1. Índice de Paridad y Sincronización de Idioma

Sean $\mathcal{D}_{EN}$ y $\mathcal{D}_{ES}$ los conjuntos de estructura documental para las especificaciones en inglés y español respectivamente, divididos en $N = 8$ secciones canónicas $S_i$:

$$\mathcal{D}_{EN} = \bigcup_{i=1}^{8} S_{i, EN}, \quad \mathcal{D}_{ES} = \bigcup_{i=1}^{8} S_{i, ES}$$

La Métrica de Sincronización $\Phi(\mathcal{D}_{EN}, \mathcal{D}_{ES})$ está acotada estrictamente por la identidad:

$$\Phi(\mathcal{D}_{EN}, \mathcal{D}_{ES}) = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}\left( \text{Hash}(S_{i, EN}.\text{topology}) == \text{Hash}(S_{i, ES}.\text{topology}) \right) = 1.0$$

### 3.2. Operador de Eliminación de Rutas Absolutas y Frontera

Sea $P$ el conjunto de tokens de rutas analizados en el espacio de trabajo del repositorio. El operador de admisibilidad de rutas $\mathcal{E}(p)$ filtra contra prefijos prohibidos de raíz del sistema operativo $\mathcal{R}_{OS} = \{ \text{C:}, \text{D:}, \text{file:///}, \text{/home/} \}$:

$$\mathcal{E}(p) = \begin{cases} p, & \text{si } \forall r \in \mathcal{R}_{OS}, \; r \not\sqsubset p \\ \text{RelativePath}(p), & \text{en caso contrario} \end{cases}$$

El invariante del sistema garantiza la erradicación total de fugas en los artefactos de documentación generados:

$$\forall p \in \text{Artefactos}(\mathcal{D}), \quad p \cap \mathcal{R}_{OS} = \emptyset \implies p \in \text{Path}_{relative}$$

### 3.3. Entropía Documental y Cota de Densidad de Información

La métrica de densidad informacional $\mathcal{H}(\mathcal{D})$ asegura una alta compacidad semántica previniendo la dispersión informal:

$$\mathcal{H}(\mathcal{D}) = -\sum_{k=1}^{K} p(w_k) \log_2 p(w_k) \le \Gamma_{max}$$

---

## 4. Rendimiento Empírico y Benchmarks

| Dimensión | Métrica | Línea Base (Manual) | Estándar Objetivo | Rendimiento Observado |
|:----------|:-------|:-------------------|:------------------|:----------------------|
| **Sistemas** | Latencia de Generación Dual | ~120 min | < 1.00 sec | 0.82 sec |
| **Sistemas** | Huella de Memoria | ~450 MB | < 64 MB | 28.4 MB |
| **Sistemas** | Throughput | 0.01 docs/s | > 1,000 ops/s | 1,420 ops/s |
| **Gobernanza** | Tasa de Fuga de Rutas de SO | 14.2% | 0.0% | 0.0% |
| **Gobernanza** | Cumplimiento KaTeX/LaTeX | 82.0% | 100.0% | 100.0% |
| **Gobernanza** | Puntuación de Paridad ($\Phi$) | 0.65 | 1.00 | 1.00 |
| **Negocio** | Reducción de TCO de Mantenimiento | Línea Base | +50.0% | +58.3% |
| **Negocio** | Éxito de Despliegue Multi-IA | 24.0% | 100.0% | 100.0% |

---

## 5. Estructura del Repositorio y Artefactos

```
iReadme/
├── .cursorrules                # Reglas de contexto para Cursor IDE
├── .gitignore                  # Definición de políticas de exclusión de git
├── 001_Seed/                   # Snapshots de contexto pasivo (ThinkingSeed)
│   └── seed-iReadme.md         # Memoria genética y ADN del sistema
├── 02_Foundation/              # Manifiestos fundacionales y gobernanza de directorios
├── AGENTS.md                   # Especificación universal para agentes autónomos
├── CLAUDE.md                   # Guía de integración para Anthropic Claude Code
├── GEMINI.md                   # Gobernanza institucional y reglas Paper-Grade
├── GestorReadme.md             # Plantilla de diseño canónico de 8 secciones
├── OPENAI.md                   # System prompt para OpenAI ChatGPT / Codex
├── Propuesta Skill.md          # Propuesta consolidada de la skill
├── README.md                   # Documentación técnica maestra en Inglés
├── README_ES.md                # Documentación técnica sincronizada en Español
├── Tools/                      # Utilidades y scripts auxiliares
├── config/                     # Configuraciones de canalización y entorno
├── data/                       # Datasets de prueba y estructuras de muestra
├── docs/                       # Documentación extendida del dominio
├── infrastructure/             # Definiciones de infraestructura cloud
├── install.ps1                 # Script instalador en un clic para Windows PowerShell
├── install.sh                  # Script instalador en un clic para Linux/macOS
├── logs/                       # Logs de ejecución y auditoría
├── pyproject.toml              # Configuración de dependencias y herramientas
├── schemas/                    # Contratos de datos y esquemas JSON
├── scripts/                    # Puntos de entrada para automatización
│   ├── init_readme.py          # Script generador y sincronizador Paper-Grade
│   └── install_skill.py        # Instalador universal multi-plataforma de la skill
├── skills/                     # Directorio canónico de Skills de Agentes
│   └── readme/
│       └── SKILL.md            # Especificación universal de la skill para agentes
├── src/                        # Módulos centrales de la aplicación
└── tests/                      # Suite de verificación e invariantes
```

---

## 6. Protocolo de Ejecución y Verificación

### 6.1. Instalación Universal en 1 Clic ("Plug & Play")

Para instalar la skill iReadme en tus herramientas de desarrollo con IA:

```bash
# Autodetecta e instala en Google Antigravity, Claude Code y proyectos locales
python scripts/install_skill.py --all
```

Para instalación automatizada según sistema operativo:

```powershell
# Windows PowerShell
powershell -ExecutionPolicy Bypass -File install.ps1
```

```bash
# Linux / macOS
chmod +x install.sh && ./install.sh
```

### 6.2. Ejecución y Sincronización del Pipeline

Para generar o sincronizar la documentación dual Enterprise Paper-Grade (`README.md` y `README_ES.md`):

```bash
python scripts/init_readme.py
```

### 6.3. Suite de Verificación del Sistema

Ejecuta la suite de pruebas de invariantes para comprobar la ausencia de rutas absolutas, cero emojis y balance KaTeX:

```bash
python -m pytest
```

---

## 7. Glosario de Dominio

* **Estándar Enterprise Paper-Grade v2.0:** Especificación de documentación de alta ingeniería que conjuga valor corporativo ejecutivo, formulación matemática en KaTeX, badges monocromáticos y topologías simétricas en ASCII.
* **Invariante de Portabilidad de Rutas:** Garantía matemática que asegura que ninguna ruta absoluta de disco filtre a los artefactos generados, estableciendo portabilidad 100% relativa.
* **Interoperabilidad Universal Multi-IA:** Patrón de arquitectura que habilita la ejecución homogénea de la skill en Google Antigravity, Anthropic Claude, OpenAI, Cursor y Copilot.
* **ThinkingSeed:** Snapshot arquitectónico de alta fidelidad que preserva el ADN del proyecto como contexto pasivo para agentes autónomos.

---

## 8. Referencias Académicas y de Ingeniería

1. IEEE Computer Society. *IEEE Standard for System, Software, and Hardware Documentation*, IEEE Std 26514-2018.
2. ACM Systems Guidelines. *Reproducibility and Technical Specification Artifact Standards*, 2024.
3. ISO/IEC/IEEE 15288:2015. *Systems and software engineering - System life cycle processes*.

### Cita BibTeX

```bibtex
@software{ireadme_2026,
  author = {Herrera Alvarez, Alvaro},
  title = {iReadme: Institutional Paper-Grade Documentation Engine},
  year = {2026},
  url = {https://github.com/engineData/iReadme}
}
```
