import os
import sys
import optparse
from jinja2 import Environment, FileSystemLoader
import glob


usage="usage=%prog [options] \n"
usage+="USE: python createCondors.py -p ttHH -s skim"

parser = optparse.OptionParser(usage=usage)
parser.add_option("-e", "--dataEra", dest="dataEra", default=2017,
        help="data year of the JABDT training", metavar="dataEra")

# parser.add_option("-o", "--outPath", dest="outPath", default="/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/JABDT/condor",
        # help="Path of Output Folder containing condor files, default: 'condor'", metavar="outPath")

parser.add_option("-p", "--process", dest="process", default="ttbar",
                  help="Process of the card and Name of the Output Folder", metavar="process")

parser.add_option("-c", "--cpus", dest="cpus", default=1,
                  help="CPU request", metavar="cpus")

parser.add_option("-m", "--memory", dest="memory", default=20000,
                  help="Memory request", metavar="memory")

parser.add_option("-n", "--numberfile", dest="numberfile", default=20,
                  help="Number of files per job", metavar="numberfile")

# parser.add_option("-d", "--disk", dest="disk", default=5000,
                #   help="Disk request", metavar="disk")

# parser.add_option("-s", "--step", dest="step", default="skim",
#                   help="Step of the JABDT", metavar="step")

(options, args) = parser.parse_args()

SETUP = "cd BoostedTTH/BoostedAnalyzer/test"

DELETE = "rm *root" + "\n" + "rm *txt"

MEMORY = options.memory
# DISK = options.disk
CPU = options.cpus

# obtain the input files

# if options.process == "ttHH":
#     if options.dataEra == 2017:
#         allFiles = sorted(glob.glob(
#             '/eos/uscms/store/group/lpctthrun2/wwei/UL/2017/ntuple/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/sl_LEG_ntuple_2017_2/*/*/*root'))
if options.process == "ttbar":
    if options.dataEra == 2017:
        allFiles = sorted(glob.glob(
            '/eos/uscms/store/group/lpctthrun2/wwei/UL/2017/skim/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/sl_skims_MC_LEG_2017/221014_141722/*/*root'))

outPath = "/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/crab/condor/{}/".format(options.dataEra) + options.process
if not os.path.exists(outPath):
    os.system("mkdir -p " + outPath)


environment = Environment(loader=FileSystemLoader("."))
scriptTemplate = environment.get_template("condor_template.sh")
jdlTemplate = environment.get_template("condor_template.jdl")

OUTDIR = "root://cmseos.fnal.gov//store/user/wwei/UL/2017/ttSL"

# eospath = "root://cmseos.fnal.gov/"

for i, file in enumerate(allFiles):

    inputfile = file.replace("/eos/uscms", "")

    # INFILE = "xrdcp -f " + eospath + file + " ."
    if i % options.numberfile == 0:
        allinputfile = "inputFiles=" + inputfile
    
    else:
        allinputfile += " inputFiles=" + inputfile
    
    if (i+1) % options.numberfile == 0:
        k = (i+1)/options.numberfile
        print("run with every {} files, {} times".format(options.numberfile, k))

        ROOTOUTFILE = "ntuples_{}_nominal_Tree.root".format(k)
        TXTOUTFILE = "ntuples_{}_nominal_Cutflow.txt".format(k)
        
        TRANSFEROUTFILE = "xrdcp -f " + ROOTOUTFILE + " " + OUTDIR + "/" + ROOTOUTFILE + \
            "\n" + "xrdcp -f " + TXTOUTFILE + " " + OUTDIR + "/" + TXTOUTFILE + "\n"

        RUNCOMMAND = "cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py isData=False outName=ntuples_{} maxEvents=999999999 systematicVariations=nominal dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False weight=3.42E-06 systematicVariations=nominal ".format(k) + allinputfile

        scriptFileName = outPath + "/" + options.process + "_ntuple_{}.sh".format(k)
        scriptcontent = scriptTemplate.render(
            # SCRAM_ARCH = SCRAM_ARCH,
            # CMSSW_VERSION = CMSSW_VERSION,
            SETUP = SETUP,
            # INFILE = INFILE,
            RUNCOMMAND = RUNCOMMAND,
            # OUTDIR = OUTDIR,
            TRANSFEROUTFILE=TRANSFEROUTFILE,
            # EVEN_OUTFILE = EVEN_OUTFILE,
            # ODD_OUTFILE = ODD_OUTFILE,
            DELETE = DELETE
        )
        with open(scriptFileName, mode="w") as scriptFile:
            scriptFile.write(scriptcontent)
            print("... wrote {}".format(scriptFileName))

        # for jdl file

        EXECUTABLE = scriptFileName
        FILES = scriptFileName
        OUTFILES = scriptFileName.split(".")[0]

        jdlFileName = outPath + "/" + options.process + "_ntuple_{}.jdl".format(k)
        jdlcontent = jdlTemplate.render(
            MEMORY = MEMORY,
            # DISK = DISK,
            CPU = CPU,
            EXECUTABLE = EXECUTABLE,
            FILES = FILES,
            OUTFILES = OUTFILES
        )
        with open(jdlFileName, mode="w") as jdlFile:
            jdlFile.write(jdlcontent)
            print("... wrote {}".format(jdlFileName))

    if i == len(allFiles) - 1:
        k = i / options.numberfile + 1
        print("run with the last set of files")

        ROOTOUTFILE = "ntuples_{}_nominal_Tree.root".format(k)
        TXTOUTFILE = "ntuples_{}_nominal_Cutflow.txt".format(k)

        TRANSFEROUTFILE = "xrdcp -f " + ROOTOUTFILE + " " + OUTDIR + "/" + ROOTOUTFILE + \
            "\n" + "xrdcp -f " + TXTOUTFILE + " " + OUTDIR + "/" + TXTOUTFILE + "\n"

        RUNCOMMAND = "cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py isData=False outName=ntuples_{} maxEvents=999999999 systematicVariations=nominal dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False weight=3.42E-06 systematicVariations=nominal ".format(k) + allinputfile

        scriptFileName = outPath + "/" + \
            options.process + "_ntuple_{}.sh".format(k)
        scriptcontent = scriptTemplate.render(
            # SCRAM_ARCH = SCRAM_ARCH,
            # CMSSW_VERSION = CMSSW_VERSION,
            SETUP=SETUP,
            # INFILE = INFILE,
            RUNCOMMAND=RUNCOMMAND,
            # OUTDIR = OUTDIR,
            TRANSFEROUTFILE=TRANSFEROUTFILE,
            # EVEN_OUTFILE = EVEN_OUTFILE,
            # ODD_OUTFILE = ODD_OUTFILE,
            DELETE=DELETE
        )
        with open(scriptFileName, mode="w") as scriptFile:
            scriptFile.write(scriptcontent)
            print("... wrote {}".format(scriptFileName))

        # for jdl file

        EXECUTABLE = scriptFileName
        FILES = scriptFileName
        OUTFILES = scriptFileName.split(".")[0]

        jdlFileName = outPath + "/" + \
            options.process + "_ntuple_{}.jdl".format(k)
        jdlcontent = jdlTemplate.render(
            MEMORY=MEMORY,
            # DISK = DISK,
            CPU=CPU,
            EXECUTABLE=EXECUTABLE,
            FILES=FILES,
            OUTFILES=OUTFILES
        )
        with open(jdlFileName, mode="w") as jdlFile:
            jdlFile.write(jdlcontent)
            print("... wrote {}".format(jdlFileName))
