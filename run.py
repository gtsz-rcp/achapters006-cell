import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.getcwd())))
from BartlebyMachine.bartleby import Bartleby
from BartlebyMachine.config import Config
from pypandoc.pandoc_download import download_pandoc

__config_file = os.path.join(os.getcwd(), 'config.yaml')
Config = Config.instance(config_file = __config_file)
bartleby = Bartleby(Config)
bartleby.Scrivener().make_book()