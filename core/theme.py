class UserTheme:
    """
    Sistema de Temas para la App de Usuario de FinancApp.
    Enfoque: Premium, Moderno, Limpio (Basado en Estética Fundify).
    """
    # Paleta de Colores
    PRIMARY = "#B6F09C"         # Verde Menta / Active Accent
    SECONDARY = "#0F172A"       # Azul Marino Profundo (Primary Dark)
    BACKGROUND = "#F8FAFC"      # Slate Ligero (Más profesional que el azul pastel)
    PANEL = "#F7FBFD"           # Fondo de Sidebar/Paneles
    SURFACE = "#FFFFFF"         # Blanco (Cards)
    LINK = "#4F46E5"            # Indigo (Links Premium)
    DIVIDER = "#E2E8F0"         # Slate ligero para bordes/divisores
    
    TEXT_PRIMARY = "#0F172A"    # Títulos y texto fuerte
    TEXT_SECONDARY = "#334155"  # Cuerpo de texto
    TEXT_MUTED = "#64748B"      # Labels y textos secundarios (Slate)
    
    # Estados
    SUCCESS = "#B6F09C"
    ERROR = "#FF8282"           # Coral suave
    WARNING = "#FCD34D"
    
    # Radios (Redondeo Premium)
    RADIUS_XL = 30              
    RADIUS_LG = 20              # Cards del Dashboard
    RADIUS_MD = 12              # Inputs / Menú items
    RADIUS_SM = 8
    
    # Dimensiones Estándar
    COMPONENT_WIDTH = 360       
    BUTTON_PADDING = 25         

    # Tipografía
    FONT_FAMILY = "Inter, Montserrat, sans-serif"


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
