# Skill: Búsqueda de Trabajo para Avril Velasco

## Propósito

Sistema completo de búsqueda de empleo multi-canal para Avril Velasco (22 años, Quito, Negocios Internacionales USFQ, Marketing Digital). Este skill orquesta estrategias de LinkedIn, email outbound, optimización de CV, preparación de entrevistas y seguimiento — todo automatizado y medido.

## Contexto de Avril

- **Nombre:** Avril Velasco
- **Edad:** 22 años
- **Ubicación:** Quito, Ecuador
- **Formación:** Negocios Internacionales (USFQ)
- **Experiencia:** Community Manager / Marketing Digital en Growix SA
- **Skills:** Photoshop, Illustrator, Canva, CapCut, AutoCAD, inglés B2
- **Contacto:** avrilvelasco@gmail.com, 0999568215
- **Objetivo:** Posiciones en marketing digital, branding, community management, relaciones internacionales

## Metodología Híbrida Definitiva — 5 Fases

### Fase 0: Inteligencia de Mercado y Benchmark

Antes de escribir código o lanzar campañas:

1. **Investigación de fricciones reales:** ¿Qué problemas tienen las empresas ecuatorianas en marketing digital? ¿Qué skills faltan?
2. **Análisis de competidores laborales:** ¿Qué perfiles similares a Avril están consiguiendo trabajo? ¿En qué empresas? ¿Con qué salarios?
3. **Framework Grand Slam:** Empaquetar la oferta de valor de Avril de forma innegable.

> **Regla de oro:** Documentar TODO en `specs/market_context.md` antes de avanzar.

### Fase 1: Planificación Estricta (Spec-Driven Development)

4. **Diálogo de Contexto de Negocio:** Definir con precisión qué busca Avril (remoto/híbrido/presencial, industria, rango salarial, crecimiento profesional).
5. **Índice de Tareas Atómicas:** Descomponer en tareas pequeñas e independientes.
6. **Despliegue de SpecKit:** Centralizar documentación en `/specs/`.
   - `market_context.md` — Investigación de mercado
   - `system_architecture.md` — Stack tecnológico y flujos
   - `design_system.md` — Estética y tono de comunicación
   - `user_persona_avril.md` — Perfil detallado y objetivos

### Fase 2: Reglas Operativas (Skills)

7. **Skills reutilizables:** Cada canal de búsqueda tiene su propio skill:
   - `skills/01_linkedin_outreach/` — Estrategia de contacto en LinkedIn
   - `skills/02_email_campaign/` — Campañas de email outbound
   - `skills/03_cv_optimizer/` — Optimización de CV y portafolio
   - `skills/04_interview_prep/` — Preparación de entrevistas
8. **Condición de Parada:** Cada skill define qué significa "listo" (ej: "10 conexiones LinkedIn enviadas", "5 emails personalizados enviados").

### Fase 3: Ejecución Agéntica

9. **Comando `/goal`:** Ejecutar objetivos apuntando a specs y skills.
   - Ejemplo: `/goal Genera 5 mensajes de LinkedIn personalizados para reclutadores de marketing digital en Quito, aplicando las reglas de la skill 01_linkedin_outreach y el perfil de Avril.`
10. **Recursividad y Autocorrección:** El agente itera hasta cumplir la condición de parada.
11. **Agentes en Paralelo:** Múltiples skills pueden ejecutarse simultáneamente.

### Fase 4: Auditoría y QA Automatizado

12. **IA Revisando a la IA:** Un agente auditor revisa la calidad de los mensajes, emails y CVs generados.
13. **Tests de Calidad:** Verificar que los mensajes sean personalizados, no genéricos.
14. **Validación Visual:** Revisar que el CV y portafolio se vean profesionales.

### Fase 5: QA Humano

15. **Inventario de Discrepancias:** Lista de verificación manual antes de enviar.
16. **Prueba con Muestras Reales:** Avril revisa cada mensaje/email antes de enviar.
17. **Refinamiento Estratégico:** Ajustar el tono, el pitch y el targeting semanalmente.

## Estructura de Archivos

```
Busqueda_Trabajo_Avril/
├── SKILL.md                 # Este archivo — manual operativo maestro
├── README.md                # Descripción del proyecto
├── SPEC.md                  # Especificaciones técnicas
├── PLAN.md                  # Plan de implementación
├── specs/
│   ├── market_context.md
│   ├── system_architecture.md
│   ├── design_system.md
│   └── user_persona_avril.md
├── skills/
│   ├── 01_linkedin_outreach/SKILL.md
│   ├── 02_email_campaign/SKILL.md
│   ├── 03_cv_optimizer/SKILL.md
│   └── 04_interview_prep/SKILL.md
├── templates/
│   ├── email_outbound.md
│   ├── linkedin_message.md
│   ├── cv_template.md
│   └── elevator_pitch.md
└── src/
    └── (código Python/scripts)
```

## Reglas de Oro

1. **Nunca enviar sin aprobación de Avril.** Todo mensaje/email/CV pasa por revisión humana antes de envío.
2. **Personalización > Volumen.** Es mejor 5 mensajes ultra-personalizados que 50 genéricos.
3. **Métricas semanales.** Trackear: conexiones enviadas, respuestas recibidas, entrevistas agendadas, ofertas recibidas.
4. **Iteración constante.** Lo que no funciona esta semana se ajusta la próxima.
5. **Documentar aprendizajes.** Cada interacción, rechazo o éxito se registra para mejorar.

## Cómo Usar Este Skill

### Para Generar un Mensaje de LinkedIn
```
/goal Usando la skill 01_linkedin_outreach y el perfil de Avril en specs/user_persona_avril.md, genera un mensaje de conexión personalizado para [NOMBRE_RECLUTADOR] de [EMPRESA] que busca [ROL].
```

### Para Generar un Email Outbound
```
/goal Usando la skill 02_email_campaign, genera un email de outreach para [EMPRESA] dirigido a [PUESTO] destacando la experiencia de Avril en Growix SA y su stack de herramientas.
```

### Para Optimizar el CV
```
/goal Usando la skill 03_cv_optimizer, adapta el CV de Avril para la vacante de [ROL] en [EMPRESA], enfatizando las skills relevantes del job description.
```

### Para Preparar Entrevista
```
/goal Usando la skill 04_interview_prep, genera 10 preguntas técnicas y 5 comportamentales para una entrevista de [ROL] en [EMPRESA], con respuestas modelo basadas en el perfil de Avril.
```

## Próximos Pasos Inmediatos

1. Completar `specs/user_persona_avril.md` con datos precisos
2. Investigar 10 empresas objetivo en Quito/GYE para marketing digital
3. Generar plantillas base para cada canal
4. Configurar sistema de tracking (Google Sheets o Notion)
5. Lanzar primera oleada de outreach (semilla)
