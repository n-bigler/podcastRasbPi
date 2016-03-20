# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 19:29:09 2016

@author: nico
"""
#!/usr/bin/python



import Tkinter as tk
import vlc

class PodcastRabPi(Tkinter.Tk):

    def __init__(self, root):
        Tkinter.Tk.__init__(self, root)
        self.root = root
        self.initialize()
    
    def initialize(self):
        self.geometry('800x600')
        self.grid()
        


        buttonForum = tk.Button(self, text='Forum', command=self.loadForum)
        buttonForum.grid(padx=10, column=0, row=0, sticky='EW')
        buttonPause = tk.Button(self, text='Pause', command=self.pausePlaying)
        buttonPause.grid(padx=10, column=1, row=1, sticky='EW')
        buttonPlay = tk.Button(self, text='Play', command=self.playPlaying)
        buttonPlay.grid(padx=10, column=2, row=1, sticky='EW')
        buttonStop = tk.Button(self, text='Stop', command=self.stopPlaying)
        buttonStop.grid(padx=10, column=0, row=1, sticky='EW')
    
    def loadForum(self):
        #play forum
        self.p = vlc.MediaPlayer("./podcasts/Forum-La-1ère/20160319forum20160319standarddeveloppement-108ed5663d.mp3")
        self.p.play()
        
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
    app.quitApp()