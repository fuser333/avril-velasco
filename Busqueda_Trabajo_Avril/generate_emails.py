#!/usr/bin/env python3
"""
Generador de emails outbound para Avril Velasco.
Lee la base de datos SQLite y genera emails personalizados por empresa.
Uso: python3 generate_emails.py --provincia PICHINCHA --limite 50 --output emails_pichincha.csv
"""

import sqlite3
import csv
import argparse
import random
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "base_maestra_copia.db")

ASUNTOS = [
    "{empresa} + marketing internacional — una idea rápida",
    "Community manager bilingüe para {empresa}",
    "¿Buscan alguien para contenido multi-país?",
    "Marketing digital + diseño — Propuesta para {empresa}",
    "Vi {empresa} y pensé en una colaboración",
]

PLANTILLA_EMAIL = """Hola equipo de {empresa},

Vi que {empresa} trabaja en {sector_breve}. Hace 6 meses gestioné el lanzamiento de contenido para Growix SA en Ecuador, Colombia y USA, aumentando el engagement 40% en 3 meses.

Soy Avril Velasco, estudio Negocios Internacionales en la USFQ y manejo el stack completo de diseño (Photoshop, Illustrator, Canva, CapCut) + Meta Business Suite. Mi perfil bilingüe (español/inglés B2) me permite crear campañas que conectan en mercados latinos y anglosajones.

¿Tienen 15 min esta semana para conversar sobre cómo podría aportar al equipo de marketing?

Saludos,

Avril Velasco
Marketing Digital & Comercio Internacional
📧 avrilvelasco@gmail.com | 📱 +593 999568215
💼 linkedin.com/in/avrilvelasco
🌐 https://avrilvelasco.com
"""

def sector_breve(actividad):
    """Extrae una descripción corta del sector para personalizar el email."""
    act = actividad.lower()
    if "publicidad" in act or "marketing" in act:
        return "publicidad y marketing"
    elif "audiovisual" in act or "cinematografica" in act or "television" in act or "video" in act:
        return "producción audiovisual"
    elif "software" in act or "informatica" in act or "tecnologia" in act:
        return "tecnología y software"
    elif "telecomunicacion" in act:
        return "telecomunicaciones"
    elif "internet" in act or "electronico" in act:
        return "e-commerce y digital"
    else:
        return "comunicación y marketing"

def generar_email(empresa, actividad):
    sector = sector_breve(actividad)
    asunto = random.choice(ASUNTOS).format(empresa=empresa.split(" ")[0] if len(empresa.split(" ")) > 0 else empresa)
    cuerpo = PLANTILLA_EMAIL.format(empresa=empresa, sector_breve=sector)
    return asunto, cuerpo

def main():
    parser = argparse.ArgumentParser(description="Genera emails outbound para Avril")
    parser.add_argument("--provincia", default="PICHINCHA", help="Provincia a filtrar (default: PICHINCHA)")
    parser.add_argument("--sector", choices=["marketing", "audiovisual", "software", "telecom", "ecommerce", "todos"], default="todos", help="Sector a filtrar")
    parser.add_argument("--limite", type=int, default=50, help="Número máximo de emails a generar (default: 50)")
    parser.add_argument("--output", default="emails_outbound.csv", help="Archivo de salida CSV")
    parser.add_argument("--con-telefono", action="store_true", help="Solo empresas con teléfono")
    args = parser.parse_args()

    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    # Construir query
    conditions = ["provincia = ?"]
    params = [args.provincia.upper()]

    if args.sector != "todos":
        sector_map = {
            "marketing": "(LOWER(actividad) LIKE '%publicidad%' OR LOWER(actividad) LIKE '%marketing%' OR LOWER(actividad) LIKE '%comunicaci%' OR LOWER(actividad) LIKE '%relaciones publicas%')",
            "audiovisual": "(LOWER(actividad) LIKE '%audiovisual%' OR LOWER(actividad) LIKE '%cinematografica%' OR LOWER(actividad) LIKE '%television%' OR LOWER(actividad) LIKE '%video%' OR LOWER(actividad) LIKE '%radiodifusion%')",
            "software": "(LOWER(actividad) LIKE '%software%' OR LOWER(actividad) LIKE '%informatica%' OR LOWER(actividad) LIKE '%tecnologia%')",
            "telecom": "(LOWER(actividad) LIKE '%telecomunicacion%' OR LOWER(actividad) LIKE '%telefonia movil%' OR LOWER(actividad) LIKE '%radio busqueda%')",
            "ecommerce": "(LOWER(actividad) LIKE '%internet%' OR LOWER(actividad) LIKE '%electronico%' OR LOWER(actividad) LIKE '%venta a distancia%')",
        }
        conditions.append(sector_map[args.sector])

    if args.con_telefono:
        conditions.append("COALESCE(telefono,'') != ''")

    where_clause = " AND ".join(conditions)
    query = f"SELECT * FROM empresas_avril_limpia WHERE {where_clause} ORDER BY RANDOM() LIMIT ?"
    params.append(args.limite)

    cur.execute(query, params)
    rows = cur.fetchall()

    if not rows:
        print(f"❌ No se encontraron empresas con los filtros: provincia={args.provincia}, sector={args.sector}")
        db.close()
        return

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.output)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["#", "EMPRESA", "EMAIL", "TELEFONO", "PROVINCIA", "ACTIVIDAD", "ASUNTO", "CUERPO_EMAIL"])
        for i, row in enumerate(rows, 1):
            email = row["email_info"] or row["email_gerencia"] or row["email_contacto"] or ""
            asunto, cuerpo = generar_email(row["nombre"], row["actividad"])
            writer.writerow([
                i,
                row["nombre"],
                email,
                row["telefono"] or "",
                row["provincia"],
                row["actividad"][:100] + "..." if len(row["actividad"]) > 100 else row["actividad"],
                asunto,
                cuerpo,
            ])

    print(f"✅ {len(rows)} emails generados en: {output_path}")
    print(f"📍 Provincia: {args.provincia}")
    print(f"🏢 Sector: {args.sector}")
    print(f"📧 Con teléfono: {'Sí' if args.con_telefono else 'No (cualquiera)'}")
    db.close()

if __name__ == "__main__":
    main()
