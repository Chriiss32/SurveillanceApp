import subprocess

def automaic_start(name, path):
    # Команда, для добавления в регистр автоматического запуска программмы
    command = f'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v {name} /t REG_SZ /d "{path}" /f'
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
