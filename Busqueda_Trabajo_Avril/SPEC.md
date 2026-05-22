# SPEC — Sistema de Búsqueda de Trabajo Avril Velasco

## Visión

Un sistema semi-automatizado que multiplique la efectividad de búsqueda de empleo de Avril mediante:
- Personalización masiva de outreach (LinkedIn + Email)
- Optimización de CV por vacante
- Preparación estructurada de entrevistas
- Tracking y aprendizaje continuo

## Alcance

### Incluye
- Generación de mensajes personalizados para LinkedIn
- Generación de emails outbound a empresas objetivo
- Adaptación de CV por rol/empresa
- Generación de preguntas y respuestas modelo para entrevistas
- Sistema de tracking de métricas

### Excluye
- Automatización de envío (todo requiere aprobación humana)
- Scraping automatizado de job boards (por ahora)
- CRM completo (usar Google Sheets/Notion)

## Stack Tecnológico

| Componente | Herramienta |
|------------|-------------|
| Generación de contenido | Claude Code (este skill) |
| Tracking | Google Sheets o Notion |
| CV editable | Canva / Google Docs |
| Email | Gmail personal |
| LinkedIn | Perfil profesional |
| Portafolio | `web/index.html` existente |

## Flujos Principales

### Flujo 1: LinkedIn Outreach
1. Identificar empresa objetivo y reclutador
2. Investigar perfil del reclutador (rol, posts recientes)
3. Generar mensaje personalizado usando skill 01
4. Revisión humana por Avril
5. Envío manual
6. Registro en tracking

### Flujo 2: Email Outbound
1. Identificar empresa objetivo y contacto directo
2. Investigar empresa (web, noticias, cultura)
3. Generar email personalizado usando skill 02
4. Revisión humana por Avril
5. Envío manual
6. Seguimiento en 5-7 días si no responde

### Flujo 3: CV Adaptativo
1. Recibir job description de vacante
2. Analizar keywords y requisitos
3. Adaptar CV destacando experiencias relevantes
4. Generar versión optimizada
5. Revisión humana por Avril

### Flujo 4: Interview Prep
1. Recibir información de entrevista (empresa, rol, formato)
2. Generar preguntas técnicas y comportamentales
3. Generar respuestas modelo basadas en experiencia de Avril
4. Generar preguntas para hacer al entrevistador
5. Simular mock interview

## Estrategia de Contenido

### Pitch Principal de Avril
> "Marketing digital con experiencia real en comercio internacional (Ecuador/Colombia/USA). Especialista en branding visual, comunidades online y contenido que convierte. Bilingüe, herramientas modernas, mentalidad de crecimiento."

### Verticales Target
1. **Marketing Digital** — Agencias, startups, e-commerce
2. **Community Management** — Marcas con presencia social activa
3. **Branding / Diseño** — Empresas que necesitan identidad visual
4. **Comercio Exterior** — Exportadoras, trading companies

### Empresas Objetivo (Plantilla)
- [ ] Empresa 1: ___ | Sector: ___ | Contacto: ___ | Canal: ___
- [ ] Empresa 2: ___ | Sector: ___ | Contacto: ___ | Canal: ___
- [ ] Empresa 3: ___ | Sector: ___ | Contacto: ___ | Canal: ___

## Criterios de Éxito

- 10+ outreach enviados por semana
- 20%+ tasa de respuesta
- 3+ entrevistas en 30 días
- 1+ oferta formal en 60 días

## Riesgos y Mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Mensajes demasiado genéricos | Skill de auditoría IA + revisión humana obligatoria |
| Burnout de Avril | Sistema de tracking visual, celebrar pequeñas victorias |
| Mercado saturado | Diferenciación por nicho (bilingüe + comercio internacional + diseño) |
| Falta de experiencia "sénior" | Enfocar en potencial de crecimiento, actitud y stack de herramientas |
