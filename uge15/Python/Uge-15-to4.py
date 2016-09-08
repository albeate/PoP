# -*- coding: utf-8 -*-r
import re
'''
15to4 Skriv et program som ved hjælp af regulæreudtryk og Python modulet re indlæser en streng
bestående af ord og derpå opdeler strengen i ord ved at finde mellemrumstegn og dele strengen
ved disse.
'''
print 'her'


taste = raw_input("Indtast data:")
print taste

print re.split(r'[ ]', taste)
