# Modo: outbound-ecuador — Email Campaign a Empresas Ecuatorianas

## Propósito

Enviar emails outbound personalizados a empresas de marketing/publicidad/audiovisual en Ecuador usando la base de datos del SRI enriquecida con emails.

## Diferencia con el modo `scan` original

- **scan**: Busca ofertas en portales de carreras (Greenhouse, Ashby, Lever) de empresas grandes tech
- **outbound-ecuador**: Genera emails de outreach a PYMES ecuatorianas que NO tienen portales de carreras formales

## Input

1. `config/profile.yml` — perfil de Avril Velasco
2. `portals.yml` — lista de empresas ecuatorianas con email
3. Base de datos: `../data/base_maestra_copia.db` — 7,876 empresas filtradas

## Output

CSV con: empresa, email, teléfono, asunto, cuerpo del email listo para enviar.

## Ejecución

```bash
# Generar lote de 50 emails para empresas de marketing en Pichincha
python3 ../Busqueda_Trabajo_Avril/generate_emails.py \
  --provincia PICHINCHA \
  --sector marketing \
  --limite 50 \
  --con-telefono \
  --output batch_pichincha_$(date +%Y%m%d).csv

# Revisar antes de enviar
cat batch_pichincha_20260524.csv | head -5
```

## Estrategia de seguimiento

| Día | Acción |
|-----|--------|
| 0 | Email inicial (usar template de `templates/email_outbound.md`) |
| 5-7 | Follow-up si no responde |
| 14 | Break-up email si no responde |

## Reglas

1. **Máximo 10 emails por día** — evitar spam
2. **Personalizar el asunto** con el nombre de la empresa
3. **Mencionar algo específico** de la empresa si es posible
4. **CTA claro**: 15 min de call o envío de CV
5. **Llevar tracker** de quién respondió
