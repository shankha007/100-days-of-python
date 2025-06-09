# Modifying Global Scope
enemies = 1

def increase_enemies():
    global enemies # Forcing to change global variable
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
