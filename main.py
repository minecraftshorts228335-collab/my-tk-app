CONVERSIONS = {
"Километры → мили": lambda value: value * 0.621371,
"Килограммы → фунты": lambda value: value * 2.20462,
"°C → °F": lambda value: value * 9 / 5 + 32,
}

def convert():
    try:
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Введите число, например 12.5")
        return
    
    conversion_name = conversion_box.get()
    converted = CONVERSIONS[conversion_name](value)
    result_label.config(text=f"Результат: {converted:.2f}")
    
convert_button = ttk.Button(root, text="Конвертировать", command=convert)
convert_button.pack(pady=8)