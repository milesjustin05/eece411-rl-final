import inspect
import simulator

# variables, functions, classes
for name, value in vars(simulator).items():
    if not name.startswith("__"):
        print(name, "->", type(value).__name__)

# class/attributes for the class
cls = simulator.LogisticsSimulator
print("\nMethods and attributes of LogisticsSimulator:")
for name, value in vars(cls).items():
    if not name.startswith("__"):
        print(" ", name, "->", type(value).__name__)

# functions signatures (parameter names and defaults)
print("\nSignatures:")
for name, fn in inspect.getmembers(cls, inspect.isfunction):
    print(" ", name, inspect.signature(fn))