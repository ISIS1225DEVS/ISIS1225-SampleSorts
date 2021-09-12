import os
import sys
file_path = os.path.join(os.path.dirname(__file__), '..')
file_dir = os.path.dirname(os.path.realpath('__file__'))
sys.path.insert(0, os.path.abspath(file_path))
data_dir_prev = file_dir + '/LabSorts-S5-G3/Data/GoodReads/'
data_dir = data_dir_prev.replace('\\','/')
#print(data_dir)

