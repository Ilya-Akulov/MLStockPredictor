import pandas as pd
from io import StringIO

class DataHandler:
    """
    Класс, который содержит все функции обработки и преобразования данных
    """


    @classmethod
    def prepeare_data(cls, ticker_data: str) -> pd.DataFrame:
        """
        Функция преобразования информации о тикере в датафрейм
        """
        df = pd.read_csv(StringIO(ticker_data))
        df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE'])
        return df[['TRADEDATE', 'CLOSE']]