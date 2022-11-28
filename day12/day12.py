# Modifying global scope

enemies = 1

# Bad idea - don't mess with global scope locally
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# Better idea - provide a return statement and assign function to the variable.
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies() * 10

print(f"enemies outside function: {enemies}")