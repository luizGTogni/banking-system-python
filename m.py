import os

from colorama import Fore

menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[F] Fechar

=> """

LIMIT_WITHDRAWAL = 500.00
DAILY_WITHDRAWAL_LIMITS = 3

bank_infos = {
    'balance': 0,
    'withdrawals_made': 0,
    'deposits': [],
    'withdrawals': []
}

def deposit():
    value = float(input('\nInforme um valor para o depósito: '))

    if value <= 0:
        return True, 'Informe um valor válido'

    bank_infos["deposits"].append(value)
    bank_infos['balance'] += value
    return False, ''

def withdraw():
    value = float(input('\nInforme um valor para o saque: '))

    if bank_infos['withdrawals_made'] >= DAILY_WITHDRAWAL_LIMITS:
        return True, 'Você excedeu os 3 saques diários!'
    
    if value > bank_infos['balance']:
        return True, 'Você não tem esse saldo na conta!'
    
    if value > LIMIT_WITHDRAWAL:
        return True, 'Você não pode sacar mais de R$ 500.00 por saque!'
    
    bank_infos['withdrawals_made'] += 1
    bank_infos['withdrawals'].append(value)
    bank_infos['balance'] -= value
    return False, ''

def bank_statement():
    if len(bank_infos['deposits']) == 0 and len(bank_infos['withdrawals']) == 0:
        print('\nSeu extrato está vazio no momento :(')

    if len(bank_infos['deposits']) > 0:
        print('DEPÓSITOS'.center(10))
        for idx, deposit_value in enumerate(bank_infos['deposits']):
            print(f'{idx} - R$ {deposit_value:.2f}')

    if len(bank_infos['withdrawals']) > 0:
        print('SAQUES'.center(10))
        for idx, withdraw_value in enumerate(bank_infos['withdrawals']):
            print(f'{idx} - R$ {withdraw_value:.2f}')

    while True:
        print('\npressione [V] para voltar para o menu.')
        option = input('')

        if option.upper() == 'V':
            break

    return False, ''

options = {
    'D': deposit,
    'S': withdraw,
    'E': bank_statement,
}

def view_balance(): 
    print(f'R$ {bank_infos["balance"]:.2f}')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    view_balance()
    option = input(menu)

    if option.upper() == 'F':
        break
    
    os.system('cls' if os.name == 'nt' else 'clear')

    view_balance()
    is_error, msg_error = options.get(option.upper())()

    if is_error:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(Fore.RED + msg_error + '\n')
            print(Fore.WHITE + 'pressione [V] para voltar para o menu.')
            option = input('')

            if option.upper() == 'V':
                break

