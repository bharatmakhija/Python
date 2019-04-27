from SshWithPython.Config import Config
import paramiko

class sshConnect:

    def __init__(self):
        self.connection = None


    def make_connection(self):
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.connection.connect(Config.server, username=Config.user_name, password=Config.password)
        except Exception as e:
            print(str(e))


    def execute_command(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.connection.exec_command(command)
        print(ssh_stdout.readlines())

    def change_directory(self, path):
        command = 'cd ' + path
        self.execute_command(command)



k = sshConnect()
k.make_connection()
k.execute_command('pwd')
k.execute_command('ls')
k.change_directory('/opt/')
k.execute_command('pwd')
k.execute_command('ls')