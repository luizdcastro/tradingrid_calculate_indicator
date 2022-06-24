import talib
import pandas as pd
pd.options.mode.chained_assignment = None

def indicators(df):

    open = df['open']
    close = df['close']
    high = df['high']
    low = df['low']
    volume = df['volume']    

    # SuperTrend   
    df['atr'] = talib.ATR(high, low, close, timeperiod=10) 

    df['upperband'] = ((df['high'] + df['low']) / 2) + (3 * df['atr'])
    df['lowerband'] = ((df['high'] + df['low']) / 2) - (3 * df['atr'])      
    df['in_uptrend'] = True       

    for current in range(1, len(df.index)):
        previous = current - 1
        
        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False
        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]                

    df['ema_10'] = talib.EMA(close, timeperiod=10)
    df['ma_10'] = talib.MA(close, timeperiod=10, matype=0)
    df['ema_20'] = talib.EMA(close, timeperiod=20)
    df['ma_20'] = talib.MA(close, timeperiod=20, matype=0)
    df['ema_30'] = talib.EMA(close, timeperiod=30)
    df['ma_30'] = talib.MA(close, timeperiod=30, matype=0)
    df['ema_40'] = talib.EMA(close, timeperiod=40)
    df['ma_40'] = talib.MA(close, timeperiod=40, matype=0)
    df['ema_50'] = talib.EMA(close, timeperiod=50)
    df['ma_50'] = talib.MA(close, timeperiod=50, matype=0)
    df['ema_100'] = talib.EMA(close, timeperiod=100)
    df['ma_100'] = talib.MA(close, timeperiod=100, matype=0)
    df['ema_200'] = talib.EMA(close, timeperiod=200)
    df['ma_200'] = talib.MA(close, timeperiod=200, matype=0)

    df['ad'] = talib.AD(high, low, close, volume)
    df['obv'] = talib.OBV(close, volume)
    df['bb_upperband'], df['bb_middleband'], df['bb_lowerband'] = talib.BBANDS(
        close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    df['wma'] = talib.WMA(close, timeperiod=30)
    df['adx'] = talib.ADX(high, low, close, timeperiod=14)
    df['aroondown'], df['aroonup'] = talib.AROON(high, low, timeperiod=14)
    df['macd'], df['macdsignal'], df['macdhist'] = talib.MACD(
        close, fastperiod=12, slowperiod=26, signalperiod=9)
    df['mfi'] = talib.MFI(high, low, close, volume, timeperiod=14)
    df['mom'] = talib.MOM(close, timeperiod=10)
    df['rsi'] = talib.RSI(close, timeperiod=14)
    df['slowk'], df['slowd'] = talib.STOCH(high, low, close, fastk_period=5,
                               slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    df['willr'] = talib.WILLR(high, low, close, timeperiod=14) 

    # Pattern Recognition
    df['cdlhammer'] = talib.CDLHAMMER(open, high, low, close)
    df['cdlinvertedhammer'] = talib.CDLINVERTEDHAMMER(open, high, low, close)
    df['cdlengulfing'] = talib.CDLENGULFING(open, high, low, close)
    df['cdlpiercing'] = talib.CDLPIERCING(open, high, low, close)
    df['cdlmorningstar'] = talib.CDLMORNINGSTAR(
        open, high, low, close, penetration=0)
    df['cdl3whitesoldiers'] = talib.CDL3WHITESOLDIERS(open, high, low, close)
    df['cdlabandonedbaby'] = talib.CDLABANDONEDBABY(
        open, high, low, close, penetration=0)
    df['cdlbreakaway'] = talib.CDLBREAKAWAY(open, high, low, close)
    df['cdlhangingman'] = talib.CDLHANGINGMAN(open, high, low, close)
    df['cdlshootingstar'] = talib.CDLSHOOTINGSTAR(open, high, low, close)
    df['cdleveningstar'] = talib.CDLEVENINGSTAR(
        open, high, low, close, penetration=0)
    df['cdl3blackcrows'] = talib.CDL3BLACKCROWS(open, high, low, close)
    df['cdldarkcloudcover'] = talib.CDLDARKCLOUDCOVER(
        open, high, low, close, penetration=0)
    df['cdldoji'] = talib.CDLDOJI(open, high, low, close)
    df['cdlspinningtop'] = talib.CDLSPINNINGTOP(open, high, low, close)
    df['cdlharami'] = talib.CDLHARAMI(open, high, low, close)
    df['cdl3linestrike'] = talib.CDL3LINESTRIKE(open, high, low, close)
    df['cdldragonflydoji'] = talib.CDLDRAGONFLYDOJI(open, high, low, close)
    df['cdlmatchinglow'] = talib.CDLMATCHINGLOW(open, high, low, close)
    df['cdltasukigap'] = talib.CDLTASUKIGAP(open, high, low, close) 
    
    return df