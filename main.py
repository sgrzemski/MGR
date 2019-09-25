from pyhocon import ConfigFactory
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
configuration = ConfigFactory.parse_file('application.conf')
gztan_path = configuration.get('datasets.gztan.path')
gztan_genres = gztan_path + "\genres"
features = ['spectrograms','zero-crossing','spectral-centroid','spectral-rolloff','mel-cepstrum']

def getFileList(path):
  filelist = []
  for root, dirs, files in os.walk(path):
    for file in files:
      if file.endswith(".wav"):
        filelist.append(os.path.join(root, file))
  return filelist

def getDatasetClasses(path):
  genrelist = os.listdir(path)
  return genrelist

def prepareOutputDirs(path, feature_types):
  for output_type in feature_types:
    if not os.path.exists(path + '\\' + output_type):
      os.makedirs(path + '\\' + output_type)


samples = getFileList(gztan_path)
genres = getDatasetClasses(gztan_path + "\genres")
prepareOutputDirs(gztan_path, features)

# audio_path = samples[1]
# x , sr = librosa.load(audio_path)
# X = librosa.stft(x)
# Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()
# plt.show()