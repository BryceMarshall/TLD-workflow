import bisect

def parse_coordinates(coord_str):
    coords = []
    for line in coord_str.strip().split('\n'):
        if line != 'None':
            coords.append(tuple(map(float, line.strip('()').split(','))))
    return coords

def create_grid(coords):
    vertical_lines = []
    horizontal_lines = []
    
    for coord in coords:
        if coord[0] == coord[2]:  # Vertical line
            vertical_lines.append(coord[0])
        elif coord[1] == coord[3]:  # Horizontal line
            horizontal_lines.append(coord[1])
    
    vertical_lines = sorted(set(vertical_lines))
    horizontal_lines = sorted(set(horizontal_lines))
    
    return vertical_lines, horizontal_lines

def find_grid_square(point, vertical_lines, horizontal_lines):
    x, y = point
    
    col = bisect.bisect_right(vertical_lines, x) - 1
    row = bisect.bisect_right(horizontal_lines, y) 
    
    return row, col

def encode_points(points, vertical_lines, horizontal_lines):
    encoded = []
    for point in points:
        x, y = point[0], point[1]
        row, col = find_grid_square((x, y), vertical_lines, horizontal_lines)
        encoded.append(f"({x}, {y}) -> Grid square: ({row}, {col})")
    return encoded


with open('gridlines.txt') as f:
    coord_str = f.read()
coords = parse_coordinates(coord_str)

vertical_lines, horizontal_lines = create_grid(coords)

with open('output.txt') as f:
    coord_str = f.read()
test_points = parse_coordinates(coord_str)

encoded_points = encode_points(test_points, vertical_lines, horizontal_lines)

for point in encoded_points:
    print(point)

