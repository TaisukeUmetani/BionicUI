import subprocess
message = input('commit message: ')
branch = input('branch: ')
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', message])
subprocess.run(['git', 'push', 'origin', branch])
