# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:44:35 2016

@author: nico
"""

from Media import Media
import vlc
import os
import pdb



class LiveStream(Media):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        

    def load(self, Instance, Player):
        playlist = Instance.media_list_new()
        # playlist.add_media('http://stream.srg-ssr.ch/m/la-1ere/mp3_128')
        playlist.add_media(self.url)

        Player.set_media_list(playlist)
        # p=Instance.media_player_new() 
        # p.set_mrl('http://stream.srg-ssr.ch/m/la-1ere/mp3_128')
        # p.play()                

        return self.url.split('/')[-1]

      
    def play(self):

        return 0
        

    def pause(self):
        return 0
        
        
    def stop(self):
        return 0
        
