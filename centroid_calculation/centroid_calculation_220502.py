# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:45:28 2022

@author: user
"""
#REF
#https://blog.csdn.net/KindleKin/article/details/121318530?spm=1035.2023.3001.6557&utm_medium=distribute.pc_relevant_bbs_down_v2.none-task-blog-2~default~OPENSEARCH~Rate-2.pc_relevant_bbs_down_v2_default&depth_1-utm_source=distribute.pc_relevant_bbs_down_v2.none-task-blog-2~default~OPENSEARCH~Rate-2.pc_relevant_bbs_down_v2_default

import numpy as np
import pandas as pd

def cal_area(vertices): #Gauss's area formula
    A = 0.0
    point_p = vertices[1]
    for point in vertices:
        A += (point[1]*point_p[0] - point[0]*point_p[1])
        point_p = point
    return abs(A)/2


def cal_centroid(points):
    A = cal_area(points)
    c_x, c_y = 0.0, 0.0
    point_p = points[-1] # point_p means the previous vertex
    for point in points:
        c_x +=((point[0] + point_p[0]) * (point[1]*point_p[0] - point_p[1]*point[0]))
        c_y +=((point[1] + point_p[1]) * (point[1]*point_p[0] - point_p[1]*point[0]))
        point_p = point
        
    return c_x / (6*A), c_y / (6*A)

def read_file(filename):
    points = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'x, y' in line:
                continue
            x, y = line.strip().split(',') # strip \n and then split comma
            x = float(x)
            y = float(y)
            points.append([x, y])
        print(points)
    return points #上方只完成print proudct, 還需要把值return到product

#points = [[-1., -1.], [-2., -1.], [-2., -2.], [-1., -2.] ]
#points = np.array(points)
#points = [(832,1093),(810,1121),(787,1156),(827,1173),(838,1167),(858,1157),(873,1132),(873,1107),(832,1093)]

points = read_file('points.csv')
#points = list(map(int, points2))
print(points)

centroid = cal_centroid(points)
print(centroid)

#centroid2 = cal_centroid(points2)
#print(centroid2)

# =============================================================================
# fr = open("points.csv", 'r')
# frw =open("points_w.csv", 'w')
# 
# line = fr.readlines()
#     for L in line:
#         string = L.strip("\n").split(",")
#         a = np.float64(string[0])
#         b = np.float64(string[0])
#         
#         str = '%f,%f\n' % (a,b)
#         print(str)
#         frw.write(str)
# 
# frw.close()        
# fr.close()
# =============================================================================

 
print(points)
print(type(points[0][0]))

# =============================================================================
# points = np.array(points)
# x, y = cal_centroid(points)
# print('x : ', x, 'y : ', y)
# =============================================================================

##2-----------------------------
# =============================================================================
# def centroid(vertexes):
#      _x_list = [vertex [0] for vertex in vertexes]
#      _y_list = [vertex [1] for vertex in vertexes]
#      _len = len(vertexes)
#      _x = sum(_x_list) / _len
#      _y = sum(_y_list) / _len
#      return(_x, _y)
#  
#     
# polygon_data = [[-1., -1.], [-2., -1.], [-2., -2.], [-1., -2.] ]
# print(centroid(polygon_data)) # (0.5, 0.5)
# =============================================================================
