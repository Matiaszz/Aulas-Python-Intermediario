# .venv\Scripts\python .\Modulos\sbprocess.py
# é um modulo que executa comandos no CMD, Powershell, e outros prompts
import subprocess
import sys

os = sys.platform
cmd = ['ping', '127.0.0.1', '-c', '4']
encoding = 'utf_8'

if os == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp852'

process = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    encoding=encoding,  # praticamente um utf8

)
# print(process.args)
# print(process.stderr)
print(process.stdout)
# print(process.returncode)
