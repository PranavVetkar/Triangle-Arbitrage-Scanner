import ccxt
import time

class TriangleArb:
    def __init__(self):
        self.exchange = ccxt.binance()
        self.pair1 = 'BTC/USDT'
        self.pair2 = 'ETH/BTC'
        self.pair3 = 'ETH/USDT'

    def get_rates(self):
        tickers = self.exchange.fetch_tickers([self.pair1, self.pair2, self.pair3])
        
        return {
            'btc_usdt': tickers[self.pair1]['ask'],
            'eth_btc': tickers[self.pair2]['ask'],
            'eth_usdt': tickers[self.pair3]['bid']
        }

    def scan(self):
        print(f"--- Scanning Triangle: {self.pair1} -> {self.pair2} -> {self.pair3} ---")
        while True:
            try:
                r = self.get_rates()
                
                start_amount = 100
                
                btc_amount = start_amount / r['btc_usdt']
                
                eth_amount = btc_amount / r['eth_btc']
                
                end_amount = eth_amount * r['eth_usdt']
                
                profit = end_amount - start_amount
                profit_pct = (profit / start_amount) * 100
                
                if profit_pct > 0:
                    print(f"✅ [PROFIT] Loop: {profit_pct:.4f}% | End: ${end_amount:.4f}")
                else:
                    print(f"❌ [LOSS] Loop: {profit_pct:.4f}%")

                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    scanner = TriangleArb()
    scanner.scan()