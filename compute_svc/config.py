import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
pb_dir = os.path.join(BASE_DIR, 'pb')
sys.path.append(pb_dir)
cfg = {}
