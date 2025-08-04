import tkinter as tk #Using tkinter library as GUI
from tkinter import messagebox

def calculate_rula():
    try:
        upper_arm = int(entry_upper_arm.get())
        lower_arm = int(entry_lower_arm.get())
        wrist = int(entry_wrist.get())
        neck = int(entry_neck.get())
        trunk = int(entry_trunk.get())

        # Illustrative number only 
        total_score = upper_arm + lower_arm + wrist + neck + trunk

        if total_score <= 5:
            result = f"Score: {total_score} - Acceptable posture"
        elif total_score <= 7:
            result = f"Score: {total_score} - Investigate further"
        else:
            result = f"Score: {total_score} - Immediate change required"

        messagebox.showinfo("RULA Assessment Result", result)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer scores.")

# GUI setup 
app = tk.Tk()
app.title("Ergonomic RULA Assessment")

tk.Label(app, text="Upper Arm Score (1–6):").grid(row=0, column=0, sticky='e')
tk.Label(app, text="Lower Arm Score (1–3):").grid(row=1, column=0, sticky='e')
tk.Label(app, text="Wrist Score (1–4):").grid(row=2, column=0, sticky='e')
tk.Label(app, text="Neck Score (1–6):").grid(row=3, column=0, sticky='e')
tk.Label(app, text="Trunk Score (1–6):").grid(row=4, column=0, sticky='e')

entry_upper_arm = tk.Entry(app)
entry_lower_arm = tk.Entry(app)
entry_wrist = tk.Entry(app)
entry_neck = tk.Entry(app)
entry_trunk = tk.Entry(app)

entry_upper_arm.grid(row=0, column=1)
entry_lower_arm.grid(row=1, column=1)
entry_wrist.grid(row=2, column=1)
entry_neck.grid(row=3, column=1)
entry_trunk.grid(row=4, column=1)

tk.Button(app, text="Calculate RULA Score", command=calculate_rula).grid(row=5, columnspan=2, pady=10)

app.mainloop()