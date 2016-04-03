# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:44:35 2016

@author: nico
"""

from Media import Media
import vlc
import os
import pdb



class Podcast(Media):
    def __init__(self, name, directory):
        self.name = name
        self.dir = directory
        self.to_play = list()
        
        

    def load(self, Instance, Player):

        #get list of files in folder
        files = os.listdir(self.dir);
        files_sorted = sorted(files, reverse=True)
        last_date = files_sorted[0][0:10]
        del self.to_play[:]
        #--- for forum ---
        #get all files

        for item in files_sorted:
            if item[0:10] == last_date and item[25:29] != "full": #"f" is for full, which is to full 1h mp3
                self.to_play.append(self.dir + os.sep + item)


        #put the files in order
        self.to_play = sorted(self.to_play, key=self.findPosition)

        playlist = Instance.media_list_new(self.to_play)

        Player.set_media_list(playlist)
        return self.to_play[0].split('/')[-1]

    def findPosition(self,item):
        name = item.split(os.sep)[-1]
        position = name.split('-', 1)[1][0]
        return position

        
      
    def play(self):

        return 0
        

    def pause(self):
        return 0
        
        
    def stop(self):
        return 0
        



