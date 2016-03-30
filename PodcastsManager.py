# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:06:40 2016

@author: nico
"""

import vlc
import os
from Podcast import Podcast
from LiveStream import LiveStream
import pdb

DOWNLOAD_DIRECTORY = 'podcasts'
LIVE_DIRECTORY = 'live'


class PodcastsManager:
    
    def __init__(self):
        current_directory = '/home/nico/Documents/projects/workingFiles/podcastRasbPi'
        self.download_directory = current_directory + os.sep + DOWNLOAD_DIRECTORY
        self.titles = {}
        self.media = list()
        self.media.append(Podcast("Forum", DOWNLOAD_DIRECTORY + os.sep + 'Forum-La1?re'))
        self.titles['forum'] = 0
        self.media.append(Podcast("Le journal horaire",  DOWNLOAD_DIRECTORY + os.sep + 'LeJournalhoraire-La1?re'))
        self.titles['journal'] = 1
        self.media.append(Podcast("La librairie francophone",  DOWNLOAD_DIRECTORY + os.sep + 'Lalibrairiefrancophone-La1?re'))
        self.titles['librairie'] = 2

        self.media.append(LiveStream("La 1ère - Live",   current_directory + os.sep + LIVE_DIRECTORY + os.sep + "mp3_128.m3u"))
        self.titles['la1erelive'] = 3


        self.vlcInstance = vlc.Instance()
        self.player = self.vlcInstance.media_list_player_new()

        
    def load(self, media_name):
        ind_title = self.titles[media_name]
        self.media[ind_title].load(self.vlcInstance, self.player)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        #self.player.release()

    def next(self):
        self.player.next()
