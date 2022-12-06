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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
