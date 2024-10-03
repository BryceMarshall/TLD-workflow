import questionary
import glob
from rm2util.Notebook import Notebook


def load_files():
    filelist = glob.glob("/home/bryce/repos/rm2/TLD-workflow/xochitl/*.metadata")
    return [load_file(file) for file in filelist]

def load_file(filename):
    left = filename.rfind("/") + 1
    right = filename.rfind(".metadata")
    basename = filename[left:right]
    try:
        return Notebook(filename[:right])
    except:
        print(f"Error loading {basename}")
        return None


notebooks = [nb for nb in load_files() if nb is not None] 

def gettag(notebooks: list[Notebook]):
    tagname = "Coordinate Grid"
    tag = questionary.select("Select a tag", choices=["Coordinate Grid"]).ask()
    notebooks = [nb.get_page_with_tag(tagname) for nb in notebooks]
    print(notebooks)

choice = questionary.select("What would you like to do?", choices=["Access today's notebook", "Get a reference to a grid", "Get a notebook by name"]).ask()

if choice == "Access today's notebook":
    nb = notebooks[0]
    print(nb) 
    print("Notebook accessible at nb")
    pass

elif choice == "Get a reference to a grid":
    gt = gettag(notebooks)
    print(gt)
    pass
elif choice == "Get a notebook by name":
    name = questionary.text("Enter the name of the notebook").ask()
    nb = [nb for nb in notebooks if nb.name == name][0]
    print(nb) 
    print("Notebook accessible at nb")



#tagname = questionary.select("Select a tag", choices=["Coordinate Grid"]).ask()
