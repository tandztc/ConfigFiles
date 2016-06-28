import subprocess
import sys
import time
import logging
import os
import logging.handlers
#print(os.path.dirname(sys.argv[0]))
log_path = os.path.join(os.path.dirname(sys.argv[0]),'monitor.log')
logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s',
        level=logging.DEBUG,
        #        filename=log_path,
        handlers=[logging.handlers.TimedRotatingFileHandler(log_path, when="midnight")])
def SquidRunning():
    sp=subprocess.run(['systemctl','is-active','squid'],stdout=subprocess.PIPE)
    #print(sp.stdout)
    if  sp.stdout.strip() == b'active':
        return True
    else:
        return False
    
def CheckFailed():
    subprocess.call(['sudo', 'systemctl', 'stop', 'squid'])
    subprocess.call(['sudo', 'systemctl', 'stop', 'mylighttpd'])

#print(return_code)
def Check():
    sp=subprocess.run(['vnstat','--oneline'],stdout=subprocess.PIPE)
    out_put =str(sp.stdout,'utf-8')
    traffic_out=out_put.split(';')[9].split(' ')
    num=float(traffic_out[0])
    unit=traffic_out[1];
    if unit == 'TiB':
        logging.warning('Oh my god! ' + str(num) + ' TiB')
        return 2
    elif unit=='GiB' and num>14:
        logging.warning('Watch out! Current traffic is %s GiB',num)
        return 2
    else:
        logging.debug('Everything is OK! Current traffic is %s %s',num,unit)
        return 0;
def RunOnce():
    res=Check()
    if res != 0:
        logging.info('check result is %s, try stop relevant services', str(res))
        CheckFailed()
def main():
    while(SquidRunning()):    
        
        time.sleep(5)
RunOnce()

