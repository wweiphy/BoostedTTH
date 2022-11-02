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

files = [
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/9A966159-D383-0C43-AAE9-BCEF27AF5014.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/79503076-B52E-5543-A93F-FDAF7B6865EB.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/E1661DF6-7B04-4E46-9C3F-E754B37476B9.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/C53BA3D8-36C0-9C46-8737-6AAA20D93E93.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/715ABA82-59AC-5B45-AA66-10AE76EB7D53.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/699B151E-8C15-1442-AEB4-BC013DCBE389.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/19B6B5FF-167C-304D-B76A-BA1175B781C1.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/B4F38525-E537-E64A-A409-80096B46D8BD.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/AF3D81E2-B6C6-6C49-9806-3B94CA6FB153.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/35E5A035-210F-3540-8F1B-F57F9856FA01.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/97EBE876-27C6-2647-BA89-17FCECC8650A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/EF72D4EB-22E1-E645-B891-E3E40ADFE41C.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/BB8047F1-68A8-C04D-9859-5ECC1E15DE33.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/1669D3D4-91D2-4F49-AA39-8BB9136A7CD0.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/B13A1097-A211-514F-9ACD-C17F114BCA69.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/952A25FF-C304-1548-B4D1-99FC6C9525BD.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/E98B166F-11AA-274C-82CD-78D1419417F4.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/C5FF9E6A-A322-D341-AF38-2C3A61B0C11A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/4950445F-482D-5D45-8B63-268CD64E42C8.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/E9135ECF-C3E8-0148-A6FA-CAF67C4C1D61.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/2FA8B456-97B0-8E49-8AC5-57DE820A5C75.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/9A92E1BA-2139-0940-B983-C56EAB1DE590.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/6C693D60-B62E-B141-996D-99580F43441D.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/F7540961-F8A1-444C-A981-CC4B22319F61.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/BA758959-76FE-CA49-A1EB-CA71C02A8F9C.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/57F42D6D-7B36-B946-903E-3169C4345EE4.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/A4DF089C-65A7-A04B-B391-6947B5839040.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/3571A1DD-5596-B44B-B396-D22A9E2307FA.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/9AF320E7-1D7F-7242-872A-D0F9F6CD1D3A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/CFBB1C90-AF32-294F-BB29-C810FAD81733.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/0EA33D8D-5AD8-EF47-A3E2-E6CF94A9526C.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/0B889FAA-2835-7D47-B30A-95D4B24F9AD0.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/4D691066-483B-DD44-9934-9AF318047930.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/2973ACED-C40E-BB49-9036-22AA8A4A8747.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/9F4C8A5F-D399-8548-8740-943ABFC4731A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/5F6EA1B5-74E9-CE4D-AA32-B42942318ECC.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/7A2AB467-BA24-B54D-9763-ED66B2682503.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/5CC7AFA7-1B4F-C745-B64C-9309FEAAAE64.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/5701BD57-6512-454C-9EC7-6696AC240442.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/D0747618-CBB8-024A-AF99-49B7C707197D.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/B22DA95A-7BE4-6A42-B4EE-481AD31C6B6D.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/FC235710-37E5-9946-AB02-9545F0139E10.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/CAF07A0F-F862-5440-A48A-FC33A12F4E5F.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/FCB9E2A0-7C4D-B94E-8FA2-8A9FF3B36856.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/DE0EF70A-10E4-074E-AE81-0F9D18042768.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/72E5A9FE-6314-754F-92E4-78A8514042C9.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/20BC7CDE-36A9-644B-85C7-D5B6AFB87DCC.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/86AF6B34-1013-DA48-A133-D97BAE4BC81E.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/F852CB6D-04D6-1144-90A0-C9AB1A5B0B73.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/54C88C00-C107-294F-8E36-DA0B797E2FC6.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/DC4E5D1D-1625-2049-A593-4AD650849939.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/B300F399-05A1-984C-99DC-858F76562795.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/FB1DD598-2A64-794F-9637-D40551C5644C.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/7E41E1A2-9D1F-8941-8DF6-74BF6A56ECFE.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/7222CE7B-9FA3-FB4C-A527-BA92D1F0B8A7.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/65A10EE3-87AC-1742-A5F4-9BAAC563C07A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/A03E9476-F0B1-A34B-8607-9F97F923FD38.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/0EF4B9DD-BCF8-994B-A9F9-AC1542E2D898.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/D5194780-321B-C249-B4AD-26FB95CA6FFA.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/A47E030B-FF76-5245-B6E7-21DE4E352D0A.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/4191DEAE-6F71-F441-89EF-3533BAA37C38.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/331D2B34-ADB1-0348-9F67-CC8B180FDBE7.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/680FA1BA-ECEB-2946-8183-369334C139D7.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/286969EC-E16D-DD48-8410-4D5D6FF918A4.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/3DC83D03-774E-6D42-83D7-FD98C0B28260.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/41CC7B95-1B5A-5340-A622-E8B9015EA89E.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/028BD0B4-CE7A-3441-B63F-4295074287E8.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/27AE1802-F64A-6944-909D-AD9E4BE34699.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/46EB5B4F-BEF2-074A-800E-17F1F321EE01.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/C860075E-044B-1249-8658-A341A4290C40.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/2CCC947D-7CC5-914C-943D-4D5722B2FB3C.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/E948C3C8-0981-594E-BBCC-57F64BCA709E.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/2236763E-C71D-CF4E-8AC5-AAD317B66035.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/0A82F177-14AC-5641-974C-D2291AA9D904.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/3226964C-CE01-E347-92DA-506BEFE7D190.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/F212FCB5-6850-4148-83D7-9E12163C8528.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/EDEBCC10-5015-D54F-ADA5-BD28B503CAAD.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/9D7B5F74-A2C7-5B4C-9ADF-48793EA90FD1.root',
'/store/mc/RunIISummer20UL17MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/80000/772A68F7-891E-A042-8023-052D5C06338B.root',

]
a = GetTotalSampleNumbers(files)
print "ratio: ", a
