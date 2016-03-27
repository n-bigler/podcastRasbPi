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
        

        forum_image = tk.PhotoImage(file='images/forum.gif')
        buttonForum = tk.Button(self,width=128, height=128, image=forum_image,  command=self.loadForum)
        buttonForum.image = forum_image
        buttonForum.grid(padx=10, column=0, row=0, sticky='EW')

        journal_image = tk.PhotoImage(file='images/journal.gif')
        buttonJournal = tk.Button(self,width=128, height=128, image=journal_image, command=self.loadJournal)
        buttonJournal.image = journal_image
        buttonJournal.grid(padx=10, column=1, row=0, sticky='EW')

        librairie_image = tk.PhotoImage(file='images/librairie.gif')
        buttonLibrairie = tk.Button(self, width=128, height=128, image=librairie_image, command=self.loadLibrairie)
        buttonLibrairie.image = librairie_image
        buttonLibrairie.grid(padx=10, column=2, row=0, sticky='EW')

        stop_image = tk.PhotoImage(file='images/stop.gif')
        buttonStop = tk.Button(self, width=128, height=128, image=stop_image, command=self.stopPlaying)
        buttonStop.image = stop_image
        buttonStop.grid(padx=10, column=0, row=1, sticky='EW')

        pause_image = tk.PhotoImage(file='images/pause.gif')
        buttonPause = tk.Button(self, width=128, height=128, image=pause_image, command=self.pausePlaying)
        buttonPause.image = pause_image
        buttonPause.grid(padx=10, column=1, row=1, sticky='EW')

        play_image = tk.PhotoImage(file='images/play.gif')
        buttonPlay = tk.Button(self, width=128, height=128, image=play_image, command=self.playPlaying)
        buttonPlay.image = play_image
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
