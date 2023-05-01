from keras.utils import get_file

class DatasetDownloader():
    def __init__(self):
        self._dataset_dir = ''
        self._dataset_name = ''
        self._dataset_url = ''
    
    def __init__(self, dataset_dir, dataset_name, dataset_url):
      self._dataset_dir = dataset_dir
      self._dataset_url = dataset_url
      self._dataset_name = dataset_name
      
    def setUrl(self, url):
        self._dataset_url = url
        
    def setDirectory(self, dir):
        self._dataset_dir = dir
        
    def setDatasetName(self, name):
        self._dataset_name = name
        
    def download(self):
        return get_file( origin=self._dataset_url, 
                 cache_dir=self._dataset_dir, 
                 cache_subdir=self._dataset_name, 
                 extract=True)
        
