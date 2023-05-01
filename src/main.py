from utils.DataDownloader import DatasetDownloader
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(ROOT_DIR, 'data')

def main():
    url = 'http://peipa.essex.ac.uk/pix/mias/all-mias.tar.gz'
    dataset_dir = DATA_PATH
    dataset_name = 'mias'
    
    downloader = DatasetDownloader(dataset_dir, dataset_name, url)
    dataset_dir = os.path.dirname(downloader.download())
    print(dataset_dir)


if __name__=="__main__":
    main()