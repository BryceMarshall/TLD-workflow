from Notebook import Notebook
# Get script parameters from command line
#import sys
#target = sys.argv[0]
#print(sys.argv)

import glob


filelist = glob.glob("/home/bryce/repos/rm2/TLD-workflow/xochitl/52ab*.metadata")
for line in filelist[:1]:
    left = line.rfind("/") + 1
    right = line.index(".metadata")
    assert type(right) == int
    assert type(left) == int
    basename = line[left:right]

    notebook = Notebook(line[:right])
    nb = notebook

    testjson = nb.pages
    print(testjson)


# If no parameters are provided, use a default target

