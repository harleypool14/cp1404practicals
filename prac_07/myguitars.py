from guitar import Guitar


def main():
    """Main program for guitar collection management."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Loaded guitars:")
    display_guitars(guitars)

    # Add the __lt__ method to the Guitar class for sorting by year
    Guitar.__lt__ = lambda self, other: self.year < other.year

    print("\nSorted by year:")
    guitars.sort()
    display_guitars(guitars)

    # Get new guitars from user
    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar.name} has been added.")
        except ValueError:
            print("Invalid input. Please enter valid numbers for year and cost.")
        name = input("Name: ")

    # Save all guitars back to file
    save_guitars(guitars, filename)
    print("\nGuitars have been saved to", filename)

    print("\nFinal guitar collection:")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, year, cost = line.strip().split(',')
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty guitar list.")
    return guitars


def save_guitars(guitars, filename):
    """Save the guitars to a file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def get_new_guitar():
    """Get guitar details from user and return a Guitar object."""
    print("Enter your new guitar details (or just press Enter to stop)")
    name = input("Name: ")
    if name == "":
        return None

    try:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        return Guitar(name, year, cost)
    except ValueError:
        print("Invalid input. Please enter valid numbers for year and cost.")
        return None


def display_guitars(guitars):
    """Display all guitars."""
    if not guitars:
        print("No guitars to display")
        return

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
