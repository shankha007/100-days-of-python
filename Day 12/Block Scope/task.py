game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy)

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

# print(new_enemy) # Will cause error