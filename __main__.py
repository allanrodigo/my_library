from crud.backups import (
    create_backup,
    clean_backups,
)
from crud.export_csv import (
    export_csv,
    import_csv,
)
from crud.operations import (
    add_book,
    show_books,
    remove_book,
    search_book_by_author,
    update_price,
    create_table,
)
from crud.utils import get_valid_price


def show_menu():
    print("""
    1. Adicionar novo livro
    2. Exibir todos os livros
    3. Atualizar preço de um livro
    4. Remover um livro
    5. Buscar livros por author
    6. Exportar dados para CSV
    7. Importar dados de CSV
    8. Fazer backup do banco de dados
    9. Sair
    """)

def main():
    create_table()
    while True:
        show_menu()
        choose = input("Escolha uma opção: ")

        match choose:
            case '1':
                title = input("Título: ")
                author = input("author: ")
                year = int(input("Ano de publicação: "))
                price = get_valid_price()
                add_book(title, author, year, price)
                create_backup()
            case '2':
                show_books()
            case '3':
                book_id = int(input("ID do livro: "))
                new_price = get_valid_price()
                update_price(book_id, new_price)
                create_backup()
            case '4':
                book_id = int(input("ID do livro: "))
                remove_book(book_id)
                create_backup()
            case '5':
                author = input("author: ")
                search_book_by_author(author)
            case '6':
                export_csv()
            case '7':
                path = input("Caminho do arquivo CSV: ")
                import_csv(path)
            case '8':
                create_backup()
            case '9':
                clean_backups()
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
