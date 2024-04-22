import datetime
import shutil
import schedule # type: ignore
import time
import os


def job(diretorio_atual, diretorio_destino):
    try:
        # Verifica se o diretório de destino já existe
        if os.path.exists(diretorio_destino):
            print(f"O diretório de destino '{diretorio_destino}' já existe.")
            return

        # Realizando o backup apenas se o diretório de destino não existir
        backup = shutil.copytree(diretorio_atual, diretorio_destino)
        if backup:
            print(f"Backup realizado com sucesso para: {diretorio_destino}")
    except shutil.Error as e:
        print(f"Falha ao realizar o backup. Erro: {e}. Por favor, tente novamente.")


def main():
    data_hora_str = input(
        "Por favor, insira a data e hora de início do backup (formato: AAAA-MM-DD HH:MM): "
    )
    diretorio_atual = input("Informe o diretório que deseja realizar o backup: ")
    diretorio_destino = input("Informe o diretório que deseja salvar o arquivo de backup: ")

    try:
        data_hora_inicio = datetime.datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print(
            "Formato inválido. Certifique-se de inserir a data e hora no formato correto (AAAA-MM-DD HH:MM)."
        )
        return

    # Agendar o job
    schedule.every().day.at(data_hora_str).do(job, diretorio_atual=diretorio_atual, diretorio_destino=diretorio_destino)

    print(f"Backup agendado para: {data_hora_inicio}")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
