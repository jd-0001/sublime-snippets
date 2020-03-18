import os, ntpath

print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
projects_directory = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "projects")

def get_all_projects():
    projects = []
    for root, dirs, files in os.walk(projects_directory): 
        for file in files:
            if file.endswith(".sublime-project"): 
                projects.append(f"{root}/{str(file)}")

    return projects


# Get all projects
projects = get_all_projects()

# List projects withindex
print("\nAvailable Projects:")
for index, project in enumerate(projects):
    print(f"{index+1}) {os.path.splitext(ntpath.basename(project))[0]}")

# Get user input
selection = input("\nChoose Project Number: ")

# If not valid int raise err
try:
    project_index = int(selection) - 1
except ValueError:
    print("Invalid Project!")
    exit()

# Check selected project is in available projects
try:
    project_to_open = projects[project_index]
except IndexError:
    print("Selected Project doesn't exist!")
    exit()

# Open selected project using index
os.system(f"subl -a --project {project_to_open}")
