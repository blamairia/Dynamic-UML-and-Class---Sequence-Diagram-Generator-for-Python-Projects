import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import ast


class ImportExtractor(ast.NodeVisitor):
    """
    Extract imported modules and classes from a Python script.
    """
    def __init__(self):
        self.imports = set()

    def visit_ImportFrom(self, node):
        if node.module:
            for name in node.names:
                self.imports.add(name.name)
        self.generic_visit(node)


def extract_imported_classes(script_path):
    """
    Extract classes and modules imported in the script.
    """
    try:
        with open(script_path, "r") as file:
            tree = ast.parse(file.read())
        extractor = ImportExtractor()
        extractor.visit(tree)
        return extractor.imports
    except Exception as e:
        print(f"Error extracting imports: {e}")
        return set()


def execute_script(input_script, working_dir):
    """
    Run the input script normally to generate the trace log.
    """
    try:
        command = ["python", input_script]
        subprocess.run(command, check=True, cwd=working_dir)
        messagebox.showinfo("Success", f"Script executed successfully. Trace log should be in: {working_dir}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Script execution failed: {e}")


def parse_trace_log(log_file_path, output_puml_path, relevant_classes):
    """
    Parse the trace log and generate a PlantUML sequence diagram.
    """
    try:
        with open(log_file_path, "r") as log_file:
            lines = log_file.readlines()

        interactions = []
        current_caller = "Main"
        object_mapping = {}

        for line in lines:
            if "funcname" in line:
                parts = line.split(",")
                if len(parts) >= 2:
                    module_name = parts[0].split(":")[-1].strip()
                    func_name = parts[1].split(":")[-1].strip()

                    if any(rc.lower() in module_name.lower() for rc in relevant_classes):
                        if module_name not in object_mapping:
                            object_mapping[module_name] = f"Object{len(object_mapping)+1}"

                        caller = current_caller
                        callee = object_mapping[module_name]

                        interactions.append((caller, callee, func_name))
                        current_caller = callee

        with open(output_puml_path, "w") as puml_file:
            puml_file.write("@startuml\n")
            for obj, alias in object_mapping.items():
                puml_file.write(f"participant \"{obj}\" as {alias}\n")

            for caller, callee, func_name in interactions:
                puml_file.write(f"{caller} -> {callee}: {func_name}()\n")

            puml_file.write("@enduml\n")

        messagebox.showinfo("Success", f"Sequence diagram saved: {output_puml_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Parsing failed: {e}")


def generate_sequence_diagram(input_script, output_dir, project_name):
    """
    Combine script execution and parsing to generate a sequence diagram dynamically.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Execute the script to generate the trace log
    execute_script(input_script, os.path.dirname(input_script))

    # Define the trace log path
    trace_log_path = os.path.join(os.path.dirname(input_script), "trace_log.txt")
    if not os.path.exists(trace_log_path):
        messagebox.showerror("Error", f"Trace log not found in: {os.path.dirname(input_script)}")
        return

    # Extract relevant classes from the script
    relevant_classes = extract_imported_classes(input_script)
    if not relevant_classes:
        messagebox.showerror("Error", "No relevant classes found in the script.")
        return

    # Parse the trace log to generate a sequence diagram
    sequence_diagram_path = os.path.join(output_dir, f"{project_name}.puml")
    parse_trace_log(trace_log_path, sequence_diagram_path, relevant_classes)

    # Generate PNG using PlantUML
    try:
        subprocess.run(["plantuml", sequence_diagram_path], check=True)
        messagebox.showinfo(
            "Success", f"Sequence diagram PNG generated: {os.path.join(output_dir, f'{project_name}.png')}"
        )
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"PlantUML generation failed: {e}")


def on_submit():
    input_script = script_path.get()
    output_dir = output_dir_path.get()
    project_name = project_name_entry.get()

    if not input_script or not output_dir or not project_name:
        messagebox.showerror("Error", "All fields are required.")
        return

    generate_sequence_diagram(input_script, output_dir, project_name)


# GUI Setup
root = tk.Tk()
root.title("Universal Sequence Diagram Generator")

# Script Path
tk.Label(root, text="Python Script Path:").grid(row=0, column=0, sticky="w")
script_path = tk.Entry(root, width=50)
script_path.grid(row=0, column=1, padx=10)
tk.Button(
    root, text="Browse", command=lambda: script_path.insert(0, filedialog.askopenfilename())
).grid(row=0, column=2)

# Output Directory
tk.Label(root, text="Output Directory:").grid(row=1, column=0, sticky="w")
output_dir_path = tk.Entry(root, width=50)
output_dir_path.grid(row=1, column=1, padx=10)
tk.Button(
    root, text="Browse", command=lambda: output_dir_path.insert(0, filedialog.askdirectory())
).grid(row=1, column=2)

# Project Name
tk.Label(root, text="Project Name:").grid(row=2, column=0, sticky="w")
project_name_entry = tk.Entry(root, width=50)
project_name_entry.grid(row=2, column=1, padx=10)

# Submit Button
tk.Button(root, text="Generate", command=on_submit).grid(row=3, column=1, pady=10)

root.mainloop()
