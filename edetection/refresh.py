#coding=utf-8
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://114.215.94.141:8081/SITO2000/login.jsp#")