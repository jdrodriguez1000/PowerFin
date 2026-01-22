# Guía de Estilos de FinancApp

Esta guía define el sistema de diseño, los patrones visuales y los componentes de UI para las aplicaciones de **Usuario** y **Administrador** de FinancApp, evolucionando hacia una estética modernista, limpia y premium basada en el concepto "Fundify".

---

## 🟢 1. Aplicación de Usuario (FinancApp User)
*Basado en la estética Premium Dashboard v2 (Referencia: FUNDIFY)*

### 🎨 Sistema de Colores (Paleta Fundify)
- **Primary Canvas (Background):** `#D0E7F5` (Azul Cielo Pastel - Fondo de la aplicación)
- **Panel/Sidebar Background:** `#F7FBFD` (Casi blanco, con un toque azulado)
- **Active Accent:** `#B6F09C` (Menta brillante para estados activos y éxitos)
- **Primary Dark:** `#0F172A` (Azul Marino Profundo para tarjetas especiales y texto principal)
- **Surface (Cards):** `#FFFFFF` (Blanco Puro)
- **Expense/Negative:** `#FF8282` (Coral/Rojo suave para salidas)
- **Muted Text:** `#64748B` (Gris Slate para etiquetas y fechas)

### 🧱 Componentes de UI Detallados

#### A. Navegación (Sidebar)
- **Estilo:** Fondo `#F7FBFD`, borde derecho muy sutil.
- **Item Activo:** 
  - Fondo: `#B6F09C` con `border_radius=12`.
  - Icono/Texto: Color `#0D2B1E` (verde oscuro).
- **Item Inactivo:**
  - Color: `#64748B`.
- **Get Pro Card:** Un contenedor inferior con fondo `#0F172A`, texto blanco y botón de acción en color `#B6F09C`.

#### B. Tarjetas de Resumen (KPI Cards)
- **Diseño:** Fondo blanco, esquinas redondeadas (`border_radius=20`), sombra muy suave.
- **Elementos Internos:**
  - Icono superior izquierdo.
  - Indicador de tendencia (pequeña cápsula verde/roja con el %).
  - Valor principal en fuente pesada (`weight="bold"`).
  - Título descriptivo debajo en `#64748B`.

#### C. Tarjeta de Cuenta Principal (Credit Card Style)
- **Fondo:** `#0F172A` (Azul Marino).
- **Decoración:** Patrones circulares sutiles.
- **Contenido:** Nombre, balance en blanco, detalles de tarjeta.

#### D. Visualización de Datos (Charts & Progress)
- **Gráficos de Barras:** Barras duales en `#0F172A` y `#B6F09C`.
- **Barras de Progreso:** Fondo `#F1F5F9` con progreso en `#B6F09C`.
- **Gráfico de Dona:** Centro con valor total, segmentos en colores coordinados.

---

## 🔵 2. Aplicación de Administrador (FinancApp Admin)
*Basado en `baseAdmin.webp`*

### 🎨 Sistema de Colores
- **Primario:** `#0EA5E9` (Azul Cielo)
- **Background:** `#F8FAFC` (Slate ligero)
- **Sidebar Background:** `#FFFFFF` (Blanco)
- **Status Colors:**
  - Success: `#22C55E`
  - Error: `#EF4444`

### 🧱 Componentes de UI Detallados

#### A. Botones (Buttons)
- **Botón Primario:**
  - **Fondo:** `#0EA5E9`
  - **Color de Texto:** `#FFFFFF`
  - **Borde:** `border_radius=8` (Cuadrado con puntas suavizadas)
- **Botones de Filtro/Acción:**
  - **Fondo:** `#F1F5F9` (Gris azulado)
  - **Color de Texto:** `#64748B`
  - **Borde:** `border_radius=8`

#### B. Cajas de Texto y Búsqueda
- **Search Bar:**
  - **Fondo:** `#F1F5F9`
  - **Border:** `border_width=0` (Sin borde, usar fondo)
  - **Icono:** Lupa en color `#94A3B8` al inicio.
  - **Border Radius:** `border_radius=10`

#### C. Tablas y Filas (DataTables)
- **Encabezado:** Texto en gris fuerte, negrita suave.
- **Filas:**
  - Espaciado vertical cómodo.
  - Avatares circulares para usuarios.
  - **Status Badges:** Fondo semi-transparente del color del estado con texto sólido (ej: Fondo verde claro, texto verde oscuro).

#### D. Tarjetas de Resumen (Summary Cards)
- **Estilo:** Minimalista.
- **Acento:** Pequeña línea o icono lateral que indique la tendencia (flecha verde arriba, roja abajo).

---

## 📐 3. Guía de Interacción Común

### Hover Effects
- **User App:** Los botones deben oscurecer el verde lima ligeramente al pasar el mouse.
- **Admin App:** Las filas de las tablas deben tener un `hover_color="#F8FAFC"`.

### Tipografía por Componente
- **Labels de Input:** Font size 12-14px, Peso 500 (Medium).
- **Valores Numéricos (Cuentas):** Grande (24-32px), Bold (700) para la App de Usuario.
- **Textos de Tabla:** 13px, Regular para la App de Admin.

