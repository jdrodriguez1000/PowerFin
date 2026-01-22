# Product Requirements Document (PRD) - PowerFin
**Versión:** 1.9
**Estado:** Documento Maestro Integrado
**Fecha:** 22 de enero de 2026

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
*   **Persistencia (Control de Cambios v1.7):** El idioma preferido se guarda inmediatamente en el perfil de Supabase durante el onboarding.

### 3.2. Onboarding Educativo (Punto de Partida)
Asistente lineal obligatorio para nuevos usuarios que incluye validación de perfil completa, configuración de ingresos, fondos de emergencia y gastos esenciales.

### 3.3. Gestión Multimoneda y Cuentas
*   **Multimoneda Independiente:** USD, EUR, COP. Balances aislados.
*   **Visualización:** Formato estandarizado **"Código - Nombre País"**.
*   **Gestión de Efectivo:** Manejado como una cuenta para trazabilidad total.

### 3.4. Planeación de Base Cero (Presupuesto)
*   **Asignación Total:** Cada peso/dólar debe tener un destino.
*   **Metodología:** El usuario asigna trabajo a su capital hasta que el saldo por asignar llegue a cero.

### 3.5. Simulador de Patrimonio e Inversión
*   **Proyección Multi-plazo:** 1 mes hasta 20 años.
*   **Rendimiento Real:** Ajuste por inflación para ver "Poder de Compra de Hoy".

### 3.6. Fondos de Ahorro y Metas
*   **Gestión de Fondos:** Emergencias, Viajes, Educación, etc.
*   **Indicador de Autonomía:** `Total Fondos / Gasto Diario Esencial`.

### 3.7. Dashboard y Salud Patrimonial (Control de Cambios v1.9)
La vista principal presenta una narrativa estratégica mediante KPIs y análisis de eficiencia:

#### A. Los 4 KPIs Maestros:
1.  **Saldo Total:** Capital líquido por asignar (dinero "huérfano").
2.  **Días de Autonomía:** Cobertura de gastos esenciales con fondos actuales.
3.  **Total Ahorrado:** Patrimonio acumulado en fondos con propósito.
4.  **Índice Pasivo:** % de gastos totales (incluyendo deudas e hipotecas) cubiertos por ingresos pasivos.

#### B. Sección de Salud Patrimonial:
*   **Índice de Eficiencia de Capital (IEC):** Métrica porcentual que mide qué tan bien está trabajando el dinero del usuario frente a una inflación de referencia y tasas de mercado.
*   **Costo de Oportunidad:** Valor monetario real que el usuario deja de ganar por mantener saldos en instrumentos de bajo rendimiento.

### 3.8. Estructura de Navegación del Dashboard (Control de Cambios v1.9)
El Sidebar de navegación sigue una jerarquía lógica de gestión financiera:
1.  **Resumen:** Visión estratégica y KPIs.
2.  **Presupuesto:** Planeación de base cero (Asignación de cada peso).
3.  **Objetivos:** Gestión de fondos y metas de ahorro.
4.  **Transacciones:** Registro histórico y flujo de caja diario.
5.  **Cuentas:** Inventario de bancos, efectivo e inversiones.
---
6.  **Mi Perfil:** Caracterización y datos personales.
7.  **Ajustes:** Configuración técnica, moneda base e idioma.
---
8.  **Cerrar Sesión:** Salida segura.

### 3.9. Autenticación y Experiencia de Usuario
Incluye flujo "Zero Friction" en verificación, sanitización de emails, y diseño Split-Screen Premium.

---

## 4. Requerimientos No Funcionales
*   Arquitectura i18n extensible.
*   Integridad Financiera (Lógica de Libro Mayor).
*   Rendimiento (< 300ms en cálculos).
*   Seguridad (AES-256, RLS en Supabase).

---

## 5. Hoja de Roadmap
1.  **Fase 1 (MVP):** Onboarding, Cuentas, Ingresos básicos.
2.  **Fase 2 (Control Total):** Dashboard con 4 KPIs, Salud Patrimonial (IEC/Costo Oportunidad), Presupuesto Base Cero.
3.  **Fase 3 (Automatización):** Aportes automáticos, Transacciones Recurrentes.

---

## 6. Control de Cambios

| Versión | Fecha | Autor | Descripción del Cambio |
| :--- | :--- | :--- | :--- |
| **1.0** | 15-ene-2026 | Equipo Producto | Creación del documento original. |
| **1.8** | 22-ene-2026 | Antigravity AI | Definición de los **4 KPIs Maestros del Dashboard**. |
| **1.9** | 22-ene-2026 | Antigravity AI | Inclusión de indicadores de **Salud Patrimonial** (IEC y Costo de Oportunidad) y definición de la **Estructura de Menús** del Dashboard. |
