#!/usr/bin/env python
from __future__ import with_statement
import os
import shutil
import sys
import time
from contextlib import closing
from zipfile import ZipFile, ZIP_DEFLATED

def buildCsvName(course, type):
	return "group-" + course + "-" + type + "_report.csv"

def zipdir(basedir, archivename):
	assert os.path.isdir(basedir)
	with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
	    for root, dirs, files in os.walk(basedir):
	        #NOTE: ignore empty directories
	        for fn in files:
	            absfn = os.path.join(root, fn)
	            zfn = absfn[len(basedir)+len(os.sep)-1:] #XXX: relative path
	            z.write(absfn, zfn)

basedir = "/Users/Mike/Downloads"
archivename = (time.strftime("%x")).replace("/", "-") + ".zip"

# TODO: check if folder exists first
gdPath = os.path.join(basedir, "Game Design/")
os.mkdir(gdPath)

groupReportPath = os.path.join(basedir, buildCsvName("1271", "group"))
questReportPath = os.path.join(basedir, buildCsvName("1271", "quest"))
userReportPath = os.path.join(basedir, buildCsvName("1271", "user"))

shutil.move(groupReportPath, gdPath)
shutil.move(questReportPath, gdPath)
shutil.move(userReportPath, gdPath)

# TODO: check if folder exists first
agdPath = os.path.join(basedir, "Advanced Game Design/")
os.mkdir(agdPath)

groupReportPath = os.path.join(basedir, buildCsvName("1293", "group"))
questReportPath = os.path.join(basedir, buildCsvName("1293", "quest"))
userReportPath = os.path.join(basedir, buildCsvName("1293", "user"))

shutil.move(groupReportPath, agdPath)
shutil.move(questReportPath, agdPath)
shutil.move(userReportPath, agdPath)

# TODO: check if folder exists first
tgdPath = os.path.join(basedir, "TEC Game Design/")
os.mkdir(tgdPath)

groupReportPath = os.path.join(basedir, buildCsvName("1312", "group"))
questReportPath = os.path.join(basedir, buildCsvName("1312", "quest"))
userReportPath = os.path.join(basedir, buildCsvName("1312", "user"))

shutil.move(groupReportPath, tgdPath)
shutil.move(questReportPath, tgdPath)
shutil.move(userReportPath, tgdPath)

zipdir(basedir, archivename)

# archivePath = os.path.join("/usr/local/bin/", archivename)
archivePath = os.path.join("/Users/Mike/", archivename)


# move archive to desktop
shutil.move(archivePath, "/Users/Mike/Desktop")
# delete folders from Downloads
shutil.rmtree(gdPath)
shutil.rmtree(agdPath)
shutil.rmtree(tgdPath)
