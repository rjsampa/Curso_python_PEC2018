# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 00:35:35 2018

@author: rafael
"""

import pandas as pd
import seaborn as sas
data = pd.read_csv('IRS.csv')#,encoding='utf-8')
data.describe()

sas.pairplot(data, hue = 'species')

