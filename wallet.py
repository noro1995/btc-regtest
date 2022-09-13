from bitcoinlib.wallets import Wallet, wallet_delete_if_exists, wallet_exists, wallet_create_or_open
from bitcoinlib.mnemonic import Mnemonic
import os
import base64


def wallet(wallet='Wallet', mnemonic=None, network='testnet'):
    if wallet_exists(wallet):
        return Wallet(wallet)
    if mnemonic is None:
        mnemonic = Mnemonic().generate()
    print('Mnemonic: \n', mnemonic)
    if not os.path.exists('wallets'):
        os.mkdir('wallets')
    with open(f'wallets/{wallet}.txt', 'w') as f:
        f.write(f'{wallet}:{base64.b64encode(mnemonic.encode())}')
        print('wallet file created...')
    return Wallet.create(
        name=wallet,
        keys=mnemonic,
        network=network
    )


def wallet_delete(wallet):
    name = f'wallets/{wallet}.txt'
    if os.path.exists(name):
        os.remove(name)
    return wallet_delete_if_exists(wallet)
