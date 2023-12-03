# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:24:28 2023

@author: Dell
"""
import pandas as pd
# import csv
###############################start-combining-channel-playlist#########################################

csv1 = pd.read_csv("C:/Users/ANSHIKA TANDON/Downloads/testchannel.csv")
csv1.head()

csv2 = pd.read_csv("C:/Users/ANSHIKA TANDON/Downloads/playlistid.csv")
csv2.head()

merged_data = csv1.merge(csv2,on=["channel_id"])
print (merged_data.head())

df = merged_data.head()
df.to_csv("C:/Users/ANSHIKA TANDON/Downloads\\firstleveljoin.csv")

###############################end-combining-channel-playlist#############################################################

###############################start-combining-channel-playlist-video#########################################
csv3 = pd.read_csv("C:/Users/ANSHIKA TANDON/Downloads\\firstleveljoin.csv" )
csv3.head()
print(csv3)

csv4= pd.read_csv("C:/Users/ANSHIKA TANDON/Downloads/video.csv")
csv4.head()

result = pd.merge(csv3, csv4, how="outer", on=["playlist_id"])
print(result)

result.to_csv("C:/Users/ANSHIKA TANDON/Downloads\\secondleveljoin.csv")
###############################end-combining-channel-playlist-video#########################################

