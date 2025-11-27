print("\t ~ Bem vindo ao mundo Invertido dos carros da GLT ~ ")
print(" \t \t ~ Cadastro do Cliente GLT ~")
cliente_nome = input("Informe seu nome: ").strip().title()
cliente_number = input("Informe o telefone de contato: ").strip()
saldoFinal = float(input("Saldo disponível (R$): "))
print(f"\nBem vindo, {cliente_nome}")

def menu():
    print("\t \t OPÇÕES ")
    print("+=" * 25)
    print(f"\t Saldo disponível: {saldoFinal:.2f}")
    print("\n 1- LISTA DE VEÍCULOS ")
    print("\n 2- VENDER VEICULOS ")
    print("\n 3- ALUGAR VEICULOS ")
    print("\n 4- COMPRAR VEICULOS ")
    print("\n 0- SAIR ")

inventory = [
    # -------------------- SUVS --------------------
    {"id": "SUV001", "categoria": "SUV", "marca": "Jeep", "modelo": "Renegade", "ano": 2021, "preco": 112000.0, "status": "disponivel"},
    {"id": "SUV002", "categoria": "SUV", "marca": "Jeep", "modelo": "Compass", "ano": 2022, "preco": 165000.0, "status": "disponivel"},
    {"id": "SUV003", "categoria": "SUV", "marca": "Hyundai", "modelo": "Creta", "ano": 2022, "preco": 115000.0, "status": "disponivel"},
    {"id": "SUV004", "categoria": "SUV", "marca": "Nissan", "modelo": "Kicks", "ano": 2021, "preco": 108000.0, "status": "disponivel"},
    {"id": "SUV005", "categoria": "SUV", "marca": "Volvo", "modelo": "XC40", "ano": 2020, "preco": 220000.0, "status": "disponivel"},
    {"id": "SUV006", "categoria": "SUV", "marca": "Peugeot", "modelo": "3008", "ano": 2018, "preco": 124000.0, "status": "disponivel"},

    # -------------------- SEDANS --------------------
    {"id": "SED001", "categoria": "Sedan", "marca": "Toyota", "modelo": "Corolla", "ano": 2020, "preco": 85000.0, "status": "disponivel"},
    {"id": "SED002", "categoria": "Sedan", "marca": "Honda", "modelo": "Civic", "ano": 2019, "preco": 83000.0, "status": "disponivel"},
    {"id": "SED003", "categoria": "Sedan", "marca": "Chevrolet", "modelo": "Cruze", "ano": 2019, "preco": 92000.0, "status": "disponivel"},
    {"id": "SED004", "categoria": "Sedan", "marca": "Volkswagen", "modelo": "Voyage", "ano": 2017, "preco": 45000.0, "status": "disponivel"},
    {"id": "SED005", "categoria": "Sedan", "marca": "Hyundai", "modelo": "HB20S", "ano": 2021, "preco": 72000.0, "status": "disponivel"},
    {"id": "SED006", "categoria": "Sedan", "marca": "Audi", "modelo": "A3", "ano": 2019, "preco": 168000.0, "status": "disponivel"},

    # -------------------- MOTOS --------------------
    {"id": "MOT001", "categoria": "Moto", "marca": "Honda", "modelo": "CG 160", "ano": 2021, "preco": 14500.0, "status": "disponivel"},
    {"id": "MOT002", "categoria": "Moto", "marca": "Honda", "modelo": "Biz 125", "ano": 2020, "preco": 13000.0, "status": "disponivel"},
    {"id": "MOT003", "categoria": "Moto", "marca": "Yamaha", "modelo": "Fazer 250", "ano": 2022, "preco": 21000.0, "status": "disponivel"},
    {"id": "MOT004", "categoria": "Moto", "marca": "Yamaha", "modelo": "Factor 150", "ano": 2021, "preco": 15000.0, "status": "disponivel"},
    {"id": "MOT005", "categoria": "Moto", "marca": "BMW", "modelo": "GS 310", "ano": 2020, "preco": 33000.0, "status": "disponivel"},
    {"id": "MOT006", "categoria": "Moto", "marca": "Kawasaki", "modelo": "Ninja 400", "ano": 2019, "preco": 28000.0, "status": "disponivel"},

    # -------------------- CAMINHONETES --------------------
    {"id": "CAM001", "categoria": "Caminhonete", "marca": "Toyota", "modelo": "Hilux", "ano": 2020, "preco": 240000.0, "status": "disponivel"},
    {"id": "CAM002", "categoria": "Caminhonete", "marca": "Chevrolet", "modelo": "S10", "ano": 2019, "preco": 198000.0, "status": "disponivel"},
    {"id": "CAM003", "categoria": "Caminhonete", "marca": "Ford", "modelo": "Ranger", "ano": 2021, "preco": 210000.0, "status": "disponivel"},
    {"id": "CAM004", "categoria": "Caminhonete", "marca": "Nissan", "modelo": "Frontier", "ano": 2022, "preco": 230000.0, "status": "disponivel"},
    {"id": "CAM005", "categoria": "Caminhonete", "marca": "Volkswagen", "modelo": "Amarok", "ano": 2020, "preco": 225000.0, "status": "disponivel"},
    {"id": "CAM006", "categoria": "Caminhonete", "marca": "Fiat", "modelo": "Toro", "ano": 2021, "preco": 145000.0, "status": "disponivel"}
]

# Função para buscar veículo pelo ID
def buscar_por_id(vid):
    # Retorna o veículo com o ID informado
    return next((v for v in inventory if v["id"] == vid), None)

def lista_veiculos():
    print("\nLista de Veículos:")
    print("-" * 35)
    for v in inventory:
       
        print(f"{v['id']:8} | {v['categoria']:12} | {v['marca']:8} {v['modelo']:12} | Ano: {v['ano']} | R$ {v['preco']:,.2f}")
    print("-" * 35)

# Função de Compra
def comprar_veiculo(saldo):
    print("\n\t | Compra de veículo GLT | ")

    novo = {}

    novo["id"] = input("ID do veículo: ").strip().upper()
    novo["categoria"] = input("Categoria (SUV, Sedan, Moto...): ").strip().title()
    novo["marca"] = input("Marca: ").strip().title()
    novo["modelo"] = input("Modelo: ").strip().title()
    novo["ano"] = int(input("Ano: "))
    
    # 25% de acréscimo no preço base para o inventário
    preco_base = float(input("Preço base (sem acréscimo) R$: "))
    novo["preco"] = preco_base * 1.25  
    novo["status"] = "disponivel"

    inventory.append(novo)
    print(f"\nVeículo cadastrado! Preço no inventário (com 25% de acréscimo): R$ {novo['preco']:,.2f}\n")
    return saldo 

# Função de Venda
def vender_veiculo(saldo):
    print("\t \t Bem vindo a venda de veículos GLT ")
    valor = input(" Informe o ID do veículo que deseja vender:").strip().upper()
    v = buscar_por_id(valor)
    
    if not v:
        print("ID não encontrado.")
        return saldo
    
    if v["status"] != "disponivel":
        print("Veículo indisponível para venda.")
        return saldo

    # 12% de desconto sobre o preço de inventário
    preco_venda = v["preco"] * 0.88  # 100% - 12% = 88% (0.88)
    saldo += preco_venda
    inventory.remove(v)
    
    print(f"Veículo {v['id']} vendido por R$ {preco_venda:,.2f} (Preço do inventário - 12% de desconto).\nSaldo atualizado: R$ {saldo:,.2f}")
    return saldo

def alugar_veiculo(valor):
    print("\n--- Aluguel de Veículo GLT ---")

    vid = input("Informe o ID do veículo: ").strip().upper()
    v = buscar_por_id(vid)

    if not v:
        print("ID não encontrado.")
        return valor

    if v["status"] != "disponivel":
        print("Veículo indisponível para aluguel.")
        return valor

    dias = int(input("Quantidade de dias: "))
    valor_total = dias * 159 
       # aluguel por dia

    print(f"Valor total do aluguel: R$ {valor_total:.2f}")

    if valor < valor_total:
        print("Saldo insuficiente para o aluguel.")
        return valor
        
    # Desconta e remove
    valor -= valor_total
    inventory.remove(v)

    print(f"Veículo {v['id']} alugado por {dias} dias.\nSaldo restante: R$ {valor:.2f}")
    return valor

# Loop principal
while True:
    menu()
    opcao = input("\n Informe uma opção das opções: ")
    
    # Estrutura match case
    match opcao:
        case "1":
            lista_veiculos()
        case "2":
            saldoFinal = vender_veiculo(saldoFinal)
        case "3":
            saldoFinal = alugar_veiculo(saldoFinal)
        case "4":
            saldoFinal = comprar_veiculo(saldoFinal)
        case "0":
            print(" Até, logo ... GLT Agradece a prefência...")
            break
        case _:
            print("Opção inválida. Tente novamente.")