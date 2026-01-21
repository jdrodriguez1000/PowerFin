# Product Requirements Document (PRD) - PowerFin
**Versión:** 1.6  
**Estado:** Documento Maestro Integrado  
**Fecha:** 20 de enero de 2026

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
*   **Persistencia:** El idioma preferido del usuario debe guardarse en su perfil para mantener la consistencia entre sesiones y dispositivos.

### 3.2. Onboarding Educativo (Punto de Partida)
Asistente lineal obligatorio para nuevos usuarios:
*   **Paso 1:** Registro y configuración de Ingreso Principal.
*   **Paso 2:** Creación del primer **Fondo de Emergencia** (Sugerencia 10% del ingreso).
*   **Paso 3:** Definición de **Gastos Esenciales** base (Arriendo, Alimentos).
*   **Paso 4:** Visualización del primer hito: **"Tienes X Días de Autonomía / Meta: 180 Días"**.

### 3.3. Gestión Multimoneda y Cuentas
*   **Multimoneda Independiente:** USD, EUR, COP. Balances aislados para evitar distorsión por tasas de cambio.
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
