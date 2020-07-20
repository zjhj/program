#!/usr/bin/python3
# -*- coding:utf-8 -*-

from PIL import Image
from selenium import webdriver

import pyocr

screen_file = '/tmp/1.png'
code_file = '/tmp/2.png'

browser = None
try:
	browser = webdriver.Firefox()
	browser.get( 'url_of_oa' )

	# fill the login information
	browser.find_element_by_id('userid').send_keys( 'user_name' )
	browser.find_element_by_id('password').send_keys( 'user_pswd' )
	browser.find_element_by_id('veryCode').click()
	browser.get_screenshot_as_file( screen_file )

	code_img = browser.find_element_by_id('imgObj')
	img_left_x,img_left_y = code_img.location['x'],code_img.location['y']
	img_right_x,img_right_y = img_left_x+code_img.size['width'],img_left_y+code_img.size['height']

	Image.open( screen_file ).crop( (img_left_x,img_left_y,img_right_x,img_right_y) ).save( code_file )

	curr_code = pyocr.get_available_tools()[0].image_to_string( Image.open(code_file) )
	print( "verify code: {}".format(curr_code) )
	browser.find_element_by_id('veryCode').send_keys( curr_code )
	browser.find_element_by_id('goLogin').click()

	# to get address book
	for curr_link in browser.find_elements_by_class_name('eachdata'):
		if curr_link.text == '通讯录':
			curr_link.click()
			break

	for curr_handle in browser.window_handles:
		if curr_handle != browser.current_window_handle:
			browser.switch_to.window( curr_handle )
			if browser.title == 'xxxxxxxx':
				break


except Exception as ex:
	print( ex )
finally:
	if browser is not None:
		#browser.close()
		pass
