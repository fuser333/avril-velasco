# Bitácora Avril Velasco — 2026-05-22

> Son las 3:00 AM. Deploy completado. Todo online.

---

## ✅ Hecho hoy

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
- Para que Avril suba fotos, videos y links de Canva/TikTok

### 📦 Repo GitHub creado
- **URL**: https://github.com/fuser333/avril-velasco
- Privado, 46 archivos versionados

### 📚 Skills y documentación creada
- `DEPLOY.md` — info exacta del servidor de Spaceship
- `~/.claude/skills/spaceship-deploy/SKILL.md` — skill reutilizable para cualquier deploy a Spaceship

---

## 🔧 Proceso de deploy (para recordar)

1. SSH puerto 22 bloqueado desde nuestra red → usamos puerto custom `21098`
2. Clave SSH `AvrilVelascoV1` tenía passphrase desconocida → no usamos SSH
3. Creamos cuenta FTP `avrilupload@avrilvelasco.com` en cPanel
4. Subimos archivos por FTP pero quedaron dentro de `/avrilupload/`
5. Usamos script PHP auto-destructivo para mover archivos a la raíz del dominio
6. Creamos `/subir/` con uploader y protección `.htaccess` + `.htpasswd`

---

## ⏰ Hora de deploy final
03:00 AM (UTC-5)

---

*Todo funcionando. A dormir.*
