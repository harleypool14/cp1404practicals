"""
Project management program for tracking projects and their details.
Estimate: 3.5 hours
Time Taken: Around 5 hours (split over a few days)
"""
import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"


def main():
    """Main program for project management."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = input(MENU + "\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        choice = input(MENU + "\n>>> ").lower()

    save_choice = input(f"Would you like to save to {FILENAME}? ")
    if save_choice.lower() != ["no", "n", "no, i think not."]:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename) as file:
        # Skip the header line
        file.readline()
        for line in file:
            parts = line.strip().split('\t')
            # Create Project object from data
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, 'w') as file:
        # Write header
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        # Write data
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                  file=file)


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    print("Incomplete projects: ")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects: ")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after specified date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%y").date()

    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects):
        print(project)


def add_new_project(projects):
    """Get project details from user and add to projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))

    # Convert date format from dd/mm/yy to dd/mm/yyyy for project creation
    date = datetime.datetime.strptime(date_string, "%d/%m/%y")
    date_string_full = date.strftime("%d/%m/%Y")

    project = Project(name, date_string_full, priority, cost_estimate, percent_complete)
    projects.append(project)


def update_project(projects):
    """Update a selected project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percentage, new_priority)


main()
