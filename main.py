from wallet import wallet

def main():

    w = wallet(wallet='ongrid', network='testnet')
    t = w.send_to('moFey39e5hGtrQia3s4NJCDA2ryBMeqhq9', '0.0006 TBTC', offline=False, network='testnet')
    w.scan()
    # print(t)
    # print(t.info())
    print(w.info())

if __name__ == '__main__':
    main()

