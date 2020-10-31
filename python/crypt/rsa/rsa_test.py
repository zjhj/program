#!/usr/bin/python3
#  -*- coding: utf-8 -*-

from Crypto import Random
from Crypto.PublicKey import RSA

r = RSA.importKey( open('pubkey.pem','rb').read() )
print( r.n )
print( r.e )


