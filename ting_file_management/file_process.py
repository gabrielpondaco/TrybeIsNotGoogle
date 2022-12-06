import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file_to_list = txt_importer(path_file)
    output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_to_list),
        "linhas_do_arquivo": file_to_list
    }
    instance.enqueue(output)
    sys.stdout.write(f"{output}")


def remove(instance):
    if (instance.__len__() == 0):
        sys.stdout.write("Não há elementos\n")
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
