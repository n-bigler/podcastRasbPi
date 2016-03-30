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
        self.geometry('480x320+0+0')
        # make it cover the entire screen
        #w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        #self.overrideredirect(1)
        #self.geometry("%dx%d+0+0" % (w, h))
        #self.grid()

        frame_podcasts = tk.Frame(self)
        

        buttonForum = tk.Button(frame_podcasts, text="Forum", font=('Arial', 14, 'bold'),  command=self.loadForum)
        buttonForum.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5)

        buttonJournal = tk.Button(frame_podcasts, text='Le Journal', font=('Arial', 14, 'bold'), command=self.loadJournal)
        buttonJournal.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5)

        buttonLibrairie = tk.Button(frame_podcasts, text="La Librairie\nFrancophone", font=('Arial', 14, 'bold'), command=self.loadLibrairie)
        buttonLibrairie.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5)

        buttonLa1ereLive = tk.Button(frame_podcasts, text="La 1ère\nlive", font=('Arial', 14, 'bold'), command=self.loadLa1ereLive)
        buttonLa1ereLive.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=5)



        frame_podcasts.pack(side=tk.TOP, fill=tk.BOTH, expand=1, pady=5)

        frame_button = tk.Frame(self)

        stop_image = tk.PhotoImage(file='images/stop.gif')
        buttonStop = tk.Button(frame_button, height=120, image=stop_image, command=self.stopPlaying)
        buttonStop.image = stop_image
        buttonStop.pack(fill=tk.BOTH, expand=1, side=tk.LEFT, padx=5)

        pause_image = tk.PhotoImage(file='images/pause.gif')
        buttonPause = tk.Button(frame_button, height=120,  image=pause_image, command=self.pausePlaying)
        buttonPause.image = pause_image
        buttonPause.pack(fill=tk.BOTH, expand=1, side=tk.LEFT, padx=5)

        play_image = tk.PhotoImage(file='images/play.gif')
        buttonPlay = tk.Button(frame_button, height=120,  image=play_image, command=self.playPlaying)
        buttonPlay.image = play_image
        buttonPlay.pack(fill=tk.BOTH, expand=1, side=tk.LEFT,padx=5)

        next_image = tk.PhotoImage(file='images/next.gif')
        buttonNext = tk.Button(frame_button, height=120,  image=next_image, command=self.nextPlaying)
        buttonNext.image = next_image
        buttonNext.pack(fill=tk.BOTH, expand=1, side=tk.LEFT, padx=5)

        frame_button.pack(side=tk.TOP, fill=tk.BOTH, expand=1, pady=5)

    def loadForum(self):
        self.loadMedia('forum')

    def loadJournal(self):
        self.loadMedia('journal')

    def loadLibrairie(self):
        self.loadMedia('librairie')

    def loadLa1ereLive(self):
        self.loadMedia('la1erelive')
    
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
