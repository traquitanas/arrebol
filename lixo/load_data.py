import os
from setuptools.config import read_configuration

setup_cfg = os.path.join(os.path.dirname('.'), 'setup.py')
if os.path.isfile(setup_cfg):
    print('yes')

    for kwargs in read_configuration(setup_cfg).values():
    #     #setup_cfg_data.update(kwargs)
        #print(kwargs)
        pass

