import dis
import types
import hidden_4

def print_sorted_names():
    # Get the names defined in the module
    module_names = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in module_names if not name.startswith('__')]

    # Print the names in alphabetical order
    for name in sorted(filtered_names):
        print(name)

if __name__ == "__main__":
    # Check if the module is a compiled module
    if isinstance(hidden_4, types.ModuleType):
        # Print the sorted names
        print_sorted_names()
    else:
        print("Error: The provided module is not a compiled module.")
