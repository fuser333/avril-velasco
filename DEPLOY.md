# 🚀 Deploy a Spaceship — Avril Velasco

> Info exacta del servidor. NO buscar en otros lados.

---

## 📡 Servidor

| Dato | Valor |
|---|---|
| **Dominio** | `avrilvelasco.com` |
| **Servidor** | `server26.shared.spaceship.host` |
| **IP** | `66.29.148.75` |
| **Usuario cPanel** | `nlffikeqmk` |
| **Puerto SSH** | `21098` |
| **Puerto FTP** | `21` |
| **Panel cPanel** | `https://server26.shared.spaceship.host:2083` |

---

## 🔑 SSH

```bash
ssh -p 21098 -i ~/.ssh/AvrilVelascoV1 nlffikeqmk@66.29.148.75
```

> La clave privada está en `~/Downloads/AvrilVelascoV1`.  
> Tiene passphrase — pedirla si se necesita usar SSH directo.

---

## 📤 FTP (más fácil para subir archivos)

```bash
# Usar cuenta FTP creada en cPanel → FTP Accounts
# Ejemplo:
lftp -u avrilupload@avrilvelasco.com,PASSWORD ftp://66.29.148.75
```

> **Importante:** la cuenta FTP creada en cPanel queda dentro de `/avrilupload/`  
> en el servidor real. Para poner archivos en la raíz del dominio hay que:
> 1. Crear la cuenta FTP apuntando a la raíz del dominio (dejar directorio en blanco), o
> 2. Usar un script PHP para mover archivos desde `/avrilupload/` a `/`

---

## 🌐 Estructura del sitio en producción

```
avrilvelasco.com/
├── index.html              ← Portfolio principal
├── manual-de-marca.html    ← Manual de marca
├── v2-cyberpunk.html       ← Variantes de diseño
├── v3-magazine.html
├── v4-aurora.html
├── assets/                 ← Logos e imágenes
└── subir/                  ← Uploader protegido
    ├── index.html
    └── .htaccess           ← Protegido con contraseña
```

### Acceso al uploader
- URL: `https://avrilvelasco.com/subir/`
- Usuario: `avril`
- Contraseña: `velasco2025`

---

## ⚡ Plan B: Deploy rápido sin SSH (File Manager)

Si no hay acceso SSH o el puerto no responde:

1. Entrar a cPanel: `https://server26.shared.spaceship.host:2083`
2. Abrir **File Manager** (icono carpeta amarilla)
3. Navegar a la carpeta del dominio `avrilvelasco.com/`
4. Botón **Upload** arriba
5. Arrastrar el archivo ZIP con los archivos web
6. Click derecho en el ZIP → **Extract**
7. Listo

---

## 🛠️ Comandos útiles

```bash
# Probar si un puerto SSH está abierto
nc -zv 66.29.148.75 21098

# Probar puerto FTP
nc -zv 66.29.148.75 21

# Subir archivo por FTP con curl
curl -T index.html ftp://66.29.148.75/ --user avrilupload@avrilvelasco.com:PASSWORD
```

---

## 📝 Notas

- **NO** tocar los archivos de otras empresas (imagemIA, H3L, etc.)
- Cada partner tiene su **propio cPanel** con datos independientes
- El puerto SSH es **custom** (no el 22 estándar)
- Si la clave SSH dice `not authorized` en cPanel → hacer clic en **Administrar → Autorizar**

---

*Actualizado: 2026-05-22*
