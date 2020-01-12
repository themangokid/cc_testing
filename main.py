# Coding style: https://www.python.org/dev/peps/pep-0008/
import requests  # https://requests.readthedocs.io/en/master/user/quickstart/
import json
import extra

# De olika intervallen är för att skicka bitcoin
blockchain_fee_btc_ = 'fastestFee: The lowest fee (in satoshis per byte) that will currently result in the fastest transaction confirmations (usually 0 to 1 block delay).\n halfHourFee: The lowest fee (in satoshis per byte) that will confirm transactions within half an hour (with 90% probability).\n hourFee: The lowest fee (in satoshis per byte) that will confirm transactions within an hour (with 90% probability).\n'
print(blockchain_fee_btc_)

r = requests.get('https://bitcoinfees.earn.com/api/v1/fees/recommended', data={'key': 'value'})
print(r.json())

"""
Kommentarer kan vara på svenska men all kod bör vara på engelska.
"""


class Customer:  # förslag: name, investment, trading_on, buy_only, number_of_months
    def __init__(self, name, investing, trading_allowed, buy_only, time_interval_of_investment):
        self.namn = name
        self.investing = investing
        self.trading_allowed = trading_allowed
        self.bara_kop = buy_only
        self.binance_withdraw_fee = 50  # 0.0005 BTC
        self.trading_tillatet_fee_percent = 1 - (
                time_interval_of_investment * 10) / 100  # 10% avdrag på totala feen per månad vi får trada med det kapitalet. max 10 mån

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
        if self.bara_kop == "ja":
            print("bara_köp")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Foretagets fee:      {3}\n"
                  "Total fees för kund: {4}\n".format(self.namn, self.investing, self.coinbase_fee,
                                                      self.company_fee, (self.cb_total_fees + self.company_fee)))
        elif self.trading_allowed == "ja":
            print("trading_tillåten")
            print("Köpare:              {0}\n"
                  "Investering:         {1}\n"
                  "Coinbase fee: (köp): {2}\n"
                  "Coinbase fee: (send):{2}\n"
                  "Binance  fee: (send):{3}\n"
                  "Foretagets fee:      {4}\n"
                  "Total fees för kund: {5}\n".format(self.namn, self.investing, self.coinbase_fee,
                                                      self.binance_withdraw_fee, self.company_fee, ((
                                                                                                            self.cb_total_fees + self.company_fee + self.binance_withdraw_fee) * self.trading_tillatet_fee_percent)))


# Trading tillåten
# Namn, investering, trading_tillatet, bara_kop, antal_manader
kund1 = Customer("Evert Noobsson", 50000, "ja", "nej", 10)
kund1.result()

# Bara köp
# Namn, investering, trading_tillatet, bara_kop, antal_manader
kund2 = Customer("Evert Noobsson", 50000, "nej", "ja", 0)
kund2.result()

# Riktig kund krook
krook = Customer("Krook1", 3000, "nej", "ja", 0)
krook.result()
