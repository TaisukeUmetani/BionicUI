import subprocess
choose = int(input('commit [0] or commit & push [1]: '))


def commit():
    message = input('commit message: ')
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])


if choose == 1:
    commit()
else:
    commit()
    branch = input('branch: ')
    subprocess.run(['git', 'push', 'origin', branch])

print('Done!')
