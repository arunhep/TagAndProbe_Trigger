#name = 'DYJets_UL2018_EleTrig'
name = 'DYJets_UL2018_MuonTrig'
# name = 'RunIIAutumn18_102X_v2'

dataset = {
   'DYJetsToLL_UL2018': '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
   }


#nevents = -1
#lumisPerJob = {
#   'Run2017B':        100,
#   'Run2017C':        100,
#   'Run2017D':        100,
#   'Run2017E':        100,
#   'Run2017F':        100,
#   }

listOfSamples = [
   # Run3Winter
     'DYJetsToLL_UL2018'
   ]

if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   #config.General.workArea = 'crab_MC_EleTrigEff_UL2018'
   config.General.workArea = 'crab_MC_MuonTrigEff_UL2018'
   config.General.transferLogs = False

   config.JobType.allowUndistributedCMSSW = True
   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler.py'
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   config.Data.splitting = 'Automatic'
#   config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
   config.Data.publication = False
   config.Data.totalUnits = -1
   #config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/arun/TriggerEff_RunII_ULLegacy/MC_EleTrigEff_UL2018'
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/arun/TriggerEff_RunII_ULLegacy/MC_MuonTrigEff_UL2018'

   config.Site.storageSite ='T2_CH_CERN'
 #  config.Site.blacklist = ['T2_BR_SPRACE', 'T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
 #     config.Data.splitting = 'Automatic'
      config.Data.inputDataset = dataset[sample]
#      config.Data.unitsPerJob = lumisPerJob[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()
