import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


class Tooltip:
    """
    Tooltip class for displaying hover information.
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20

        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(
            tw, text=self.text, justify="left",
            background="lightyellow", relief="solid", borderwidth=1,
            font=("tahoma", "8", "normal")
        )
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


def generate_class_diagram(input_dir, output_dir, project_name, options):
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
        command = ["pyreverse", "-o", "png", "-p", project_name] + options + [input_dir]
        subprocess.run(command, check=True)

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

    # Gather options from checkboxes
    options = []
    if include_associations.get():
        options.append("-A")
    if include_attributes.get():
        options.append("-S")
    if show_dependencies.get():
        options.append("--show-dependencies")
    if filter_mode_all.get():
        options.append("--filter-mode=ALL")
    if filter_mode_analyze.get():
        options.append("--filter-mode=ANALYZE")
    if filter_mode_special.get():
        options.append("--filter-mode=SPECIAL")
    if verbose_mode.get():
        options.append("--verbose")

    generate_class_diagram(input_dir, output_dir, project_name, options)


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

# Options Section
tk.Label(root, text="Options:").grid(row=3, column=0, sticky="w")

include_associations = tk.BooleanVar()
assoc_cb = tk.Checkbutton(root, text="Include Associations (-A)", variable=include_associations)
assoc_cb.grid(row=4, column=0, columnspan=3, sticky="w")
Tooltip(assoc_cb, "Show associations between classes (e.g., relationships, dependencies).")

include_attributes = tk.BooleanVar()
attr_cb = tk.Checkbutton(root, text="Include Attributes (-S)", variable=include_attributes)
attr_cb.grid(row=5, column=0, columnspan=3, sticky="w")
Tooltip(attr_cb, "Include attributes of classes in the UML diagrams.")

show_dependencies = tk.BooleanVar()
dep_cb = tk.Checkbutton(root, text="Show Dependencies (--show-dependencies)", variable=show_dependencies)
dep_cb.grid(row=6, column=0, columnspan=3, sticky="w")
Tooltip(dep_cb, "Display dependency relationships between classes.")

filter_mode_all = tk.BooleanVar()
filter_all_cb = tk.Checkbutton(root, text="Filter Mode ALL (--filter-mode=ALL)", variable=filter_mode_all)
filter_all_cb.grid(row=7, column=0, columnspan=3, sticky="w")
Tooltip(filter_all_cb, "Include all classes in the UML diagram.")

filter_mode_analyze = tk.BooleanVar()
filter_analyze_cb = tk.Checkbutton(root, text="Filter Mode ANALYZE (--filter-mode=ANALYZE)", variable=filter_mode_analyze)
filter_analyze_cb.grid(row=8, column=0, columnspan=3, sticky="w")
Tooltip(filter_analyze_cb, "Include only classes explicitly referenced in the project.")

filter_mode_special = tk.BooleanVar()
filter_special_cb = tk.Checkbutton(root, text="Filter Mode SPECIAL (--filter-mode=SPECIAL)", variable=filter_mode_special)
filter_special_cb.grid(row=9, column=0, columnspan=3, sticky="w")
Tooltip(filter_special_cb, "Include special classes explicitly imported into the project.")

verbose_mode = tk.BooleanVar()
verbose_cb = tk.Checkbutton(root, text="Verbose Mode (--verbose)", variable=verbose_mode)
verbose_cb.grid(row=10, column=0, columnspan=3, sticky="w")
Tooltip(verbose_cb, "Enable verbose output for detailed debugging information.")

# Submit Button
tk.Button(root, text="Generate", command=on_submit).grid(row=11, column=1, pady=10)

root.mainloop()
