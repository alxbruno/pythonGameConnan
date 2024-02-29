import time

print('ig')


def main():
    # Initialize game state
    player_health = 100
    player_hunger = 100
    player_thirst = 100
    player_inventory = []
    current_location = "Wasteland"

    # Game loop
    while True:
        # Display player stats
        print(f"Health: {player_health}, Hunger: {player_hunger}, Thirst: {player_thirst}")
        print(f"Inventory: {player_inventory}")
        print(f"Location: {current_location}")

        # Check for player input
        action = input("What would you like to do? (explore, gather, build, eat, drink, quit): ")

        # Process player input
        if action == "explore":
            print("You explore the area.")
            time.sleep(2)
            print("You find some resources.")
            player_inventory.append("Resource")
        elif action == "gather":
            print("You gather resources.")
            time.sleep(2)
            print("You find some food.")
            player_inventory.append("Food")
        elif action == "build":
            print("You build a shelter.")
            time.sleep(2)
            print("Your shelter is complete.")
        elif action == "eat":
            if "Food" in player_inventory:
                print("You eat some food.")
                time.sleep(2)
                player_inventory.remove("Food")
                player_hunger += 20
            else:
                print("You don't have any food.")
        elif action == "drink":
            if "Water" in player_inventory:
                print("You drink some water.")
                time.sleep(2)
                player_inventory.remove("Water")
                player_thirst += 20
            else:
                print("You don't have any water.")
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action.")

        # Update player stats
        player_hunger -= 5
        player_thirst -= 5

        # Check for game over
        if player_hunger <= 0 or player_thirst <= 0:
            print("You died of hunger or thirst.")
            break

        # Wait for a moment before the next loop iteration
        time.sleep(1)

if __name__ == "__main__":
    main()
    import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Exodus: The Chronicles of the Lost World")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up physics
gravity = (0, 0.1)

# Create player object
player_rect = pygame.Rect(100, 100, 50, 50)
player_color = white

# Main game loop
while True:
    screen.fill(black)

    # Apply gravity to player
    player_rect.y += gravity[1]

    # Check for collisions with ground
    if player_rect.y + player_rect.height > screen_height:
        player_rect.y = screen_height - player_rect.height

    # Draw player
    pygame.draw.rect(screen, player_color, player_rect)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
