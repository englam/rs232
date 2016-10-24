import os, logging

def save_log(dut_name,dut_ip, ping_status):
    logpath = "%s" %(dut_name)

    FORMAT = '%(asctime)-15s %(clientip)s %(message)s %(ping)-8s'
    logging.basicConfig(format = FORMAT, filename = logpath,level=logging.DEBUG)

    d = {'clientip': dut_ip, 'ping': ping_status}
    logger = logging.getLogger('tcpserver11')

    console = logging.StreamHandler() #output streams
    aformat = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')

    console.setFormatter(aformat)

    logger.addHandler(console)
    logger.info('Ping Status:', extra=d)


save_log("WAP150","192.168.1.245","OK")