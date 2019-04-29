#!/usr/bin/python3
import configparser

# configurations ##############################################################
config = configparser.ConfigParser()
config.read('config.ini')

apikey = config['misc']['apikey']
set_id = config['misc']['set_id']
operating_system = config['misc']['os']
author = config['misc']['author']

print(author)

# main program ################################################################

    
# functions ###################################################################
    
        
# gui #########################################################################

        
# top-level ###################################################################