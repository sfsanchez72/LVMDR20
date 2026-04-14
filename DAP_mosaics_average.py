#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


from astropy.table import Table
from astropy.table import vstack as tab_vstack

from lvmdap.dap_tools import list_columns,read_DAP_file,map_plot_DAP,scatter
from matplotlib import use as mpl_use
#mpl_use('Agg')

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import rcParams as rc
rc.update({'font.size': 19,\
           'font.weight': 900,\
           'text.usetex': True,\
           'path.simplify'           :   True,\
           'xtick.labelsize' : 19,\
           'ytick.labelsize' : 19,\
#           'xtick.major.size' : 3.5,\
#           'ytick.major.size' : 3.5,\
           'axes.linewidth'  : 2.0,\
               # Increase the tick-mark lengths (defaults are 4 and 2)
           'xtick.major.size'        :   6,\
           'ytick.major.size'        :   6,\
           'xtick.minor.size'        :   3,\
           'ytick.minor.size'        :   3,\
           'xtick.major.width'       :   1,\
           'ytick.major.width'       :   1,\
           'lines.markeredgewidth'   :   1,\
           'legend.numpoints'        :   1,\
           'xtick.minor.width'       :   1,\
           'ytick.minor.width'       :   1,\
           'legend.frameon'          :   False,\
           'legend.handletextpad'    :   0.3,\
           'font.family'    :   'serif',\
           'mathtext.fontset'        :   'stix',\
           'axes.facecolor' : "w",\
           
          })
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as mpl_colors



# In[2]:


import os
import fnmatch

def find_files(directory, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

def Table_mean_rows(input_table):
    mean_values = {}
    for col in input_table.colnames:
        if np.issubdtype(input_table[col].dtype, np.number):
            mean_values[col] = np.mean(input_table[col])
        else:
            mean_values[col] = None  # Handle non-numeric columns if necessary

        # Create a new table with the computed means
    mean_row = {col: [mean_values[col]] for col in input_table.colnames if mean_values[col] is not None}
    output_table = Table(mean_row)
#    output_table.add_column([''],name='id')
#    output_table.rename_columns(output_table.colnames, input_table.colnames)
    return output_table

#mpl.use('TkAgg')#,warn=False, force=True)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


from astropy.io import fits, ascii
from astropy.table import vstack as tab_vstack


# In[26]:


dap_dir = '/disk-a/sanchez/LVM/LVM/ver_231113/output_ofelia_new/'
pattern = '*.dap.fits.gz'

#list_sel = ('ra','dec','flux_pe_6583.45','flux_pe_6562.85','flux_pe_5006.84')
list_sel = ('ra','dec','flux_pe_6583.41','flux_pe_6562.68','flux_pe_5006.84')

verbose=False
matching_files = find_files(dap_dir, pattern)
I=0
for file in matching_files:
    print(I,file)
    tab_DAP_tmp=read_DAP_file(file,verbose=verbose)
    try:
        tab_DAP_sec=tab_DAP_tmp[list_sel]
        if (I==0):
            tab_DAP = tab_DAP_sec
        else:
            tab_DAP=tab_vstack([tab_DAP,tab_DAP_sec])
        I=I+1        
    except:
        print('Non equal files...')


# In[36]:


dap_dir = '/disk-a/sanchez/LVM/LVM/ver_231113/output_ofelia_new/'
pattern = '*.dap.fits.gz'
DIR_out = 'DAP_0.1.3_mean'
lvmid='mean_DAP'



#list_sel = ('ra','dec','flux_pe_6583.45','flux_pe_6562.85','flux_pe_5006.84')
list_sel = ('ra','dec','flux_pe_6583.41','flux_pe_6562.68','flux_pe_5006.84')

verbose=False
matching_files = find_files(dap_dir, pattern)
I=0
for file in matching_files:
    print(I,file)
    tab_DAP_tmp=read_DAP_file(file,verbose=verbose)
    m_tab_DAP = Table_mean_rows(tab_DAP_tmp)
    m_tab_DAP.add_column([file],name='id')
    a_files = file.split('/')
    file_sec=a_files[-1].replace('lvmSFrame-','')
    file_sec=file_sec.replace('.fits','')
    m_tab_DAP['fiberid']=[file_sec] 
    try:
        tab_DAP_sec=m_tab_DAP[list_sel]        
        if (I==0):
            tab_DAP = tab_DAP_sec
        else:
            tab_DAP=tab_vstack([tab_DAP,tab_DAP_sec])
        I=I+1        
    except:
        print('Non equal files...')



hdu_hdr = fits.PrimaryHDU()
hdu_DAP = fits.BinTableHDU(tab_DAP,name='PT')
hdu_list = fits.HDUList([hdu_hdr,hdu_DAP])#,names=('PRIMARY','FLUX','ERROR','SKY'))
out_file = f'{DIR_out}/{lvmid}.fits'
hdu_list.writeto(out_file,overwrite=True)


