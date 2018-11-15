import numpy as np

def points_to_vector(p1, p2):
    # convert to numpy array
    p1 = np.array(p1)
    p2 = np.array(p2)
    # create vector from points
    vector = p1 - p2
    return vector

def direction(vector):
    # create unit vector
    u = vector / np.linalg.norm(vector)
    # calc angle
    theta = np.degrees(np.arctan(u[1]/u[0]))
    return theta

