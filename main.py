import tkinter as tk
from tkinter import ttk
from converter import CONVERSIONS, convert_value

# Список для хранения истории последних конвертаций (максимум 5)
history_list = []

def perform_conversion():
    try:
        # Безопасное считывание числа (замена запятой на точку)
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Ошибка: введите число (например, 12.5)")
        return
    
    conv_name = conversion_box.get()
    if not conv_name:
        result_label.config(text="Выберите направление конвертации")
        return
    
    try:
        result = convert_value(conv_name, value)
        result_text = f"Результат: {result:.2f}"
        result_label.config(text=result_text)
        
        # Добавление в историю
        rule_info = CONVERSIONS[conv_name]
        history_item = f"{value} {rule_info['from']} ➔ {result:.2f} {rule_info['to']}"
        history_list.insert(0, history_item)
        if len(history_list) > 5:
            history_list.pop()
        
        # Обновление истории на экране
        history_box.config(state="normal")
        history_box.delete("1.0", tk.END)
        history_box.insert(tk.END, "\n".join(history_list))
        history_box.config(state="disabled")
        
    except Exception as e:
        result_label.config(text=f"Ошибка расчета: {e}")

def swap_units():
    """Меняет местами единицы для выбранного пункта."""
    current = conversion_box.get()
    
    # Словарь точных пар для взаимной замены
    swaps = {
        "Километры → мили": "Мили → километры",
        "Мили → километры": "Километры → мили",
        "Килограммы → фунты": "Фунты → килограммы",
        "Фунты → килограммы": "Килограммы → фунты",
        "°C → °F": "°F → °C",
        "°F → °C": "°C → °F",
        "USD → KZT": "KZT → USD",
        "KZT → USD": "USD → KZT"
    }
    
    # Если текущий пункт есть в словаре пар, меняем его
    if current in swaps:
        target = swaps[current]
        # Проверяем, есть ли такой пункт в выпадающем списке
        if target in conversion_box['values']:
            conversion_box.set(target)

# Создание главного окна
root = tk.Tk()
root.title("Продвинутый конвертер единиц")
root.geometry("420x460")

# Заголовок
heading = tk.Label(root, text="Мультиконвертер", font=("Arial", 14, "bold"))
heading.pack(pady=10)

# Поле для ввода числа
value_entry = ttk.Entry(root, font=("Arial", 11), width=25)
value_entry.pack(pady=5)
value_entry.insert(0, "1")

# Выпадающий список категорий/направлений
conversion_box = ttk.Combobox(
    root,
    values=list(CONVERSIONS.keys()),
    state="readonly",
    font=("Arial", 10),
    width=30
)
conversion_box.current(0)
conversion_box.pack(pady=5)

# Фрейм для кнопок управления
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=8)

convert_button = ttk.Button(btn_frame, text="Конвертировать", command=perform_conversion)
convert_button.grid(row=0, column=0, padx=5)

swap_button = ttk.Button(btn_frame, text="⇄ Поменять местами", command=swap_units)
swap_button.grid(row=0, column=1, padx=5)

# Метка для вывода текущего результата
result_label = ttk.Label(root, text="Результат появится здесь", font=("Arial", 11, "bold"))
result_label.pack(pady=8)

# Панель истории
history_label = ttk.Label(root, text="История последних конвертаций:", font=("Arial", 10))
history_label.pack(anchor="w", padx=40, pady=(10, 2))

history_box = tk.Text(root, height=5, width=42, font=("Courier", 9), state="disabled")
history_box.pack(pady=5)

# Запуск главного цикла
root.mainloop()