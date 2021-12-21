with open('input.txt', 'r') as f:
    algo, image = f.read().split('\n\n')
    image = [list(x) for x in image.split('\n')]
    rows = len(image)
    cols = len(image[0])


def find_neighbors(x, y):
    neighbors = []
    x_vals = [-1, 0, +1]
    y_vals = [-1, 0, +1]
    for x2 in x_vals:
        for y2 in y_vals:
            if (y + y2 >= 0 and x + x2 >= 0 and y + y2 < cols and x + x2 < rows):
                neighbors.append(image[x + x2][y + y2])
    return neighbors


def get_img_binary(pixels):
    img_binary = []
    for px in pixels:
        if px == '.':
            img_binary.append('0')
        elif px == '#':
            img_binary.append('1')
    return ''.join(img_binary)


def get_output_pixel(binary):
    decimal = int(binary, 2)
    return algo[decimal]
