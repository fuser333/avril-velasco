# Uso de la Base de Datos para Email Campaign

## Qué se hizo

1. **Copia de la base maestra** en `../data/base_maestra_copia.db` (163 MB, sin tocar el original)
2. **Filtro limpio**: 7,876 empresas sin colegios/universidades, con email
3. **Script generador**: `generate_emails.py` — lee la base y genera emails outbound
4. **Lotes iniciales generados**:
   - `emails_pichincha_marketing.csv` — 50 empresas de marketing en Quito (con teléfono)
   - `emails_guayas_marketing.csv` — 50 empresas de marketing en Guayaquil (con teléfono)

## Cómo generar más emails

```bash
cd "Busqueda_Trabajo_Avril"

# 50 empresas de marketing en Pichincha
python3 generate_emails.py --provincia PICHINCHA --sector marketing --limite 50 --con-telefono --output batch_1.csv

# 30 empresas de audiovisual en Guayas
python3 generate_emails.py --provincia GUAYAS --sector audiovisual --limite 30 --con-telefono --output batch_2.csv

# 100 empresas de cualquier sector en Pichincha
python3 generate_emails.py --provincia PICHINCHA --sector todos --limite 100 --output batch_3.csv
```

## Opciones del script

| Opción | Valores | Default |
|---|---|---|
| `--provincia` | PICHINCHA, GUAYAS, AZUAY, etc. | PICHINCHA |
| `--sector` | marketing, audiovisual, software, telecom, ecommerce, todos | todos |
| `--limite` | Número de empresas | 50 |
| `--con-telefono` | Solo empresas con teléfono | false |
| `--output` | Nombre del archivo CSV | emails_outbound.csv |

## Estructura del CSV generado

- `#` — Número de fila
- `EMPRESA` — Nombre de la empresa
- `EMAIL` — Email de contacto (info@, gerencia@, contacto@)
- `TELEFONO` — Teléfono corporativo
- `PROVINCIA` — Provincia
- `ACTIVIDAD` — Actividad económica
- `ASUNTO` — Asunto del email
- `CUERPO_EMAIL` — Email completo listo para copiar y pegar

## Recomendación de uso

1. **Abre el CSV en Excel o Google Sheets**
2. **Revisa los emails antes de enviar** — son templates, personalízalos si conoces algo específico de la empresa
3. **Envía 5-10 por día** — no mandes 100 de golpe o caes en spam
4. **Haz follow-up** a los 5-7 días si no responden (usa la plantilla Email 2 del SKILL.md)
5. **Lleva registro** de quién respondió en una columna extra del Excel

## Datos disponibles en la base

| Sector | Empresas con email |
|---|---|
| Marketing / Publicidad / Comunicación | 5,888 |
| Telecomunicaciones | 2,209 |
| E-commerce / Internet | 1,311 |
| Audiovisual / Medios | 859 |
| Software / Tecnología | 300 |

**Por provincia:** Pichincha 3,140 · Guayas 2,675 · Azuay 432 · Manabí 260
