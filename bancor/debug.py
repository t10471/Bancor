class Debug:

    def __init__(self, bancor):
        self.bancor = bancor

    def buy(self, paid_connected_tokens, issued_tokens, effective_rate):
        m = 'No. {} Buy Paid: {:.5f} ETH Received: {:.5f} BNT Effective Rate: {:.5f} ETH/BNT'
        print(m.format(self.bancor.epoch, paid_connected_tokens, issued_tokens, effective_rate))

    def sell(self, destroyed_tokens, paidout_connected_tokens, effective_rate):
        m = 'No. {} Sell Paid: {:.5f} BNT Received: {:.5f} ETH Effective Rate: {:.5f} ETH/BNT'
        print(m.format(self.bancor.epoch, destroyed_tokens, paidout_connected_tokens, effective_rate))

    def result(self, price):
        m = 'Connector Balance: {:.5f} BNT Supply: {:.5f} Price(Ether/BNT): {:.5f}'
        print(m.format(self.bancor.connector_barance, self.bancor.bnt_supply, price))

class DummyDebug:

    def __init__(self, bancor):
        pass

    def buy(self, E, t, p):
        pass

    def sell(self, T, e, p):
        pass

    def result(self, p):
        pass
