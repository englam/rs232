import os, logging

logpath = os.getcwd() + "/logs"

FORMAT = '%(asctime)-15s %(clientip)s %(message)s %(user)-8s'
logging.basicConfig(format = FORMAT, filename = logpath,level=logging.DEBUG)

d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver11')

console = logging.StreamHandler() #output streams
aformat = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')

console.setFormatter(aformat)

logger.addHandler(console)
logger.info('Protocol problem:', extra=d)
