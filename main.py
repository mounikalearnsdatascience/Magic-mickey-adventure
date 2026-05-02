print("✨ Welcome to Magic Mickey Adventure! ✨")
print("Hey Mickey, can you come out? Your friend is here!")

friendship_points = 0

choice = input("Mickey appears! What would you like to do? (cheese/play/adventure): ").lower()

if choice == "cheese":
    print("🧀 Mickey loves the cheese! Friendship +10")
    friendship_points += 10
elif choice == "play":
    print("🎈 You both play happily together! Friendship +15")
    friendship_points += 15
elif choice == "adventure":
    print("🌟 You go on a magical adventure together! Friendship +20")
    friendship_points += 20
else:
    print("😊 Mickey smiles politely but seems confused.")

print(f"Your final friendship points: {friendship_points}")
print("Thanks for playing Magic Mickey Adventure!")
