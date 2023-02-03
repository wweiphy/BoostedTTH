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
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/AA85336E-6C97-774D-95C8-CD6671EAE9C5.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/33AC3BAC-F744-A943-A1EB-C602FD017193.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/4E934BE9-F269-4C45-9A9D-AD304C1D0E83.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/EA7C5F81-A83B-F142-92D7-FDF22CEC6EC7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/85F49635-50A1-AB48-98D6-9CB89F7E0263.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/FFDDABF4-E92D-2941-812A-A815D6870EDC.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7AFD664B-BFBF-944D-8BB5-CF975C789926.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/91005717-9459-3E4A-B7BE-7C477FE1F5F8.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/783A6C6B-9BD7-E74E-8374-EABDE6C856A0.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/9AD8FC2B-540E-574D-A99D-C71D844E5ABF.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/01C10F1D-ED00-9B4B-8840-B1698BAD5449.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/E34CB8FA-27DA-A44B-B3B8-A3D8465B488B.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/71E9AF6D-36C0-F749-A6F4-AEBAD1DF800E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/DA339B17-A7A7-724A-BCDA-17F327F13C98.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/22DFFB13-FF20-8148-B8B9-AFF5591356E2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/7CD70BA0-94DF-7147-9795-307EAA53CC9E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TT4b_TuneCP5_13TeV_madgraph_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/3CCA9EC6-7D3C-1449-B904-A60BE79881C9.root',


]


files_ttbb = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/6B456F77-8B5C-6849-A6BB-EDE751029B1F.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/0DE12EDC-6079-074B-9AD7-75F3DBB831B0.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/BDFF712F-4287-3E46-A65C-AE8DDC434A22.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/A1407352-A55F-2D4E-9083-BDB7B3C67B50.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/8C23253E-637C-824D-8A5F-C9CE8A1BE427.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/DCF8EABB-7A1D-D047-89AD-45B092E9F149.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/6D708B0C-F541-F242-8ABB-D87A219F7347.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/669C0E4F-4F27-094F-AFDC-537CBEB97893.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/BA0489B2-7041-9E45-A073-2033D10053E1.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/7F722D75-6521-6141-AB30-1EB7DD01F6F5.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/13D36A42-E296-DC47-933E-FE65FE1193F0.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/702706B4-0E64-034A-8EA0-A39B9FD39D63.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/B9337EF7-85AC-E741-98B9-88A2B0152F1A.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/3B363590-A5A8-8B40-A7E9-992D3943DCDD.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/B74915FE-ED37-A044-AC12-CC902E730456.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/15F91D49-8690-4D49-BCE4-0FB35A57EC28.root',
'/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/120000/4519C8A6-A599-D84A-B963-E46218F6A284.root',


]

files_tthh = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/38D19787-FC33-C94A-AEA8-1BB996A6702B.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/3C0126E4-2EF2-354B-94FC-94BE3A944B7B.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/71818EB7-9DA3-EC4F-BDA3-347607753C2C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/32826D60-39ED-7B40-9DE7-15FB6B1E393B.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/AB34BD11-43FC-AD48-AEA1-9EF40D8FBE84.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/B3A7A3F7-C4D0-FC41-AFBC-2FBCD2B7EAD0.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/35FA5CD6-25C5-7548-8815-AE2D8199B86D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/35300F1E-B9F8-F844-9C6D-48613FDAA747.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/580E3E04-660C-2F4D-BF3F-420BBB9C242E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/50A6B0C4-0C19-AA45-8224-9A84D043D871.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/B7C3B680-ED87-BC46-9251-D274F5D959AD.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/E22266B8-58C0-6F45-8E20-79EDA5F64DBE.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/80000/3D53228E-C00A-B54D-B8FE-4B6843DDC013.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/5103FD2A-4362-3E41-A242-C6B26AE1554F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/C964933C-0402-814E-ADAC-A97E941D21D3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/CD7FDAF5-5C33-7345-AAC5-9644CE546472.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/1340CFFC-CEC7-9849-9365-3D2A8493FCE3.root',


]

files_tth = [
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/60B47B6E-E2FA-BD46-AC33-4F8C5754446D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/218F8710-A13F-EC46-898B-7CC502F57690.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/91DD91A7-52EA-614D-81AB-110EFC537144.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/1F6409A7-1EA4-2441-BA70-83738837D8DE.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/BDEA2DD8-0C35-D04E-BED2-D2051481E5DC.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/62481A74-A91E-CD4A-B833-14F7B191201A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/0E3FF79A-89A3-904B-B6D3-66763A4D05F9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/DCCDCB85-BE23-704A-9591-72795198D3EE.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2510000/42160452-E30E-974B-AAFF-89B0BC33365D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/47540F97-23DE-CB48-ACCC-E7B2E0C7F4DA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/230000/A232EA90-2533-8342-80BE-6DC0F6908016.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/226439D2-FE99-134F-9787-792FDE2B2554.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/250000/972D9AFD-8E2B-F649-BD9A-B4F4F9ABAE2A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/250000/249FC360-4756-8B48-AD7C-D9D356691625.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/250000/73B936AC-3528-5D41-8719-880BBE75BE9E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/E0BCF89E-54B7-4D4C-923C-619940A7F1D3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/40000/4007671F-2966-104D-AA5D-751DFF8FC103.root',

]

files_ttsl = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/F3E92FD9-A390-3444-B1E6-7E7EE4021D15.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/9EF8E759-6286-0343-8DE3-D75B45AB0BDF.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/648A5E42-661C-2544-85EE-836B9F50A6B7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/F8593E31-2D30-E747-8FD2-B1CF1EBF2563.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/A4CDDC86-1C5F-2C48-88F3-99A4BAD11FD5.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/57EF6A47-C142-B647-AE29-48ACFF2F9607.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/48B3CDB4-5AD8-F541-9404-DB133970BF17.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/114F7EAD-AD51-B847-84A3-C9C733F629D3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/B7301036-C83A-E24F-BD67-E4C5A7713BB9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/28C547F3-C9F3-B448-B42B-2DF4B99C486F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/54DA6537-B2E2-D44F-9489-865AB49345FC.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/55437372-F33E-3448-B707-DBB7CB43CFA1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/3B576716-01E9-6244-8A79-488046543CE3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/130000/6FCDC553-27FF-5341-9CC2-AD4FC7269552.root',


]

files_ttzh=[
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/F6C44A41-1F50-914A-A69C-9C54167E96FD.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/B1A5A31B-C723-044C-BF82-91AFE33065E2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/963C1011-1436-AE41-B524-E02339F589AB.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/2B3FE02D-ACCE-A041-8DF0-8E49DB0DCE41.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/31E93E51-6CDE-C24B-8C57-05A77F45DF1C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/2EC2C009-B856-6642-85A8-DF141D8F5903.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/BA435025-6023-2847-9952-7F803BE46342.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/DCD5A266-C74D-E946-B8E3-54483D7838BA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/E0315513-B41E-9F41-92E5-CE43BAF5CAAA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/0AD2D7DE-1D2B-A347-AB8C-AE31A27EE7AC.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/29928AE7-B9DD-EE46-9CFD-B7B402DBE945.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/88197DD8-CC17-B446-8AA8-1A3C8B40D31A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/71578181-6CFA-0A45-833F-E63E979160BE.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/50ADCCD8-0082-D844-B057-56D6BB2643D9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/4E0DB8A0-2FE1-3444-B78F-F29E21FBBA22.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/AEDBE689-CBA2-9F40-8080-0F9C2F6873D4.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2560000/D8864694-7206-084E-8B89-F90B358D6E2D.root',


]

files_ttzbb = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/B6261BA0-D310-3545-8FC0-FDCB0CB540A2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/E41A0FCE-BE50-4F42-AB56-859C42B9B223.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/525C12DE-EC69-E043-B6F1-00AD8C2A699E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/BF575C02-43D8-3840-93FB-C7432D9030C7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/4D7CDEC5-833F-E143-A976-D4DB712D8EA1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/CFEA5929-0B3B-0547-8A08-EBC8508E05E1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/CDB9E9F2-6E47-214C-BC2B-8595B24F3AD2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/9F70F692-FF6C-A641-ABD7-582E78EB9EDA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/8E05A797-FAD1-B740-A85C-20FEC77F7F06.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/84A112EA-1B61-6344-B9F1-B64AF4EA9B3B.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/4DEFBDE2-A99E-2E4C-9CD8-204B0FA4A6FF.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/6E83D88D-A8A8-4643-960A-0E349FA61868.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/AA19BE33-2910-3C48-8588-52AD60A6A52D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/7CEF0AC0-3230-5640-9BC7-E90C2D7BD775.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/C6E48B95-A815-134B-97A8-904722C07E10.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/6D074508-83AC-C647-8A29-0822A842A540.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZToBB_TuneCP5_13TeV-amcatnlo-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/D3A8513C-136D-8941-B2CA-8889857DA499.root',


]

files_ttzz = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/BB5485F6-5BB6-C646-A0C8-1B1DD4A50767.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/500775DB-D994-2B42-896D-057C88D496E2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/6B05DB04-8127-784E-8F36-3C8E2F8CE64D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/2EFF5FCB-9525-F743-9A84-89CCBEB72C98.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/3267581B-F628-BB44-B1B9-1605EAC446CE.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/DD6EDD81-1D57-3A47-A5B2-50CB35C3E45C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/39C34DAF-2908-7749-A475-625082417FBB.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/322918CB-8ACF-3945-ABD6-A5A42E91AD41.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/94354DF5-9C28-5F4F-84DB-4255152639BB.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/F03B5B0D-5319-3140-93C0-5386C013E8C6.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/54B7AF31-F981-5D48-9A99-19E3A70F055F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/870397D7-4956-E144-8B8D-6DED7077D559.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/F85C1DF5-AEBC-4C49-A4FF-39F49F8A9AD3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/2177AF39-DC13-C74C-9513-BA0DAE4645D9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/EA669A89-D741-B644-AADD-797920CDB399.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/7ED4C399-1F92-7B4F-B860-A84627BB5DC1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/30000/15469840-1283-B647-AA88-08518758BAF7.root',


]

files_ttdl = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/8C01F451-0EE0-E84D-BC4D-DA55AE6D5F20.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/26566461-4FC0-154A-BDB5-A23A4DD79BD8.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/472A86BB-6955-8644-A3A2-DBB07C896F28.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/EC97AB46-EF0A-9C47-8E0D-2639658EB054.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/EA6A507D-6D3B-C845-9328-597BF0D8A2D3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/3E7CBC97-7A92-464A-AC83-1996115CB253.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/16D2EF2C-F1CE-EB4F-BF90-4483319627B9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/282A5B68-0D8A-DD49-BF28-BC0A1B9B553F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/C98D2E63-6B1A-E04A-A249-7851E76F2DA6.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/27FD95A6-55F3-7A49-8F53-C260BFF1D341.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/BAA168FB-BAC7-D84C-833D-13515F19CDF7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/C9FFC467-B112-1D44-8D3A-AD87495BAAB2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30000/A2EFBE59-538E-EC43-B4FB-381853992495.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/CA2A8D4D-58B0-9E40-81DB-3D5E8E44D401.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/836AB741-4C37-DC40-B4CC-EEE2740EA900.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/E886D552-CB3D-4244-98AC-33B859B16404.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/30001/C6D07A55-D5F3-9444-AFB8-763DBEDBBA69.root',


]

files_ttbbdl = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/E8E7FF75-A4C1-E046-BA66-A91FFF561BF9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/EF29F2C9-CB7E-FD46-BDDE-0C02FEE81F83.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/2DAC27AF-A103-3646-9350-DC636A9D3D93.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/CE9AFF2B-9BDF-8442-89A8-FE9A6D73250F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/61B09896-DB4C-784E-94ED-5D99003D9B38.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/B1491585-11BB-204A-A8E3-E7F2A177D258.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/4D256FEB-9D44-5A4D-B3F4-052BBA9101C3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/D834036D-6172-2A49-B5BE-99066D6DEDD7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/1E72CCC3-25B1-C647-9A61-663637A23EB0.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/75033986-FF0A-0A42-B95C-DD75B0D85E25.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/6C9D82C9-CC76-CD45-B9F6-950FFF08BBD6.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/F0F62625-BD8E-094A-87B1-85D4DAED9E4C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/5D1E24E0-9B9D-6849-936A-1AC8A38FEB96.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/90F944F3-9AE2-7948-99F3-114A0D15A683.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/E51612E2-6081-954F-8568-752D12E3B0C5.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/A6CE2FD0-B628-714E-B633-AD0211D22919.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/280000/8713A345-179F-6648-8FC2-D224A04C890E.root',


]

files_tthsl = [
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/29F8674D-04C0-234E-A9D8-5B9D237CC666.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/F18C6B78-1FC6-104D-AED0-77CE28A5A5C7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/5D89B6AB-5CEA-2647-96B1-A0BF635762F0.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/3F9C7498-A808-EB44-8DB6-A2C6BE14E667.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/309BE18B-8994-854F-AA7F-F77D60B8643E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/1BBE5B46-EFC9-954D-B6D6-EB1045D03818.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/ED4386CD-D1DC-E44F-8F4F-2D5623E74974.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/0F26CD33-12F9-5B4D-BE00-1E45925BF2E8.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/0FC6A0E2-062D-C14B-9244-B3199ED46CC5.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/E2420427-0F6C-3546-AEBC-FB1E9B06B792.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/B78A85B6-8AB3-1143-B9DE-C08620DAFAA2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/734FDBD3-6E81-F84F-BF6F-45B9C37ACEEA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/E8B39CDB-4806-BB49-92B0-6B429B1A14A4.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/1B6C2D36-E83C-5B4A-BB78-5667A2761C7D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttToSemiLep_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/50000/002D59E0-4C2C-7B43-A617-E6B9F80C7D20.root',

]

files_tthdl = [
  
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/7AD23944-FF87-564C-8B4D-9F0106383EC1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/C76B11DC-441D-9349-849C-51B19738404C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/01CEA982-0CDC-984A-925F-89CCF1765A41.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/E2871E6C-A9DF-5842-B249-9B9B26E8B112.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/340B8464-428A-8F4B-866E-B63A07D1C617.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/20E2333E-5605-8643-892B-08F0E5F0375D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/15FEFDCB-772B-0E4F-87BC-E1F096424F6E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/9482C148-B302-EA40-8E0A-0B9B2ED62420.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/F33C5C94-898B-C445-A2E9-7BD97A889D2A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/AFF293A2-25B4-A44D-A4B1-DE43834B4D44.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/464EBA22-655D-6541-9000-225BB773774E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/CD6556C1-7525-3844-ABF5-24FD27A1A6E3.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/111914E9-BABB-B142-B295-B08AB62C780A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/5B7B61A2-9C51-6642-8AF7-71AD77FE9E11.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/5F9C42A8-F150-9A49-ACFC-DC0BF02A5C35.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/8C8DFC9F-BB7F-4A4E-B32F-70F4272FE5ED.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/ttHTobb_ttTo2L2Nu_M125_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/60000/6514CFA9-5A9C-0B45-8C90-1625D4030F9D.root',

]

files_ttzzext = [

    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/0ED6A9FF-5088-A649-A046-9070581873B1.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/1EE87249-7000-3B4B-8003-6D6784BD7C0D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/AC40A3D0-5737-B04F-B443-AA686489451A.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/50BC5714-A0DF-924C-A7F9-BF899B9D7C56.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/B8D6315A-1A88-E14C-8C2F-BEDCDA9135E0.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/7D8EDDB6-67E4-4548-B73B-18FF9DC737F9.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/2D3352B5-97A0-844E-B7D4-5CAF219265C8.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/1AF99356-658E-374C-81E5-50B5AE878606.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/5054B71E-0E0F-D54C-BC2E-17071EF6F5C2.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/F213C01D-41D7-3047-AE3E-6D4AA404F90F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/93030409-9E05-2B4B-9431-71CF2AE66685.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/C17D493E-084E-6646-BDAC-55ACB0E995B7.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/0C36EC6F-BE77-B248-880A-4FA64BDEECC6.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/5EC43F80-2555-1A49-A016-61157184DC2D.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/F02C9E65-64A3-A44C-8636-19799F039217.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/D204A807-E5D3-064E-A616-B6254E8D1A94.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/60000/0403805A-B9B2-3848-B936-514A58A30CF0.root',


]

files_ttzhext = [
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/198A69BB-0F56-C84E-B76B-D1393550169E.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/9C71394B-B834-AE40-8E68-69C59F813133.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/BA89731F-2E9C-634C-AA31-2E32F5AEFA30.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/8B9DCD30-23A7-8A47-9AA1-6847E68FE530.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/8012DA04-5A3F-524C-8A92-E165A6508B22.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/ECE74EE4-1D3F-6742-82AA-C0DD8F458B0F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/3EB5698E-FDE9-294D-9F7A-E702BDE75F10.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/57BCB6DB-DE04-7947-BB3F-5D56934FDFF6.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/E5D59CC1-394E-EE4E-9200-B5F8016AAD0F.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/8493FF89-B74A-6D45-A535-B0F71D42EF73.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/35D9F462-7DBF-2B40-944C-C1354A34EFEF.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/00C1059D-F0C6-0F4F-9F85-6651CA3B00CA.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/0F305B0A-A82F-084D-A357-F370FCEBE656.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/CE9237A3-E00C-384D-92B9-98A75F474A9C.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/C8E109E8-6E9F-6149-BD51-5551B4D0C9EC.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/3D809745-DD3F-C144-8C66-871B0F658C60.root',
    '/store/mc/RunIISummer20UL18MiniAODv2/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1_ext1-v2/50000/FEAC292D-F2FD-DE48-AF0F-5C549BD80075.root',

]

a = GetTotalSampleNumbers(files_tthsl)
print "ratio: ", a
