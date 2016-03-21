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
        
        

    def load(self, Instance, Player):
        #pdb.set_trace()
        media = Instance.media_new(self.dir + os.sep + "test.mp3")
        Player.set_media(media)
        return 0
        
      
    def play(self):

        return 0
        

    def pause(self):
        return 0
        
        
    def stop(self):
        return 0
        
