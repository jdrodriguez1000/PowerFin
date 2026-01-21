class UserTheme:
    """
    Sistema de Temas para la App de Usuario de FinancApp.
    Enfoque: Vibrante, Moderno, Premium.
    """
    # Paleta de Colores
    PRIMARY = "#B6E33E"         # Verde Lima (Acción)
    SECONDARY = "#002A1C"       # Verde Bosque (Sidebar/Branding)
    BACKGROUND = "#F4F7F6"      # Gris Neutro claro
    SURFACE = "#FFFFFF"         # Blanco (Cards)
    
    TEXT_PRIMARY = "#000000"    # Títulos
    TEXT_SECONDARY = "#4A4A4A"  # Cuerpo
    TEXT_MUTED = "#8E8E8E"      # Labels/Secundario
    
    # Radios y Bordes
    RADIUS_XL = 30              # Botones tipo píldora / Widgets principales
    RADIUS_LG = 25              # Cards del Dashboard
    RADIUS_MD = 15              # Inputs
    
    # Dimensiones Estándar
    COMPONENT_WIDTH = 360       # Ancho estándar para inputs y botones
    BUTTON_PADDING = 25         # Padding para botones (más alto)

    # Tipografía
    FONT_FAMILY = "Montserrat, Inter, Proxima Nova, sans-serif"


class AdminTheme:
    """
    Sistema de Temas para la App de Administrador de FinancApp.
    Enfoque: Profesional, Analítico, Limpio.
    """
    # Paleta de Colores
    PRIMARY = "#0EA5E9"         # Azul Cielo (Acción)
    BACKGROUND = "#F8FAFC"      # Slate Ligero
    SURFACE = "#FFFFFF"         # Blanco (Sidebar/Cards)
    
    # Estados
    SUCCESS = "#22C55E"
    ERROR = "#EF4444"
    WARNING = "#F59E0B"
    
    TEXT_TITLE = "#1E293B"      # Azul Oscuro
    TEXT_BODY = "#64748B"       # Gris Slate
    
    # Radios y Bordes
    RADIUS_MD = 10              # Búsqueda / Componentes
    RADIUS_SM = 8               # Botones / Filas Tablas

    # Tipografía
    FONT_FAMILY = "Inter, Roboto, Segoe UI, sans-serif"


class SharedConfig:
    """Configuraciones de espaciado comunes para ambas apps."""
    PADDING_GLOBAL = 20
    SPACING_VERTICAL = 16
    
    SHADOW_SOFT = {
        "blur_radius": 15,
        "color": "#0D000000", # 5% Opacity
        "offset": (0, 4)
    }
