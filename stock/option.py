from pandas_datareader.yahoo.options import Options as YahooOptions

"""
1、获取option数据
2、分析
3、画图

"""


class Option:
    def __init__(self, symbol, type, start=None, end=None):
        self.symbol = symbol
        self.type = type
        self.start = start
        self.end = end
        self.tool = YahooOptions(symbol)
        self.optionData = None

    def data(self):
        self.optionData = self.tool.get_all_data()
        return self

    def p(self):
        print(self.optionData.head())

    def draw(self):
        pass


if __name__ == '__main__':
    Option('AAPL', 'put').data().p()
