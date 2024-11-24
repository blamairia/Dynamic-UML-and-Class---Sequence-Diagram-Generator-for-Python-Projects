import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_class_diagram(input_dir, output_dir, project_name):
    """
    Generate UML class diagrams for a full project folder using Pyreverse.
    """
    if not os.path.exists(input_dir):
        messagebox.showerror("Error", f"The directory {input_dir} does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    os.chdir(output_dir)
    try:
        subprocess.run(
            ["pyreverse", "-o", "png", "-p", project_name, input_dir], check=True
        )
        diagram_path = os.path.join(output_dir, f"classes_{project_name}.png")
        if os.path.exists(diagram_path):
            messagebox.showinfo("Success", f"Class diagram generated: {diagram_path}")
        else:
            messagebox.showerror("Error", "Diagram was not generated.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Pyreverse failed: {e}")


def on_submit():
    input_dir = project_dir_path.get()
    output_dir = output_dir_path.get()
    project_name = project_name_entry.get()

    if not input_dir or not output_dir or not project_name:
        messagebox.showerror("Error", "All fields are required.")
        return

    generate_class_diagram(input_dir, output_dir, project_name)


# GUI Setup
root = tk.Tk()
root.title("UML Generator (Project Folder)")

# Project Directory
tk.Label(root, text="Project Directory:").grid(row=0, column=0, sticky="w")
project_dir_path = tk.Entry(root, width=50)
project_dir_path.grid(row=0, column=1, padx=10)
tk.Button(root, text="Browse", command=lambda: project_dir_path.insert(0, filedialog.askdirectory())).grid(row=0, column=2)

# Output Directory
tk.Label(root, text="Output Directory:").grid(row=1, column=0, sticky="w")
output_dir_path = tk.Entry(root, width=50)
output_dir_path.grid(row=1, column=1, padx=10)
tk.Button(root, text="Browse", command=lambda: output_dir_path.insert(0, filedialog.askdirectory())).grid(row=1, column=2)

# Project Name
tk.Label(root, text="Project Name:").grid(row=2, column=0, sticky="w")
project_name_entry = tk.Entry(root, width=50)
project_name_entry.grid(row=2, column=1, padx=10)

# Submit Button
tk.Button(root, text="Generate", command=on_submit).grid(row=3, column=1, pady=10)

root.mainloop()
