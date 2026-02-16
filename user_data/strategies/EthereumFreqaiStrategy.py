import logging
from pandas import DataFrame
from freqtrade.strategy import IStrategy
import talib.abstract as ta

logger = logging.getLogger(__name__)

class EthereumFreqaiStrategy(IStrategy):
    """
    Ethereum FreqAI Strategy
    Using Machine Learning to predict Ethereum price movements.
    """
    
    # Strategy parameters
    can_short = False
    timeframe = '5m'
    
    # ROI and Stoploss
    minimal_roi = {"0": 0.1}
    stoploss = -0.10
    
    process_only_new_candles = True
    use_exit_signal = True
    
    def feature_engineering_expand_all(self, dataframe: DataFrame, period: int,
                                       metadata: dict, **kwargs) -> DataFrame:
        dataframe["%-rsi-period"] = ta.RSI(dataframe, timeperiod=period)
        dataframe["%-mfi-period"] = ta.MFI(dataframe, timeperiod=period)
        dataframe["%-adx-period"] = ta.ADX(dataframe, timeperiod=period)
        return dataframe

    def feature_engineering_expand_basic(self, dataframe: DataFrame, metadata: dict, **kwargs) -> DataFrame:
        dataframe["%-day_of_week"] = dataframe["date"].dt.dayofweek
        dataframe["%-hour_of_day"] = dataframe["date"].dt.hour
        return dataframe

    def set_freqai_targets(self, dataframe: DataFrame, metadata: dict, **kwargs) -> DataFrame:
        # Target: price change in 24 candles (2 hours on 5m timeframe)
        dataframe["&-s_close"] = dataframe["close"].shift(-24) / dataframe["close"] - 1
        return dataframe

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Start FreqAI
        dataframe = self.freqai.start(dataframe, metadata, self)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['&-s_close'] > 0.01) & # Predict > 1% gain
                (dataframe['do_predict'] == 1)    # Prediction is valid
            ),
            'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (
                (dataframe['&-s_close'] < 0) # Predict loss
            ),
            'exit_long'] = 1
        return dataframe
