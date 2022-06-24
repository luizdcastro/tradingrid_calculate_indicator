from flask import Flask, request, jsonify
import pandas as pd
from indicators import indicators
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/indicator', methods=['POST'])
def indicator():

    req = request.get_json()
    symbol, interval, data = req['symbol'], req['interval'], req['data']

    response = pd.DataFrame({
        'open': data['open'],
        'high': data['high'],
        'low': data['low'],
        'close': data['close'],
        'volume': data['volume']
    })

    df = indicators(response)

    list = []

    for (
        open,
        low,
        high,
        close,
        volume,
        ema_10, ema_20, ema_30, ema_40, ema_50, ema_100, ema_200,
        ma_10, ma_20, ma_30, ma_40, ma_50, ma_100, ma_200,
        atr,
        in_uptrend,
        ad,
        obv,
        upperband, middleband, lowerband,
        wma,
        adx,
        aroondown, aroonup,
        macd, macdsignal, macdhist,
        mfi,
        mom,
        rsi,
        slowk, slowd,
        willr,
        cdlhammer,
        cdlinvertedhammer,
        cdlengulfing,
        cdlpiercing,
        cdlmorningstar,
        cdl3whitesoldiers,
        cdlabandonedbaby,
        cdlbreakaway,
        cdlhangingman,
        cdlshootingstar,
        cdleveningstar,
        cdl3blackcrows,
        cdldarkcloudcover,
        cdldoji,
        cdlspinningtop,
        cdlharami,
        cdl3linestrike,
        cdldragonflydoji,
        cdlmatchinglow,
        cdltasukigap

    ) in zip(
            df['open'],
            df['low'],
            df['high'],
            df['close'],
            df['volume'],
            df['ema_10'], df['ema_20'], df['ema_30'], df['ema_40'], df['ema_50'], df['ema_100'], df['ema_200'],
            df['ma_10'], df['ma_20'], df['ma_30'], df['ma_40'], df['ma_50'], df['ma_100'], df['ma_200'],
            df['atr'],
            df['in_uptrend'],
            df['ad'],
            df['obv'],
            df['bb_upperband'], df['bb_middleband'], df['bb_lowerband'],
            df['wma'],
            df['adx'],
            df['aroondown'], df['aroonup'],
            df['macd'], df['macdsignal'], df['macdhist'],
            df['mfi'],
            df['mom'],
            df['rsi'],
            df['slowk'], df['slowd'],
            df['willr'],
            df['cdlhammer'],
            df['cdlinvertedhammer'],
            df['cdlengulfing'],
            df['cdlpiercing'],
            df['cdlmorningstar'],
            df['cdl3whitesoldiers'],
            df['cdlabandonedbaby'],
            df['cdlbreakaway'],
            df['cdlhangingman'],
            df['cdlshootingstar'],
            df['cdleveningstar'],
            df['cdl3blackcrows'],
            df['cdldarkcloudcover'],
            df['cdldoji'],
            df['cdlspinningtop'],
            df['cdlharami'],
            df['cdl3linestrike'],
            df['cdldragonflydoji'],
            df['cdlmatchinglow'],
            df['cdltasukigap']
    ):

        response = {
            "symbol": symbol,
            "interval": interval,
            "data": {
                'candle': {
                    'open': open,
                    'low': low,
                    'high': high,
                    'close': close,
                    'volume': volume
                },
                'indicators': {
                    'ema': {
                        'ema_10': ema_10,
                        'ema_20': ema_20,
                        'ema_30': ema_30,
                        'ema_40': ema_40,
                        'ema_50': ema_50,
                        'ema_100': ema_100,
                        'ema_200': ema_200,
                    },
                    'ma': {
                        'ma_10': ma_10,
                        'ma_20': ma_20,
                        'ma_30': ma_30,
                        'ma_40': ma_40,
                        'ma_50': ma_50,
                        'ma_100': ma_100,
                        'ma_200': ma_200,
                    },
                    'atr': atr,
                    'supertrend': in_uptrend,
                    'ad': ad,
                    'obv': obv,
                    'bbands': {
                        'upperband': upperband,
                        'middleband': middleband,
                        'lowerband': lowerband
                    },
                    'wma': wma,
                    'adx': adx,
                    'arron': {
                        'aroondown': aroondown,
                        'aroonup': aroonup
                    },
                    'macd': {
                        'macd': macd,
                        'macdsignal': macdsignal,
                        'macdhist': macdhist,
                    },
                    'mfi': mfi,
                    'mom': mom,
                    'rsi': rsi,
                    'stoch': {
                        'slowk': slowk,
                        'slowd': slowd,
                    },
                    'willr': willr
                },
                'patterns': {
                    'cdlhammer': cdlhammer,
                    'cdlinvertedhammer': cdlinvertedhammer,
                    'cdlengulfing': cdlengulfing,
                    'cdlpiercing': cdlpiercing,
                    'cdlmorningstar': cdlmorningstar,
                    'cdl3whitesoldiers': cdl3whitesoldiers,
                    'cdlabandonedbaby': cdlabandonedbaby,
                    'cdlbreakaway': cdlbreakaway,
                    'cdlhangingman': cdlhangingman,
                    'cdlshootingstar': cdlshootingstar,
                    'cdleveningstar': cdleveningstar,
                    'cdl3blackcrows': cdl3blackcrows,
                    'cdldarkcloudcover': cdldarkcloudcover,
                    'cdldoji': cdldoji,
                    'cdlspinningtop': cdlspinningtop,
                    'cdlharami': cdlharami,
                    'cdl3linestrike': cdl3linestrike,
                    'cdldragonflydoji': cdldragonflydoji,
                    'cdlmatchinglow': cdlmatchinglow,
                    'cdltasukigap': cdltasukigap
                }
            }
        }

        list.append(response)

    return jsonify(list[-2:])
