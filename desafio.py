agenda = {}

incluirNovoNome = input("Digite o nome que deseja adicionar: ")
telefone = input("Digite o telefone: ")

incluirTelefone = input("Digite o nome que deseja adicionar: ")
if incluirTelefone not in agenda:
    incluirTelefone = input("Digite o telefone que deseja adicionar: ")
    agenda[nome].append(telefone)

excluirTelefone = input("Digite o nome que deseja excluir telefone: ")
if excluirTelefone not in agenda:
        telefone = input("Digite o telefone que deseja excluir: ")
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)