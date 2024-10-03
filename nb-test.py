from rm2util.Notebook import Notebook, Page
from rmscene import SceneTree
from rmscene import read_blocks, build_tree
from rmscene.scene_items import Line, Point
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

    import pdb; pdb.set_trace()
    notebook = Notebook(line[:right])
    nb = notebook
    blocks = read_blocks(nb.pagelist[0].content)

    
