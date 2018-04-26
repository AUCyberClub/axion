from ConfigParser import SafeConfigParser

def config_set(section, key, value):
    config = SafeConfigParser()
    config.read('imports/globals.ini')
#   Section will be added if it's neccesary > 
#   if config.has_section(section) == False:
#       config.add_section()
    config.set(section, key, value)
    
    with open('imports/globals.ini', 'w') as f:
        config.write(f)

def config_get(section, key):
    config = SafeConfigParser()
    config.read('imports/globals.ini')
    return config.get(section, key)