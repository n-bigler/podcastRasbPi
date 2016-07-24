# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:44:35 2016

@author: nico
"""

from Media import Media
import vlc
import os
import pdb
import logging



class Podcast(Media):
    def __init__(self, name, directory):
        self.name = name
        self.dir = directory.rstrip('/');
        self.to_play = list()

        
        

    def load(self, Instance, Player):

        #get list of files in folder
        files = os.listdir(self.dir);
        files_sorted = sorted(files, reverse=True)
        last_date = files_sorted[0][0:8]
        self.to_play = [];

        #--- for forum ---
        #get all files
        if files_sorted[0][12:17] == 'forum':
            
            for item in files_sorted:
                if item[0:8] == last_date and item.split('_')[2] != "full" and item.split('_')[3] != 'rfp': #"f" is for full, which is to full 1h mp3
                    self.to_play.append(item)

            #put the files in order
            self.to_play = sorted(self.to_play, key=self.findPosition)
        else:
            self.to_play[:] = files_sorted

            
        self.to_play_fullpath = [];
        for item in self.to_play:
            self.to_play_fullpath.append(self.dir + os.sep + item)
            logging.debug(self.dir + os.sep + item)
            

        playlist = Instance.media_list_new(self.to_play_fullpath)

        Player.set_media_list(playlist)
        return self.to_play[0].split('/')[-1]

    def findPosition(self,item):
        name = item.split(os.sep)[-1]
        position = name.split('_', 4)
        if position[3] == 'mfp':
            return 10
        
        return int(position[3].split('-')[1])

        
      
    def play(self):

        return 0
        

    def pause(self):
        return 0
        
        
    def stop(self):
        return 0
        



