from __future__ import division

import numpy as np
import os
import brewer2mpl
import matplotlib.colors as col
import matplotlib.cm as cm


def set_ticks(ax, color):
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    for line in ax.xaxis.get_ticklines():
        line.set_color(color)
    for line in ax.yaxis.get_ticklines():
        line.set_color(color) 
    ax.tick_params(which = 'minor', color = color)   

    
def get_output_path(homedir):
    thisrun = os.path.basename(os.path.normpath(os.getcwd()))
    outdir = homedir+'/Production/athena/figures/'+thisrun+'/'
    return outdir

bmap = brewer2mpl.get_map('Paired','Qualitative',5) 
c1 = '0.2'    # gray
c2 = bmap.mpl_colors[1]  # blue 
c3 = bmap.mpl_colors[3]  # green
c4 = bmap.mpl_colors[4]  # light red
c2l = bmap.mpl_colors[0] # light blue
c3l = bmap.mpl_colors[2] # light green
c4d = (.9*c4[0], .9*c4[1], .9*c4[2])  # lighter red  

bmap2 = brewer2mpl.get_map('Oranges','Sequential',5) 
textlightbg = bmap2.mpl_colors[4]

bmap3 = brewer2mpl.get_map('YlOrRd','Sequential',3)
cred = bmap3.mpl_colors[2]
credlight = bmap3.mpl_colors[1]
credlighter = bmap3.mpl_colors[0]
csink = bmap3.mpl_colors[2]

bmap3 = brewer2mpl.get_map('Blues','Sequential',3)
cblue = bmap3.mpl_colors[2]
cbluelight = bmap3.mpl_colors[1]
cbluelighter = bmap3.mpl_colors[0]


"""
old colormap for volume density slices
""
cdict_vol = {'red': ((0.0, 255/255, 255/255),
                     (0.25, 205/255, 205/255),
                     (0.5, 156/255, 156/255),
                     (0.75, 83/255, 83/255),
                     (1.0, 17/255, 17/255)),
           'green': ((0.0, 255/255, 255/255),
                     (0.25, 205/255, 205/255),
                     (0.5, 155/255, 155/255),
                     (0.75, 102/255, 102/255),
                     (1.0, 53/255, 53/255)), 
            'blue': ((0.0, 255/255, 255/255),
                     (0.25, 205/255, 205/255),
                     (0.5, 155/255, 155/255),
                     (0.75, 143/255, 143/255),
                     (1.0, 132/255, 132/255))}
cmapvol = col.LinearSegmentedColormap('my_colormapVD', cdict_vol, N=256, gamma=1.0)
cm.register_cmap(name='nickmapVD', cmap=cmapvol)
"""

"""
colormap for volume density slices
"""
r = 120
g = 130
b = 145
midlo = 0.32  # 0.25 is linear. larger value extends white toward middle
midhi = 0.25   # 0.25 is linear. smaller value extends black toward middle

cdict_vol = {'red': ((0.0, 255/255, 255/255),
                 (0.25, (r+midlo*2*(255-r))/255, (r+midlo*2*(255-r))/255),
                 (0.5, r/255, r/255),
                 (0.75, midhi*r/255, midhi*r/255),
                 (1.0, 0/255, 0/255)),
       'green': ((0.0, 255/255, 255/255),
                 (0.25, (g+midlo*2*(255-g))/255, (g+midlo*2*(255-g))/255),
                 (0.5, g/255, g/255),
                 (0.75, midhi*g/255, midhi*g/255),
                 (1.0, 0/255, 0/255)), 
        'blue': ((0.0, 255/255, 255/255),
                 (0.25, (b+midlo*2*(255-b))/255, (b+midlo*2*(255-b))/255),
                 (0.5, b/255, b/255),
                 (0.75, midhi*b/255, midhi*b/255),
                 (1.0, 0/255, 0/255))}
cmapvol = col.LinearSegmentedColormap('my_colormapVD', cdict_vol, N=256, gamma=1.0)
cm.register_cmap(name='nickmapVD', cmap=cmapvol)



"""
colormap for surface density projections
"""
r = 145
g = 138
b = 130
midlo = 0.4  # 0.25 is linear. larger value extends white toward middle
midhi = 0.23   # 0.25 is linear. smaller value extends black toward middle

cdict_col = {'red': ((0.0, 255/255, 255/255),
                 (0.25, (r+midlo*2*(255-r))/255, (r+midlo*2*(255-r))/255),
                 (0.5, r/255, r/255),
                 (0.75, midhi*r/255, midhi*r/255),
                 (1.0, 0/255, 0/255)),
       'green': ((0.0, 255/255, 255/255),
                 (0.25, (g+midlo*2*(255-g))/255, (g+midlo*2*(255-g))/255),
                 (0.5, g/255, g/255),
                 (0.75, midhi*g/255, midhi*g/255),
                 (1.0, 0/255, 0/255)), 
        'blue': ((0.0, 255/255, 255/255),
                 (0.25, (b+midlo*2*(255-b))/255, (b+midlo*2*(255-b))/255),
                 (0.5, b/255, b/255),
                 (0.75, midhi*b/255, midhi*b/255),
                 (1.0, 0/255, 0/255))}
cmapcol = col.LinearSegmentedColormap('my_colormapSD', cdict_col, N=256, gamma=1.0)
cm.register_cmap(name='nickmapSD', cmap=cmapcol)


"""
color spectrum for sink particles
"""
cdict_sink = {'red': ((0.0, 255/255, 255/255),
                      (1.0, 255/255, 255/255)),
            'green': ((0.0, 223/255, 223/255),
                      (1.0, 105/255, 105/255)),
             'blue': ((0.0, 179/255, 179/255),
                      (1.0, 10/255, 10/255))}  
cmapsink = col.LinearSegmentedColormap('my_colormapSink', cdict_sink, N=256, gamma=1.0)
cm.register_cmap(name='nickmapSink', cmap=cmapsink)    