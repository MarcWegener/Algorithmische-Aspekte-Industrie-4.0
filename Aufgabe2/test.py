import math


points = [(3.3310697,-1.1350884),
(17.757551,-0.58846694),
(34.999565,-0.7697443),
(54.452972,-2.8673427),
(70.94716,-3.722526),
(77.51356,4.201349),
(101.124504,4.76613),
(-4.7994227,16.010006),
(20.375952,9.998167),
(32.570896,14.798522),
(47.68654,10.720342),
(64.773155,9.875),
(79.594025,10.967927),
(98.04866,13.247571),
(-5.326403,22.989153),
(21.134417,33.172714),
(34.493576,31.603687),
(52.9735,30.957943),
(60.51334,25.19242),
(82.310936,23.974655),
(102.05111,32.184616),
(1.6880635,44.02491),
(17.742033,40.14927),
(32.7076,46.562138),
(47.29052,44.853924),
(63.465984,44.992462),
(85.5989,43.30811),
(95.93604,47.88431),
(-2.6570907,54.62206),
(22.03119,51.980846),
(33.884037,56.283737),
(43.955395,50.922295),
(61.23965,61.884884),
(78.85669,51.351536),
(98.027824,59.96266),
(3.73029,67.17839),
(16.350712,72.649155),
(32.59064,70.075584),
(49.654263,66.74712),
(62.867996,70.64556),
(84.39243,67.71635),
(95.53006,67.949814),
(-1.1910756,89.29078),
(18.658268,83.928276),
(31.275661,87.7345),
(52.04865,87.70249),
(68.84127,87.299614),
(84.34114,86.038445),
(95.547554,79.53062),
(-0.58490217,97.39885),
(20.473246,95.27904),
(35.252335,97.781624),
(50.26747,101.64708),
(71.47852,102.93546),
(87.381905,101.39124),
(95.995224,102.18583)]


def merge_sort(arr, coord):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    pointsleft = arr[:mid]
    pointsright = arr[mid:]

    left_sorted = merge_sort(pointsleft, coord)
    right_sorted = merge_sort(pointsright, coord)
    cmbo = merge(left_sorted,right_sorted, coord)
    return cmbo

def merge(A, B, coord):

    i = j = 0
    C = []

    if coord == 'x':
        coord = 0
    elif coord == 'y':
        coord = 1

    while i < len(A) and j < len(B):
        if A[i][coord] <= B[j][coord]:
            C.append(A[i])
            i += 1

        elif B[j][coord] < A[i][coord]:
            C.append(B[j])
            j += 1

    while i < len(A) and j == len(B):
        C.append(A[i])
        i += 1

    while j < len(B) and i == len(A):
        C.append(B[j])
        j += 1

    return C

def first_sort(points):
    Px = merge_sort(points, 'x')
    Py = merge_sort(points, 'y')
    return Px,Py

Px, Py = first_sort(points)

def find_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(arr):
    size = len(arr)
    minimum_distance = find_dist(arr[0], arr[1])
    target_pair = (arr[0], arr[1])

    if len(arr) == 2:
        return find_dist(arr[0], arr[1]), arr[0], arr[1]

    for i in range(0,size):
        for j in range(i+1,size):
            distance = find_dist(arr[i], arr[j])
            if distance < minimum_distance:
                minimum_distance = distance
                target_pair = (arr[i], arr[j])

    return minimum_distance, target_pair
    
def closest_pair(Px,Py):

    if len(Px) <= 3:
        return brute_force(Px)

    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Rx = Px[midpoint_x:]
    median_x = Px[midpoint_x]
    Qy,Ry = [], []

    for point in Py:
        if point[0] < int(median_x[0]):
            Qy.append(point)
        else:
            Ry.append(point)

    min_distance_left = closest_pair(Qx, Qy)
    min_distance_right = closest_pair(Rx, Ry)
    min_distance = min(min_distance_left, min_distance_right)
    x_bar = Qx[-1][0]
    Sy = []

    for y in Py:
        if x_bar - min_distance[0] < y[0] < x_bar + min_distance[0]:
            Sy.append(y)
    
    for i in range(len(Sy) - 1):
        for j in range(i+1, min(i + 7, len(Sy))):
            points = Sy[i]
            points_close = Sy[j]
            dist = find_dist(points, points_close)

            if dist < min_distance[0]:
                min_distance = (dist, points, points_close)

    return min_distance
    
print(closest_pair(Px,Py))


