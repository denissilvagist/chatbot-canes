import calcularfrete
total_compra = 0.0
catcozinha = ["1 - Cooktop 4 Bocas de Indução Electrolux Efficient (IE4TW) 220V - R$ 1.749,00","2 - Geladeira Ideal+ Panasonic BT41 Frost Free Tecnologia Antibactéria 391L Branca - NR-BT41PD2WB 220V - R$ 2.148,89","3 - Fogão 5 Bocas Atlas Mônaco Top Glass Mesa de Vidro Bivolt - R$ 1.101,06 ","4 - Electrolux Purificador de Água Gelada Fria e Natural Touch Bivolt grafite PE12G - R$ 649,90","5 - Geladeira Refrigerador HQ Frost Free Side By Side 460 Litros Inox HQ-460SBSFF (220, Volts) - R$ 3.615,60 ","6 - Air Fryer Oven Electrolux por Rita Lobo 12L Digital Experience EAF86 220V - R$ 569,90","7 - Micro-ondas Electrolux Efficient ME23B 23L Branco 220V - R$ 554,44","8 - Liquidificador Mondial Turbo Power L-99 FB 550W 2,2L Preto 220V - R$ 189,90","9 - Batedeira Mondial Prática B-44 400W com Tigela 3,6L 220V - R$ 139,90","10 - Sanduicheira e Grill Britânia BGR27I Antiaderente 850W 220V - R$ 119,90"]
catsala =["1 - Smart TV Samsung Crystal UHD 4K CU7700 55 Polegadas Wi-Fi Bluetooth - R$ 2.799,00","2 - Smart TV LG UHD AI ThinQ 4K 50UR8750PSA 50 Polegadas - R$ 2.499,90","3 - Soundbar JBL Cinema SB170 220W com Subwoofer Sem Fio - R$ 999,90","4 - Home Theater Soundbar Samsung HW-B550 410W Bluetooth - R$ 1.299,00","5 - Ar-Condicionado Split Inverter LG Dual Voice 12000 BTUs Frio 220V - R$ 2.199,90","6 - Ventilador de Torre Mallory Air Timer TS+ 126W 220V - R$ 349,90","7 - Caixa de Som Bluetooth JBL PartyBox Club 120 com Luzes LED - R$ 2.499,00","8 - Purificador de Ar Philco PPA01A com Filtro HEPA Bivolt - R$ 699,90","9 - Projetor Full HD Epson EpiqVision FH02 Smart Streaming - R$ 3.499,00","10 - Receptor e Assistente Inteligente Amazon Fire TV Cube 4K Wi-Fi - R$ 899,90"]
catlavanderia = ["1 - Máquina de Lavar Electrolux Essential Care 13kg LED13 Branca 220V - R$ 2.099,90","2 - Máquina de Lavar Brastemp BWK13AB 13kg Branca 220V - R$ 2.349,00","3 - Lava e Seca Samsung WD11M 11kg/7kg Inverter Branca 220V - R$ 3.899,90","4 - Lava e Seca LG VC4 11kg com Inteligência Artificial AIDD 220V - R$ 4.299,00","5 - Ferro de Passar a Vapor Philips Walita Série 5000 DST5040 220V - R$ 299,90","6 - Ferro de Passar a Vapor Electrolux Easyline SIE70 220V - R$ 149,90","7 - Passadeira a Vapor Vertical Mondial VIP Care VP-07 220V - R$ 329,90","8 - Secadora de Roupas Electrolux Essential Care 11kg STH11 Branca 220V - R$ 2.799,90","9 - Centrífuga de Roupas Suggar Giromax 15kg Branca 220V - R$ 499,90","10 - Varal Elétrico Secador de Roupas Wanke Elegance 8 Varetas 220V - R$ 699,90"]
carrinho = []   
while True:
    print("========== Canes Store ============")
    print("     Onde comprar aqui é caro!")
    print("1 - Comprar\n2 - Carrinho\n3 - Trabalhe Conosco\n4 - Calcular frete\n5 - Sair")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        while True:
            print("========== Catálogo de categorias ==========")
            print("1 - Cozinha\n2 - Sala de Estar\n3 - Lavanderia\n4 - Finalizar Compra\n5 - Voltar ao menu principal")
            opcat = int(input("escolha uma categoria ou finalizar compra: "))
            if opcat == 1:
                print("========== Produtos de Cozinha ==========")
                for i in catcozinha:
                    print(i)
                opproduto = int(input("Escolha um produto: "))
                if opproduto == 1:
                    print("Você escolheu Cooktop 4 Bocas de Indução Electrolux Efficient")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  1749
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    #carrinho.append(f"Cooktop 4 Bocas de Indução Electrolux Efficient (IE4TW) 220V - {valor_total}")
                    carrinho.append(catcozinha[0]+ f"- R$ {valor_total}")
                    
                elif opproduto == 2:
                    print("Você escolheu Geladeira Ideal+ Panasonic BT41")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2148.89
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[1]+ f"- R$ {valor_total}")
                elif opproduto == 3:
                    print("Você escolheu Fogão 5 Bocas Atlas Mônaco Top Glass")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  1101.06
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[2]+ f"- R$ {valor_total}")
                elif opproduto == 4:
                    print("Você escolheu Electrolux Purificador de Água Gelada Fria")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  649.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[3]+ f"- R$ {valor_total}")
                elif opproduto == 5:
                    print("Você escolheu Geladeira Refrigerador HQ Frost Free Side")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  3615.60
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[4]+ f"- R$ {valor_total}")
                elif opproduto == 6:
                    print("Você escolheu Air Fryer Oven Electrolux por Rita Lobo 12L")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  569.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[5]+ f"- R$ {valor_total}")
                elif opproduto == 7:
                    print("Você escolheu Micro-ondas Electrolux Efficient ME23B 23L")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  554.44
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[6]+ f"- R$ {valor_total}")
                elif opproduto == 8:
                    print("Você escolheu Liquidificador Mondial Turbo Power L-99 FB 550W")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  189.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[7]+ f"- R$ {valor_total}")
                elif opproduto == 9:
                    print("Você escolheu Batedeira Mondial Prática B-44 400W")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  139.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[8]+ f"- R$ {valor_total}")
                elif opproduto == 10:
                    print("Você escolheu Sanduicheira e Grill Britânia BGR27I Antiaderente 850W 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  119.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catcozinha[9]+ f"- R$ {valor_total}")
                else:
                    print("Produto inexistente!")
            elif opcat == 2:
                print("========== Produtos para sala de estar ==========")
                for i in catsala:
                    print(i)
                opproduto = int(input("Escolha um produto: "))
                if opproduto == 1:
                    print("Você escolheu Smart TV Samsung Crystal UHD 4K CU7700 55")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2799.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[0]+ f"- R$ {valor_total}")
                elif opproduto == 2:
                    print("Você escolheu Smart TV LG UHD AI ThinQ 4K 50UR8750PSA 50 Polegadas")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2499.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[1]+ f"- R$ {valor_total}")
                elif opproduto == 3:
                    print("Você escolheu Soundbar JBL Cinema SB170 220W com Subwoofer Sem Fio")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  999,90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[2]+ f"- R$ {valor_total}")
                elif opproduto == 4:
                    print("Você escolheu Home Theater Soundbar Samsung HW-B550")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  1299.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[3]+ f"- R$ {valor_total}")
                elif opproduto == 5:
                    print("Você escolheu Ar-Condicionado Split Inverter LG Dual Voice")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2199.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[4]+ f"- R$ {valor_total}")
                elif opproduto == 6:
                    print("Você escolheu Ventilador de Torre Mallory Air Timer TS+ 126W 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  349.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[5]+ f"- R$ {valor_total}")
                elif opproduto == 7:
                    print("Você escolheu Caixa de Som Bluetooth JBL PartyBox Club 120 com Luzes LED")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2499.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[6]+ f"- R$ {valor_total}")
                elif opproduto == 8:
                    print("Você escolheu Purificador de Ar Philco PPA01A com Filtro HEPA Bivolt")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  699.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[7]+ f"- R$ {valor_total}")
                elif opproduto == 9:
                    print("Você escolheu Projetor Full HD Epson EpiqVision FH02 Smart Streaming")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  3499.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[8]+ f"- R$ {valor_total}")
                elif opproduto == 10:
                    print("Você escolheu Receptor e Assistente Inteligente Amazon Fire TV Cube 4K")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  899.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catsala[9]+ f"- R$ {valor_total}")
                else:
                    print("Produto inexistente!")
            elif opcat == 3:
                print("========== Produtos para lavanderia ==========")
                for i in catlavanderia:
                    print(i)
                opproduto = int(input("Escolha um produto: "))
                if opproduto == 1:
                    print("Você escolheu Máquina de Lavar Electrolux Essential Care 13kg LED13 Branca 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2099.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 2:
                    print("Você escolheu Máquina de Lavar Brastemp BWK13AB 13kg Branca 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2349.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 3:
                    print("Você Lava e Seca Samsung WD11M 11kg/7kg Inverter Branca 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *   3899.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 4:
                    print("Você escolheu Lava e Seca LG VC4 11kg com Inteligência Artificial AIDD 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  4299.00
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 5:
                    print("Você escolheu Ferro de Passar a Vapor Philips Walita Série 5000 DST5040 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  299.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 6:
                    print("Você escolheu Ferro de Passar a Vapor Electrolux Easyline SIE70 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  149.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 7:
                    print("Você escolheu Passadeira a Vapor Vertical Mondial VIP Care VP-07 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  329.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 8:
                    print("Você escolheu Secadora de Roupas Electrolux Essential Care 11kg STH11 Branca 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  2799.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 9:
                    print("Você escolheu Centrífuga de Roupas Suggar Giromax 15kg Branca 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  499.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                elif opproduto == 10:
                    print("Você escolheu Varal Elétrico Secador de Roupas Wanke Elegance 8 Varetas 220V")
                    quantidade = int(input("Digite a quantidade: "))
                    valor_total = quantidade *  699.90
                    total_compra = total_compra + valor_total
                    print(f"Você pagará R${valor_total} desse produto")
                    print(f"O total parcial da compra é de R${total_compra}")
                    carrinho.append(catlavanderia[0]+ f"- R$ {valor_total}")
                else:
                    print("Produto inexistente!")
            elif opcat == 4:
                for i in carrinho:
                    print(i)
                print(f"Seu total é de R$ {total_compra}")
                estado= input("Digite seu estado: ")
                valor_frete = calcularfrete.frete(estado)
                totalComFrete = total_compra+valor_frete
                print(f"Seu total com o frete é de R$ {totalComFrete}")
                print("")
                print("1 - PIX\n2 - Crédito\n3 - Débito")
                oppagamento = int(input("Escolha uma opção de pagamento"))
                if oppagamento == 1:
                    print("Chave pix: denis.silvace@hotmail.com")
                    total_compra = 0
                    carrinho.clear()
                    break
                elif oppagamento == 2:
                    print("Insira seu cartão de Crédito")
                    print("Pagamento aprovado com sucesso!")
                    total_compra = 0
                    carrinho.clear()
                    break
                elif oppagamento == 3:
                    print("Insira seu cartão de Débito")
                    print("Pagamento aprovado com sucesso!")
                    total_compra = 0
                    carrinho.clear()
                    break
                else:
                    print("Opção de pagamento inválida!")
            elif opcat == 5:
                break
            else:
                print("Categoria inexistente!")
    elif opcao == 2:
        for i in carrinho:
            print (i)
        print (f"Seu total é de R${total_compra}")
        limpar = int(input("Deseja limpar carrinho\n1 - Sim\n2 - Não\n"))
        if limpar == 1:
            total_compra=0
            carrinho.clear()
            print("Carrinho Vazio")
        else:
            print("Continuando a compra!")
    elif opcao == 3:
        NomeCompleto = input("Digite seu nome completo: ")
        email = input("Digite seu email:")
        telefone = input("Digite seu telefone:")
        print("Obrigado! Em breve entraremos em contato")
    elif opcao == 4:
        uf = input("Digite seu estado: ")
        valor_frete = calcularfrete.frete(uf)
        print(f"seu frete é de R${valor_frete}")
    elif opcao == 5:
        print("Obrigado por utilizar nossos serviços! Esperamos não contar com você novamente!")
        break
    else:
        print("Opção inválida, digite 1 ou 2 ou 3 ou 4")