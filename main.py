from pyhocon import ConfigFactory
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
configuration = ConfigFactory.parse_file('application.conf')

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

def prepareOutputDirs(path, feature_types, genres):
  for output_type in feature_types:
    if not os.path.exists(path + '\\' + output_type):
      os.makedirs(path + '\\' + output_type)
    for genre in genres:
      if not os.path.exists(path + '\\' + output_type + '\\' + genre):
        os.makedirs((path + '\\' + output_type + '\\' + genre))

def generateSpectrogram(path):
  x, sr = librosa.load(path)
  X = librosa.stft(x)
  Xdb = librosa.amplitude_to_db(abs(X))
  plt.figure(figsize=(8, 5))
  librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
  plt.axis('off')
  output_path = path.replace('genres','spectrograms')
  plt.savefig(output_path.replace('wav','png'),bbox_inches='tight', transparent='true')

def generateDataSetSpectrograms(dataset_samples):
  for sample in dataset_samples:
    generateSpectrogram(sample)

# def generateCentroid:
#
# def generateRollOff:
#
# def generateMelCepstrum:

gztan_path = configuration.get('datasets.gztan.path')
gztan_genres = gztan_path + "\genres"
features = ['spectrograms','spectral-centroid','spectral-rolloff','mel-cepstrum']

gztan_samples = getFileList(gztan_path)
gztan_genres = getDatasetClasses(gztan_path + "\genres")
#prepareOutputDirs(gztan_path, features, gztan_genres)
#generateSpectrogram(samples[0])
generateDataSetSpectrograms(gztan_samples)

