# Product Requirements Document (PRD) - PowerFin
**Versión:** 1.7
**Estado:** Documento Maestro Integrado
**Fecha:** 21 de enero de 2026

## 1. Introducción y Visión
**PowerFin** es un sistema operativo para las finanzas personales. Más que una aplicación de presupuestos, actúa como un **simulador de patrimonio**, un **automatizador de decisiones** y un **educador financiero** integrado.

El núcleo de la aplicación es el concepto de **"Ciclo de Claridad Financiera"**, transformando la ansiedad económica en hábitos automatizados y crecimiento patrimonial tangible mediante la metodología de **Presupuesto de Base Cero**.

## 2. Definición de Roles de Usuario (RBAC)
1.  **Admin (Super Administrador):**
    *   **Gestión de Maestros:** Control de categorías, monedas, tipos de cuentas e **Instrumentos Financieros** (Tasas de rendimiento).
    *   **CMS Educativo:** Gestión de textos del glosario e insights contextuales en múltiples idiomas.
    *   **Auditoría y Soporte:** Gestión de usuarios y capacidad de impersonación para soporte técnico.
2.  **Owner (Dueño de Negocio):**
    *   **Analytics Avanzado:** Visualización de OKRs, embudos de conversión (Funnel de Onboarding) y métricas de retención.
3.  **Usuario Final:**
    *   **Gestión Operativa:** Onboarding guiado, registro de transacciones, planeación de base cero y gestión de fondos/metas.

---

## 3. Requerimientos Funcionales

### 3.1. Internacionalización (Multi-idioma)
La aplicación debe ser global y accesible para diferentes mercados:
*   **Idiomas Soportados:** Español (ES), Inglés (EN) y Portugués (PT).
*   **Idioma por Defecto:** Español.
*   **Alcance:** La interfaz completa, mensajes de error, notificaciones, glosario educativo e insights deben estar disponibles en los tres idiomas.
*   **Persistencia (Control de Cambios v1.7):** El idioma preferido se guarda inmediatamente en el perfil de Supabase durante el onboarding. Si un usuario cambia de dispositivo, la aplicación carga su idioma preferido automáticamente tras el login.

### 3.2. Onboarding Educativo (Punto de Partida)
Asistente lineal obligatorio para nuevos usuarios:
*   **Paso 0 (Control de Cambios v1.7):** Validación de Perfil. El sistema detecta logins con datos incompletos (Moneda/Idioma) y fuerza una redirección al flujo de Onboarding, impidiendo el acceso al Dashboard hasta completar los datos maestros.
*   **Paso 1:** Registro y configuración de Ingreso Principal.
*   **Paso 2:** Creación del primer **Fondo de Emergencia** (Sugerencia 10% del ingreso).
*   **Paso 3:** Definición de **Gastos Esenciales** base (Arriendo, Alimentos).
*   **Paso 4:** Visualización del primer hito: **"Tienes X Días de Autonomía / Meta: 180 Días"**.

### 3.3. Gestión Multimoneda y Cuentas
*   **Multimoneda Independiente:** USD, EUR, COP. Balances aislados para evitar distorsión por tasas de cambio.
*   **Visualización (Control de Cambios v1.7):** Las monedas se presentan en formato estandarizado **"Código - Nombre País"** (ej: *COP - Peso Colombia*, *USD - Dólar Estados Unidos*) para claridad absoluta.
*   **Gestión de Efectivo:** Manejado como una "cuenta" más para trazabilidad total de retiros y depósitos.
*   **Traslados entre Cuentas:** Movimientos internos que no afectan el presupuesto de gastos/ingresos.

### 3.4. Planeación de Base Cero y Control de Gastos
*   **Asignación Total:** Cada peso/dólar debe tener un destino (Gasto, Ahorro o Inversión).
*   **Bloqueo y Traslado:** El sistema impide registrar gastos que superen lo planeado. Requiere un **Traslado de Fondos** manual entre conceptos para cubrir excedentes.
*   **Marcación de Escencialidad:** Todo gasto se clasifica como *Esencial* o *No Esencial*.

### 3.5. Simulador de Patrimonio e Inversión
*   **Proyección Multi-plazo:** Visualización a 1 mes, 1 año, hasta 20 años.
*   **Instrumentos de Rendimiento (Simulados):**
    *   Liquidez (5% E.A.)
    *   CDT (8% E.A.)
    *   Fondo Indexado (10% E.A.)
*   **Ajuste por Inflación:** Switch para ver el "Poder de Compra de Hoy".
*   **Insight de Costo de Oportunidad:** Notificación semanal de cuánto dinero se deja de ganar por tener saldos inactivos.

### 3.6. Fondos de Ahorro y Metas
*   **Gestión de Fondos:** Emergencias, Viajes, Educación.
*   **Métodos de Aporte:** Manual (Libre), Automático (Valor Fijo) o Porcentual (% de ingresos).
*   **Indicador de Autonomía:** `Días de Autonomía = Total Fondos / Gasto Diario Esencial`.

### 3.7. Autenticación y Experiencia de Usuario (Control de Cambios v1.7)
*   **Flujo "Zero Friction" en Verificación:** Si un usuario intenta ingresar sin confirmar su email, el sistema:
    1.  Detecta el error específico.
    2.  Muestra una vista de feedback amigable (sin crash ni error genérico).
    3.  Dispara automáticamente el reenvío del correo de verificación.
*   **Sanitización de Redirección:** El enlace de verificación enviado por correo se sanitiza para garantizar que el usuario regrese a la raíz de la aplicación web (`/`), evitando errores de enrutamiento por fragmentos o parámetros residuales.
*   **Diseño Split-Screen:** Vistas de Login y Registro unificadas bajo un diseño de pantalla dividida (Hero Image a la izquierda, Formulario a la derecha) para una percepción "Premium" desde el primer contacto.
*   **Arquitectura Modular del Dashboard:** La vista principal se compone de elementos reutilizables (`Sidebar`, `SummaryCard`, `QuickAction`) para facilitar el mantenimiento y la escalabilidad futura.

---

## 4. Requerimientos No Funcionales
*   **Arquitectura i18n:** Uso de archivos de localización (JSON) para facilitar la escalabilidad a nuevos idiomas.
*   **Integridad Financiera:** Lógica de "Libro Mayor" para evitar duplicidad o pérdida de dinero en traslados.
*   **Rendimiento:** Cálculos de proyecciones en < 300ms.
*   **Seguridad:** Encriptación AES-256, Autenticación mediante Supabase y RLS.
*   **Cumplimiento (Disclaimers):** Advertencia obligatoria en simuladores sobre la naturaleza estimada de los rendimientos.
*   **Analytics:** Instrumentación de eventos para medir el éxito de los OKRs.

---

## 5. Dashboard Administrativo (PowerPanel)
*   **Métricas OKRs:** Registro vs Activación, Interacción con Glosario, Comprensión de Días de Autonomía.
*   **Funnel de Conversión:** Visualización del flujo de Onboarding para detectar puntos de abandono.

---

## 6. Hoja de Roadmap
1.  **Fase 1 (MVP):** Onboarding, Cuentas, Ingresos, Planeación Base Cero y Días de Autonomía. Implementación básica de i18n (ES/EN).
2.  **Fase 2 (Control Total):** Traslados entre cuentas, Simulador de Patrimonio con Inflación e Instrumentos. Inclusión de Portugués (PT).
3.  **Fase 3 (Automatización):** Aportes automáticos a fondos, Transacciones Recurrentes y Alertas al 90%.
4.  **Fase 4 (Admin & Educación):** CMS educativo multi-idioma, Panel de OKRs avanzado y Gestión de Soporte.

---

## 7. Control de Cambios e Historial de Versiones

| Versión | Fecha | Autor | Descripción del Cambio |
| :--- | :--- | :--- | :--- |
| **1.0** | 15-ene-2026 | Equipo Producto | Creación del documento original. |
| **1.6** | 20-ene-2026 | Antigravity AI | Ajustes menores y clarificación de roles. |
| **1.7** | 21-ene-2026 | Antigravity AI | Inclusión de **Smart Resend Logic** (Auth), Lógica de **Persistencia de Idioma**, Estandarización de formato de **Monedas**, y Arquitectura **Modular** del Dashboard. Se añade sección 3.7 específica para mejoras de UX en autenticación. |
