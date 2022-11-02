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

files_tt4b = [
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


files_ttbb = [
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7E8D7B3F-8954-C443-A29E-0F285D9820C7.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/66EC6F91-A2F0-744D-BC45-F53A6D418DDF.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7E06BF34-9BD2-3541-BDD2-D574C7DE6EAC.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/80BEF1AA-E9AA-C649-AC9E-E8795B724551.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/1AB7DC24-4F69-5C4E-A6ED-E908BCE5E4E3.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/EB305C37-00E3-9040-8439-6EA883487D00.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/4FC32FB9-25E8-504B-985E-9893F0CBBE54.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/2F1C6B26-13B5-464F-982E-E8E6C9EF5035.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/C7C72623-F052-3644-81A4-B1DC8B3D3024.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/80BAF868-4E98-7847-8E13-D2031A0FF587.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/22E694CD-C506-1443-A60B-5EB886CE0307.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/11B7B045-A077-2A48-9E03-9E9CA3359DE7.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/5DFAA63C-44B6-BC4F-BD92-D8C161E56F25.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/E31874E7-1603-CB4B-BABF-EFE4AE57AD3B.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/9DF5AAA1-D71D-8544-ACCE-170474DABE57.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/C4E84438-83E5-1E4C-8674-6DE1D78DA32D.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/72DEA750-00D9-A14A-BCAC-03B13B64E4CD.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/1B7579CF-B422-B04E-AD30-6EC957483953.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/881755FF-5DEE-C84B-A7E2-66526EC31834.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/FB344C81-16B1-2D4A-9EA0-3B4A4B848A00.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/F9EA3285-68DC-1644-8539-2F54B083192C.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/231D2515-55CC-1344-A6EF-C11B83538E68.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/96C204D6-1BF6-B943-A9CD-88377A961698.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/E80EC760-D42F-7944-83DB-4EA7CD67FD19.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/FBC94133-F769-4A48-B5F3-D0C9B54DCDDC.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/D6F112B1-D8DB-3845-8481-35712338B7A0.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/AD24DF77-AE07-1E40-9948-8BD23456256F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/9A338147-DA47-7B4E-869F-A1BDE0C2072E.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/AD506B59-3280-CE42-8F01-C2CC85076495.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/EBDB8FDC-0F64-6043-9434-90A623C97E9B.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/3551B523-302E-1A40-853E-CB841CB2E6BE.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/A46F5EEA-B712-7649-966B-7A8A13B3A14A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/F6382791-F22A-4D48-8DFD-273EBB072A51.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/3D2E69C3-D8EE-254D-8DFF-466EC0465238.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/8B2D707E-0CC2-E64C-8634-756645F8916F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/C784AC53-2A48-7D43-A4EA-C68A4A1A7636.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/50E154A1-5E60-7243-A12E-AD35717DC94B.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/59893757-401B-3D46-826B-B85184C6BA21.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/B7A0D334-354E-3D44-8006-DA2101E2B8C1.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/704E4B3E-C97F-7542-A4BD-D83EB50AEE3C.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/D047EC42-0B0E-3F40-8E9A-D3807AD695FF.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/C1D9F623-73EF-D045-8037-D293FF46EA47.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/F5CC0ADC-8A74-C343-80C0-697E9F77BAE9.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/B5126C7A-3632-4743-B439-82892B4FFC47.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/7DEE9642-2C91-854C-A5A8-2B544CF951C6.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/F9B5F090-33E3-4240-B87D-09BC0725D62F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/260000/4AE873BF-F1BE-A344-9149-B980D030E421.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/B1BA515E-EB62-5047-AD47-AB0DB5EE7734.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/23310832-F0E9-C44D-8F89-E2A882446B85.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/763CC774-6404-1243-A7C6-741722C01D6A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AA2937CE-A540-814E-A6A2-B09742D7C908.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/0EBB4423-F9FA-464D-893D-FA1F7DE709FD.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/280000/FBFF770F-E81C-DE4F-A0D9-65FD66CDE87A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/7D30C9BB-68D7-2145-8155-17F2C118638B.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/B1326B41-9C2D-E741-8D3C-8BEDA5996125.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/C33C7640-0508-F24E-9499-1EEDEB627179.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/74E6FD6D-641C-B945-9547-659376F4286A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/2743FC6D-648E-114E-BA5F-D67305D8C45D.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/AB8B1477-09B6-5B49-BA4D-E1392CB03B53.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/213A311C-5412-2945-9FEE-6E590C7EC5A0.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/9744173A-6986-AA47-92C8-38C0E432E3E4.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/8389FF22-3362-064D-9BB7-020C12AE99E9.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/14C90B32-46D3-6F40-9411-0FDE42C08294.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/2107EBCC-AA4D-FA43-9373-D3F8174E7957.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/270000/F0F0C87F-8139-B549-9C14-820908F941E8.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/130000/6F1ECC22-FFCB-184F-8D9C-36EC5930C1BB.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/51FA4D73-8115-DC42-BE46-21B6EB32DC60.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/FEDE7A7D-9561-1440-9094-909B433349EC.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/3770CA46-9856-754A-BDC2-B08A283F7E9D.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/AE23E610-2CC6-E34C-B1A1-5428905C81F5.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/33A435E5-6F6F-1E48-87D0-929F0FCB74B9.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/ED589C12-3917-334B-A4B8-30A8495AF031.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/E54F6404-FE78-D940-8A69-1E7F11870B8A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/549CE1BA-742A-0340-932B-01D4B01BF9BC.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/8BD7D851-2F48-634D-8CE8-A4B06372E17A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/4558A583-C5EB-C344-8CA7-01B6E4D83B26.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/5F7198CD-35E3-3249-A493-514A5897E764.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/2531C47F-0509-6B4F-8CD9-22A9EF8FC6E6.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/120000/1C62027C-288F-CE4C-9A62-602C92963E9F.root',

]

files_tthh = [
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/0C897178-5BC2-834B-8222-DB4CF5CFE9AA.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/155FF1DC-913E-354C-B96A-E1DAD45B47E8.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/FDF00BAC-C2A9-444D-92D9-BDF60BFD3DF4.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/4D4B4820-4698-DB42-A835-7C0AF8CF8E10.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/EFCFE2D3-4435-654A-872E-1D3AD1AC2C89.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/2315D2AA-6ED8-8647-BB1B-9EA72B09CF62.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/310D0E49-6125-564F-AAE9-0C3D7D9BB32E.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/EC0F795A-FEEE-E54D-B8FF-569504A00717.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/7F963E83-D8F6-A64B-AEB1-B120E478B238.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/8CEBCB68-FA78-EB4A-8766-568F678B1E47.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/0B37A433-1F0C-664A-AC5C-0B2BD3A02D1F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/05CB1A7E-2A10-514E-8E1F-76E9749EE10D.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/946D79F5-1499-D34A-B4D5-260F6D2CCD64.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/799D6B2C-36DF-6641-B4D2-D0070A3BE57E.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/309BD732-4B24-C44C-8486-04894765CB41.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/E8A85089-2FFA-AC48-A808-1D2D8666031D.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/A5B458A8-1FA6-E746-928B-4B3301600C90.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/2D2E732B-4031-7A48-AEEC-E545D9915123.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/D5FFAD80-0030-6644-A3C9-88154FD8887C.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/93C5C5FA-FA7B-694E-95AE-52CD4C74AF52.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/FC007669-70CE-BB4F-BC6D-F72B34DDC9F9.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/D5815373-8C72-474B-B6B0-B54110F77F16.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/FDC8D10C-6F3E-114A-B9D2-812C008435C2.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/381CC773-F312-2B48-BE43-B5419AD13EA8.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/9F69E142-3355-4B48-9237-348784331524.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/44698E5B-B44F-3C43-A4B5-DB964CCC2E2A.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/173EA92A-AC26-4348-A8FC-BCC343BC30A3.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/9D3A189D-5596-9446-81DB-1884FBE1204E.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/67C2A760-B125-B943-BA99-2553D25AEFD8.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/648C6B15-9A52-D947-B2C1-F614B5EBD8BA.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/FC9194B7-A05E-574E-9D93-8B597825FFF2.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/2BCDDA09-97E8-D24C-B693-D593EF1019AB.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/03FFC028-D89C-FB44-9231-04A26115670F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/03507104-66DC-EA4B-8BFE-A9A70BFA2077.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/2F61088D-9731-0745-9300-AC2A24BC5FC6.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/4A3F1645-6A88-694F-884E-D5231C49680C.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/BBA97264-085C-794B-8E34-7CA9F36F15D0.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/23F817AC-7FAA-D74F-8462-ED2578D9B175.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/25649086-4C4E-E042-8BF9-90BE29CAC330.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/FAB7DA7C-CC5F-A045-B907-988654AB4E66.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/E307CF31-A601-6547-8A30-3333881AF13F.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/84FE7360-55F3-9548-91F3-9248AD1EE5E1.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/4A3A40BB-F477-F145-8F3F-1AB2ECFFBA19.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/2D29AC0D-6C01-5447-9DF6-699334266CBB.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/910CE1DB-259C-6E48-B8C1-65DE32C088A2.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/F14F769D-0778-F246-A0F9-ECAD83C5191B.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/0E8F34F9-6934-E74F-9B5E-5BF597DE4006.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/C7EA59A8-88B2-3549-9B6B-5F13E725FF62.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/05920222-9864-BD4C-9375-3C33E9BFE658.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/3ED549FB-1A5E-2C4A-81D1-3BF184E0B640.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/FB75B41D-F110-FC44-99AC-27D8CC5B5D61.root',
    '/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/30000/6FEB63C4-7116-2E4B-8F80-D575B62148AA.root',

]
a = GetTotalSampleNumbers(files_tthh)
print "ratio: ", a
