# Coding style: https://www.python.org/dev/peps/pep-0008/
# https://requests.readthedocs.io/en/master/user/quickstart/
# souce https://medium.com/@randerson112358/get-bitcoin-price-in-real-time-using-python-98b7393b6152  inte perfekt realtime
# https://bitcoin.stackexchange.com/questions/1195/how-to-calculate-transaction-size-before-sending-legacy-non-segwit-p2pkh-p2sh/46379
import requests
import json
import blockchain


# Denna klassen ska ta in en cc och sedan skicka ut den riktiga kostnanden i SEK/DOLLAR/USD
class Transaction_fees:
    def __init__(self, cc):
        self.cc = cc
        cc_name = cc
        print(cc_name)
        cc = requests.get("https://api.coinmarketcap.com/v1/ticker/{}".format(cc_name))
        print(cc.json()[0]['price_usd'])


    def btc_transfer(self):
        r = requests.get('https://bitcoinfees.earn.com/api/v1/fees/recommended', data={'key': 'value'})
        btc_fee_price = json.loads(r.text)
        satoshi = btc_fee_price.get('fastestFee', "")
        satoshi_f = float(satoshi)
        btc_price_request = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin")
        btc_price = (btc_price_request.json()[0]["price_usd"])
        btc_price_f =float(btc_price)

        print(satoshi_f)
        print(btc_price_f)

        btc_transfer_fee = btc_price_f * satoshi_f * 0.00000001
        return btc_transfer_fee


class Customer:
    def __init__(self, name, investing, trading_allowed, buy_only, time_interval_of_investment):
        self.name = name
        self.investing = investing
        self.trading_allowed = trading_allowed
        self.buy_only = buy_only
        self.binance_withdraw_fee = 50  # 0.0005 BTC
        self.trading_tillatet_fee_percent = 1 - (
                time_interval_of_investment * 10) / 100

        if self.investing < 100:
            self.coinbase_fee = 10
        elif self.investing > 100 < 250:
            self.coinbase_fee = 15
        elif self.investing > 250 < 500:
            self.coinbase_fee = 20
        elif self.investing > 500 < 2000:
            self.coinbase_fee = 30
        self.cb_total_fees = self.coinbase_fee * 2

        if trading_allowed == "nej":
            if self.investing <= 500:
                self.company_fee = self.cb_total_fees + 50
            elif self.investing >= 500 <= 1000:
                self.company_fee = self.cb_total_fees + 150
            elif self.investing >= 2500 <= 5000:
                self.company_fee = self.cb_total_fees + 200
            elif self.investing >= 5000 <= 10000:
                self.company_fee = self.cb_total_fees + 250
            elif self.investing >= 10000:
                self.company_fee = self.cb_total_fees + 350
        elif trading_allowed == "ja":
            if self.investing <= 500:
                self.company_fee = self.cb_total_fees + self.binance_withdraw_fee + 50
            elif self.investing >= 500 <= 1000:
                self.company_fee = self.cb_total_fees + self.binance_withdraw_fee + 150
            elif self.investing >= 2500 <= 5000:
                self.company_fee = self.cb_total_fees + self.binance_withdraw_fee + 200
            elif self.investing >= 5000 <= 10000:
                self.company_fee = self.cb_total_fees + self.binance_withdraw_fee + 250
            elif self.investing >= 10000:
                self.company_fee = self.cb_total_fees + self.binance_withdraw_fee + 350

    def result(self):
        if self.buy_only == "ja":
            print("buy_only")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Foretagets fee:      {3}\n"
                  "Total fees för kund: {4}\n".format(self.name, self.investing, self.coinbase_fee,
                                                      self.company_fee, (self.cb_total_fees + self.company_fee)))
        elif self.trading_allowed == "ja":
            print("trading_allowed")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Binance  fee: (send):{3}\n"
                  "Foretagets fee:      {4}\n"
                  "Total fees för kund: {5}\n".format(self.namn, self.investing, self.coinbase_fee,
                                                      self.binance_withdraw_fee, self.company_fee, ((
                                                                                                            self.cb_total_fees + self.company_fee + self.binance_withdraw_fee) * self.trading_tillatet_fee_percent)))

# Run customer calcs
def customers():
    kund1 = Customer("Evert Noobsson", 50000, "ja", "nej", 10)
    kund1.result()
    kund2 = Customer("Evert Noobsson", 50000, "nej", "ja", 0)
    kund2.result()
    rk = Customer("rk", 3000, "nej", "ja", 0)
    rk.result()
    f = Customer("f", 1000, "nej", "ja", 0)
    f.result()



transaction = Transaction_fees('bitcoin')
print(transaction.btc_transfer())
