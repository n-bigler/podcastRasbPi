#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:29:09 2016

@author: nico
"""




import Tkinter as tk
import pdb
from PodcastsManager import PodcastsManager

class PodcastRabPi(tk.Tk):

    def __init__(self, root):
        tk.Tk.__init__(self, root)
        self.root = root
        self.initialize()
        self.manager = PodcastsManager()
    
    def initialize(self):
        self.geometry('800x600')
        self.grid()
        

        buttonForum = tk.Button(self, text='Forum', command=self.loadMedia)
        buttonForum.grid(padx=10, column=0, row=0, sticky='EW')
        buttonPause = tk.Button(self, text='Pause', command=self.pausePlaying)
        buttonPause.grid(padx=10, column=1, row=1, sticky='EW')
        buttonPlay = tk.Button(self, text='Play', command=self.playPlaying)
        buttonPlay.grid(padx=10, column=2, row=1, sticky='EW')
        buttonStop = tk.Button(self, text='Stop', command=self.stopPlaying)
        buttonStop.grid(padx=10, column=0, row=1, sticky='EW')
    
    def loadMedia(self):
        #play forum
        self.manager.load('forum')
        self.manager.play()
        
    def stopPlaying(self):
        self.p.stop()
        
    def pausePlaying(self):
        self.p.pause()
            
    def playPlaying(self):
        self.p.play()

if __name__ == "__main__":
    app = PodcastRabPi(None)
    app.title('Podcast RabPi v0.1')
    app.mainloop()
