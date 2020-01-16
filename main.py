# Coding style: https://www.python.org/dev/peps/pep-0008/
import requests  # https://requests.readthedocs.io/en/master/user/quickstart/
import json


# De olika intervallen är för att skicka bitcoin
blockchain_fee_btc_ = 'fastestFee: The lowest fee (in satoshis per byte) that will currently result in the fastest transaction confirmations (usually 0 to 1 block delay). \n ' \
                      'halfHourFee: The lowest fee (in satoshis per byte) that will confirm transactions within half an hour (with 90% probability). \n ' \
                      'hourFee: The lowest fee (in satoshis per byte) that will confirm transactions within an hour (with 90% probability). \n'
print(blockchain_fee_btc_)


btc_satoshi_fee = requests.get('https://bitcoinfees.earn.com/api/v1/fees/recommended', data={'key': 'value'})
print(btc_satoshi_fee.json())

#souce https://medium.com/@randerson112358/get-bitcoin-price-in-real-time-using-python-98b7393b6152  inte perfekt realtime
#BTC fee var jobbigare att räkna ut än jag trodde om du vill kika på det så kan du kolla här.
#https://bitcoin.stackexchange.com/questions/1195/how-to-calculate-transaction-size-before-sending-legacy-non-segwit-p2pkh-p2sh/46379
btc_price_request = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin")
btc_price = (btc_price_request.json()[0]["price_usd"])
print(btc_price)
class kund:
    def __init__(self, namn, investering, trading_tillatet, bara_kop, antal_manader):
        self.namn = namn
        self.investering = investering
        self.trading_tillatet = trading_tillatet
        self.bara_kop = bara_kop
        self.binance_withdraw_fee = 50  # 0.0005 BTC
        self.trading_tillatet_fee_percent = 1 - (
                antal_manader * 10) / 100  # 10% avdrag på totala feen per månad vi får trada med det kapitalet. max 10 mån

        if self.investering < 100:
            self.coinbase_fee = 10
        elif self.investering > 100 < 250:
            self.coinbase_fee = 15
        elif self.investering > 250 < 500:
            self.coinbase_fee = 20
        elif self.investering > 500 < 2000:
            self.coinbase_fee = 30
        self.cb_total_fees = self.coinbase_fee * 2

        if trading_tillatet == "nej":
            if self.investering <= 500:
                self.foretagets_fee = self.cb_total_fees + 50
            elif self.investering >= 500 <= 1000:
                self.foretagets_fee = self.cb_total_fees + 150
            elif self.investering >= 2500 <= 5000:
                self.foretagets_fee = self.cb_total_fees + 200
            elif self.investering >= 5000 <= 10000:
                self.foretagets_fee = self.cb_total_fees + 250
            elif self.investering >= 10000:
                self.foretagets_fee = self.cb_total_fees + 350
        elif trading_tillatet == "ja":
            if self.investering <= 500:
                self.foretagets_fee = self.cb_total_fees + self.binance_withdraw_fee + 50
            elif self.investering >= 500 <= 1000:
                self.foretagets_fee = self.cb_total_fees + self.binance_withdraw_fee + 150
            elif self.investering >= 2500 <= 5000:
                self.foretagets_fee = self.cb_total_fees + self.binance_withdraw_fee + 200
            elif self.investering >= 5000 <= 10000:
                self.foretagets_fee = self.cb_total_fees + self.binance_withdraw_fee + 250
            elif self.investering >= 10000:
                self.foretagets_fee = self.cb_total_fees + self.binance_withdraw_fee + 350

    def result(self):
        if self.bara_kop == "ja":
            print("bara_köp")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Foretagets fee:      {3}\n"
                  "Total fees för kund: {4}\n".format(self.namn, self.investering, self.coinbase_fee,
                                                      self.foretagets_fee, (self.cb_total_fees + self.foretagets_fee)))
        elif self.trading_tillatet == "ja":
            print("trading_tillåten")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Binance  fee: (send):{3}\n"
                  "Foretagets fee:      {4}\n"
                  "Total fees för kund: {5}\n".format(self.namn, self.investering, self.coinbase_fee,
                                                      self.binance_withdraw_fee, self.foretagets_fee, ((
                                                                                                               self.cb_total_fees + self.foretagets_fee + self.binance_withdraw_fee) * self.trading_tillatet_fee_percent)))


# Trading tillåten
# Namn, investering, trading_tillatet, bara_kop, antal_manader
kund1 = kund("Evert Noobsson", 50000, "ja", "nej", 10)
kund1.result()

# Bara köp
# Namn, investering, trading_tillatet, bara_kop, antal_manader
kund2 = kund("Evert Noobsson", 50000, "nej", "ja", 0)
kund2.result()

# Riktig kund krook
krook = kund("Krook1", 3000, "nej", "ja", 0)
krook.result()
