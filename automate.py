# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:05:34 2021

@author: svaag
"""
from selenium import webdriver

web = webdriver.chrome()
web.get('https://smartoblat.trondheimparkering.no/accounts/login/?next=/')
