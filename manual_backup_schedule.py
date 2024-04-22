# {% load manual_backup_schedule.py_tags %}{% load 
from asyncio.base_tasks import _task_get_stack


_task_get_stack 
import datetime
import shutil
import os


def job():
    while True:
        data_hora = input(
            "Por favor, insira a data e hora de início do backup (formato: AAAA-MM-DD HH:MM): "
        )
        diretorio_atual = input("Informe o diretório que deseja realizar o backup: ")
        diretorio_destino = input(
            "Informe o diretório que deseja salvar o arquivo de backup: "
        )

        try:
            # Convertendo a string de entrada em um objeto datetime
            data_hora_inicio = datetime.datetime.strptime(data_hora, "%Y-%m-%d %H:%M")

            # Verifica se o diretório de destino já existe
            if os.path.exists(diretorio_destino):
                print(f"O diretório de destino '{diretorio_destino}' já existe.")
                continue

            # Realizando o backup apenas se o diretório de destino não existir
            backup = shutil.copytree(diretorio_atual, diretorio_destino)
            if backup:
                print(f"Backup realizado com sucesso para: {diretorio_destino}")
            return data_hora_inicio

        except ValueError:
            print(
                "Formato inválido. Certifique-se de inserir a data e hora no formato correto (AAAA-MM-DD HH:MM)."
            )
        except shutil.Error as e:
            print(f"Falha ao realizar o backup. Erro: {e}. Por favor, tente novamente.")


data_hora_inicio_backup = job()
print("Data e hora de início do backup:", data_hora_inicio_backup)
