import sys;
#from IPython import get_ipython

#ipython = get_ipython()
#ipython.magic('load_ext autoreload')
#ipython.magic('autoreload')

sys.path.insert(0,'./api')
sys.path.insert(0,'../api')
sys.path.insert(0,'../../api')
sys.path.insert(0,'../../../api')

import qgrid
import pandas as pd

oss_version = 0.41

from oss_hugo.API_Hugo_OSS import API_Hugo_OSS
hugo = API_Hugo_OSS()