#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64

def crypt_esab64( plain_data ):
	return base64.b64encode(plain_data)[:-2][::-1]+base64.b64encode(plain_data)[-2:]

def decrypt_esab64( cipher_data ):
	return base64.b64decode( cipher_data[:-2][::-1] + cipher_data[-2:] )
