# python createCrabs.py -i ttHH_UL_samples_2017.csv -o ttHH_full_sys --ntuple

import csv
import os
import shutil
import sys
from subprocess import call
import optparse

"""
USE: python createCrabs.py -i csvFile --ntuple 
"""
usage="usage=%prog [options] \n"
usage+="USE: python createCrabs.py -i csvFile --ntuple  "

parser = optparse.OptionParser(usage=usage)
parser.add_option("-i", "--inputCSV", dest="csvFile",default="ttH_legacy_samples_2018.csv",
        help="Input CSV SampleList", metavar="csvFile")
parser.add_option("-o", "--outname", dest="outName",default="",
        help="Name of Output Folder containing crab configs, default: CSVname+'_configs'", metavar="outName")
parser.add_option("--ntuple", action="store_true", dest="ntuple" ,default=False,
        help="Specifiy, if you want to create crabConfigs for NTupling, default=False. ", metavar="ntuple")
parser.add_option("--systematics", action="store_true", dest="systematics" ,default=False,
        help="Specifiy, if you want to create crabConfigs for systematics, default=False. ", metavar="systs")
parser.add_option("--nsysts", dest="nsysts" ,default=100, type=int,
        help="Specifiy, how many systematic variations should be processed in a single crab job, default=100", metavar="nsysts")
parser.add_option("--runconfig", dest="runconfig" ,default="boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py",
        help="Specifiy the cmsRun config, default=boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py", metavar="runconfig")



(options, args) = parser.parse_args()

# csvfile=open(sys.argv[1],'r') 
csvfile=open(options.csvFile,'r') 
reader = csv.DictReader(csvfile, delimiter=',')
if options.outName=="":
    outname = options.csvFile.partition('.')[0]+"_configs"
else:
    outname = options.outName

# workarea = "crab_skims"
# dbsinstance = "global"
# ntuple=False
# slimmed=False
# ntupletag=""
# cmsoutname = "skim"

# if options.slimmed:
#     ntuple=True
#     slimmed=True
#     workarea = "crab_slims"
#     outname+="_slimmedntuple"
#     ntupletag = "MEM_slimmed_ntuples"
#     cmsoutname = "MEM"

if options.ntuple:
    ntuple = True
    workarea = "crab_ntuple"
    outname+="_ntuple"
    ntupletag = "ntuple"
    dbsinstance = "global"
    cmsoutname = "ntuples"


print outname
os.system("mkdir -p " + outname)

release = "CMSSW_10_6_29"
rel = "106X"

def repl(old,new,filename):
    cmd=" ".join(["sed","-i","'s|"+old+"|"+new+"|g'",filename])
    call(cmd,shell=True)

def get_list_of_systematics(filename):
    systs=[]
    with open(filename,"r") as f:
        systs=f.readlines()
    systs=[s.rstrip('\n') for s in systs]
    systs=[s.rstrip('\t') for s in systs]
    good_systs=[s for s in systs if not (s.startswith("#") or len(s)==0)]
    if len(good_systs) != len(set(good_systs)):
        print "ERROR specifying list of systematics: DUPLICATE ENTRIES"
        sys.exit()
    if not "nominal" in good_systs:
        #print "WARNING: no 'nominal' variation specified...adding it"
        good_systs.insert(0,"nominal")

    print "Systematic variations:"
    for syst in good_systs:
        print "  '"+syst+"'"

    return good_systs

def split_for_systematic_variations(variations,nvariations):
    #print variations
    syst_str = ""
    systs = []
    k=0
    for i in range(len(variations)):
        if(k==nvariations):
            systs.append(syst_str)
            syst_str = ""
            k=0
        if(k==0):
            syst_str = syst_str+variations[i]
        else:
            syst_str = syst_str+","+variations[i]
        k+=1
    if(i==(len(variations)-1) and k!=nvariations):
        systs.append(syst_str)
    return systs


lumimask = ''
for row in reader:
    if not ("#" or "") in row["name"]:
        #print variation_list
        if row['isData']=='FALSE':
            if ntuple and not options.systematics:
                src='common/template_cfg_ntuple.py'
                datasets=row['boosted_dataset'].split(",")
                variation_list = get_list_of_systematics("common/systematicVariationsNone.txt")
                print("Creating crab configs to Ntuple without systs, therefore using common/systematicVariationsNone.txt")
            elif ntuple and options.systematics:
                src='common/template_cfg_ntuple.py'
                datasets=row['boosted_dataset'].split(",")
                variation_list = get_list_of_systematics("common/systematicVariations_new.txt")
                print("Creating crab configs to Ntuple with systs, therefore using common/systematicVariations_new.txt")
        else:
            variations_list = ['nominal']
            src='common/template_cfg_data_ntuple.py'
            variation_list = get_list_of_systematics("common/systematicVariationsNone.txt")
            datasets=row['boosted_dataset'].split(",")
            print("Creating crab configs to Ntuple with systs, therefore using common/systematicVariations_new.txt")
            print(row['run'])
            if row['run'] == '2018':
                lumimask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
            elif row['run'] == '2017':
                lumimask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
            elif row['run'] == "2016preVFP" or row['run'] == "2016postVFP":
                lumimask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'

        variations_list = split_for_systematic_variations(variation_list,options.nsysts)

        for variations,l in zip(variations_list,range(len(variations_list))):
            print "looking at systematic sources ",variations
            for dataset,i in zip(datasets,range(len(datasets))):
                print "looking at dataset ",dataset
                # out='configs_ntuples/'+row['name']+'_'+str(i)+"_"+str(l)+'_crab.py'
                out= outname+'/'+row['name']+'_'+str(i)+"_"+str(l)+'_crab.py'
                filenames = []
                # if ntuple and options.systematics:
                for filename in variations.split(","):
                    if filename=="nominal":
                        filenames.append("ntuples_"+filename+"_Tree.root")
                        filenames.append("ntuples_"+filename+"_Cutflow.txt")
                    else: 
                        filenames.append("ntuples_"+filename+"up"+"_Tree.root")
                        filenames.append("ntuples_"+filename+"up"+"_Cutflow.txt")
                        filenames.append("ntuples_"+filename+"down"+"_Tree.root")
                        filenames.append("ntuples_"+filename+"down"+"_Cutflow.txt")

                shutil.copy(src,out)
                

                if row['isData']=='TRUE':
                    # dataSetTag = 'sl_LEG_NTUPLETAG_DATAERA'
                    splitting = 'EventAwareLumiBased'
                    units = 80000
                    repl('LUMIMASK',lumimask,out)
                else:
                    # dataSetTag = 'sl_skims_MC_'+rel+'_LEG_DATAERA'
                    splitting = 'FileBased'
                    units = '2'


                if ntuple:
                    requestName = row['name']+"_"+row["run"]+"_ntuple_"+str(i)+"_"+str(l)



                repl('THEREQUESTNAME',requestName,out)
                # repl('OUTPUTDATASETTAG',dataSetTag,out)
                repl('THEINPUTDATASET',dataset,out)
                repl('NTUPLETAG',ntupletag,out)
                repl('DATAERA',row['run'],out)
                repl('GLOBALTAG',row['globalTag'],out)
                
                repl('SPLITTING',splitting,out)
                repl('UNITSPERJOB',units,out)

                # repl('SLIMMED',str(slimmed),out)
                # repl('SEEDS',str(slimmed),out)
                #repl('GENERATORNAME',row['generator'],out)
                repl('WEIGHT',row['weight'],out)
                repl('SYSTEMATICVARIATIONS',variations,out)
                repl('RELEASE',release,out)
                repl('OUTPUTFILES',str(filenames).replace("'",'"'),out)
                repl('CMSSWPATH',str(os.environ['CMSSW_BASE']+"/src/BoostedTTH/BoostedAnalyzer/test/"),out)
                repl('RUNCONFIG',options.runconfig,out)
                repl('WORKAREA',workarea,out)
                repl('DBSINSTANCE',dbsinstance,out)
                repl('OUTNAME',cmsoutname,out)

                if row['isData']=='TRUE':

                    repl('ISDATA','True',out)

                if row['isData']=='FALSE':

                    repl('ISDATA','False',out)


                    


