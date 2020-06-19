from configparser import ConfigParser
 
cfg = ConfigParser()
cfg.read('test.ini')
 
print(cfg.sections())


for item in cfg.items():
    print(item)

print(cfg.items('debug'))
print(cfg.get('debug', 'log_errors'))
 
print(cfg.getint('server', 'port'))
 
