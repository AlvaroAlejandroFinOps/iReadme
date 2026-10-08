# Propuesta Consolidada: Skill iReadme (Enterprise Paper-Grade v2.0)

Este documento especifica la integración formal de la skill universal `iReadme` para ecosistemas de agentes autónomos de IA (Google Antigravity, Anthropic Claude, OpenAI, Cursor y GitHub Copilot).

---

## 1. Definición Canónica de la Skill (`skills/readme/SKILL.md`)

```yaml
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
```

## 2. Directivas de Diseño Enterprise Paper-Grade

1. **Zero Path Leakage (Portabilidad Total):**
   - Prohibido filtrar rutas locales absolutas (`C:\`, `D:\`, `file:///`, `/home/`).
   - Todos los hipervínculos deben ser 100% relativos a la raíz del repositorio.
2. **Zero Emojis & Rigor Institucional:**
   - Cero emojis, iconos decorativos o lenguaje informal.
   - Prosa densa, estratégica y precisa de grado publicación IEEE / ACM.
3. **Lenguaje Corporativo de Vanguardia:**
   - Resumen ejecutivo estructurado en 3 pilares: (1) Tensión operacional y coste de inacción, (2) Propuesta de valor estratégico (ROI, TCO, gobernanza), y (3) Tesis arquitectónica.
4. **Formulación Matemática Formal en $\LaTeX$:**
   - Expresar rigurosamente funciones objetivo, cotas operacionales, invariantes de paridad y teoría de la información en notación LaTeX estándar (`$$...$$` y `$...$`).
5. **Topología Arquitectónica en Cajas ASCII:**
   - Diagramas monospaciados simétricos que diferencian planos de control y planos de datos/analítica.
6. **Matriz Bimodal de Benchmarking:**
   - Medición simultánea de métricas de sistemas (latencia p99, throughput) y métricas de gobernanza de plataforma (fuga de rutas 0.0%, índice de paridad 1.0, SLA compliance).
7. **Instalación Universal ("Plug & Play"):**
   - Soporte nativo para instalación en 1 comando a través de `install.sh`, `install.ps1` y `scripts/install_skill.py`.