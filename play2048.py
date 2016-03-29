from selenium import webdriver
#imports the module that will allow you to use Selenium
from selenium.webdriver.common.keys import Keys
#imports the module that will allow you to use the up, down, left, and right keys on your keyboard

def play2048( times ):
    browser = webdriver.Firefox()
    browser.get('https://gabrielecirulli.github.io/2048/')
    #opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    htmlElem = browser.find_element_by_tag_name('html')
    #calls browser.find_element_by_tag_name('html') so to send keys to the general web pag
    for num in range(times):
        #uses the parameter 'times' to determine how many times the code will try to play the game
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        #for each 'time', the code presses these keys in this order: UP, RIGHT, DOWN, LEFT

    elem = browser.find_element_by_class_name('score-container')
    #finds the element in which the score is contained
    print(elem.text)
    #prints the final score after all tries to the screen

    
