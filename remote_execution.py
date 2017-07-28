import paramiko 


def remote_execution():
    user = 'harish'
    psswd = 'harish'
    host = 'localhost'
    port = 2222
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host,username=user,password=psswd,port=port)
        stdin, stdout, stderr = client.exec_command('cd ~/repos && sh myscript.sh')
        print "stdout",stdout.readlines()
        print "stderr",stderr.readlines()
    except Exception as e:
        print('Exception found while executin command',str(e))


if __name__=='__main__':
    remote_execution()
