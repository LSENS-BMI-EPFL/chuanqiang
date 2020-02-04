# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:03:08 2020

@author: czhang
"""

# Search and Count function


import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import bokeh.io
import bokeh.plotting
from bokeh.io import output_file, show
from bokeh.layouts import column, row
from bokeh.plotting import figure
import sys
import glob 
import os 
import scipy.io as sio
import numpy as np
import decimal as dc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
from natsort import natsorted, ns
from bokeh.models import Legend
from pathlib import Path
from scipy.stats import norm

performance =np.array([6, 2, 6, 1, 6, 2, 6, 6, 5, 5, 6, 4, 2, 4, 2, 6, 6, 6, 6, 3, 6, 6,
       6, 2, 6, 6, 6, 6, 6, 2, 6, 5, 5, 6, 2, 6, 6, 2, 6, 6, 4, 2, 6, 1,
       6, 4, 6, 4, 5, 5, 2, 6, 4, 4, 4, 6, 5, 2, 3, 6, 2, 6, 6, 4, 6, 2,
       6, 6, 6, 6, 2, 6, 6, 6, 6, 2, 4, 6, 6, 5, 2, 6, 6, 6, 4, 4, 2, 6,
       2, 4, 4, 4, 4, 2, 5, 4, 2, 2, 5, 6, 2, 6, 6, 6, 6, 2, 6, 6, 6, 4,
       4, 2, 6, 2, 5, 6, 6, 2, 6, 5, 6, 4, 2, 3, 6, 6, 4, 6, 4, 4, 4, 4,
       1, 2, 2, 6, 2, 6, 3, 6, 1, 6, 4, 6, 2, 4, 6, 4, 6, 0, 6, 2, 6, 2,
       4, 4, 4, 4, 2, 6, 2, 6, 4, 4, 1, 2, 6, 2, 4, 4, 0, 4, 1, 0, 4, 2,
       4, 4, 2, 4, 4, 2, 5, 1, 2, 5, 5, 4, 4, 1, 2, 2, 4, 2, 2, 4, 6, 2,
       6, 4, 2, 4, 6, 6, 4, 6, 2, 5, 2, 2, 4, 2, 6, 1, 4, 4, 2, 4, 6, 4,
       4, 6, 2, 0, 4, 1, 4, 0, 1, 2, 6, 4, 0, 0, 2, 4, 1, 4, 4, 4, 2, 6,
       2, 6, 4, 4, 2, 6, 1, 2, 6, 4, 0, 0, 4, 4, 4, 0, 4, 2, 6, 6, 1, 4,
       4, 2, 4, 4, 4, 2, 0, 4, 4, 4, 0, 4, 4, 4, 4, 0])

stim= np.array([-2147483648,           1, -2147483648,           1, -2147483648,
                 1, -2147483648, -2147483648,           0,           0,
       -2147483648,           0,           1,           0,           1,
       -2147483648, -2147483648, -2147483648, -2147483648,           1,
       -2147483648, -2147483648, -2147483648,           1, -2147483648,
       -2147483648, -2147483648, -2147483648, -2147483648,           1,
       -2147483648,           0,           0, -2147483648,           1,
       -2147483648, -2147483648,           1, -2147483648, -2147483648,
                 0,           1, -2147483648,           1, -2147483648,
                 0, -2147483648,           0,           0,           0,
                 1, -2147483648,           0,           0,           0,
       -2147483648,           0,           1,           1, -2147483648,
                 1, -2147483648, -2147483648,           0, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1,           0, -2147483648, -2147483648,           0,
                 1, -2147483648, -2147483648, -2147483648,           0,
                 0,           1, -2147483648,           1,           0,
                 0,           0,           0,           1,           0,
                 0,           1,           1,           0, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1, -2147483648, -2147483648, -2147483648,           0,
                 0,           1, -2147483648,           1,           0,
       -2147483648, -2147483648,           1, -2147483648,           0,
       -2147483648,           0,           1,           1, -2147483648,
       -2147483648,           0, -2147483648,           0,           0,
                 0,           0,           1,           1,           1,
       -2147483648,           1, -2147483648,           1, -2147483648,
                 1, -2147483648,           0, -2147483648,           1,
                 0, -2147483648,           0, -2147483648,           1,
       -2147483648,           1, -2147483648,           1,           0,
                 0,           0,           0,           1, -2147483648,
                 1, -2147483648,           0,           0,           1,
                 1, -2147483648,           1,           0,           0,
                 1,           0,           1,           1,           0,
                 1,           0,           0,           1,           0,
                 0,           1,           0,           1,           1,
                 0,           0,           0,           0,           1,
                 1,           1,           0,           1,           1,
                 0, -2147483648,           1, -2147483648,           0,
                 1,           0, -2147483648, -2147483648,           0,
       -2147483648,           1,           0,           1,           1,
                 0,           1, -2147483648,           1,           0,
                 0,           1,           0, -2147483648,           0,
                 0, -2147483648,           1,           1,           0,
                 1,           0,           1,           1,           1,
       -2147483648,           0,           1,           1,           1,
                 0,           1,           0,           0,           0,
                 1, -2147483648,           1, -2147483648,           0,
                 0,           1, -2147483648,           1,           1,
       -2147483648,           0,           1,           1,           0,
                 0,           0,           1,           0,           1,
       -2147483648, -2147483648,           1,           0,           0,
                 1,           0,           0,           0,           1,
                 1,           0,           0,           0,           1,
                 0,           0,           0,           0,           1])

audstim = np.array([-2147483648,           0, -2147483648,           1, -2147483648,
                 0, -2147483648, -2147483648,           0,           0,
       -2147483648,           0,           0,           0,           0,
       -2147483648, -2147483648, -2147483648, -2147483648,           1,
       -2147483648, -2147483648, -2147483648,           0, -2147483648,
       -2147483648, -2147483648, -2147483648, -2147483648,           0,
       -2147483648,           0,           0, -2147483648,           0,
       -2147483648, -2147483648,           0, -2147483648, -2147483648,
                 0,           0, -2147483648,           1, -2147483648,
                 0, -2147483648,           0,           0,           0,
                 0, -2147483648,           0,           0,           0,
       -2147483648,           0,           0,           1, -2147483648,
                 0, -2147483648, -2147483648,           0, -2147483648,
                 0, -2147483648, -2147483648, -2147483648, -2147483648,
                 0, -2147483648, -2147483648, -2147483648, -2147483648,
                 0,           0, -2147483648, -2147483648,           0,
                 0, -2147483648, -2147483648, -2147483648,           0,
                 0,           0, -2147483648,           0,           0,
                 0,           0,           0,           0,           0,
                 0,           0,           0,           0, -2147483648,
                 0, -2147483648, -2147483648, -2147483648, -2147483648,
                 0, -2147483648, -2147483648, -2147483648,           0,
                 0,           0, -2147483648,           0,           0,
       -2147483648, -2147483648,           0, -2147483648,           0,
       -2147483648,           0,           0,           1, -2147483648,
       -2147483648,           0, -2147483648,           0,           0,
                 0,           0,           1,           0,           0,
       -2147483648,           0, -2147483648,           1, -2147483648,
                 1, -2147483648,           0, -2147483648,           0,
                 0, -2147483648,           0, -2147483648,           0,
       -2147483648,           0, -2147483648,           0,           0,
                 0,           0,           0,           0, -2147483648,
                 0, -2147483648,           0,           0,           1,
                 0, -2147483648,           0,           0,           0,
                 0,           0,           1,           0,           0,
                 0,           0,           0,           0,           0,
                 0,           0,           0,           1,           0,
                 0,           0,           0,           0,           1,
                 0,           0,           0,           0,           0,
                 0, -2147483648,           0, -2147483648,           0,
                 0,           0, -2147483648, -2147483648,           0,
       -2147483648,           0,           0,           0,           0,
                 0,           0, -2147483648,           1,           0,
                 0,           0,           0, -2147483648,           0,
                 0, -2147483648,           0,           0,           0,
                 1,           0,           0,           1,           0,
       -2147483648,           0,           0,           0,           0,
                 0,           1,           0,           0,           0,
                 0, -2147483648,           0, -2147483648,           0,
                 0,           0, -2147483648,           1,           0,
       -2147483648,           0,           0,           0,           0,
                 0,           0,           0,           0,           0,
       -2147483648, -2147483648,           1,           0,           0,
                 0,           0,           0,           0,           0,
                 0,           0,           0,           0,           0,
                 0,           0,           0,           0,           0])

whstim= np.array([-2147483648,           1, -2147483648,           0, -2147483648,
                 1, -2147483648, -2147483648,           0,           0,
       -2147483648,           0,           1,           0,           1,
       -2147483648, -2147483648, -2147483648, -2147483648,           0,
       -2147483648, -2147483648, -2147483648,           1, -2147483648,
       -2147483648, -2147483648, -2147483648, -2147483648,           1,
       -2147483648,           0,           0, -2147483648,           1,
       -2147483648, -2147483648,           1, -2147483648, -2147483648,
                 0,           1, -2147483648,           0, -2147483648,
                 0, -2147483648,           0,           0,           0,
                 1, -2147483648,           0,           0,           0,
       -2147483648,           0,           1,           0, -2147483648,
                 1, -2147483648, -2147483648,           0, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1,           0, -2147483648, -2147483648,           0,
                 1, -2147483648, -2147483648, -2147483648,           0,
                 0,           1, -2147483648,           1,           0,
                 0,           0,           0,           1,           0,
                 0,           1,           1,           0, -2147483648,
                 1, -2147483648, -2147483648, -2147483648, -2147483648,
                 1, -2147483648, -2147483648, -2147483648,           0,
                 0,           1, -2147483648,           1,           0,
       -2147483648, -2147483648,           1, -2147483648,           0,
       -2147483648,           0,           1,           0, -2147483648,
       -2147483648,           0, -2147483648,           0,           0,
                 0,           0,           0,           1,           1,
       -2147483648,           1, -2147483648,           0, -2147483648,
                 0, -2147483648,           0, -2147483648,           1,
                 0, -2147483648,           0, -2147483648,           1,
       -2147483648,           1, -2147483648,           1,           0,
                 0,           0,           0,           1, -2147483648,
                 1, -2147483648,           0,           0,           0,
                 1, -2147483648,           1,           0,           0,
                 1,           0,           0,           1,           0,
                 1,           0,           0,           1,           0,
                 0,           1,           0,           0,           1,
                 0,           0,           0,           0,           0,
                 1,           1,           0,           1,           1,
                 0, -2147483648,           1, -2147483648,           0,
                 1,           0, -2147483648, -2147483648,           0,
       -2147483648,           1,           0,           1,           1,
                 0,           1, -2147483648,           0,           0,
                 0,           1,           0, -2147483648,           0,
                 0, -2147483648,           1,           1,           0,
                 0,           0,           1,           0,           1,
       -2147483648,           0,           1,           1,           1,
                 0,           0,           0,           0,           0,
                 1, -2147483648,           1, -2147483648,           0,
                 0,           1, -2147483648,           0,           1,
       -2147483648,           0,           1,           1,           0,
                 0,           0,           1,           0,           1,
       -2147483648, -2147483648,           0,           0,           0,
                 1,           0,           0,           0,           1,
                 1,           0,           0,           0,           1,
                 0,           0,           0,           0,           1])


print(performance)
TrialNumber=len(performance)
print('Total trialnumber: ',TrialNumber)

  # Plot dPrime in a signal based moving average
Aud_standard = 10
Aud_StimCounter = []
Aud_SearchDone = False


Wh_standard = 10
Wh_StimCounter = []
Wh_SearchDone = False


FA_standard = 10
FA_Counter = []
FA_SearchDone = False


WhHitChunk = np.zeros(TrialNumber)                  # Whhit Rate
AudHitChunk =  np.zeros(TrialNumber)                # Audhit Rate
FAChunk =  np.zeros(TrialNumber)                    # FArate
dprime_wh =  np.zeros(TrialNumber)                  # dprime
dprime_aud =  np.zeros(TrialNumber)  

# Note, python has 0 based indexing, while matlab has 1 based indexing.
print('***calculation report starts***')
for k in range(TrialNumber):        
        if (performance[k] == 1 or performance[k] == 3):
            print(k+1, '# trial  was updated.')
            Aud_count=Counter(performance[0:k+1])
            #print(Aud_count)
            if (Aud_count[1]+Aud_count[3]) <= Aud_standard:
                print('*normal update')
                ChunkPer = performance[0 : (k+1)]
                ChunkStim = stim[0 : (k+1)]
                ChunkAuStim = audstim[0 : (k+1)]                              
                if sum((ChunkAuStim == 1)) > 0 :
                    AudHitChunk[k] = sum((ChunkPer == 3))/sum((ChunkAuStim == 1))                
            elif (Aud_count[1]+Aud_count[3]) > Aud_standard:
                for n in reversed(range(0,k)):
                    if not Aud_SearchDone:
                        Aud_count=Counter(performance[n:k+1])
                        if (Aud_count[1]+Aud_count[3]) == Aud_standard:
                            Aud_SearchDone= True
                            print('**searched update')
                            print('**search report position: ', n)
                            ChunkPer = performance[n : (k+1)]
                            ChunkStim = stim[n : (k+1)]
                            ChunkAuStim = audstim[n : (k+1)]
                            # following part I have changed a lot.                
                            if sum((ChunkAuStim == 1)) > 0 :
                                AudHitChunk[k] = sum((ChunkPer == 3))/sum((ChunkAuStim == 1))
                Aud_SearchDone= False  # Note this indent shoud be out of for loop.        
            if AudHitChunk[k] == 1:
                Half_AudHit = 0.5/(sum((ChunkPer == 3)) + sum((ChunkPer == 1)))             
                AudHitChunk[k] = 1-Half_AudHit                
            elif AudHitChunk[k] == 0:            
                Half_AudHit = 0.5/(sum((ChunkPer == 3)) + sum((ChunkPer == 1)))  
                AudHitChunk[k] = Half_AudHit                
            else:
                AudHitChunk[k] = AudHitChunk[k]
        else:            
            AudHitChunk[k]   =  AudHitChunk[k-1]   

print('***Above report for Audio calculation***')
            
for k in range(TrialNumber):        
        if (performance[k] == 0 or performance[k] == 2):
            print(k+1, '# trial  was updated.')
            Wh_count=Counter(performance[0:k+1])
            #print(Aud_count)
            if (Wh_count[0]+Wh_count[2]) <= Wh_standard:
                print('*normal update')
                ChunkPer = performance[0 : (k+1)]
                ChunkStim = stim[0 : (k+1)]
                ChunkWhStim = whstim[0 : (k+1)]                              
                if sum((ChunkWhStim == 1)) > 0 :
                    WhHitChunk[k] = sum((ChunkPer == 3))/sum((ChunkWhStim == 1))                
            elif (Wh_count[0]+Wh_count[2]) > Wh_standard:
                for n in reversed(range(0,k)):
                    if not Wh_SearchDone:
                        Wh_count=Counter(performance[n:k+1])
                        if (Wh_count[0]+Wh_count[2]) == Wh_standard:
                            Wh_SearchDone= True
                            print('**searched update')
                            print('**search report position: ', n)
                            ChunkPer = performance[n : (k+1)]
                            ChunkStim = stim[n : (k+1)]
                            ChunkWhStim = whstim[n : (k+1)]
                            # following part I have changed a lot.                
                            if sum((ChunkWhStim == 1)) > 0 :
                                WhHitChunk[k] = sum((ChunkPer == 2))/sum((ChunkWhStim == 1))
                Wh_SearchDone= False  # Note this indent shoud be out of for loop.        
            if WhHitChunk[k] == 1:
                Half_WhHit = 0.5/(sum((ChunkPer == 2)) + sum((ChunkPer == 1)))             
                WhHitChunk[k] = 1-Half_WhHit                
            elif WhHitChunk[k] == 0:            
                Half_WhHit = 0.5/(sum((ChunkPer == 2)) + sum((ChunkPer == 1)))  
                WhHitChunk[k] = Half_WhHit                
            else:
                WhHitChunk[k] = WhHitChunk[k]
        else:            
            WhHitChunk[k]   =  WhHitChunk[k-1]                   
print('***Above report for Whisker calculation***')

for k in range(TrialNumber):        
        if (performance[k] == 4 or performance[k] == 5):
            print(k+1, '# trial  was updated.')
            FA_count=Counter(performance[0:k+1])            
            if (FA_count[4]+FA_count[5]) <= FA_standard:
                print('*normal update')
                ChunkPer = performance[0 : (k+1)]
                ChunkStim = stim[0 : (k+1)]                                            
                if sum((ChunkStim == 0)) > 0 :
                    FAChunk[k] = sum((ChunkPer == 5))/sum((ChunkStim == 0))                
            elif (FA_count[4]+FA_count[5]) > FA_standard:
                for n in reversed(range(0,k)):
                    if not FA_SearchDone:
                        FA_count=Counter(performance[n:k+1])
                        if (FA_count[4]+FA_count[5]) == FA_standard:
                            FA_SearchDone= True
                            print('**searched update')
                            print('**search report position: ', n)
                            ChunkPer = performance[n : (k+1)]
                            ChunkStim = stim[n : (k+1)]                                           
                            if sum((ChunkStim == 0)) > 0 :
                                FAChunk[k] = sum((ChunkPer == 5))/sum((ChunkStim == 0))
                FA_SearchDone= False  # Note this indent shoud be out of for loop.        
            if FAChunk[k] == 1:
                Half_FAHit = 0.5/(sum((ChunkPer == 5)) + sum((ChunkPer == 4)))             
                FAChunk[k] = 1-Half_FAHit                
            elif FAChunk[k] == 0:            
                Half_FAHit = 0.5/(sum((ChunkPer == 5)) + sum((ChunkPer == 4)))  
                FAChunk[k] = Half_FAHit                
            else:
                FAChunk[k] = FAChunk[k]
        else:            
            FAChunk[k]   =  FAChunk[k-1]   
print('***Above report for FA calculation***')
print('***calculation report finished***')



for k in range(TrialNumber):
    if not ((WhHitChunk[k] == 0) or (FAChunk[k] == 0)):
        if (performance[k] == 0 or performance[k] == 2):
            dprime_wh[k] = norm.ppf(WhHitChunk[k]) - norm.ppf(FAChunk[k])
        else:
            dprime_wh[k]= dprime_wh[k-1]
    else:
        dprime_wh[k] = 0.0

print('***Above report for WhHit Dprime calculation***')


for k in range(TrialNumber):
    if not ((AudHitChunk[k] == 0) or (FAChunk[k] == 0)):
        if (performance[k] == 1 or performance[k] == 3):
            dprime_aud[k] = norm.ppf(AudHitChunk[k]) - norm.ppf(FAChunk[k])
        else:
            dprime_aud[k]= dprime_aud[k-1]
    else:
        dprime_aud[k] = 0.0

print('***Above report for AudHit Dprime calculation***')


print('***calculation report finished***')

# Above dprime calculation definition I don´t understand, needs explaination.
        # change finished on above line
        
    # Using bokeh plot the result
    # Things plotted are: WhHit, AudHit, FA rate and dprime
    # They corresponds to the following variables:
    # WhHitChunk, AudHitChunk and FAChunk
    # dprime
        
p = bokeh.plotting.figure(
width=600,
height=400,
x_axis_label='Trial Number',
y_axis_label='Probability AudHit/WhHit/FA',
x_range=(1, TrialNumber),
title = 'test' + '|' + 'testdate'    
)    

dp = bokeh.plotting.figure(
width=600,
height=400,
x_axis_label='Trial Number',
y_axis_label='dPrime',
x_range=(1, TrialNumber),
title= 'test' + '|' + 'testdate'    
)    

p.yaxis.axis_label_text_font_style = "bold"
p.xaxis.axis_label_text_font_style = "bold"
p.title.align = 'center'

dp.yaxis.axis_label_text_font_style = "bold"
dp.xaxis.axis_label_text_font_style = "bold"
dp.title.align = 'center'


audh = p.line(
x= range(TrialNumber),
y= np.array(AudHitChunk),
line_join='bevel',
line_width=2,
color = 'blue',
)

fa = p.line(
x= range(TrialNumber),
y= np.array(FAChunk),
line_join='bevel',
line_width=2,
color = 'red',
)    
   
whhit = p.line(
x= range(TrialNumber),
y= np.array(WhHitChunk),
line_join='bevel',
line_width=2,
color = 'black',
)

d_wh = dp.line(
x= range(TrialNumber),
y= np.array(dprime_wh),
line_join='bevel',
line_width=2,
color = 'black',
)

d_aud = dp.line(
x= range(TrialNumber),
y= np.array(dprime_aud),
line_join='bevel',
line_width=2,
color = 'blue',
)

legend_dp = Legend(items=[
("AudStim" , [d_aud]),
("WhStim" , [d_wh])
], location="center")


legend_p = Legend(items=[
("AudHit" , [audh]),
("WhHit" , [whhit]),
("FA" , [fa])   
], location="center")

dp.add_layout(legend_dp, 'right')    
dp.legend.click_policy="hide"

p.add_layout(legend_p, 'right')    
p.legend.click_policy="hide"
bokeh.io.show(row(dp,p))

            
            
            