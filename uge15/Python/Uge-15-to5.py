# -*- coding: utf-8 -*-r
import re
#https://docs.python.org/2/howto/regex.html#regex-howto
#https://docs.python.org/2/library/re.html
'''
15to5 Skriv et program som indlæser en streng bestående af vilkårlige tegn og ved hjælp af re-
gulæreudtryk og Python modulet re finder alle forekomster af tegn fra en delmængde af tegn,
eksempelvis {a,b,c}, i strengen og ignorere alle andre tegn..
'''
print 'her'


taste = raw_input("Indtast data:")
print taste

print 'nr -1',re.split(r'[ ]', taste)

#print 'nr 0',re.match("^[a,b,c]*$", taste)
#print 'nr 1',re.compile('\abc+')
#print 'nr 2',re.match('abc', taste) # matches

#patt = re.compile(r'hat')
print 'nr 10', re.search(r'[abc]+', taste)
