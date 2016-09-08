from __future__ import division
import numpy as np
from scipy import linalg as lin
from math import sqrt


class vector(object):
	def __init__(self, p1, p2, v1, v2, s):
		self.p1=p1
		self.p2=p2
		self.v1=v1
		self.v2=v2
		self.s=s

	def __str__(self):
		pass

	def len(self):
		""" the lenght of a vector"""
		return np.linalg.norm(self.v1+self.v2)
	def scale(self, s):
		"""Scaling of a vector"""
		m_v1 = (self.v1/len(v1))*s
		m_v2 = (self.v1/len(v1))*s
