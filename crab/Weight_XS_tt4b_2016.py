import ROOT
import sys
import urllib2
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def GetTotalSampleNumbers(name):
    files=[]
    for file in name:
        files.append(file)
    usexroot=True
    totalNumber=0
    totweights = 0
    totevents = 0
    FileList=[]
    print files
    if usexroot:
      #print "in xroot condition"
      for f in files:
            FileList.append("root://cmsxrootd.fnal.gov/"+f)
      print "Filelist ",FileList
    
    else:
      #print "in else condition"
      FileList=files

    print "N files ", len(FileList)
    nfiles=len(FileList)
    print "counting events"
    ifile=0
    ##now count the events
    if(nfiles>0):
      for f in FileList:
        print f
        if usexroot:
          tf=ROOT.TFile.Open(str(f))
        else:
          tf=ROOT.TFile(str(f),"READ")
        tree=tf.Get("Events")
        if tree==None:
          continue
        tree.Draw("1.>>totweights(1,0,2)","GenEventInfoProduct_generator__GEN.obj.weight()","goff")
        weights = ROOT.gDirectory.Get("totweights")
        totweights += weights.Integral()
        totevents += weights.GetEntries()
        print "done with File ", ifile, "/", nfiles, f
        cumulFraction=totweights/totevents
        print "sum of entries, sum of gen weights, cumulFraction(sow/soe) ",totevents,totweights, cumulFraction
        tf.Close()
        ifile+=1
    else:
      cumulFraction=0.

    
    #print "total number of positive events: "+str(int(totalPos))
    #print "total number of negative events: "+str(int(totalNeg))
    #print "total number of events: "+str(int(totalNumber))
    print "returning fraction: "+str(cumulFraction)
    return cumulFraction

files_tth = [

'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/EFD4E99B-0B60-0245-A0D9-9947EFFF8B1E.root',
'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/260000/F8E146D6-F590-CE49-97FA-F26178D91200.root',

]

files_tthsl = [

'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/E81F29C6-C5E9-AA44-870F-5BE1397D41B9.root',
'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/667981E7-077F-444A-BE2D-E8EF34FF225D.root',

]

files_tthdl = [


'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/36B0D173-8AD4-FC49-A8BA-0BF6D0D8E0C2.root',
'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/A45C7732-1520-A748-8B28-BD2F7BFA52F7.root',
'/store/mc/RunIISummer20UL16MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/50000/78DFB41B-386B-854D-8C0C-A728D520F0E6.root',

]

files_ttsl = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/2EC505FD-B873-124E-B3C8-B1D2EB0AFC2C.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/060C33A7-7EDB-2144-84A0-6240FA42FB9D.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/120000/F11EE1A7-DAC1-D345-8E46-40AD813DE737.root',
]

files_ttdl = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/140000/5B3C6FC7-0538-D540-9216-2F02189B50B6.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/0E08F98A-B939-BF4B-A383-FFC5EB90BA9F.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/70000/F03E39BA-5F71-874C-95E0-ABE8D9704008.root',
]


files_tthh = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/80000/5346577F-DD3F-A14E-BF0D-BEBC5A3CB146.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/80000/82FDB92C-15E5-A34B-A685-9B0F74B4B85C.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/80000/251DA9E9-BDD9-3946-8976-3E299E596DFE.root',
]

files_tt4b = [

'/store/mc/RunIISummer20UL16MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/B13FE6C2-928F-D946-A21C-9FBCDFE993DA.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/270000/253BA941-BC18-6F41-9951-0E5FEBE0C838.root',
]

files_ttbbsl = [
'/store/mc/RunIISummer20UL16MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/9D3DF71B-21D8-8347-BDBD-EBE87F8CE6B0.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/270000/A70F568E-58F1-DE4C-87F9-8042C207EA91.root',
]

files_ttbbdl = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/AB2A3C19-7BD7-BF4B-86AC-8A0121FF3099.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v1/280000/197DCBC7-0082-9249-9635-7A619F0F58E2.root',

]

files_ttzz = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/614CE26B-4D69-B841-8AA6-77A0067792A8.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/5EBDA73B-8F2D-F448-9A6A-67A651C016CA.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/40000/7FED4ED2-8969-0B49-8E2E-A035639E0583.root',
]

files_ttzzext = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/EDED79ED-CF36-DA45-9519-50872F5AA681.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/14445BA2-2C92-2A4B-A9A3-F32D012CF3AA.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/AF4EDC9E-CA47-264A-B968-25A876F5079B.root',
]

files_ttz = [
'/store/mc/RunIISummer20UL16MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2550000/E02E3A81-AB9D-124F-917E-46FF906C99C0.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2550000/94567EA4-ADF7-1244-9131-FED68B298B98.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/2550000/A5AC4644-1F6C-F24C-9074-67EA2E1F0F8A.root',
]

files_ttzh = [

'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/E30CD8FC-EE9D-834E-A2B6-659F6E2AE24F.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/6416D373-9582-2446-8D42-18FC653674CA.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17-v2/30000/FD8168D9-B9DD-0F4E-964F-A1722CDAF146.root',
]

files_ttzhext = [
'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/20B138A1-E5E7-F047-9848-B4178436A024.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/C267997F-D0E3-1F4E-8EBF-4F2A74C43DBC.root',
'/store/mc/RunIISummer20UL16MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v17_ext1-v2/50000/77A07E48-A5D0-D447-8557-7CBA70B393BF.root',
]

a = GetTotalSampleNumbers(files_tth)
print "ratio: ", a
