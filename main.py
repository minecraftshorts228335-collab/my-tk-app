import tkinter as tk
from tkinter import ttk

# 1. Словарь правил конвертации
CONVERSIONS = {
    "Километры → мили": lambda value: value * 0.621371,
    "Килограммы → фунты": lambda value: value * 2.20462,
    "°C → °F": lambda value: value * 9/5 + 32,
}

# 2. Функция обработки нажатия кнопки и конвертации
def convert():
    try:
        # Заменяем запятую на точку, чтобы float не выдавал ошибку при вводе 12,5
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Введите число, например 12.5")
        return
    
    # Получаем выбранный пункт из списка
    conversion_name = conversion_box.get()
    
    # Вычисляем результат по словарю
    converted = CONVERSIONS[conversion_name](value)
    
    # Выводим результат в метку (округляем до 2 знаков)
    result_label.config(text=f"Результат: {converted:.2f}")

# 3. Создание главного окна
root = tk.Tk()
root.title("Конвертер единиц")
root.geometry("380x260")

# Заголовок
heading = tk.Label(root, text="Мой конвертер", font=("Arial", 14))
heading.pack(pady=12)

# Поле для ввода числа
value_entry = ttk.Entry(root, font=("Arial", 12))
value_entry.pack(pady=6)

# Выпадающий список с вариантами конвертации
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    font=("Arial", 11)
)
conversion_box.current(0)  # Выбрать первый пункт по умолчанию
conversion_box.pack(pady=6)

# Кнопка «Конвертировать» (передаем функцию без круглых скобок!)
convert_button = ttk.Button(root, text="Конвертировать", command=convert)
convert_button.pack(pady=8)

# Метка для вывода результата
result_label = ttk.Label(root, text="Результат появится здесь", font=("Arial", 11))
result_label.pack(pady=6)

# 4. Запуск главного цикла окна
root.mainloop()