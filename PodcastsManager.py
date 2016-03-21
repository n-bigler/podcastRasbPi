# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:06:40 2016

@author: nico
"""

import vlc
import os
from Podcast import Podcast
import pdb

DOWNLOAD_DIRECTORY = 'podcasts'


class PodcastsManager:
    
    def __init__(self):
        current_directory = '/home/nico/Documents/prjects/workingFiles/podcastRasbPi'
        self.download_directory = current_directory + os.sep + DOWNLOAD_DIRECTORY
        self.titles = {}
        self.media = list()
        self.media.append(Podcast("Forum", DOWNLOAD_DIRECTORY + os.sep + 'Forum-La1?re'))
        self.titles['forum'] = 0
        self.media.append(Podcast("Le journal horaire",  DOWNLOAD_DIRECTORY + os.sep + 'LeJournalhoraire-La1?re'))
        self.titles['journal'] = 1
        self.media.append(Podcast("La librairie francophone",  DOWNLOAD_DIRECTORY + os.sep + 'LaLibrairiefrancophone-La1\?re'))
        self.titles['librairie'] = 2
        
        self.vlcInstance = vlc.Instance()
        self.player = self.vlcInstance.media_player_new()


        
    def load(self, media_name):
        ind_title = self.titles[media_name]
        self.media[ind_title].load(self.vlcInstance, self.player)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
