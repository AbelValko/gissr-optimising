"""
Surface Volume and CSV Processor 
Original Author: Yuki Miura
Source: https://github.com/ym2540/GIS_FloodSimulation

This code generates Surface Volume .csv files that are used in the Flood Estimate code, taking DEM .TIFF files divided by division and DEM files that have been grouped with the two .TIFF files to the south and north of them. The resulting .csv files contain the volume of water above the surface of the DEM at different heights in increments of 0.25m betwwen 0-3m and in increments of 0.5m from 3.5-6.5m. This processor also creates a folder called "Intermediate Data" which can be deleted after the code has completely run.

"""

# noqa: E702


# built-in packages within python that you have to input to run certain functions
import arcpy as ap
import scipy as sp
import numpy as np
import pandas as pd
import os
import csv
import glob
import re

num_divs = 18  # however many divisions the DEM is divided into

#  Ungrouped Divs
#  Inputs to these cells are the DEMs that have been cut into divisions.

#  Surface Volume Processor

#  Process for 0-5m at 0.25 m intervals for each div.
ele_0_txt = "\\ele_0.txt"; ele_1_txt = "\\ele_1.txt"; ele_2_txt = "\\ele_2.txt"
ele_3_txt = "\\ele_3.txt"; ele_4_txt = "\\ele_4.txt"; ele_5_txt = "\\ele_5.txt"
ele_0_5_txt = "\\ele_0_5.txt"; ele_1_5_txt = "\\ele_1_5.txt"; ele_2_5_txt = "\\ele_2_5.txt" 
ele_3_5_txt = "\\ele_3_5.txt"; ele_4_5_txt = "\\ele_4_5.txt"
ele_0_25_txt = "\\ele_0_25.txt"; ele_1_25_txt = "\\ele_1_25.txt"; ele_2_25_txt = "\\ele_2_25.txt" 
ele_3_25_txt = "\\ele_3_25.txt"; ele_4_25_txt = "\\ele_4_25.txt"
ele_0_75_txt = "\\ele_0_75.txt"; ele_1_75_txt = "\\ele_1_75.txt"; ele_2_75_txt = "\\ele_2_75.txt" 
ele_3_75_txt = "\\ele_3_75.txt"; ele_4_75_txt = "\\ele_4_75.txt"

for i in range(num_divs):
    
    #  this creates the destination folder for the txt files to go into if it hasn't been created yet
    #  you can comment this out if the folders have been created since it takes a while to run
    divfolder = r"IntermediateData\newtext\div (%d)" % i
    if not os.path.exists(divfolder):
        os.makedirs(divfolder)
    
    #  this says what folder we want it to go into
    ap.env.workspace = divfolder
    
    #  this says what DEM we want to use in the Surface Volume function. 
    #  These are your input DEM files
    #  Change these to the ones relevant to your area of interest
    dem_lm = r"Data\LM_div18\dem_lm_z35_%d.TIF" % i

    # Process: Surface Volume
    # this performs Surface Volume on the DEM at the specified points.
    ap.SurfaceVolume_3d(dem_lm, ele_0_txt, "BELOW", "0", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_txt, "BELOW", "1", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_txt, "BELOW", "2", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_txt, "BELOW", "3", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_txt, "BELOW", "4", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_txt, "BELOW", "5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_5_txt, "BELOW", "0.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_5_txt, "BELOW", "1.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_5_txt, "BELOW", "2.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_5_txt, "BELOW", "3.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_5_txt, "BELOW", "4.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_25_txt, "BELOW", "0.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_25_txt, "BELOW", "1.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_25_txt, "BELOW", "2.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_25_txt, "BELOW", "3.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_25_txt, "BELOW", "4.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_75_txt, "BELOW", "0.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_75_txt, "BELOW", "1.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_75_txt, "BELOW", "2.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_75_txt, "BELOW", "3.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_75_txt, "BELOW", "4.75", "1", "0")

# Process for 0-10m at 0.5m intervals
ele_0_txt = "\\ele_0.txt"; ele_2_txt = "\\ele_2.txt"; ele_4_txt = "\\ele_4.txt" 
ele_6_txt = "\\ele_6.txt"; ele_8_txt = "\\ele_8.txt"; ele_10_txt = "\\ele_10.txt"
ele_1_txt = "\\ele_1.txt"; ele_3_txt = "\\ele_3.txt"; ele_5_txt = "\\ele_5.txt" 
ele_7_txt = "\\ele_7.txt"; ele_9_txt = "\\ele_9.txt"
ele_0_5_txt = "\\ele_0_5.txt"; ele_2_5_txt = "\\ele_2_5.txt"; ele_4_5_txt = "\\ele_4_5.txt" 
ele_6_5_txt = "\\ele_6_5.txt"; ele_8_5_txt = "\\ele_8_5.txt"
ele_1_5_txt = "\\ele_1_5.txt"; ele_3_5_txt = "\\ele_3_5.txt"; ele_5_5_txt = "\\ele_5_5.txt" 
ele_7_5_txt = "\\ele_7_5.txt"; ele_9_5_txt = "\\ele_9_5.txt"
    
for i in range(num_divs):
    
    # this creates the destination folder for the txt files to go into if it hasn't been created yet
    # you can comment this out if the folders have been created since it takes a while to run
    divfolder = r"IntermediateData\newtextlarge\div (%d)" % i
    if not os.path.exists(divfolder):
        os.makedirs(divfolder)
    
    # this says what folder we want the txt files to go into
    ap.env.workspace = divfolder
    
    # this says what DEM we want to use in the Surface Volume function
    # These are your input DEM files 
    # Change these to the ones relevant to your area of interest 
    dem_lm = r"Data\LM_div18\dem_lm_z35_%d.TIF" % i
    
    # Process: Surface Volume
    # this performs Surface Volume on the DEM at the specified points.
    ap.SurfaceVolume_3d(dem_lm, ele_0_txt, "BELOW", "0", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_txt, "BELOW", "2", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_txt, "BELOW", "4", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_6_txt, "BELOW", "6", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_8_txt, "BELOW", "8", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_10_txt, "BELOW", "10", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_txt, "BELOW", "1", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_txt, "BELOW", "3", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_txt, "BELOW", "5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_7_txt, "BELOW", "7", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_9_txt, "BELOW", "9", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_5_txt, "BELOW", "0.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_5_txt, "BELOW", "2.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_5_txt, "BELOW", "4.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_6_5_txt, "BELOW", "6.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_8_5_txt, "BELOW", "8.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_5_txt, "BELOW", "1.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_5_txt, "BELOW", "3.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_5_txt, "BELOW", "5.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_7_5_txt, "BELOW", "7.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_9_5_txt, "BELOW", "9.5", "1", "0")

# TXT to CSV Maker

# Create csv files for each div for 0-5m at 0.25m intervals
surfacevolumefolder = r"IntermediateData\NewUngroupedSmallSurfaceVolume"
if not os.path.exists(surfacevolumefolder):
    os.makedirs(surfacevolumefolder)
    
for div in range(num_divs):
    l = []
    
    files = glob.glob(r'IntermediateData\newtext\div (%d)\*.txt' % div)      # glob shoves all the text files into one container

    for file in files:
        f = open(file, 'r')
        for i, line in enumerate(f):     # read through our list of text files as a series of strings
            s = line.split(',')         # split up the strings
            result = re.findall(r"[-+]?\d*\.\d+|\d+", s[-1])        # grabs floating point numbers out of strings, which is always the last item in the string
            l.append(result)
        f.close()

    x = []  # heights
    y = []  # volumes
    for i in range(len(l)):             # the dummy list, l, has the values we want stored as every other item in the list
        if(i % 2 == 1):                     # so we need this mod 2 to get those indices
            y.append(float(l[i][0]))
            x.append(i / 8 - .125)           # this fixes the incrementation of the heights

    y = sorted(y)
    z = zip(x, y)  # with the volumes sorted we can now tie all the values together with their respective reference heights

    small_ungrouped_csv = r'IntermediateData\NewUngroupedSmallSurfaceVolume\LMN_div18_new_ungrouped_small_div{:02d}.csv'.format(div)
    with open(small_ungrouped_csv, 'w') as out:  # naming the CSV you're trying to create
        write = csv.writer(out)
        write.writerow(['height', 'volume'])
        for i in list(z):
            write.writerow(i)

# Create csv files for each div from 0-10 m at 0.5m intervals
surfacevolumefolder = r"IntermediateData\NewUngroupedSmallSurfaceVolume"
if not os.path.exists(surfacevolumefolder):
    os.makedirs(surfacevolumefolder)
    
for div in range(num_divs):
    l = []
    
    files = glob.glob(r'IntermediateData\newtext\div (%d)\*.txt' % div)      # g lob shoves all the text files into one container

    for file in files:
        f = open(file, 'r')
        for i, line in enumerate(f):     # read through our list of text files as a series of strings
            s = line.split(',')         # split up the strings
            result = re.findall(r"[-+]?\d*\.\d+|\d+", s[-1])        # grabs floating point numbers out of strings, which is always the last item in the string
            l.append(result)
        f.close()

    x = []  # heights
    y = []  # volumes
    for i in range(len(l)):             # the dummy list, l, has the values we want stored as every other item in the list
        if(i % 2 == 1):                     # so we need this mod 2 to get those indices
            y.append(float(l[i][0]))
            x.append(i / 8 - .125)           # this fixes the incrementation of the heights

    y = sorted(y)
    z = zip(x, y)  # with the volumes sorted we can now tie all the values together with their respective reference heights

    small_ungrouped_csv = r'IntermediateData\NewUngroupedSmallSurfaceVolume\LMN_div18_new_ungrouped_small_div{:02d}.csv'.format(div)
    with open(small_ungrouped_csv, 'w') as out:  # naming the CSV you're trying to create
        write = csv.writer(out)
        write.writerow(['height', 'volume'])
        for i in list(z):
            write.writerow(i)

# Creates csv files for each div from 0-10 m at 0.5m intervals
surfacevolumefolder = r"IntermediateData\NewUngroupedLargeSurfaceVolume"
if not os.path.exists(surfacevolumefolder):
    os.makedirs(surfacevolumefolder)

for div in range(num_divs):
   
    l=[]
    
    files = glob.glob(r'IntermediateData\newtextlarge\div (%d)\*.txt'%div)      #glob shoves all the text files into one container

    for file in files:
        f = open(file,'r')
        for i,line in enumerate(f):     #read through our list of text files as a series of strings
            s = line.split(',')         #split up the strings
            result = re.findall(r"[-+]?\d*\.\d+|\d+", s[-1])        #grabs floating point numbers out of strings, which is always the last item in the string
            l.append(result)
        f.close()

    x = [] #heights
    y = [] #volumes
    
    
    for i in range(len(l)):             #the dummy list, l, has the values we want stored as every other item in the list
        if(i%2==1):                     #so we need this mod 2 to get those indices

            y.append(float(l[i][0]))
            x.append(i/4 - .25)           #this fixes the incrementation of the heights

    y = sorted(y)
    z = zip(x,y) #with the volumes sorted we can now tie all the values together with their respective reference heights

    large_ungrouped_csv = r'IntermediateData\NewUngroupedLargeSurfaceVolume\LMN_div18_new_ungrouped_large_div_{:02d}.csv'.format(div)
    with open(large_ungrouped_csv,'w') as out: #naming the CSV you're trying to create
        write = csv.writer(out)
        write.writerow(['height','volume'])
        for i in list(z):
            write.writerow(i)

# CSV Combiner
#This produces 1 csv file for each of the divs in your area of interest. Now we can put NewSurfaceVolumeCombined into the Flood Estimate code!
totalsurfacevolumefolder = r"Data\NewSurfaceVolumeCombined"
if not os.path.exists(totalsurfacevolumefolder):
    os.makedirs(totalsurfacevolumefolder)

for div in range(num_divs): #does it for each div

    combined_csv = []
    
    #taking 0 to 3 in increments of 0.25
    small_ungrouped_csv = r'IntermediateData\NewUngroupedSmallSurfaceVolume\LMN_div18_new_ungrouped_small_div{:02d}.csv'.format(div)
    
    with open(small_ungrouped_csv, newline='') as File:  
        small_reader = csv.reader(File)
        small_countrow = 0
        for small_row in small_reader:
            if small_countrow < 27 and small_row != []:
                combined_csv.append(small_row)
            small_countrow+=1

    #taking 3.5 to 6.5 in increments of 0.5
    large_ungrouped_csv = r'IntermediateData\NewUngroupedLargeSurfaceVolume\LMN_div18_new_ungrouped_large_div_{:02d}.csv'.format(div)
    
    with open(large_ungrouped_csv, newline='') as File:  
        large_reader = csv.reader(File)
        large_countrow = 0
        for large_row in large_reader:
            if large_countrow > 14 and large_countrow < 32  and large_row != []:
                combined_csv.append(large_row)
            large_countrow+=1

#combined csv is now a list with header and 20 values of height

#now we create a new csv
###################################### Change name of file here * #################################
    combined_ungrouped_csv = r'Data\NewSurfaceVolumeCombined\LMN_div18_new_{:02d}.csv'.format(div)
    with open(combined_ungrouped_csv,'w') as out:
        write = csv.writer(out)
        for i in list(combined_csv):
            write.writerow(i)

# Grouped Divs
# Inputs to these cells are DEMs that have been grouped using ArcGIS's Mosaic to Raster tool with the 2 divisions north of them and the 2 divisions south of them. The name of the DEM is the centermost division.

# Surface Volume Processor
# Process for 0-5m at 0.25 m intervals for each div
ele_0_txt = "\\ele_0.txt"; ele_1_txt = "\\ele_1.txt"; ele_2_txt = "\\ele_2.txt" 
ele_3_txt = "\\ele_3.txt"; ele_4_txt = "\\ele_4.txt"; ele_5_txt = "\\ele_5.txt"
ele_0_5_txt = "\\ele_0_5.txt"; ele_1_5_txt = "\\ele_1_5.txt"; ele_2_5_txt = "\\ele_2_5.txt" 
ele_3_5_txt = "\\ele_3_5.txt"; ele_4_5_txt = "\\ele_4_5.txt"
ele_0_25_txt = "\\ele_0_25.txt"; ele_1_25_txt = "\\ele_1_25.txt"; ele_2_25_txt = "\\ele_2_25.txt" 
ele_3_25_txt = "\\ele_3_25.txt"; ele_4_25_txt = "\\ele_4_25.txt"
ele_0_75_txt = "\\ele_0_75.txt"; ele_1_75_txt = "\\ele_1_75.txt"; ele_2_75_txt = "\\ele_2_75.txt" 
ele_3_75_txt = "\\ele_3_75.txt"; ele_4_75_txt = "\\ele_4_75.txt"

for i in range(num_divs):
    
    #this creates the destination folder for the txt files to go into if it hasn't been created yet
    #you can comment this out if the folders have been created since it takes a while to run
    divfolder = r"IntermediateData\newtextgrouped\div (%d)"%i
    if not os.path.exists(divfolder):
        os.makedirs(divfolder)
    
    #this says what folder we want it to go into
    ap.env.workspace = divfolder
    
    #this says what DEM we want to use in the Surface Volume function
    #####These are your input DEM files################################
    #####Change these to the ones relevant to your area of interest####
    dem_lm = r"Data\LM_div18_grouped\groupRaster_{:02d}.TIF".format(i)

    # Process: Surface Volume
    # this performs Surface Volume on the DEM at the specified points.
    ap.SurfaceVolume_3d(dem_lm, ele_0_txt, "BELOW", "0", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_txt, "BELOW", "1", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_txt, "BELOW", "2", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_txt, "BELOW", "3", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_txt, "BELOW", "4", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_txt, "BELOW", "5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_5_txt, "BELOW", "0.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_5_txt, "BELOW", "1.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_5_txt, "BELOW", "2.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_5_txt, "BELOW", "3.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_5_txt, "BELOW", "4.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_25_txt, "BELOW", "0.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_25_txt, "BELOW", "1.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_25_txt, "BELOW", "2.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_25_txt, "BELOW", "3.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_25_txt, "BELOW", "4.25", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_75_txt, "BELOW", "0.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_75_txt, "BELOW", "1.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_75_txt, "BELOW", "2.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_75_txt, "BELOW", "3.75", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_75_txt, "BELOW", "4.75", "1", "0")
    
# Process for 0-10m at 0.5m intervals
ele_0_txt = "\\ele_0.txt"; ele_2_txt = "\\ele_2.txt"; ele_4_txt = "\\ele_4.txt" 
ele_6_txt = "\\ele_6.txt"; ele_8_txt = "\\ele_8.txt"; ele_10_txt = "\\ele_10.txt"
ele_1_txt = "\\ele_1.txt"; ele_3_txt = "\\ele_3.txt"; ele_5_txt = "\\ele_5.txt" 
ele_7_txt = "\\ele_7.txt"; ele_9_txt = "\\ele_9.txt"
ele_0_5_txt = "\\ele_0_5.txt"; ele_2_5_txt = "\\ele_2_5.txt"; ele_4_5_txt = "\\ele_4_5.txt" 
ele_6_5_txt = "\\ele_6_5.txt"; ele_8_5_txt = "\\ele_8_5.txt"
ele_1_5_txt = "\\ele_1_5.txt"; ele_3_5_txt = "\\ele_3_5.txt"; ele_5_5_txt = "\\ele_5_5.txt" 
ele_7_5_txt = "\\ele_7_5.txt"; ele_9_5_txt = "\\ele_9_5.txt"
    
for i in range(num_divs):
    
    #this creates the destination folder for the txt files to go into if it hasn't been created yet
    #you can comment this out if the folders have been created since it takes a while to run
    divfolder = r"IntermediateData\newtextgroupedlarge\div (%d)"%i
    if not os.path.exists(divfolder):
        os.makedirs(divfolder)
    
    #this says what folder we want the txt files to go into
    ap.env.workspace = divfolder
    
    #this says what DEM we want to use in the Surface Volume function
    #####These are your input DEM files################################
    #####Change these to the ones relevant to your area of interest####
    dem_lm = r"Data\LM_div18_grouped\groupRaster_{:02d}.TIF".format(i)
    
    
    # Process: Surface Volume
    # this performs Surface Volume on the DEM at the specified points.
    ap.SurfaceVolume_3d(dem_lm, ele_0_txt, "BELOW", "0", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_txt, "BELOW", "2", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_txt, "BELOW", "4", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_6_txt, "BELOW", "6", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_8_txt, "BELOW", "8", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_10_txt, "BELOW", "10", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_txt, "BELOW", "1", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_txt, "BELOW", "3", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_txt, "BELOW", "5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_7_txt, "BELOW", "7", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_9_txt, "BELOW", "9", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_0_5_txt, "BELOW", "0.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_2_5_txt, "BELOW", "2.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_4_5_txt, "BELOW", "4.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_6_5_txt, "BELOW", "6.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_8_5_txt, "BELOW", "8.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_1_5_txt, "BELOW", "1.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_3_5_txt, "BELOW", "3.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_5_5_txt, "BELOW", "5.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_7_5_txt, "BELOW", "7.5", "1", "0")
    ap.SurfaceVolume_3d(dem_lm, ele_9_5_txt, "BELOW", "9.5", "1", "0")

# TXT to CSV Maker

# Creates csv files for each div for 0-5m at 0.25m intervals
surfacevolumefolder = r"IntermediateData\NewGroupedSmallSurfaceVolume"
if not os.path.exists(surfacevolumefolder):
    os.makedirs(surfacevolumefolder)
    
for div in range(num_divs):
    l=[]
    
    files = glob.glob(r'IntermediateData\newtextgrouped\div (%d)\*.txt'%div)      #glob shoves all the text files into one container

    for file in files:
        f = open(file,'r')
        for i,line in enumerate(f):     #read through our list of text files as a series of strings
            s = line.split(',')         #split up the strings
            result = re.findall(r"[-+]?\d*\.\d+|\d+", s[-1])        #grabs floating point numbers out of strings, which is always the last item in the string
            l.append(result)
        f.close()

    x = [] #heights
    y = [] #volumes
    for i in range(len(l)):             #the dummy list, l, has the values we want stored as every other item in the list
        if(i%2==1):                     #so we need this mod 2 to get those indices
            y.append(float(l[i][0]))
            x.append(i/8 - .125)           #this fixes the incrementation of the heights

    y = sorted(y)
    z = zip(x,y) #with the volumes sorted we can now tie all the values together with their respective reference heights

    small_grouped_csv = r'IntermediateData\NewGroupedSmallSurfaceVolume\LMN_div18_new_grouped_small_div{:02d}.csv'.format(div)
    with open(small_grouped_csv,'w') as out: #naming the CSV you're trying to create
        write = csv.writer(out)
        write.writerow(['height','volume'])
        for i in list(z):
            write.writerow(i)

#Creates csv files for each div from 0-10 m at 0.5m intervals
surfacevolumefolder = r"IntermediateData\NewGroupedLargeSurfaceVolume"
if not os.path.exists(surfacevolumefolder):
    os.makedirs(surfacevolumefolder)

for div in range(num_divs):
   
    l=[]
    
    files = glob.glob(r'IntermediateData\newtextgroupedlarge\div (%d)\*.txt'%div)      #glob shoves all the text files into one container

    for file in files:
        f = open(file,'r')
        for i,line in enumerate(f):     #read through our list of text files as a series of strings
            s = line.split(',')         #split up the strings
            result = re.findall(r"[-+]?\d*\.\d+|\d+", s[-1])        #grabs floating point numbers out of strings, which is always the last item in the string
            l.append(result)
        f.close()

    x = [] #heights
    y = [] #volumes
    
    
    for i in range(len(l)):             #the dummy list, l, has the values we want stored as every other item in the list
        if(i%2==1):                     #so we need this mod 2 to get those indices

            y.append(float(l[i][0]))
            x.append(i/4 - .25)           #this fixes the incrementation of the heights

    y = sorted(y)
    z = zip(x,y) #with the volumes sorted we can now tie all the values together with their respective reference heights

    large_grouped_csv = r'IntermediateData\NewGroupedLargeSurfaceVolume\LMN_div18_new_grouped_large_div_{:02d}.csv'.format(div)
    with open(large_grouped_csv,'w') as out: #naming the CSV you're trying to create
        write = csv.writer(out)
        write.writerow(['height','volume'])
        for i in list(z):
            write.writerow(i)

# CSV Combiner
totalsurfacevolumefolder = r"Data\NewSurfaceVolumeGrouped"
if not os.path.exists(totalsurfacevolumefolder):
    os.makedirs(totalsurfacevolumefolder)

for div in range(num_divs): #does it for each div

    combined_csv = []
    
    #taking 0 to 3 in increments of 0.25
    small_grouped_csv = r'IntermediateData\NewGroupedSmallSurfaceVolume\LMN_div18_new_grouped_small_div{:02d}.csv'.format(div)
    
    with open(small_grouped_csv, newline='') as File:  
        small_reader = csv.reader(File)
        small_countrow = 0
        for small_row in small_reader:
            if small_countrow < 27 and small_row != []:
                combined_csv.append(small_row)
            small_countrow+=1

    #taking 3.5 to 6.5 in increments of 0.5
    large_grouped_csv = r'IntermediateData\NewGroupedLargeSurfaceVolume\LMN_div18_new_grouped_large_div_{:02d}.csv'.format(div)
    
    with open(large_grouped_csv, newline='') as File:  
        large_reader = csv.reader(File)
        large_countrow = 0
        for large_row in large_reader:
            if large_countrow > 14 and large_countrow < 32  and large_row != []:
                combined_csv.append(large_row)
            large_countrow+=1

#combined csv is now a list with header and 20 values of height

#now we create a new csv
############################just change the name of this guy here * ######################################
    combined_grouped_csv = r'Data\NewSurfaceVolumeGrouped\LMN_div18_new_grouped_{:02d}.csv'.format(div)
    with open(combined_grouped_csv,'w') as out:
        write = csv.writer(out)
        for i in list(combined_csv):
            write.writerow(i)
# This produces 1 "grouped" csv file for each of the divs in your area of interest. Now we can put NewSurfaceVolumeGrouped into the Flood Estimate code!