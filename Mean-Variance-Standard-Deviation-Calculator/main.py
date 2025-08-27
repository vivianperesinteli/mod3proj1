# Import the function and the test library
import mean_var_std
from unittest import main

# Example usage of function
print("Running calculation with the sample list:")
try:
    result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    import json
    print(json.dumps(result, indent=2))
except ValueError as e:
    print(e)

print("\n" + "="*30 + "\n")

# Automatically runs the unit tests from ttest_module.py 
print("Starting unit tests...")
main(module='test_module', exit=False)
