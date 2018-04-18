class Bancor:

    def __init__(self, connector_barance, bnt_supply, weight, graph, debug):
        self.connector_barance = connector_barance
        self.bnt_supply = bnt_supply
        self.weight = weight
        self.epoch = 0
        start_price = connector_barance / (bnt_supply * weight)
        self.graph = graph(start_price)
        self.debug = debug(self)

    def _buy(self, paid_connected_tokens):
        issued_tokens = self.bnt_supply * ((1.0 + paid_connected_tokens / self.connector_barance) ** self.weight - 1.0)
        self.connector_barance += paid_connected_tokens
        self.bnt_supply += issued_tokens
        return issued_tokens

    def buy(self, paid_connected_tokens):
        self.epoch += 1
        issued_tokens = self._buy(paid_connected_tokens)
        effective_rate = paid_connected_tokens / issued_tokens
        self.debug.buy(paid_connected_tokens, issued_tokens, effective_rate)
        price = self.result()
        self.graph.buy(effective_rate, issued_tokens, price)
        return issued_tokens

    def _sell(self, destroyed_tokens):
        paidout_connected_tokens = self.connector_barance * (1.0 - (1.0 - destroyed_tokens / self.bnt_supply) ** (1.0 / self.weight))
        self.connector_barance -= paidout_connected_tokens
        self.bnt_supply -= destroyed_tokens
        return paidout_connected_tokens

    def sell(self, destroyed_tokens):
        self.epoch += 1
        paidout_connected_tokens = self._sell(destroyed_tokens)
        effective_rate = paidout_connected_tokens / destroyed_tokens
        self.debug.sell(destroyed_tokens, paidout_connected_tokens, effective_rate)
        price = self.result()
        self.graph.sell(effective_rate, paidout_connected_tokens, price)
        return paidout_connected_tokens

    def result(self):
        price = self.connector_barance / (self.bnt_supply * self.weight)
        self.debug.result(price)
        return price

    def plot(self):
        self.graph.plot(self.epoch)
