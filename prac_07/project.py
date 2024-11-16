"""Project class for managing project details."""
import datetime


class Project:
    """Represent a project object."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date() if start_date else None
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than comparison based on priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if project is complete."""
        return self.completion_percentage == 100

    def update(self, completion_percentage="", priority=""):
        """Update completion percentage and priority if provided."""
        if completion_percentage:
            self.completion_percentage = int(completion_percentage)
        if priority:
            self.priority = int(priority)