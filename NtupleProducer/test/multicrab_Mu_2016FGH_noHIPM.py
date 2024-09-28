dataset = {
   'Run2016F' : '/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD',
   'Run2016G' : '/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD',
   'Run2016H' : '/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD',
   }
#nevents = -1 
lumisPerJob = {
   'Run2016F':        500,
   'Run2016G':        500,
   'Run2016H':        500,
   }

listOfSamples = [
   'Run2016F',        
   'Run2016G',        
   'Run2016H',        
   ]

if __name__ == '__main__':

   from CRABClient.UserUtilities import config
   config = config()

   from CRABAPI.RawCommand import crabCommand
   from multiprocessing import Process

   def submit(config):
       res = crabCommand('submit', config = config)

   config.General.workArea = 'crab_TrigEff_HWW_Muon_2016_noHIPM'
   config.General.transferLogs = False

   config.JobType.allowUndistributedCMSSW = True
   config.JobType.pluginName = 'Analysis'
   config.JobType.psetName = 'runNtupler_2016.py'
   config.JobType.outputFiles = ['TnP_ntuple.root']

   config.Data.inputDBS = 'global'
   config.Data.splitting = 'LumiBased'
   config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'
   config.Data.publication = False
   config.Data.totalUnits = -1
   config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/arun/TriggerEff_RunII_ULLegacy/TrigEff_HWW_Muon_2016_noHIPM'

   config.Site.storageSite ='T2_CH_CERN'
 #  config.Site.blacklist = ['T2_BR_SPRACE', 'T2_US_Wisconsin', 'T1_RU_JINR', 'T2_RU_JINR', 'T2_EE_Estonia']

   listOfSamples.reverse()
   for sample in listOfSamples:

      config.General.requestName = sample
      config.Data.splitting = 'Automatic'
      config.Data.inputDataset = dataset[sample]
      config.Data.unitsPerJob = lumisPerJob[sample]
      config.Data.outputDatasetTag = sample
      p = Process(target=submit, args=(config,))
      p.start()
      p.join()
