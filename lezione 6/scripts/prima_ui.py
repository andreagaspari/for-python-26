import tkinter as tk

app = tk.Tk()
app.title("La mia prima UI")
app.geometry("400x300")

label = tk.Label(app, text="Ciao Mondo!", font=("Arial", 20))
label.pack(pady=50)

app.mainloop()