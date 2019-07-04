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
        help="Specifiy, if you want to create crabConfigs for NTupling, default=False. Will use skimmed samples in boosted_datasets column of csvFile", metavar="ntuple")

(options, args) = parser.parse_args()

# csvfile=open(sys.argv[1],'r') 
csvfile=open(options.csvFile,'r') 
reader = csv.DictReader(csvfile, delimiter=',')
if options.outName=="":
    outname = options.csvFile.partition('.')[0]+"_configs"
else:
    outname = options.outName

if options.ntuple:
    outname+="_ntuple"
print outname
os.system("mkdir -p " + outname)

release = "CMSSW_9_4_13"
rel = "94X"

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

    #print "Systematic variations:"
    #for syst in good_systs:
        #print "  '"+syst+"'"

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


 
for row in reader:
    if not ("#" or "") in row["name"]:
        #print variation_list
        if options.ntuple:
            src='common/template_cfg_ntuple.py'
            datasets=row['boosted_dataset'].split(",")
            variation_list = get_list_of_systematics("common/systematicVariations.txt")
            print("Creating crab configs to Ntuple, therefore using common/systematicVariations.txt")
        else:
            src='common/template_cfg.py'
            datasets=row['dataset'].split(",")
            variation_list = get_list_of_systematics("common/systematicVariationsNone.txt")

        variations_list = split_for_systematic_variations(variation_list,100)
        if row['isData']=='True':
            variations_list = ['nominal']
        for variations,l in zip(variations_list,range(len(variations_list))):
            print "looking at systematic sources ",variations
            for dataset,i in zip(datasets,range(len(datasets))):
                print "looking at dataset ",dataset
                # out='configs_ntuples/'+row['name']+'_'+str(i)+"_"+str(l)+'_crab.py'
                out= outname+'/'+row['name']+'_'+str(i)+"_"+str(l)+'_crab.py'
                filenames = []
                for filename in variations.split(","):
                    if filename=="nominal":
                        filenames.append("ntuples_"+filename+"_Tree.root")
                    else: 
                        filenames.append("ntuples_"+filename+"up"+"_Tree.root")
                        filenames.append("ntuples_"+filename+"down"+"_Tree.root")
                shutil.copy(src,out)
                
                if "2018" in row["run"]:
                    release = "CMSSW_10_2_13"
                    rel = "102X"

                if row['isData']=='TRUE':
                    dataSetTag = 'KIT_tthbb_sl_skims_DATA_'+rel+'_LEG_DATAERA'
                    splitting = 'EventAwareLumiBased'
                    units = '80000'
                else:
                    dataSetTag = 'KIT_tthbb_sl_skims_MC_'+rel+'_LEG_DATAERA'
                    splitting = 'FileBased'
                    units = '2'


                repl('THEREQUESTNAME',row['name']+"_"+str(i)+"_"+str(l),out)
                repl('OUTPUTDATASETTAG',dataSetTag,out)
                repl('THEINPUTDATASET',dataset,out)
                repl('DATAERA',row['run'],out)
                repl('GLOBALTAG',row['globalTag'],out)
                repl('ISDATA',row['isData'],out)
                repl('SPLITTING',splitting,out)
                repl('UNITSPERJOB',units,out)
                #repl('GENERATORNAME',row['generator'],out)
                repl('WEIGHT',row['weight'],out)
                repl('SYSTEMATICVARIATIONS',variations,out)
                repl('RELEASE',release,out)
                repl('OUTPUTFILES',str(filenames).replace("'",'"'),out)
