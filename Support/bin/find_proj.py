#!/usr/bin/python

import sys, os.path, re, os

def check(pth):
	# print "Checking:", pth
	return ((os.path.isfile(os.path.join(pth,"build.sbt")) or os.path.isfile(os.path.join(pth,"project/Build.scala")) or
		os.path.isfile(os.path.join(pth,"project/build.properties"))) and os.path.isdir(os.path.join(pth,"src")))

d = sys.argv[1]

while (d != '') and (d != '/'):
	if check(d):
		print d
		exit(0)
	(d, f) = os.path.split(d)

exit(1)
