# start with some designs that need to be printed.
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# simulate printing each design, until none are left.
# Move each design to completed_models after printing.

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# Displaying all completed models.
# print("\nThe following models have been printed:")

# for completed_model in completed_models:
#     print(completed_model)


import printing_functions_8_15 as pf


designs_to_print = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

pf.print_models(designs_to_print, completed_models)
pf.show_completed_models(completed_models)