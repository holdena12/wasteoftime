import tkinter as tk
from tkinter import ttk

total_points = 0

def on_button_click(button_name):
    global total_points

    entry = ttk.Entry(window)
    entry.pack()

    submit_button = ttk.Button(window, text="Submit", command=lambda: process_input(entry.get(), button_name, entry, submit_button))
    submit_button.pack()

def process_input(user_input, button_name, entry_widget, submit_widget):
    global total_points
    try:
        number = float(user_input)
        multiplier = float(button_names[button_name])
        result = number * multiplier
        total_points += result
        points_label.config(text=f"Total Points: {total_points:.2f}")  # Update the total points label
        entry_widget.pack_forget()  # Hide the entry widget
        submit_widget.pack_forget()  # Hide the submit button
    except ValueError:
        # Handle invalid input
        pass

def create_styled_button(parent, text, button_name):
    style = ttk.Style()
    style.configure("TButton",
                    font=("Comic book Sans", 12),
                    padding=10,
                    background="#4CAF50",
                    foreground="black")
    button = ttk.Button(parent, text=text, style="TButton", command=lambda name=button_name: on_button_click(name))
    return button

window = tk.Tk()
window.title("Styled Buttons Example")

points_label = tk.Label(window, text=f"Total Points: {total_points:.2f}")
points_label.pack(anchor="ne", padx=10, pady=10)

button_names = {
    " Pushup": 4,
    "Pull up": 7,
    "Leg lift": 2.5,
    "Steps ": 0.05,
    " Sit up": 3,
    " Burpees": 5.5,
    "Crunches ": 2,
    "Squats ": 2,
    "Lunges ": 2,
    "V-ups ": 2.5
}

buttons = {}
for key, value in button_names.items():
    button = create_styled_button(window, key, key)
    buttons[key] = button
    button.pack(pady=5)

window.mainloop()
