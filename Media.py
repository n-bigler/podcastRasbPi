# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 17:36:45 2016

@author: nico
"""
from abc import ABCMeta, abstractmethod

class Media:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def load(self):
        return
        
    @abstractmethod        
    def play(self):
        return
        
    @abstractmethod
    def pause(self):
        return
        
    @abstractmethod
    def stop(self):
        return