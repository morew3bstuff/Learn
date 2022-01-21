enemies = 1

def increse_enemies():
    enemies = 2
    print(f"enemies inside function {enemies}.")

increse_enemies()
print(f"enemies outside function {enemies}.")

def drink_potion():
    potion_strength = 3
    print(f"potion strength is {potion_strength}.")

# This will give a name error
# print(f"potion strength is {potion_strength}.")

player_health = 10

def display_player_health():
    # Since player health is a global variable we can use it inside a function
    print(f"player health is {player_health}.")

display_player_health()

# There is no block scope
game_level = 3
enemies_list = ["Zombie", "Alien", "Skeleton"]
if game_level < 5:
    new_enemy = enemies_list[0]
# Variable inside the if block can be used outside of the if block
print(new_enemy)

# Modify global scope
energy = 1
energy_b = 1

def increse_energy():
    # Now it knows we want to work with the global variable, not good practice
    global energy
    energy += 2
    print(f"energy inside function {energy}.")

def increse_energy_b():
    return energy_b + 2

increse_energy()
print(f"energy outside function {energy}.")
print()

# Best option to have the function modify the original value and reassign the value to the variable
energy = increse_energy_b()
print(f"energy outside function {energy}.")