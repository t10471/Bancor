import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Graph:

    def __init__(self, price):
        self.lefts = []     # x-coordinate of left line of each Bar
        self.widths = []    # width of each Bar
        self.heights = []   # height of each Bar(effective price)
        self.prices = []    # height of each price(self.starting price and resulting price)
        self.actions = []    # action of each har, 0: Red, 1:Green
        self.x = 0.00       # x-coordinate of current Bar(first bar self.starts from '0')
        self.price = price  # current price(self.starting price of ETH/BNT)
        self.color = {
            'sell': {'bar': '#D24D57', 'plot': '#96281B'},
            'buy': {'bar': '#3FC380', 'plot': '#3FC380'},
        }

    def buy(self, effective_rate, issued_tokens, price):
        self.actions.append("buy")
        self.widths.append(np.array([issued_tokens]))
        self.heights.append(np.array([effective_rate]))
        self.lefts.append(self.x)
        self.x += issued_tokens
        self.prices.append(self.price)
        self.price = price

    def sell(self, effective_rate, paidout_connected_tokens, price):
        self.actions.append("sell")
        self.widths.append(np.array([paidout_connected_tokens]))
        self.heights.append(np.array([effective_rate]))
        self.lefts.append(self.x)
        self.x += paidout_connected_tokens
        self.prices.append(self.price)
        self.price = price

    def _color(self, action, plot_location):
        return self.color[action][plot_location]

    def plot(self, epoch):
        self.lefts.append(self.x)
        self.prices.append(self.price)
        max_price = 0.0
        min_price = 0.0
        y = 0.0

        for i in range(0, epoch):
            plt.bar(self.lefts[i], self.heights[i], width=self.widths[i],
                    color=self._color(self.actions[i], 'bar'))
            plt.plot([self.lefts[i], self.lefts[i + 1]], [self.prices[i], self.prices[i + 1]],
                     color=self._color(self.actions[i], 'plot'))
            y += self.widths[i]
            max_price = max_price if max_price > self.prices[i] else self.prices[i]
            min_price = max_price if min_price < self.prices[i] else self.prices[i]

        plt.plot(self.lefts, self.prices, 'ro', color='#000000')
        plt.axis([0, y, min_price * 0.9, max_price * 1.1])
        plt.xlabel('Amount [BNT] Green: issued, Red: destroyed')
        plt.ylabel('Price [ ETH/BNT ]')
        plt.title('Flow of Transactions')
        ax = plt.gca()
        y_formatter = ticker.ScalarFormatter(useOffset=False)
        ax.yaxis.set_major_formatter(y_formatter)
        plt.grid(True)
        plt.show()
