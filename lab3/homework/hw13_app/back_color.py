from random import *

def is_inside(p, r):
    x_p = p[0]
    y_p = p[1]
    x_r_0 = r[0]
    y_r_0 = r[1]
    width = r[2]
    height = r[3]
    x_r_1 = x_r_0 + width
    y_r_1 = y_r_0 + height
    delta_x_0 = abs(x_p - x_r_0)
    delta_x_1 = abs(x_p - x_r_1)
    delta_y_0 = abs(y_p - y_r_0)
    delta_y_1 = abs(y_p - y_r_1)
    if delta_x_0 + delta_x_1 == width and delta_y_0 + delta_y_1 == height:
        return True
    else:
        return False

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes 

def generate_quiz():
    text = choice([dic['text'].upper() for dic in shapes])
    color = choice([dic['color'] for dic in shapes])
    quiz_type = randint(0, 1)
    return [
                text,
                color,
                quiz_type # randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    p = [x, y]
    text = text.lower()
    if quiz_type == 0:
        rect = [dic['rect'] for dic in shapes if dic['text'] == text][0]
    else:
        rect = [dic['rect'] for dic in shapes if dic['color'] == color][0]
    if is_inside(p,rect): 
        return True
    else:
        return False
