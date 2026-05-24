# Pendientes Avril Velasco — Para continuar mañana

---

## 🚨 URGENTES (hacer primero)

### 1. Enviar link del uploader a Avril
- **URL**: https://avrilvelasco.com/subir/
- **Usuario**: `avril`
- **Contraseña**: `velasco2025`
- Pedirle que suba: fotos, videos, links de Canva, links de TikTok
- Sin esto el portfolio sigue con placeholders

### 2. Revisar que Avril pueda entrar al uploader
- Probar desde su celular y computadora
- Si tiene problemas con la contraseña, revisar `.htpasswd`

### 3. Rotar contraseña del FTP temporal
- La cuenta `avrilupload@avrilvelasco.com` todavía existe en cPanel
- Cambiar la contraseña o borrar la cuenta si ya no se necesita

---

## 📸 CONTENIDO (cuando Avril suba archivos)

### 4. Reemplazar placeholders del portfolio
- Actualizar `web/index.html` con fotos reales de Avril
- Actualizar galería de proyectos con trabajos reales
- Agregar videos de TikTok / Reels si los sube

### 5. Crear página de proyectos individuales
- Cada proyecto del portfolio debería tener su propia página
- Ej: `/proyectos/growix-social-media.html`

### 6. Subir logo real de Growix SA
- Reemplazar placeholder en sección de experiencia

---

## 🎨 DISEÑO Y MEJORAS

### 7. Elegir versión final del portfolio
- Actualmente hay 4 versiones: v2-cyberpunk, v3-magazine, v4-aurora
- Decidir cuál es la principal y redirigir las otras
- O hacer A/B testing

### 8. Optimizar imágenes para web
- Comprimir fotos que suba Avril (TinyPNG, Squoosh)
- Generar versiones WebP para navegadores modernos

### 9. Agregar SEO básico
- Meta tags en `<head>` (title, description, Open Graph)
- Favicon
- Sitemap.xml

---

## 🔍 BUSQUEDA DE TRABAJO

### 10. Activar campaña de LinkedIn
- Usar skill `Busqueda_Trabajo_Avril/skills/01_linkedin_outreach/`
- Personalizar mensajes con datos reales de Avril
- Enviar 10 conexiones/día a empresas objetivo

### 11. Preparar email de outbound
- ✅ DONE: Script `generate_emails.py` creado
- ✅ DONE: 52 empresas en `portals.yml` (50 Pichincha + Cervecería Nacional + AB InBev)
- ✅ DONE: Email para Pilsener listo en `outbound_pilsener.md`
- Enviar 5-10 emails por día, llevar tracker en CSV

### 12. Optimizar CV de Avril
- Usar skill `03_cv_optimizer`
- Adaptar a Community Manager / Marketing Digital
- Generar PDF ATS-optimizado con career-ops

---

## 🛠️ TÉCNICOS

### 13. Configurar SSL forzoso
- Verificar que https://avrilvelasco.com/ redirija HTTP → HTTPS
- A veces LiteSpeed necesita regla en `.htaccess`

### 14. Crear página 404 personalizada
- Que combine con el diseño del portfolio
- Link de vuelta al inicio

### 15. Analytics
- Agregar Google Analytics o Plausible
- Para saber cuánta gente visita el portfolio

### 16. Formulario de contacto funcional
- Actualmente el portfolio solo muestra email y WhatsApp
- Considerar Formspree o similar para formulario sin backend

---

## 📱 REDES SOCIALES

### 17. Conectar dominio a Linktree alternativo
- El portfolio ya puede servir como "link in bio"
- Agregar botones destacados a TikTok, Instagram, LinkedIn

### 18. Preview cards para redes
- Cuando comparten https://avrilvelasco.com/ en WhatsApp/LinkedIn
- Debe mostrar imagen preview, título y descripción

---

## ✅ COMPLETADOS (no tocar)

- [x] Portfolio creado y deployado
- [x] Uploader funcionando con protección
- [x] Manual de marca online
- [x] Repo GitHub privado creado
- [x] Skill de deploy a Spaceship documentado
- [x] 18 departamentos con skills creados
- [x] Sistema de búsqueda de trabajo estructurado
- [x] Fixes de versión móvil (hero, navbar, cita, foto About)
- [x] Base de datos de empresas ecuatorianas copiada y filtrada (7,876 empresas)
- [x] Career-Ops clonado y adaptado para Avril (perfil + portals.yml + modo outbound)
- [x] Email outbound generado para Pilsener / Cervecería Nacional
- [x] Script `generate_emails.py` para generar lotes de emails
- [x] CSVs exportados: 50 empresas Pichincha + 50 empresas Guayas

---

*Creado: 2026-05-22 03:00 AM*

## Nuevas tareas (post-research Top 10 repos)

- [ ] **Delay anti-spam**: Añadir `time.sleep(random(30, 120))` entre envíos de email en generate_emails.py
- [ ] **Blacklist SQLite**: Crear tabla `empresas_rechazadas` para no re-contactar empresas que dijeron "no"
- [ ] **CV en imagen**: Generar versión JPG del CV para envío por WhatsApp (en Ecuador WhatsApp es el canal principal)
- [ ] **ATS scoring**: Script que evalúa match empresa vs perfil Avril (1-10) y prioriza las mejores
- [ ] **GitHub Actions**: Workflow para ejecutar generate_emails.py semanalmente y enviar reportes
- [ ] **Dashboard tracking**: HTML simple para ver estado de todas las empresas contactadas
- [ ] **JobSpy integration**: Probar `pip install python-jobspy` para scrapear LinkedIn/Indeed Ecuador
- [ ] **Pipeline outbound**: Adaptar el pipeline de 6 etapas de ApplyPilot a email outbound ecuatoriano
