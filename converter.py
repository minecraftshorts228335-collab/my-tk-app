# Модуль с логикой конвертации единиц

CONVERSIONS = {
    # Длина
    "Километры → мили": {"category": "Длина", "func": lambda v: v * 0.621371, "from": "км", "to": "мили"},
    "Мили → километры": {"category": "Длина", "func": lambda v: v / 0.621371, "from": "мили", "to": "км"},
    
    # Масса
    "Килограммы → фунты": {"category": "Масса", "func": lambda v: v * 2.20462, "from": "кг", "to": "фунты"},
    "Фунты → килограммы": {"category": "Масса", "func": lambda v: v / 2.20462, "from": "фунты", "to": "кг"},
    
    # Температура
    "°C → °F": {"category": "Температура", "func": lambda v: v * 9/5 + 32, "from": "°C", "to": "°F"},
    "°F → °C": {"category": "Температура", "func": lambda v: (v - 32) * 5/9, "from": "°F", "to": "°C"},
    
    # Валюта (по условному фиксированному курсу)
    "USD → KZT": {"category": "Валюта", "func": lambda v: v * 485.0, "from": "USD", "to": "KZT"},
    "KZT → USD": {"category": "Валюта", "func": lambda v: v / 485.0, "from": "KZT", "to": "USD"},
}

def convert_value(conversion_name, value):
    """Выполняет конвертацию по имени выбранного правила."""
    if conversion_name in CONVERSIONS:
        rule = CONVERSIONS[conversion_name]
        result = rule["func"](value)
        return result
    raise ValueError("Неизвестное правило конвертации")

# Защита модуля от случайного запуска
if __name__ == "__main__":
    print("Это модуль конвертации. Запустите main.py для открытия графического интерфейса.")