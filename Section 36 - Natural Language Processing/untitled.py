# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 01:17:05 2020

@author: n_kon
"""

""" tsv file is short for Tab Separated File
as opposed to comma separated file . This is useful in reviews
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter = '\t', quoting = 3)
# The quoting above is set to 3 to ignore double quotes

# Clean the texts
# Get rid of useless words and create the bag of words
