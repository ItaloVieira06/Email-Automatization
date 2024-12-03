#importações
import subprocess
import interface


#executável
if __name__ == '__main__':
     cmd = "main.py -u abcd -p 1234"
     subprocess.call(cmd, Shell=True)