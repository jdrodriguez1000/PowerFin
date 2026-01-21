# Guía de Estilos de FinancApp

Esta guía define el sistema de diseño, los patrones visuales y los componentes de UI para las aplicaciones de **Usuario** y **Administrador** de FinancApp, basándose en los conceptos visuales proporcionados.

---

## 🟢 1. Aplicación de Usuario (FinancApp User)
*Basado en `baseUser.webp`*

### 🎨 Sistema de Colores
- **Primario:** `#B6E33E` (Verde Lima)
- **Dark Neutral:** `#002A1C` (Verde Bosquesidebar)
- **Background:** `#F4F7F6` (Gris Neutro muy claro)
- **Card Background:** `#FFFFFF` (Blanco Puro)

### 🧱 Componentes de UI Detallados

#### A. Botones (Buttons)
- **Botón Primario (`ElevatedButton`):**
  - **Fondo:** `#B6E33E`
  - **Color de Texto:** `#002A1C` (Oscuro)
  - **Borde:** `border_radius=30` (Píldora/Cápsula completa)
  - **Sombra:** Suave, `elevation=2`
- **Botón Secundario / Outline:**
  - **Border:** `1px solid #B6E33E`
  - **Color de Texto:** `#B6E33E`
  - **Borde:** `border_radius=30`
- **Botón de Icono (Sidebar):**
  - **Activo:** Ícono blanco, fondo sutil si es necesario.
  - **Inactivo:** Ícono gris claro/opaco.

#### B. Cajas de Texto (TextFields/Inputs)
- **Estilo General:**
  - **Fondo:** `#FFFFFF`
  - **Borde:** `border_color="#E0E0E0"` (Gris muy claro)
  - **Focus:** `focus_color="#B6E33E"`
  - **Border Radius:** `border_radius=15`
  - **Content Padding:** Amplio para una sensación "aireada".

#### C. Tarjetas (Cards / Containers)
- **Dashboard Cards:**
  - **Fondo:** `#FFFFFF`
  - **Border Radius:** `border_radius=25`
  - **Sombra:** `box-shadow: 0px 4px 15px rgba(0, 42, 28, 0.05)`
- **Special Card (Ahorro/Cards):**
  - Fondo oscuro `#002A1C` con texturas de gradiente o patrones circulares sutiles en verde.

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

