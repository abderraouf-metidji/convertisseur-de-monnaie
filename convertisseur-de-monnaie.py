import tkinter as tk
import requests

conversion_history = []

preferred_currencies = []

def add_preferred_currency():
    currency = entry_preferred.get()
    preferred_currencies.append(currency)
    entry_preferred.delete(0, "end")
    label_result["text"] = f"{currency} a été ajouté à la liste des devises préférées"

def convert():
    amount = float(entry_amount.get())
    from_currency = entry_from.get()
    to_currency = entry_to.get()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if to_currency not in data["rates"]:
        label_result["text"] = "Devise non valide"
        return

    rate = data["rates"][to_currency]
    converted_amount = amount * rate

    label_result["text"] = f"{converted_amount} {to_currency}"

    conversion_history.append({
    "amount": amount,
    "from": from_currency,
    "to": to_currency,
    "converted_amount": converted_amount
})

def show_preferred_currencies():
    preferred_text = "Devises préférées:\n"
    for currency in preferred_currencies:
        preferred_text += f"{currency}\n"
    preferred_window = tk.Toplevel(root)
    preferred_window.title("Devises préférées")
    preferred_widget = tk.Text(preferred_window)
    preferred_widget.insert("1.0", preferred_text)
    preferred_widget.pack()
    preferred_window.mainloop()

def show_history():
    history_text = "Historique des conversions:\n"
    for conversion in conversion_history:
        history_text += f"{conversion['amount']} {conversion['from']} -> {conversion['converted_amount']} {conversion['to']}\n"
    history_window = tk.Toplevel(root)
    history_window.title("Historique")
    history_widget = tk.Text(history_window)
    history_widget.insert("1.0", history_text)
    history_widget.pack()
    history_window.mainloop()


root = tk.Tk()
root.title("Convertisseur de devises")

label_amount = tk.Label(root, text="Montant à convertir :")
entry_amount = tk.Entry(root)
label_from = tk.Label(root, text="Devise d'origine :")
entry_from = tk.Entry(root)
label_to = tk.Label(root, text="Devise cible :")
entry_to = tk.Entry(root)

button_convert = tk.Button(root, text="Convertir", command=convert)
button_history = tk.Button(root, text="Historique", command=show_history)

label_result = tk.Label(root, text="")

label_preferred = tk.Label(root, text="Ajouter devise préférée :")
entry_preferred = tk.Entry(root)
button_add_preferred = tk.Button(root, text="Ajouter", command=add_preferred_currency)
button_show_preferred = tk.Button(root, text="Afficher devises préférées", command=show_preferred_currencies)

label_preferred.pack()
entry_preferred.pack()
button_add_preferred.pack()
button_show_preferred.pack()

label_amount.pack()
entry_amount.pack()
label_from.pack()
entry_from.pack()
label_to.pack()
entry_to.pack()
button_convert.pack()
label_result.pack()
button_history.pack()

root.mainloop()