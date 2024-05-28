import subprocess

def automaic_start(name, path):
    # Команда, для добавления в регистр автоматического запуска программмы
    command = fr'reg add "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" /v {name} /t REG_SZ /d "{path}" /f'

    # Запуск команды
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Вывод результата
    print(stdout.decode())
    if stderr:
        print("Error:", stderr.decode())