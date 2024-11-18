CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """A Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare two guitars based on their year."""
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage 50+ years old."""
        return self.get_age() >= VINTAGE_AGE
