################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# throws error due to being outside of the drink_potion() function
print(potion_strength)

# Global Scope

player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()  # must be within local scope to be recognized


print(player_health)

# There is no Block Scope

game_level = 3


def create_enemy():
    enemies = ['Skeleton', 'Zombie', 'Alien']
    if game_level < 5:
        new_enemy = enemies[0]
        # variables created within a function
        # are only avail within that function


print(new_enemy)

# Modifying Global Scope
enemies = 1


def increase_enemies():
    global enemies
    return enemies + 1
    print(f"enemies")

enemies = increase_enemies()
print(enemies)


# Global Constants

PI = 3.14159
URL = "https://google.com"
TWITTER_HANDLE = "@alic"

