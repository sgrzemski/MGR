from pyhocon import ConfigFactory
import os
configuration = ConfigFactory.parse_file('application.conf')
gztan_path = configuration.get('datasets.gztan.path')

def getFileList(path):
  filelist = []
  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith(".wav"):
        filelist.append(os.path.join(root, file))
  return filelist

samples = getFileList(gztan_path)