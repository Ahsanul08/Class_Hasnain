# First import the module

import paramiko 

# Get an SSHClient object

'''
with paramiko.SSHClient() as ssh:
     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     ssh.connect('192.168.33.10', username = 'vagrant', password= 'vagrant')
     stdin, stdout, stderr = ssh.exec_command('sudo ls')
     stdin.write('vagrant')
     stdin.flush()
     print(stdout.read())
'''


#		language    ---------------->   internal buffer(language) -----------------------> os buffer -----------------------> disk
#                                                        f.write();f.flush()                           f.fsync()      

'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect('192.168.33.10', username = 'vagrant', password= 'vagrant')

with ssh.open_sftp() as ftp:


    with ftp.file('test.txt','a+') as f:
        f.write('This is a test file')

ssh.close()   

'''

#multiple server;

import getpass

class ParamikoConnection:
    
     def __init__(self, username, password, hostname_list=[], connection_list=[]):
         self.hostname_list = hostname_list
         self.connection_list = connection_list
         self.username = username
         self.password = password      

     def create_connection(self):
         for host in self.hostname_list:
             ssh = paramiko.SSHClient()
             ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
             ssh.connect(host, username = self.username, password = self.password)
             self.connection_list.append(ssh)

     def get_connection_from_hostname(self, hostname):
         if hostname in self.hostname_list:
             host_index = self.hostname_list.index(hostname)
             return self.connection_list[host_index]


     def run_command(self, hostname, command):
         connection = self.get_connection_from_hostname(hostname)
         if connection:
             stdin, stdout, stderr = connection.exec_command(command)
             #stdin.write('y')
             #stdin.flush()
             return stdout.read() 
             


password = getpass.getpass()
#username = getpass.getuser()
username = 'vagrant'



paramiko_connection = ParamikoConnection(username, password)
paramiko_connection.hostname_list.append('192.168.33.10')
paramiko_connection.create_connection()
print(paramiko_connection.run_command('192.168.33.10', 'ls'))

                                                                                             
