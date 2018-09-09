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

# Test 

p = [200, 120]
r = [140, 60, 100, 200]
if is_inside(p, r):
    print('Your function is correct!')
else:
    print('Bugs detected!')

