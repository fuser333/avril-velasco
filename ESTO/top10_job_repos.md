# 🏆 TOP 10 Repositorios para Búsqueda de Empleo (2026)
## Análisis comparativo para el caso de Avril Velasco — Ecuador

> Fecha: 2026-05-14  
> Búsqueda: Global (GitHub) + China (Gitee/GitHub)  
> Contexto: Marketing Digital / Community Manager / Ecuador (PYMES)

---

## 📊 Resumen Ejecutivo

| # | Repositorio | Stars | Tipo | Mercado | Relevancia Avril |
|---|-------------|-------|------|---------|-----------------|
| 1 | **career-ops** (santifer) | ~45k | Framework AI | Global tech | ⭐⭐⭐⭐⭐ Ya adaptado |
| 2 | **AIHawk** (feder-cr) | 29.8k | Auto-apply LinkedIn | Global | ⭐⭐☆☆☆ ARCHIVADO, baneado |
| 3 | **ApplyPilot** (Pickle-Pixel) | ~8k | Full pipeline auto-apply | Global | ⭐⭐⭐⭐☆ Robar ideas pipeline |
| 4 | **JobSpy** (Bunsly) | 10k+ | Scraper Python | Global boards | ⭐⭐⭐⭐☆ Motor de scraping |
| 5 | **get_jobs** (loks666) | ~5k | Auto-apply China | China (Boss/51job/智联/猎聘) | ⭐⭐⭐☆☆ Ideas de delay/spam control |
| 6 | **AutoApply AI** (Rayyan9477) | ~3k | Full stack + dashboard | Global | ⭐⭐⭐⭐☆ ATS scoring, resume tailoring |
| 7 | **JobSearch-Agent** (sreekar2858) | ~2k | LinkedIn + AI CV | Global | ⭐⭐⭐☆☆ Playwright + Gemini |
| 8 | **job-scraper** (anandanair) | ~1.5k | GitHub Actions + AI | Global | ⭐⭐⭐⭐☆ Automatización diaria cron |
| 9 | **ai-job-search-agent** (ashleysally00) | ~1k | Career pages scanner | Tech startups | ⭐⭐☆☆☆ Solo Greenhouse/Lever |
| 10 | **job-application-tracker** (christophernemala) | ~800 | Tracker + automation | Naukri Gulf | ⭐⭐⭐☆☆ Tracker web útil |

---

## 1. 🥇 career-ops (santifer) — YA TENEMOS ESTE
**URL:** https://github.com/santifer/career-ops  
**Stars:** ~45k | **Forks:** ~5k | **Licencia:** MIT  
**Idiomas:** EN, ES, PT, KO, JA, RU, ZH (8 idiomas)

**Qué hace:**
- Sistema de búsqueda de empleo multi-agente con Claude Code
- 14 modos: evaluar, PDF, batch, tracker, apply, contacto, deep research
- Dashboard en Go (Bubble Tea) con tema Catppuccin
- Scanner automático de portales (Greenhouse, Ashby, Lever, Workday)
- Generación de CVs PDF optimizados ATS
- Evaluación A-F con 10 dimensiones ponderadas

**Pros:**
- ✅ Diseñado para ser customizado por IA (Claude edita sus propios archivos)
- ✅ Múltiples idiomas incluido español
- ✅ Framework flexible, no "spray and pray"
- ✅ PDF generation con Playwright
- ✅ Batch processing con sub-agentes paralelos

**Cons:**
- ❌ Originalmente enfocado en roles tech (AI/ML)
- ❌ Portales occidentales (Greenhouse/Lever) no usados en Ecuador
- ❌ Requiere Node.js + Go + Playwright

**Veredicto para Avril:** ⭐⭐⭐⭐⭐ YA ADAPTADO. Nuestro `avril-job-system/` es un fork adaptado con:
- `profile.yml` para Marketing/Community Manager
- `portals.yml` con 52 empresas ecuatorianas
- Modo `outbound-ecuador.md` para email a PYMES
- Base de datos local SQLite con 7,876 empresas filtradas

---

## 2. 🥈 AIHawk (feder-cr) — EL MÁS FAMOSO, PERO MUERTO
**URL:** https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk  
**Stars:** 29,8k | **Forks:** 4,6k | **Licencia:** AGPL-3.0  
**Estado:** ⚠️ ARCHIVADO el 17 Mayo 2026 (read-only)

**Qué hace:**
- Auto-aplicador LinkedIn "Easy Apply"
- Generación dinámica de CVs con IA
- Respuestas personalizadas a preguntas de empleadores
- Filtrado inteligente y blacklist

**Pros:**
- ✅ El más popular del mundo (29.8k stars)
- ✅ Featured en Business Insider, TechCrunch, Wired
- ✅ CV tailoring automático por trabajo

**Cons:**
- ❌ **ARCHIVADO** — LinkedIn demandó al proyecto
- ❌ **BANEADO** — todos los contribuidores bloqueados por LinkedIn
- ❌ Solo funciona con LinkedIn Easy Apply (no existe en Ecuador)
- ❌ Licencia AGPL (copyleft fuerte)
- ❌ Selenium-based (lento, detectable)

**Veredicto para Avril:** ⭐⭐☆☆☆ NO SIRVE. Mercado ecuatoriano no usa LinkedIn Easy Apply. Además está muerto legalmente.

---

## 3. 🥉 ApplyPilot (Pickle-Pixel)
**URL:** https://github.com/Pickle-Pixel/ApplyPilot  
**Stars:** ~8k | **Licencia:** AGPL-3.0

**Qué hace:**
- Pipeline de 6 etapas: Discover → Enrich → Score → Tailor → Cover Letter → Auto-Apply
- Scrapea 5 job boards (Indeed, LinkedIn, Glassdoor, ZipRecruiter, Google Jobs)
- +48 portales Workday + 30 sitios directos
- Scoring AI 1-10 por trabajo
- Resume tailoring per-job con IA
- Claude Code navega formularios y submite

**Pros:**
- ✅ Pipeline muy bien estructurado
- ✅ Multi-board (no solo LinkedIn)
- ✅ Auto-apply real con navegación de formularios
- ✅ Scoring de fit antes de aplicar

**Cons:**
- ❌ Requiere Claude Code CLI + Chrome + Node.js
- ❌ Complejo de configurar
- ❌ Orientado a mercado anglosajón
- ❌ Licencia AGPL

**Veredicto para Avril:** ⭐⭐⭐⭐☆ IDEAS A ROBAR. El pipeline de 6 etapas es excelente. Podemos adaptar:
- La etapa "Score" para filtrar empresas de la base maestra
- La etapa "Tailor" para personalizar emails en vez de CVs
- El concepto de "Enrich" para investigar empresas antes de contactar

---

## 4. JobSpy (Bunsly / python-jobspy)
**URL:** https://github.com/Bunsly/JobSpy  
**Stars:** 10k+ | **Licencia:** MIT  
**Instalación:** `pip install -U python-jobspy`

**Qué hace:**
- Librería Python pura para scrapear empleos
- Soporta: LinkedIn, Indeed, Glassdoor, Google Jobs, ZipRecruiter, Bayt, BDJobs
- Retorna pandas DataFrame unificado
- Scrapeo concurrente

**Pros:**
- ✅ Simple: una función, un DataFrame
- ✅ MIT license (muy permisiva)
- ✅ Mantiene endpoints actualizados
- ✅ Ideal como motor de datos

**Cons:**
- ❌ LinkedIn rompe los endpoints cada pocos meses
- ❌ Requiere proxies para escala
- ❌ Sin emailing, sin apply, sin tracking

**Veredicto para Avril:** ⭐⭐⭐⭐☆ MOTOR ÚTIL. Si queremos scrapear LinkedIn/Indeed para ver qué empresas publican en Ecuador, JobSpy es el motor. Pero para PYMES ecuatorianas que no publican en boards, no sirve.

**Uso potencial:**
```python
from jobspy import scrape_jobs
jobs = scrape_jobs(
    site_name=["linkedin", "indeed"],
    search_term="community manager",
    location="Ecuador",
    results_wanted=100,
)
```

---

## 5. get_jobs (loks666) — EL GIGANTE CHINO
**URL:** https://github.com/loks666/get_jobs  
**Mirror China:** https://gitee.com/lok666/get_jobs  
**Stars:** ~5k+ | **Idioma:** Chino

**Qué hace:**
- Auto-aplicador para 4 plataformas chinas:
  - **Boss直聘** (Boss Zhipin) — el más grande de China
  - **前程无忧** (51job)
  - **猎聘** (Liepin)
  - **智联招聘** (Zhaopin)
- GUI web para configuración
- AI matching con GPT para saludos personalizados
- Envío automático de CV en imagen
- Filtro anti-spam (HR inactivos, headhunters, salario)
- Notificaciones WeChat en tiempo real
- Blacklist automático de empresas
- Cookie persistence (login semanal)

**Pros:**
- ✅ Diseñado para mercado de PYMES (Boss直聘 es 80% PYMES)
- ✅ Delay inteligente entre aplicaciones (anti-ban)
- ✅ Saludo personalizado con IA
- ✅ CV en imagen (mejor respuesta que PDF)
- ✅ Blacklist y filtrado avanzado

**Cons:**
- ❌ Solo funciona en plataformas chinas (irrelevante para Ecuador)
- ❌ Requiere JDK21 + Gradle + ChromeDriver
- ❌ Documentación solo en chino

**Veredicto para Avril:** ⭐⭐⭐☆☆ IDEAS VALIOSAS. Aunque no sirve directamente, tiene conceptos que podemos robar:
1. **Delay entre envíos** — evitar que nos marquen como spam
2. **Saludo personalizado con IA** — ya lo hacemos con generate_emails.py
3. **Blacklist automático** — marcar empresas que rechazaron para no re-contactar
4. **CV en imagen** — para WhatsApp (en Ecuador WhatsApp es king)
5. **Notificaciones** — recordar follow-ups

---

## 6. AutoApply AI (Rayyan9477)
**URL:** https://github.com/Rayyan9477/AutoApply-AI-Agentic-Browser-Automation-for-Job-Search  
**Stars:** ~3k

**Qué hace:**
- Full stack con React + FastAPI backend
- Job discovery: LinkedIn, Indeed, Glassdoor, Exa AI semantic search
- ATS Resume Scoring (multi-factor: skills, keywords, experience)
- Resume tailoring con LLM + generación PDF/DOCX
- Application tracking con lifecycle status
- Browser automation con browser-use + Playwright
- Dashboard real-time con funnel analytics
- Workers async con Redis
- Soporta 400+ modelos LLM vía LiteLLM

**Pros:**
- ✅ Arquitectura profesional (FastAPI + SQLAlchemy async)
- ✅ ATS scoring útil
- ✅ Browser-use para auto-apply
- ✅ Vector search con FAISS

**Cons:**
- ❌ Overkill para uso personal
- ❌ Requiere PostgreSQL + Redis + React stack
- ❌ Complejo de deploy

**Veredicto para Avril:** ⭐⭐⭐⭐☆ IDEAS DE ARQUITECTURA. Podemos robar:
- El sistema de ATS scoring para evaluar match con descripciones
- El tracking con estados (Applied → Interview → Offer → Rejected)
- El concepto de "semantic search" para matching

---

## 7. JobSearch-Agent (sreekar2858)
**URL:** https://github.com/sreekar2858/JobSearch-Agent  
**Stars:** ~2k

**Qué hace:**
- LinkedIn scraper con Playwright
- AI-powered CV generation (Gemini)
- Cover letter creation
- BugMeNot scraper para credenciales de sitios
- Pipeline unificado sync/async
- FastAPI server

**Pros:**
- ✅ Playwright más robusto que Selenium
- ✅ Anonimización (user agents, timezone, WebGL blocking)
- ✅ Proxy support
- ✅ Pipeline dual: CLI + API

**Cons:**
- ❌ Solo LinkedIn
- ❌ Requiere credenciales

**Veredicto para Avril:** ⭐⭐⭐☆☆ Playwright + anonimización son buenas técnicas si necesitamos scrapear.

---

## 8. job-scraper (anandanair)
**URL:** https://github.com/anandanair/job-scraper  
**Stars:** ~1.5k

**Qué hace:**
- Scrapeo de LinkedIn con GitHub Actions (cron diario)
- Resume parsing con pdfplumber + Gemini
- Job scoring: compara resume vs job description
- Universal LLM support (400+ modelos)
- Supabase para almacenamiento
- Custom PDF generation
- Quota management (rate limiting, budget tracking)

**Pros:**
- ✅ GitHub Actions = automatización gratis en la nube
- ✅ Job scoring con IA
- ✅ Quota management (no gastar de más en APIs)
- ✅ PDF generation

**Cons:**
- ❌ Requiere Supabase (cloud)
- ❌ Orientado a LinkedIn

**Veredicto para Avril:** ⭐⭐⭐⭐☆ GITUB ACTIONS ES CLAVE. Podemos usar GitHub Actions para:
- Ejecutar `generate_emails.py` semanalmente
- Re-scrapear portales de empresas ecuatorianas
- Enviar reportes por email

---

## 9. ai-job-search-agent (ashleysally00)
**URL:** https://github.com/ashleysally00/ai-job-search-agent  
**Stars:** ~1k

**Qué hace:**
- Escanea 50+ career pages diariamente
- Greenhouse: Anthropic, Figma, Airtable, Discord, Reddit
- Lever: Plaid, etc.
- Filtrado por keywords personalizables
- Reportes diarios limpios
- Export JSON + TXT

**Pros:**
- ✅ Simple y enfocado
- ✅ Daily reports
- ✅ Fácil de extender

**Cons:**
- ❌ Solo startups tech con Greenhouse/Lever
- ❌ No emailing, no apply

**Veredicto para Avril:** ⭐⭐☆☆☆ NO SIRVE. En Ecuador las PYMES no usan Greenhouse ni Lever.

---

## 10. job-application-tracker (christophernemala)
**URL:** https://github.com/christophernemala/job-application-tracker  
**Stars:** ~800

**Qué hace:**
- **Web tracker:** HTML/JS puro, funciona en cualquier navegador, sin backend
- **Automation system:** Python + Selenium + Flask + OpenAI
- Integración con Naukri Gulf
- Cover letter generation con OpenAI
- SQLite database

**Pros:**
- ✅ Web tracker gratis y sin instalar nada
- ✅ Dashboard Flask
- ✅ Dual mode: manual + automation

**Cons:**
- ❌ Automation solo para Naukri Gulf (mercado árabe)
- ❌ Selenium (detectable)

**Veredicto para Avril:** ⭐⭐⭐☆☆ TRACKER WEB ÚTIL. El tracker web podría servirnos para hacer seguimiento manual de las empresas contactadas por email.

---

## 🎯 Recomendación Estratégica para Avril

### Nuestra arquitectura actual (`avril-job-system/`) es CORRECTA

El repo **career-ops** ya es el mejor punto de partida. Lo que debemos hacer es **robar ideas selectivamente** de los otros repos:

### Ideas a implementar:

| De repo | Idea | Implementación |
|---------|------|---------------|
| **ApplyPilot** | Pipeline de 6 etapas | Adaptar para email outbound: Score → Tailor → Send → Track → Follow-up → Close |
| **get_jobs (China)** | Delay anti-spam | Añadir `time.sleep(random(30, 120))` entre envíos de email |
| **get_jobs (China)** | CV en imagen | Generar versión JPG del CV para WhatsApp |
| **get_jobs (China)** | Blacklist auto | Tabla `empresas_rechazadas` en SQLite |
| **AutoApply AI** | ATS scoring | Script que evalúa match empresa vs perfil Avril (1-10) |
| **AutoApply AI** | Tracking estados | Estados: Contactado → Respondió → Entrevista → Oferta → Rechazado |
| **job-scraper** | GitHub Actions | Workflow para ejecutar generate_emails.py semanal |
| **job-scraper** | Quota management | Trackear cuántos emails enviamos por semana |
| **JobSpy** | Motor de scraping | Si alguna empresa publica en LinkedIn/Indeed, scrapear con JobSpy |
| **job-tracker** | Dashboard web | Un HTML simple para ver estado de todas las empresas |

---

## 🔗 Links Directos

1. **career-ops** (ya clonado): `avril-job-system/`
2. **AIHawk** (muerto): https://github.com/feder-cr/Jobs_Applier_AI_Agent_AIHawk
3. **ApplyPilot**: https://github.com/Pickle-Pixel/ApplyPilot
4. **JobSpy**: https://github.com/Bunsly/JobSpy
5. **get_jobs (China)**: https://github.com/loks666/get_jobs
6. **AutoApply AI**: https://github.com/Rayyan9477/AutoApply-AI-Agentic-Browser-Automation-for-Job-Search
7. **JobSearch-Agent**: https://github.com/sreekar2858/JobSearch-Agent
8. **job-scraper**: https://github.com/anandanair/job-scraper
9. **ai-job-search-agent**: https://github.com/ashleysally00/ai-job-search-agent
10. **job-tracker**: https://github.com/christophernemala/job-application-tracker

---

## 📝 Notas sobre China

- **get_jobs** es el proyecto más relevante del mercado chino porque:
  - Boss直聘 = 80% PYMES (similar al mercado ecuatoriano)
  - Tienen los mismos problemas: spam, HR inactivos, contacto directo
  - Sus soluciones anti-spam son aplicables a nuestro email outbound
- Los otros repos chinos encontrados son principalmente **plantillas de CV** (no automatización)

---

> Documento generado automáticamente. Revisar periódicamente por nuevos repos.
