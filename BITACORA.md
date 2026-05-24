# Bitácora Avril Velasco

> **Regla de oro:** Todo lo que se haga en este proyecto se documenta aquí. Sin excepciones.

---

## 2026-05-22 — Deploy inicial del sitio web

### 🌐 Sitio web deployado a producción
- **Portfolio**: https://avrilvelasco.com/ → LIVE
- **Uploader**: https://avrilvelasco.com/subir/ → LIVE (protegido con auth)
- Servidor Spaceship: `server26.shared.spaceship.host` (IP: `66.29.148.75`)
- Puerto SSH: `21098`

### 📁 Estructura final en servidor
```
avrilvelasco.com/
├── index.html              ← Portfolio principal (v3 magazine)
├── manual-de-marca.html    ← Manual de marca interactivo
├── v2-cyberpunk.html       ← Variante de diseño
├── v3-magazine.html        ← Variante de diseño
├── v4-aurora.html          ← Variante de diseño
├── assets/                 ← Logos e imágenes
└── subir/                  ← Uploader protegido
    ├── index.html
    └── .htaccess           ← Auth básica (avril / velasco2025)
```

### 🔐 Uploader protegido
- Usuario: `avril`
- Contraseña: `velasco2025`

### 📦 Repo GitHub
- **URL**: https://github.com/fuser333/avril-velasco

### 📚 Skills y documentación
- `DEPLOY.md` — info del servidor Spaceship
- `~/.claude/skills/spaceship-deploy/SKILL.md` — skill reutilizable

---

## 2026-05-23 — Fixes móviles + Base de datos + Job System

### 📱 Fixes de versión móvil (v9-tabs.html)
- **Problema:** Hero tapado por navbar, foto blob gigante, cita negra tapaba foto del About
- **Fixes aplicados:**
  - `padding-top: 3.5rem` en `.mag-hero` para compensar navbar fijo
  - Foto blob reducida a 80x100px, animación desactivada en móvil
  - `<br>` en título ocultos en móvil (`display: none`)
  - Ubicación larga oculta en móvil
  - Cita negra reposicionada debajo de la foto (de absoluta a relativa)
  - `aspect-ratio: auto` en foto del About
  - Botón "Ver CV" en navbar reducido
- **Deploy:** 55,148 bytes verificado en producción

### 🗄️ Base de datos de empresas ecuatorianas
- **Origen:** `H3L 25/H3L26/01_Marketing_Ventas/base-datos-contactos/data/base_maestra.db` (163 MB, 249,461 empresas)
- **Copia local:** `data/base_maestra_copia.db` — SIN MODIFICAR el original
- **Filtro aplicado:** Excluir educación (colegios/universidades)
- **Resultado:** 7,876 empresas limpias con email

| Sector | Empresas |
|---|---|
| Marketing / Publicidad / Comunicación | 5,888 |
| Telecomunicaciones | 2,209 |
| E-commerce / Internet | 1,311 |
| Audiovisual / Medios | 859 |
| Software / Tecnología | 300 |

**Por provincia:** Pichincha 3,140 · Guayas 2,675 · Azuay 432

**CSV exportado:** `data/empresas_avril.csv` (3.1 MB, 7,876 filas)

### 💼 Job System — Career-Ops
- **Repo clonado:** `santifer/career-ops` (~45,000⭐ en GitHub)
- **Ruta local:** `avril-job-system/`
- **Adaptación para Avril:**
  - `config/profile.yml` — Perfil de Avril: Community Manager / Marketing Digital, Quito, USFQ, stack de diseño
  - `portals.yml` — 52 empresas: 50 de marketing en Pichincha + Cervecería Nacional + AB InBev
  - `modes/outbound-ecuador.md` — Nuevo modo para email outbound a PYMES ecuatorianas
  - `outbound_pilsener.md` — Email listo para Cervecería Nacional (Pilsener)

### 📧 Script de email outbound
- **Archivo:** `Busqueda_Trabajo_Avril/generate_emails.py`
- **Función:** Lee la base SQLite y genera emails personalizados por empresa
- **Lotes generados:**
  - `emails_pichincha_marketing.csv` — 50 empresas Quito
  - `emails_guayas_marketing.csv` — 50 empresas Guayaquil

### 🔍 Repositorios de job search evaluados (Top 5)

| # | Repo | Stars | Enfoque |
|---|------|-------|---------|
| 1 | **santifer/career-ops** | ~45k | AI evaluation + PDF + portal scanner + dashboard TUI |
| 2 | JobSync | ~3k | Tracker + AI resume review + job matching |
| 3 | JustAJobApp | ~2k | Gmail auto-parse + dashboard |
| 4 | Ioannis-D/Job-Application-Tracker | ~1k | AI agent para discovery |
| 5 | Claude Cowork plugin | ~500 | 9 AI skills para job seekers |

**Veredicto:** Ninguno sirve out-of-the-box para marketing digital en Ecuador. Todos son para tech/AI jobs con portales formales. La solución fue adaptar `career-ops` para email outbound a PYMES ecuatorianas.

### 📁 Archivos nuevos creados hoy
```
Avril Velasco/
├── data/
│   ├── base_maestra_copia.db      ← Copia de la base (163 MB)
│   └── empresas_avril.csv         ← 7,876 empresas filtradas (3.1 MB)
├── avril-job-system/              ← Career-Ops adaptado
│   ├── config/profile.yml         ← Perfil de Avril
│   ├── portals.yml                ← 52 empresas ecuatorianas
│   ├── modes/outbound-ecuador.md  ← Modo email outbound
│   └── outbound_pilsener.md       ← Email listo para Pilsener
├── Busqueda_Trabajo_Avril/
│   ├── generate_emails.py         ← Script generador de emails
│   ├── emails_pichincha_marketing.csv
│   ├── emails_guayas_marketing.csv
│   └── USO_BASE_DATOS.md          ← Instrucciones
└── ESTO/README.md                 ← Documento maestro del proyecto
```

---

## ⏰ Timeline

| Fecha | Hora | Qué se hizo |
|-------|------|-------------|
| 2026-05-22 | 03:00 AM | Deploy inicial del sitio web |
| 2026-05-23 | Todo el día | Fixes móviles + Base de datos + Job system |
| 2026-05-24 | 01:26 AM | Clonado career-ops + configuración completa |

---

*Documentar todo. Sin excepciones.*

---

## 2026-05-14 02:50 — Búsqueda Top 10 Repositorios Job Search (Global + China)

### Contexto
Usuario pidió re-hacer la búsqueda de los mejores repositorios para búsqueda de empleo, incluyendo China y otros mercados, con acceso a búsquedas globales.

### Búsquedas realizadas
1. `site:github.com job search automation AI stars:>1000` — repos globales
2. `site:github.com "AIHawk" OR "ApplyPilot" OR "jobspy"` — repos específicos
3. `site:gitee.com OR site:github.com 求职 招聘 找工作` — repos chinos
4. `site:github.com "job tracker" OR "application tracker"` — trackers
5. `site:github.com santifer career-ops` — verificar estado del repo actual

### Resultados: Top 10 Repositorios

| # | Repo | Stars | Estado | Relevancia Avril |
|---|------|-------|--------|-----------------|
| 1 | **career-ops** (santifer) | ~45k | ✅ Activo | YA ADAPTADO |
| 2 | **AIHawk** (feder-cr) | 29.8k | ⚠️ ARCHIVADO mayo 2026 | No sirve (LinkedIn baneado) |
| 3 | **ApplyPilot** (Pickle-Pixel) | ~8k | ✅ Activo | Robar ideas pipeline |
| 4 | **JobSpy** (Bunsly) | 10k+ | ✅ Activo | Motor scraping útil |
| 5 | **get_jobs** (loks666) China | ~5k | ✅ Activo | Ideas anti-spam + WhatsApp |
| 6 | **AutoApply AI** (Rayyan9477) | ~3k | ✅ Activo | Ideas ATS scoring + tracking |
| 7 | **JobSearch-Agent** (sreekar2858) | ~2k | ✅ Activo | Playwright + anonimización |
| 8 | **job-scraper** (anandanair) | ~1.5k | ✅ Activo | GitHub Actions automation |
| 9 | **ai-job-search-agent** (ashleysally00) | ~1k | ✅ Activo | No sirve (solo Greenhouse) |
| 10 | **job-tracker** (christophernemala) | ~800 | ✅ Activo | Tracker web manual útil |

### Hallazgos clave

1. **AIHawk está MUERTO** — LinkedIn demandó al proyecto, todos los contribuidores baneados, repo archivado el 17 mayo 2026. Confirmamos que career-ops era la elección correcta.

2. **China: get_jobs es el más relevante** — Aunque sus plataformas son chinas (Boss直聘, 51job, 智联招聘, 猎聘), sus soluciones son aplicables a Ecuador:
   - Delay anti-spam entre aplicaciones
   - CV en imagen para WhatsApp (en Ecuador WhatsApp es king)
   - Blacklist automático de empresas que rechazaron
   - Saludo personalizado con IA
   - Notificaciones en tiempo real

3. **JobSpy es el mejor motor de scraping** — Si alguna empresa ecuatoriana publica en LinkedIn/Indeed, JobSpy (`pip install python-jobspy`) es la librería más mantenida.

4. **ApplyPilot tiene el mejor pipeline** — 6 etapas: Discover → Enrich → Score → Tailor → Cover → Auto-Apply. Adaptable a nuestro flujo de email outbound.

5. **job-scraper (anandanair)** — GitHub Actions para automatización diaria. Podemos usar esto para ejecutar `generate_emails.py` semanalmente.

### Documento generado
- `ESTO/top10_job_repos.md` — 381 líneas, análisis completo comparativo

### Acciones a futuro (añadidas a PENDIENTES.md)
- Implementar delay anti-spam entre envíos de email
- Crear tabla `empresas_rechazadas` en SQLite (blacklist)
- Generar versión JPG del CV para WhatsApp
- Crear script de ATS scoring (match 1-10 empresa vs perfil)
- Configurar GitHub Actions para ejecutar generate_emails.py semanal
- Crear dashboard HTML simple para tracking de estados
