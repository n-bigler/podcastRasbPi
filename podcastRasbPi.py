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
        

        buttonForum = tk.Button(self, text='Forum', command=self.loadForum)
        buttonForum.grid(padx=10, column=0, row=0, sticky='EW')
        buttonForum = tk.Button(self, text='Journal', command=self.loadJournal)
        buttonForum.grid(padx=10, column=1, row=0, sticky='EW')
        buttonForum = tk.Button(self, text='La librairie francophone', command=self.loadLibrairie)
        buttonForum.grid(padx=10, column=2, row=0, sticky='EW')
        buttonStop = tk.Button(self, text='Stop', command=self.stopPlaying)
        buttonStop.grid(padx=10, column=0, row=1, sticky='EW')
        buttonPause = tk.Button(self, text='Pause', command=self.pausePlaying)
        buttonPause.grid(padx=10, column=1, row=1, sticky='EW')
        buttonPlay = tk.Button(self, text='Play', command=self.playPlaying)
        buttonPlay.grid(padx=10, column=2, row=1, sticky='EW')
        buttonNext = tk.Button(self, text='Next', command=self.nextPlaying)
        buttonNext.grid(padx=10, column=3, row=1, sticky='EW')


    def loadForum(self):
        self.loadMedia('forum')

    def loadJournal(self):
        self.loadMedia('journal')

    def loadLibrairie(self):
        self.loadMedia('librairie')
    
    def loadMedia(self, name):
        #play forum
        self.manager.load(name)
        self.manager.play()
        
    def stopPlaying(self):
        self.manager.stop()
        
    def pausePlaying(self):
        self.manager.pause()
            
    def playPlaying(self):
        self.manager.play()

    def nextPlaying(self):
        self.manager.next()


if __name__ == "__main__":
    app = PodcastRabPi(None)
    app.title('Podcast RabPi v0.1')
    app.mainloop()
