from compare_lib import *
import subprocess
import yaml
import os

if __name__ == '__main__':
    with open('compare.yml') as f:
        branchs = yaml.load(f.read(), Loader=yaml.FullLoader)
    for b in branchs:
        print("\n url {}".format(b['url'])) 
        print(" commit: {}".format(b['commit']))
        print(" path: {}".format(b['path']))
        clone_and_update(b['url'], b['commit'], b['path'])
        stdout = runtest(b['path'])
        try:
            simtime, realtime, performance = get_summary(stdout)
        except:
            print(stdout)
        print(" results: \n    simtime: {} ns\n    realtime: {}s\n    performance: {} ns/s\n".format(simtime, realtime, performance))
        
        
        
    
