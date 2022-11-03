#!/bin/bash

echo "Setting Up Environment"
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node
echo "System software: `cat /etc/redhat-release`" #Operating System on that node
source /cvmfs/cms.cern.ch/cmsset_default.sh
echo "Attempting setenv command"
# export SCRAM_ARCH={{SCRAM_ARCH}}
# export CMSSW_VERSION={{CMSSW_VERSION}}
# cmsrel $CMSSW_VERSION

xrdcp -s root://cmseos.fnal.gov//store/user/wwei/UL/CMSSW_10_6_29.tgz .

tar -xf CMSSW_10_6_29.tgz
rm CMSSW_10_6_29.tgz
cd CMSSW_10_6_29/src/
scramv1 b ProjectRename 

# cd $CMSSW_VERSION/src/
# cmsenv
eval `scramv1 runtime -sh`

echo "set up"

{{SETUP}}

# echo "Transfer input file(s) from EOS"

# xrdcp -f {{INFILE}} .
# {{INFILE}}

echo "Starting Executable"

{{RUNCOMMAND}}


echo "Transfer output file(s) to EOS"


{{TRANSFEROUTFILE}}


# root://cms-xrd-global.cern.ch/
# root://cmseos.fnal.gov/

# cd $CMSSW_VERSION/src
# cd ..

{{DELETE}}

echo "clear space"



