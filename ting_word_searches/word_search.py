def exists_word(word, instance):
    result = []
    for index in range(instance.__len__()):
        data = instance.search(index)
        data_lines = data["linhas_do_arquivo"]
        ocurrences = []
        for j in range(data_lines.__len__()):
            if word.lower() in data_lines[j].lower():
                ocurrences.append(j + 1)
        if len(ocurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [
                    {'linha': row} for row in ocurrences],
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
