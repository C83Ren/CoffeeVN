init 0:
    image cg Placeholder = "gui/main_menu.png"

    image cg 1 unscaled = "cg Placeholder"
    image cg 1 = "cg 1 unscaled"
    image cg 2 unscaled = "cg Placeholder"
    image cg 2 = "cg 2 unscaled"

    image cg 3 unscaled = Image("images/BirthdayKohi.png")
    image cg 3 = Transform(ImageReference("cg 3 unscaled"), zoom=0.5)
    image cg BirthdayKohi= "cg 3"

    image cg 4 unscaled = Image("images/hitona_memory.png")
    image cg 4 = "cg 4 unscaled"
    image cg 5 unscaled = "cg Placeholder"
    image cg 5 = "cg 5 unscaled"
    image cg 6 unscaled = "cg Placeholder"
    image cg 6 = "cg 6 unscaled"
    image cg 7 unscaled = "cg Placeholder"
    image cg 7 = "cg 7 unscaled"
    image cg 8 unscaled = "cg Placeholder"
    image cg 8 = "cg 8 unscaled"
    image cg 9 unscaled = "cg Placeholder"
    image cg 9 = "cg 9 unscaled"
    image cg 10 unscaled = "cg Placeholder"
    image cg 10 = "cg 10 unscaled"

    define cg_list = ["Placeholder1", "Placeholder2", "BirthdayKohi", "Placeholder4", "Placeholder5", "Placeholder6", "Placeholder7", "Placeholder8", "Placeholder9"]
