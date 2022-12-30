#pandas - library for structured data
import pandas

data = pandas.read_csv('.\introducing-python-labs\/test.csv')
print(data.columns)
print(data)

#configuration files
import configparser

cfg = configparser.ConfigParser()
xy = cfg.read('.\introducing-python-labs\/settings.cfg')
print(cfg.sections())
print(cfg.options('general'))
print(cfg.items('general'))