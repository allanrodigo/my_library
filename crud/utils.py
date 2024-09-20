def get_valid_price():
    while True:
        try:
            price_input = input("Novo preço: ").replace(",", ".")
            new_price = float(price_input)
            return new_price
        except ValueError:
            print("Erro: Por favor, insira um número válido para o preço.")