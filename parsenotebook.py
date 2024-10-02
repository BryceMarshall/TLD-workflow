from rmscene.scene_items import Line, Point
from rmscene import SceneTree
from rmscene import read_blocks, build_tree

import rmscene

# Call rmscene to parse the notebook
filename="/home/bryce/repos/rm2/TLD-workflow/xochitl/52abf53a-1998-a7cf-c543-2433a25b5151/be7ee758-11b8-429a-934e-5d12964872d5.rm"

def get_bounding_box(line: Line):
    if not line.points:
        return None
    
    min_x = min(point.x for point in line.points)
    max_x = max(point.x for point in line.points)
    min_y = min(point.y for point in line.points)
    max_y = max(point.y for point in line.points)
    
    return min_x, min_y, max_x, max_y

with open(filename, 'rb') as f:
    tree = SceneTree()
    blocks = read_blocks(f)
    build_tree(tree, blocks)

    with open("output.txt", "w") as text_file:
        for el in tree.walk():
            if el is not None:
                bbox = get_bounding_box(el)
                text_file.write(str(bbox) + "\n")
            else:
                text_file.write("None\n")
