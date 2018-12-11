# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:05:20 2018

@author: wmy
"""

from selenium.webdriver import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import time

class EssayWriter(object):
    
    def __init__(self):
        self.browser = webdriver.Chrome() 
        self.url = 'https://www.pigai.org'
        pass
    
    def open_webpage(self):   
        self.browser.get(self.url)    
        pass
    
    def login(self, username, password):
        user_element = self.browser.find_element_by_xpath("//span[@class='emailContainer']/input")
        pass_element = self.browser.find_element_by_xpath("//input[@name='password']")
        user_element.clear()
        for i in range(len(username)):     
            user_element.send_keys(username[i])
            pass
        pass_element.clear()
        for i in range(len(password)):   
            pass_element.send_keys(password[i])
            pass
        while True:
            try:
                button = self.browser.find_element_by_xpath("//span[@id='ulogin']")
                break
            except:
                time.sleep(0.5)
                pass
            pass
        ActionChains(self.browser).click(button).perform()
        time.sleep(0.1)
        ActionChains(self.browser).release().perform()
        pass
    
    def turn_to_essay(self, essay_id):
        element = self.browser.find_element_by_xpath("//input[@class='sf_txt sf_new']")
        element.clear()
        for i in range(len(essay_id)):     
            element.send_keys(essay_id[i])
            pass
        while True:
            try:
                button = self.browser.find_element_by_xpath("//button[@class='sf_bt']")
                break
            except:
                time.sleep(0.5)
                pass
            pass
        ActionChains(self.browser).click(button).perform()
        time.sleep(0.1)
        ActionChains(self.browser).release().perform()
        pass
    
    def write_title(self, title):
        element = self.browser.find_element_by_xpath("//input[@id='title']")
        element.clear()
        for i in range(len(title)):     
            element.send_keys(title[i])
            pass
        pass
    
    def write_essay(self, essay):
        element = self.browser.find_element_by_xpath("//textarea[@id='contents']")
        element.clear()
        for i in range(len(essay)):     
            element.send_keys(essay[i])
            pass
        pass
        
    pass


writer = EssayWriter()
writer.open_webpage()
writer.login('291201368@qq.com', 'di291201368')    
writer.turn_to_essay('1239349')
title = 'success and luck'
writer.write_title(title)
essay = '''    There is a saying that man proposes, god disposes, which means man plan the things and the rest of the outcome lies in the luck. This saying reflects the connection between hard-work and luck, which is though sometimes we have worked so hard, luck occupies great position, the unexpected things happen and refrain us from succeeding. In order to be successful, people work so hard, they believe they can achieve their goals, but lacking luck stops them achieving their goals. So working hard doesn’t mean bringing people success directly, they just need to try more times, without luck, they still can make their goals. Luck can help people close to success, without hard-work, they can’t be successful. Hard-work and luck make people realize their goals, but without luck, people still can make it by trying more times.
    Since we go to school, we are taught that no pain, no gain, it means that if people want to be successful, they must work hard. But the truth is that not everyone can get what they want, even they work hard so much, but if working hard does not bring success, why should they still need to work hard. In my opinion, working hard doesn’t mean the person can success certainly, success needs more factors, like the time, the luck and other things. There is no doubt that if the person does not work hard and fight for his goal, there is no way for him to get what he wants. Some actors start their career at the very young age, when they are also 40, they become famous suddenly, if they give up, they can’t be waiting for their reputation. So working hard, there is much chance to get succeed.
'''
writer.write_essay(essay)
