# 📋 ESTO — Documento Maestro Avril Velasco

> Toda la información importante en un solo lugar. Siempre leer ESTO primero.

---

## 🌐 Sitio Web

| Dato | Valor |
|---|---|
| **Dominio** | `avrilvelasco.com` |
| **Servidor** | `server26.shared.spaceship.host` |
| **IP** | `66.29.148.75` |
| **Panel cPanel** | `https://server26.shared.spaceship.host:2083` |
| **Usuario cPanel** | `nlffikeqmk` |
| **Puerto SSH** | `21098` (custom, no el 22) |
| **Puerto FTP** | `21` |

### FTP (para subir archivos)

| Dato | Valor |
|---|---|
| **Servidor** | `avrilvelasco.com` |
| **Usuario** | `avrilupload@avrilvelasco.com` |
| **Password** | `wuncud-bafhog-5vawrU` |

> ⚠️ **IMPORTANTE:** El usuario DEBE ser `avrilupload@avrilvelasco.com` (con @dominio). Solo `avrilupload` sin @dominio da error 530.

> ⚠️ Los archivos suben a `/avrilupload/` pero el dominio sirve desde `/avrilvelasco.com/`. Después de subir, usar el script PHP `mover.php` para mover archivos a la raíz.

### Estructura del sitio en producción

```
avrilvelasco.com/
├── index.html              ← Portfolio principal (v9-tabs)
├── v8-hero.html            ← Página CV
├── assets/
│   ├── avril-foto-cv.png
│   └── hoja-de-vida-avril.pdf
└── .htaccess
```

### Deploy rápido

```bash
# Conectar FTP
lftp -u 'avrilupload@avrilvelasco.com,wuncud-bafhog-5vawrU' avrilvelasco.com

# O con Python
python3 -c "
from ftplib import FTP
ftp = FTP('avrilvelasco.com')
ftp.login('avrilupload@avrilvelasco.com', 'wuncud-bafhog-5vawrU')
# ... upload files
ftp.quit()
"
```

### Script PHP mover (copiar de /avrilupload/ a raíz)

Subir `mover.php` a `/avrilupload/` y ejecutar `https://avrilvelasco.com/avrilupload/mover.php`:

```php
<?php
$here = __DIR__;
$parent = dirname($here);

function rcopy($src, $dst) {
    if (is_dir($src)) {
        if (!is_dir($dst)) mkdir($dst, 0755, true);
        foreach (scandir($src) as $f) {
            if ($f == "." || $f == "..") continue;
            rcopy("$src/$f", "$dst/$f");
        }
    } else {
        copy($src, $dst);
    }
}

foreach (["index.html", "v8-hero.html", ".htaccess"] as $f) {
    $s = "$here/$f"; $d = "$parent/$f";
    if (file_exists($s)) { copy($s, $d); echo "Copied: $f\n"; }
}

if (is_dir("$here/assets")) {
    rcopy("$here/assets", "$parent/assets");
    echo "Copied: assets/\n";
}

unlink(__FILE__);
echo "DONE\n";
```

---

## 📁 Repo GitHub

| Dato | Valor |
|---|---|
| **Repo** | `fuser333/avril-velasco` |
| **URL** | https://github.com/fuser333/avril-velasco |
| **Branch main** | Portfolio web + job-system |
| **Branch gh-pages** | GitHub Pages backup |
| **GitHub Pages** | https://fuser333.github.io/avril-velasco/ |

### Secrets configurados

| Secret | Estado |
|---|---|
| `FTP_USER` | ✅ Configurado (pero caducado) |
| `FTP_PASS` | ✅ Configurado (pero caducado) |

> Los secrets de GitHub Actions usan un password viejo. Para usar deploy automático, actualizar secrets en GitHub → Settings → Secrets and variables → Actions.

---

## 🔍 Job System (career-ops)

| Dato | Valor |
|---|---|
| **Origen** | Fork de `santifer/career-ops` |
| **Propósito** | Pipeline de búsqueda de trabajo automatizado |
| **Archivo empresas** | `portals.yml` (27 empresas rastreadas) |
| **Roles objetivo** | Community Manager, Marketing Digital, Brand Manager |
| **Ubicaciones** | Ecuador, Colombia, Perú, México, Argentina, Chile, Remote LATAM |

### Empresas rastreadas principales

- **Ecuador:** Cervecería Nacional, Grupo El Comercio, Banco Pichincha, Banco Guayaquil, Tonicorp, Telefónica, Claro, Coral, Megamaxi
- **Tech LATAM:** Rappi, Mercado Libre, Nubank, Kavak, Cornershop
- **Agencias:** Publicis, DDB, Wunderman Thompson, Ogilvy, Havas
- **Portales:** LinkedIn, Indeed, Computrabajo, Multiocupas, Un Mejor Empleo, Glassdoor

---

## 🔐 Credenciales locales

Guardadas en archivo `.ftp_credentials` (en `.gitignore`, nunca subir al repo):

```
avrilupload@avrilvelasco.com:wuncud-bafhog-5vawrU
```

### Otras credenciales guardadas en el sistema

| Servicio | Ubicación |
|---|---|
| **Spaceship API (dev)** | `~/Mis Empresas/ITSEIA/.secrets/spaceship_api.json` |
| **GitHub token** | `git credential fill` (no se guarda en repo) |
| **SSH Key** | `~/Downloads/AvrilVelascoV1` (tiene passphrase) |
| **Uploader web** | `https://avrilvelasco.com/subir/` → `avril` / `velasco2025` |

---

## 🚨 Problemas conocidos

1. **IP bloqueada por firewall** → Usar Tor (`torify lftp`) o cambiar de red
2. **FTP requiere @dominio** → `avrilupload@avrilvelasco.com`, no solo `avrilupload`
3. **Archivos quedan en /avrilupload/** → Siempre usar `mover.php` después de subir
4. **LiteSpeed cache agresivo** → Borrar y re-subir archivos para invalidar caché
5. **Puerto SSH es custom** → `21098`, no el 22 estándar

---

## 📞 Contacto / Quién es quién

| Persona | Rol |
|---|---|
| **Avril Velasco** | Dueña del sitio, Community Manager / Marketing Digital |
| **Hector Velasco** | Desarrollador, admin del proyecto |

---

*Última actualización: 2026-05-23*
*Deploy más reciente: v9-tabs mobile fix*
