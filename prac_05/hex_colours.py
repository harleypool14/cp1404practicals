COLOUR_CODES = {"aliceblue": "#f0f8ff", "coral": "#ff7f50", "darkorchid": "#9932cc", "forestgreen": "#228b22",
                "goldenrod": "#daa520", "lavender": "#e6e6fa", "maroon": "#800000", "navy": "#000080",
                "plum": "#dda0dd", "salmon": "#fa8072"}

colour = input("Enter a colour name: ").lower()
while colour != "":
    print(f"The code for {colour} is {COLOUR_CODES.get(colour)}")
    colour = input("Enter a colour name: ").lower()

