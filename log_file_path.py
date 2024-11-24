def parse_trace_log_filtered(log_file_path, output_puml_path):
    """
    Parse the trace log, filter irrelevant interactions, and convert to PlantUML sequence diagram.
    """
    try:
        # Read the log file
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()
        
        # Initialize variables
        interactions = []
        current_caller = "Main"  # Default caller
        object_mapping = {}  # Map module/class to participant

        # Filter only relevant modules/classes
        relevant_classes = {"Student", "Professor", "Course", "Person"}
        
        # Process each line
        for line in lines:
            if "funcname" in line:
                parts = line.split(",")
                if len(parts) >= 2:
                    module_name = parts[0].split(":")[-1].strip()
                    func_name = parts[1].split(":")[-1].strip()

                    # Ignore irrelevant modules/classes
                    if any(rc.lower() in module_name.lower() for rc in relevant_classes):
                        # Determine caller and callee
                        if module_name not in object_mapping:
                            object_mapping[module_name] = f"Object{len(object_mapping)+1}"

                        caller = current_caller
                        callee = object_mapping[module_name]

                        # Add interaction
                        interactions.append((caller, callee, func_name))

                        # Update current caller
                        current_caller = callee

        # Write the PlantUML file
        with open(output_puml_path, "w") as puml_file:
            puml_file.write("@startuml\n")
            # Define participants
            for obj, alias in object_mapping.items():
                puml_file.write(f"participant \"{obj}\" as {alias}\n")

            # Add interactions
            for caller, callee, func_name in interactions:
                puml_file.write(f"{caller} -> {callee}: {func_name}()\n")

            puml_file.write("@enduml\n")
        
        print(f"Sequence diagram saved to {output_puml_path}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    log_file_path = "trace_log.txt"  # Path to your trace log
    output_puml_path = "sequence_diagram_filtered.puml"  # Path to the PlantUML file
    parse_trace_log_filtered(log_file_path, output_puml_path)
