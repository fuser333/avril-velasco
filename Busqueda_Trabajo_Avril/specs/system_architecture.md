# System Architecture — Sistema de Búsqueda de Trabajo

## Arquitectura General

```
┌─────────────────────────────────────────────────────────────┐
│                    USUARIO (Avril)                          │
└──────────────┬──────────────────────────────┬───────────────┘
               │                              │
    ┌──────────▼──────────┐      ┌───────────▼────────────┐
    │  INPUT: Empresa/    │      │  INPUT: Vacante/       │
    │  Reclutador/Rol     │      │  Job Description       │
    └──────────┬──────────┘      └───────────┬────────────┘
               │                              │
    ┌──────────▼──────────┐      ┌───────────▼────────────┐
    │  SKILL: LinkedIn    │      │  SKILL: CV Optimizer   │
    │  Outreach           │      │                        │
    └──────────┬──────────┘      └───────────┬────────────┘
               │                              │
    ┌──────────▼──────────┐      ┌───────────▼────────────┐
    │  SKILL: Email       │      │  SKILL: Interview Prep │
    │  Campaign           │      │                        │
    └──────────┬──────────┘      └───────────┬────────────┘
               │                              │
               └──────────────┬───────────────┘
                              │
                    ┌─────────▼──────────┐
                    │  OUTPUT: Contenido │
                    │  Personalizado     │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  QA HUMANO (Avril) │
                    │  Revisión y Edición│
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  ENVÍO MANUAL      │
                    │  LinkedIn / Email  │
                    └─────────┬──────────┘
                              │
                    ┌─────────▼──────────┐
                    │  TRACKING          │
                    │  Google Sheets     │
                    └────────────────────┘
```

## Componentes

### 1. Motor de Generación (Claude Code)
- Recibe contexto de empresa/reclutador/vacante
- Aplica reglas de la skill correspondiente
- Genera contenido personalizado
- Itera hasta cumplir criterios de calidad

### 2. Banco de Datos (Specs)
- `user_persona_avril.md` — Perfil y experiencia
- `market_context.md` — Inteligencia de mercado
- Plantillas reutilizables en `templates/`

### 3. Skills Especializadas
- `01_linkedin_outreach/` — Mensajes de conexión
- `02_email_campaign/` — Secuencias de email
- `03_cv_optimizer/` — Adaptación de CV
- `04_interview_prep/` — Preguntas y respuestas

### 4. QA Humano
- Avril revisa cada pieza antes de enviar
- Puede editar directamente o pedir re-generación
- Aprobación final = envío

### 5. Tracking
- Google Sheets con columnas:
  - Fecha | Empresa | Contacto | Canal | Mensaje | Estado | Respuesta | Notas

## Flujo de Datos

1. **Input:** Avril proporciona empresa, rol o job description
2. **Context Loading:** Skill carga specs relevantes
3. **Generation:** Claude genera contenido personalizado
4. **Review:** Avril revisa y aprueba/rechaza
5. **Send:** Envío manual por Avril
6. **Track:** Registro en spreadsheet
7. **Learn:** Feedback alimenta mejora de futuras generaciones

## Integraciones Externas

| Servicio | Uso | Método |
|----------|-----|--------|
| LinkedIn | Outreach | Manual (Avril copia y pega) |
| Gmail | Email outbound | Manual (Avril envía) |
| Google Sheets | Tracking | Manual (Avril actualiza) |
| Canva | CV editable | Avril edita directamente |
| Portafolio Web | Referencia | `web/index.html` existente |

## No-Go (Lo que NO hace el sistema)

- No envía automáticamente mensajes
- No hace scraping de LinkedIn
- No accede a bases de datos de candidatos
- No sustituye el juicio humano de Avril
