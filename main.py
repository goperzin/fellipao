import json
import os

def montar_json_amis():
    # Define os nomes dos arquivos para processar
    arquivos = ["arquivo1.json", "arquivo2.json", "arquivo3.json"]

    while True:
        # Solicita ao usuário qual arquivo deseja alterar
        print("Escolha o arquivo para alterar:")
        for i, nome_arquivo in enumerate(arquivos, start=1):
            print(f"{i} - {nome_arquivo}")
        print("4 - SAIR")

        escolha = input("Digite o número correspondente ao arquivo: ").strip()

        try:
            indice_arquivo = int(escolha) - 1
            if indice_arquivo == len(arquivos):
                print("Encerrando o programa.")
                break
            if indice_arquivo < 0 or indice_arquivo >= len(arquivos):
                raise ValueError
            nome_arquivo = arquivos[indice_arquivo]
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        # Solicita ao usuário a entrada das AMIs
        entrada = input("Insira uma ou mais AMIs separadas por vírgula: ").strip()

        # Divide a entrada por vírgulas e remove espaços extras
        novas_amis = [ami.strip() for ami in entrada.split(",") if ami.strip()]

        try:
            # Tenta carregar o JSON existente (se existir)
            with open(nome_arquivo, "r") as arquivo:
                dados = json.load(arquivo)
        except FileNotFoundError:
            # Se o arquivo não existir, cria uma estrutura inicial
            dados = {"imagemId": []}

        # Adiciona as novas AMIs à lista existente, mantendo a ordem e evitando duplicatas
        for ami in novas_amis:
            if ami not in dados["imagemId"]:
                dados["imagemId"].append(ami)

        # Salva o JSON atualizado no arquivo
        with open(nome_arquivo, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        print(f"JSON atualizado com sucesso no arquivo {nome_arquivo}! Saída:")
        print(json.dumps(dados, indent=4))

if __name__ == "__main__":
    montar_json_amis()
