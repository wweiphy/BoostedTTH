import os
import optparse
import glob

# python haddscript.py -f 221204_test_evaluation_new


usage = "usage=%prog [options] \n"
usage += "USE: python cardmakingscript.py -n True "

parser = optparse.OptionParser(usage=usage)

# parser.add_option("-n", "--new", dest="new", default="new",
#         help="making datacard for new categorizations, total 9", metavar="new")

parser.add_option("-f", "--folder", dest="folder", default="221204_test_evaluation_new",
                  help="folder name", metavar="folder")

(options, args) = parser.parse_args()

# process_new = ['ttHH', 'ttH', 'ttZ', 'ttZH',
#                'ttZZ', 'ttlf', 'ttcc', 'ttmb', 'ttnb']
# process_old = ['ttHH', 'ttH', 'ttZ', 'ttZH',
#                'ttZZ', 'ttlf', 'ttcc', 'ttb','ttbb','tt2b','ttbbb','tt4b']


# syst = [
#   'JESup',
#   'JESdown',
#   'JERup',
#   'JERdown',
#   'JESFlavorQCDup',
#   'JESRelativeBalup',
#   'JESHFup',
#   'JESBBEC1up',
#   'JESEC2up',
#   'JESAbsoluteup',
#   'JESBBEC1yearup',
#   'JESRelativeSampleyearup',
#   'JESEC2yearup',
#   'JESHFyearup',
#   'JESAbsoluteyearup',
#   'JESFlavorQCDdown',
#   'JESRelativeBaldown',
#   'JESHFdown',
#   'JESBBEC1down',
#   'JESEC2down',
#   'JESAbsolutedown',
#   'JESBBEC1yeardown',
#   'JESRelativeSampleyeardown',
#   'JESEC2yeardown',
#   'JESHFyeardown',
#   'JESAbsoluteyeardown',
# ]

allFiles = sorted(
    glob.glob('/eos/uscms/store/group/lpctthrun2/wwei/UL/2017/ntuple/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/sl_LEG_ntuple_2017/221126_052019/0000/ntuples_nominal_Cutflow*')

# print ("doing nominal files")

for file in allFiles:

    file = file.replace("/eos/uscms","")

    command = "xrdcp root://cmseos.fnal.gov/"+file + " ."


    print ("xrdcp files: ")
    print (file)
    # print (command)

    os.system(command)





