import os
# import sys
import optparse
# from jinja2 import Environment, FileSystemLoader
import glob


usage="usage=%prog [options] \n"
usage+="USE: python createCrabs.py -n 1000"

parser = optparse.OptionParser(usage=usage)

parser.add_option("-e", "--dataEra", dest="dataEra", default=2017,
        help="data year of the JABDT training", metavar="dataEra")

# parser.add_option("-i", "--inPath", dest="inPath", default="/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/JABDT/condor",
#         help="Path of input condor files", metavar="inPath")
# parser.add_option("-s", "--step", dest="step", default="skim",
#                   help="Step of the JABDT", metavar="step")

parser.add_option("-p", "--process", dest="process", default="ttbar",
                  help="Process of the card and Name of the Output Folder", metavar="process")

(options, args) = parser.parse_args()



# obtain the input files


inPath = "/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/crab/condor/{}/{}".format(options.dataEra, options.process)


allFiles = sorted(glob.glob(inPath+"/*jdl".format(options.dataEra)))



for i, file in enumerate(allFiles):
    # if i <=100:
    #     os.system("condor_submit " + file)
#     if i > 100:
        os.system("condor_submit " + file)
    

print("finished submitting condor jobs")

