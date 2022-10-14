from macpath import dirname
import os
import shutil

dir_name = os.path.dirname(os.path.abspath(__file__))
shutil.rmtree(os.path.join(dir_name, 'tracks'))
shutil.rmtree(os.path.join(dir_name, 'plots'))
shutil.rmtree(os.path.join(dir_name, 'action_space'))