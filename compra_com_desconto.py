def msg():
    print("------" * 20)


def espaço():
    print("      " * 20)


valor_produto = int(input("Digite o valor da compra em R$: "))
espaço()

print(
    "À vista (DINHEIRO) ou cheque: 10% de desconto, DIGITE 1\n"
    "À vista no cartão (DÉBITO): 5% de desconto, DIGITE 2\n"
    "Em até 2x no cartão: PREÇO NORMAL, DIGITE 3\n"
    "3x ou mais (ATÉ 12X): 20% de juros, DIGITE 4"
)
espaço()

opcao = int(input("Por favor, digite uma opção: "))
print("PARCELAMOS EM ATÉ 12X")
espaço()

# Defina 'total_de_parcelas' com um valor padrão para evitar erros
total_de_parcelas = 1

if opcao == 4:
    total_de_parcelas = int(input("Digite a quantidade de parcelas: "))
    cartao = (20 / 100) * valor_produto
    s = (cartao + valor_produto) / total_de_parcelas

desconto1 = valor_produto * 0.1
desconto2 = valor_produto * 0.05
desconto3 = valor_produto / 2
msg()
if opcao == 1:
    valor_final = valor_produto - desconto1
    print(
        "Total a pagar com 10% de desconto é de R$ {:.2f}. Obrigado e volte sempre!".format(
            valor_final
        )
    )
elif opcao == 2:
    valor_final = valor_produto - desconto2
    print(
        "Total a pagar com 5% de desconto é de R$ {:.2f}. Obrigado e volte sempre!".format(
            valor_final
        )
    )
elif opcao == 3:
    print(
        "Total a pagar em 2x de R$ {:.2f} sem juros. Obrigado e volte sempre!".format(
            desconto3
        )
    )
elif opcao == 4:
    if total_de_parcelas > 1:
        print(
            "Sua compra de R$ {:.2f}, ficará em {}x de R$ {:.2f}. Obrigado e volte sempre!".format(
                valor_produto, total_de_parcelas, s
            )
        )
    else:
        print("Opção inválida, ou não foi fornecida a quantidade de parcelas.")
else:
    print("Opção inválida, por favor escolha uma opção válida.")
msg()
msg()
