from CRABClient.UserUtilities import config, getUsername

config = config()

config.General.requestName = 'DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8' ## EDIT
config.General.workArea = 'crab_projects'
config.General.transferLogs = False
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'RunSKFlatMaker.py'
config.JobType.sendExternalFolder = True
config.JobType.pyCfgParams = [] ## EDIT
#config.JobType.numCores = 8
#config.JobType.maxMemoryMB = 4000
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM' ## EDIT

config.Data.splitting = 'FileBased' ## EDIT
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/SKFlat/' % (getUsername())
config.Data.publication = False
config.Data.outputDatasetTag = 'SKFlatMaker_2017_v1'

#config.Site.whitelist = ['T2_CH_CERN', 'T2_US*', 'T2_DE_RWTH', 'T2_DE_DESY']
config.Site.blacklist = ['T2_RU_IHEP']
config.Site.storageSite = 'T3_KR_KISTI'
