import tkinter as tk
from tkinter import ttk
import re

# Function to evaluate password strength
def check_password_strength(event=None):
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    if score == 0:
        strength = "Very Weak"
        color = "#d32f2f"
    elif score <= 2:
        strength = "Weak"
        color = "#ff9800"
    elif score == 3:
        strength = "Moderate"
        color = "#ffc107"
    elif score == 4:
        strength = "Strong"
        color = "#4caf50"
    else:
        strength = "Very Strong"
        color = "#2e7d32"

    result_label.config(text=f"Password Strength: {strength}", fg=color)

# Toggle password visibility
def toggle_password():
    entry.config(show="" if show_password_var.get() else "*")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker by ABD")
root.geometry("550x500")
root.configure(bg="#dde9f7")
root.resizable(False, False)

# Card Frame
card = tk.Frame(root, bg="white", bd=0, relief="flat", padx=30, pady=30)
card.place(relx=0.5, rely=0.5, anchor="center")

# Title
title_label = tk.Label(
    card,
    text="🔐 Password Strength Checker",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    fg="#1a237e"
)
title_label.pack(pady=(0, 10))

# Subtitle
subtitle_label = tk.Label(
    card,
    text="Enter your password below:",
    font=("Segoe UI", 12),
    bg="white",
    fg="#444"
)
subtitle_label.pack()

# Entry field
entry = tk.Entry(card, font=("Segoe UI", 14), width=28, show="*", relief="solid", bd=1)
entry.pack(pady=(15, 5))
entry.bind("<KeyRelease>", check_password_strength)

# Show password toggle
show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(
    card,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password,
    bg="white",
    font=("Segoe UI", 10)
)
show_password_check.pack()

# Strength result
result_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 13, "bold"),
    bg="white"
)
result_label.pack(pady=(15, 5))

# Tips section
tips_title = tk.Label(
    card,
    text="💡 Tips for a Strong Password:",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    fg="#0d47a1"
)
tips_title.pack(pady=(15, 2))

tips_text = (
    "• Use at least 8 characters\n"
    "• Include UPPERCASE and lowercase letters\n"
    "• Add numbers (0–9)\n"
    "• Use symbols like @, #, $, %, etc."
)
tips_label = tk.Label(
    card,
    text=tips_text,
    font=("Segoe UI", 10),
    bg="white",
    justify="left",
    fg="#333"
)
tips_label.pack()

# Run loop
root.mainloop()
