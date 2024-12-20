def isCorrectRect(points):
     (x1, y1), (x2, y2) = points 
     return x1 < x2 and y1 < y2

class RectCorrectError(Exception):   
    pass

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")

    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2

    return not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некоректный")

    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2

    x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min))
    y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min))

    return x_overlap * y_overlap

def intersectionAreaMultiRect(rectangles):
    total_intersection_area = 0

    for i, rect1 in enumerate(rectangles):
        if not isCorrectRect(rect1):
            raise RectCorrectError(f"{i + 1}й прямоугольник некоректный")
        for rect2 in rectangles[i+1:]:
            total_intersection_area += intersectionAreaRect(rect1, rect2)

    return total_intersection_area
