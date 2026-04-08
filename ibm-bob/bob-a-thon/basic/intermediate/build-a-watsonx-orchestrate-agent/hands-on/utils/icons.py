"""
Icon utility module for Python applications.
Provides various icon sets using Unicode characters and emojis.
"""

# Status Icons
class StatusIcons:
    """Status and state indicators"""
    SUCCESS = "✓"
    ERROR = "✗"
    WARNING = "⚠"
    INFO = "ℹ"
    QUESTION = "?"
    CHECKMARK = "✔"
    CROSS = "✖"
    CIRCLE_CHECK = "✅"
    CIRCLE_CROSS = "❌"
    HOURGLASS = "⏳"
    CLOCK = "🕐"
    BELL = "🔔"
    FIRE = "🔥"
    STAR = "⭐"
    SPARKLES = "✨"


# Navigation Icons
class NavigationIcons:
    """Navigation and directional icons"""
    UP = "↑"
    DOWN = "↓"
    LEFT = "←"
    RIGHT = "→"
    UP_RIGHT = "↗"
    DOWN_RIGHT = "↘"
    DOWN_LEFT = "↙"
    UP_LEFT = "↖"
    ARROW_UP = "⬆"
    ARROW_DOWN = "⬇"
    ARROW_LEFT = "⬅"
    ARROW_RIGHT = "➡"
    BACK = "◀"
    FORWARD = "▶"
    HOME = "🏠"
    MENU = "☰"


# File and Folder Icons
class FileIcons:
    """File system related icons"""
    FOLDER = "📁"
    FOLDER_OPEN = "📂"
    FILE = "📄"
    DOCUMENT = "📃"
    PAGE = "📄"
    NOTEBOOK = "📓"
    BOOK = "📖"
    BOOKMARK = "🔖"
    CLIPBOARD = "📋"
    PACKAGE = "📦"
    ARCHIVE = "🗄"
    TRASH = "🗑"


# Action Icons
class ActionIcons:
    """Action and operation icons"""
    PLAY = "▶"
    PAUSE = "⏸"
    STOP = "⏹"
    RECORD = "⏺"
    REFRESH = "🔄"
    SYNC = "🔃"
    DOWNLOAD = "⬇"
    UPLOAD = "⬆"
    SAVE = "💾"
    EDIT = "✏"
    PENCIL = "✎"
    DELETE = "🗑"
    ADD = "➕"
    REMOVE = "➖"
    PLUS = "+"
    MINUS = "-"
    SEARCH = "🔍"
    FILTER = "🔽"
    SETTINGS = "⚙"
    GEAR = "⚙"
    WRENCH = "🔧"
    HAMMER = "🔨"
    LOCK = "🔒"
    UNLOCK = "🔓"
    KEY = "🔑"


# Communication Icons
class CommunicationIcons:
    """Communication and messaging icons"""
    EMAIL = "✉"
    ENVELOPE = "📧"
    MESSAGE = "💬"
    CHAT = "💭"
    PHONE = "📞"
    MOBILE = "📱"
    BELL = "🔔"
    MEGAPHONE = "📣"
    LOUDSPEAKER = "📢"
    ANTENNA = "📡"


# User and People Icons
class UserIcons:
    """User and people related icons"""
    USER = "👤"
    USERS = "👥"
    PERSON = "🧑"
    PEOPLE = "👨‍👩‍👧‍👦"
    ADMIN = "👨‍💼"
    DEVELOPER = "👨‍💻"
    SCIENTIST = "👨‍🔬"
    TEACHER = "👨‍🏫"
    STUDENT = "👨‍🎓"
    ROBOT = "🤖"
    ALIEN = "👽"


# Technology Icons
class TechIcons:
    """Technology and computing icons"""
    COMPUTER = "💻"
    LAPTOP = "💻"
    DESKTOP = "🖥"
    KEYBOARD = "⌨"
    MOUSE = "🖱"
    PRINTER = "🖨"
    SERVER = "🖥"
    DATABASE = "🗄"
    CLOUD = "☁"
    NETWORK = "🌐"
    WIFI = "📶"
    BATTERY = "🔋"
    PLUG = "🔌"
    CHIP = "🔲"
    CODE = "💻"
    TERMINAL = "⌨"
    BUG = "🐛"
    ROBOT = "🤖"
    AI = "🤖"


# Data and Analytics Icons
class DataIcons:
    """Data and analytics icons"""
    CHART = "📊"
    GRAPH = "📈"
    CHART_DOWN = "📉"
    PIE_CHART = "🥧"
    BAR_CHART = "📊"
    TABLE = "📋"
    CALCULATOR = "🧮"
    ABACUS = "🧮"
    MAGNIFYING_GLASS = "🔍"
    MICROSCOPE = "🔬"
    TELESCOPE = "🔭"


# Weather Icons
class WeatherIcons:
    """Weather related icons"""
    SUN = "☀"
    CLOUD = "☁"
    RAIN = "🌧"
    SNOW = "❄"
    LIGHTNING = "⚡"
    STORM = "⛈"
    WIND = "💨"
    TORNADO = "🌪"
    RAINBOW = "🌈"
    UMBRELLA = "☂"


# Emoji Icons
class EmojiIcons:
    """Common emoji icons"""
    SMILE = "😊"
    HAPPY = "😄"
    SAD = "😢"
    ANGRY = "😠"
    LOVE = "❤"
    HEART = "💖"
    THUMBS_UP = "👍"
    THUMBS_DOWN = "👎"
    CLAP = "👏"
    WAVE = "👋"
    POINT_RIGHT = "👉"
    POINT_LEFT = "👈"
    POINT_UP = "☝"
    POINT_DOWN = "👇"
    OK_HAND = "👌"
    VICTORY = "✌"
    FIST = "✊"
    MUSCLE = "💪"
    PRAY = "🙏"
    CELEBRATE = "🎉"
    PARTY = "🎊"
    GIFT = "🎁"
    TROPHY = "🏆"
    MEDAL = "🏅"
    CROWN = "👑"


# Shapes and Symbols
class ShapeIcons:
    """Geometric shapes and symbols"""
    CIRCLE = "●"
    CIRCLE_OUTLINE = "○"
    SQUARE = "■"
    SQUARE_OUTLINE = "□"
    TRIANGLE = "▲"
    TRIANGLE_DOWN = "▼"
    DIAMOND = "◆"
    DIAMOND_OUTLINE = "◇"
    BULLET = "•"
    DOT = "·"
    DASH = "—"
    ELLIPSIS = "…"
    INFINITY = "∞"
    DEGREE = "°"
    PERCENT = "%"
    HASH = "#"
    AT = "@"
    AMPERSAND = "&"


# Progress and Loading Icons
class ProgressIcons:
    """Progress and loading indicators"""
    SPINNER = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    DOTS = ["⠋", "⠙", "⠚", "⠞", "⠖", "⠦", "⠴", "⠲", "⠳", "⠓"]
    BARS = ["▁", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
    BLOCKS = ["▖", "▘", "▝", "▗"]
    ARROWS = ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"]
    PROGRESS_BAR = "█"
    PROGRESS_EMPTY = "░"
    HOURGLASS = ["⏳", "⌛"]


# Box Drawing Characters
class BoxIcons:
    """Box drawing characters for CLI interfaces"""
    # Single line
    HORIZONTAL = "─"
    VERTICAL = "│"
    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOTTOM_LEFT = "└"
    BOTTOM_RIGHT = "┘"
    CROSS = "┼"
    T_DOWN = "┬"
    T_UP = "┴"
    T_RIGHT = "├"
    T_LEFT = "┤"
    
    # Double line
    DOUBLE_HORIZONTAL = "═"
    DOUBLE_VERTICAL = "║"
    DOUBLE_TOP_LEFT = "╔"
    DOUBLE_TOP_RIGHT = "╗"
    DOUBLE_BOTTOM_LEFT = "╚"
    DOUBLE_BOTTOM_RIGHT = "╝"
    DOUBLE_CROSS = "╬"
    
    # Heavy line
    HEAVY_HORIZONTAL = "━"
    HEAVY_VERTICAL = "┃"
    HEAVY_TOP_LEFT = "┏"
    HEAVY_TOP_RIGHT = "┓"
    HEAVY_BOTTOM_LEFT = "┗"
    HEAVY_BOTTOM_RIGHT = "┛"


# Utility Functions
def get_status_icon(status: str) -> str:
    """
    Get an icon based on status string.
    
    Args:
        status: Status string (success, error, warning, info, etc.)
    
    Returns:
        Corresponding icon character
    """
    status_map = {
        'success': StatusIcons.SUCCESS,
        'error': StatusIcons.ERROR,
        'warning': StatusIcons.WARNING,
        'info': StatusIcons.INFO,
        'question': StatusIcons.QUESTION,
        'pending': StatusIcons.HOURGLASS,
        'loading': StatusIcons.HOURGLASS,
    }
    return status_map.get(status.lower(), StatusIcons.INFO)


def create_progress_bar(percentage: float, width: int = 20, filled_char: str | None = None, empty_char: str | None = None) -> str:
    """
    Create a text-based progress bar.
    
    Args:
        percentage: Progress percentage (0-100)
        width: Width of the progress bar in characters
        filled_char: Character for filled portion (default: █)
        empty_char: Character for empty portion (default: ░)
    
    Returns:
        Progress bar string
    """
    filled_char = filled_char or ProgressIcons.PROGRESS_BAR
    empty_char = empty_char or ProgressIcons.PROGRESS_EMPTY
    
    filled_width = int(width * (percentage / 100))
    empty_width = width - filled_width
    
    return f"{filled_char * filled_width}{empty_char * empty_width}"


def create_box(text: str, style: str = 'single', padding: int = 1) -> str:
    """
    Create a box around text using box drawing characters.
    
    Args:
        text: Text to put in the box
        style: Box style ('single', 'double', or 'heavy')
        padding: Padding around text
    
    Returns:
        Boxed text string
    """
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    
    if style == 'double':
        h, v = BoxIcons.DOUBLE_HORIZONTAL, BoxIcons.DOUBLE_VERTICAL
        tl, tr = BoxIcons.DOUBLE_TOP_LEFT, BoxIcons.DOUBLE_TOP_RIGHT
        bl, br = BoxIcons.DOUBLE_BOTTOM_LEFT, BoxIcons.DOUBLE_BOTTOM_RIGHT
    elif style == 'heavy':
        h, v = BoxIcons.HEAVY_HORIZONTAL, BoxIcons.HEAVY_VERTICAL
        tl, tr = BoxIcons.HEAVY_TOP_LEFT, BoxIcons.HEAVY_TOP_RIGHT
        bl, br = BoxIcons.HEAVY_BOTTOM_LEFT, BoxIcons.HEAVY_BOTTOM_RIGHT
    else:  # single
        h, v = BoxIcons.HORIZONTAL, BoxIcons.VERTICAL
        tl, tr = BoxIcons.TOP_LEFT, BoxIcons.TOP_RIGHT
        bl, br = BoxIcons.BOTTOM_LEFT, BoxIcons.BOTTOM_RIGHT
    
    width = max_length + (padding * 2)
    top = tl + (h * width) + tr
    bottom = bl + (h * width) + br
    
    boxed_lines = [top]
    for line in lines:
        padded_line = line.ljust(max_length)
        boxed_lines.append(f"{v}{' ' * padding}{padded_line}{' ' * padding}{v}")
    boxed_lines.append(bottom)
    
    return '\n'.join(boxed_lines)


# Example usage dictionary
ICON_EXAMPLES = {
    'status': {
        'success': f"{StatusIcons.SUCCESS} Operation completed successfully",
        'error': f"{StatusIcons.ERROR} An error occurred",
        'warning': f"{StatusIcons.WARNING} Warning: Check your input",
        'info': f"{StatusIcons.INFO} Information message",
    },
    'actions': {
        'save': f"{ActionIcons.SAVE} Save file",
        'edit': f"{ActionIcons.EDIT} Edit document",
        'delete': f"{ActionIcons.DELETE} Delete item",
        'search': f"{ActionIcons.SEARCH} Search...",
    },
    'progress': {
        'loading': f"{StatusIcons.HOURGLASS} Loading...",
        'processing': f"{StatusIcons.CLOCK} Processing...",
        'complete': f"{StatusIcons.CIRCLE_CHECK} Complete!",
    }
}


if __name__ == "__main__":
    # Demo of available icons
    print("=" * 50)
    print("Icon Library Demo")
    print("=" * 50)
    
    print("\n📊 Status Icons:")
    print(f"  {StatusIcons.SUCCESS} Success")
    print(f"  {StatusIcons.ERROR} Error")
    print(f"  {StatusIcons.WARNING} Warning")
    print(f"  {StatusIcons.INFO} Info")
    
    print("\n🎯 Action Icons:")
    print(f"  {ActionIcons.PLAY} Play")
    print(f"  {ActionIcons.SAVE} Save")
    print(f"  {ActionIcons.EDIT} Edit")
    print(f"  {ActionIcons.DELETE} Delete")
    print(f"  {ActionIcons.SEARCH} Search")
    
    print("\n📁 File Icons:")
    print(f"  {FileIcons.FOLDER} Folder")
    print(f"  {FileIcons.FILE} File")
    print(f"  {FileIcons.DOCUMENT} Document")
    
    print("\n💻 Tech Icons:")
    print(f"  {TechIcons.COMPUTER} Computer")
    print(f"  {TechIcons.DATABASE} Database")
    print(f"  {TechIcons.CLOUD} Cloud")
    print(f"  {TechIcons.BUG} Bug")
    print(f"  {TechIcons.ROBOT} AI/Robot")
    
    print("\n📈 Data Icons:")
    print(f"  {DataIcons.CHART} Chart")
    print(f"  {DataIcons.GRAPH} Graph")
    print(f"  {DataIcons.TABLE} Table")
    
    print("\n👤 User Icons:")
    print(f"  {UserIcons.USER} User")
    print(f"  {UserIcons.USERS} Users")
    print(f"  {UserIcons.DEVELOPER} Developer")
    
    print("\n📦 Progress Bar Examples:")
    print(f"  0%:   [{create_progress_bar(0)}]")
    print(f"  25%:  [{create_progress_bar(25)}]")
    print(f"  50%:  [{create_progress_bar(50)}]")
    print(f"  75%:  [{create_progress_bar(75)}]")
    print(f"  100%: [{create_progress_bar(100)}]")
    
    print("\n📦 Box Examples:")
    print(create_box("Single Line Box", style='single'))
    print()
    print(create_box("Double Line Box", style='double'))
    print()
    print(create_box("Heavy Line Box", style='heavy'))
    
    print("\n" + "=" * 50)

# Made with Bob
