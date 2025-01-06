import GetData as gd


symbol = "TTRAK"
begYear = 2008
endYear = 2024
exchange = "TRY"
financialGroup = 1

dc = gd.get_data(symbol, begYear, endYear, exchange, financialGroup, True)

df = gd.framed(dc, symbol)
#gd.trendAnalysis(df_Karsan,"Net Sales", "NET PROFIT AFTER TAXES", symbol)


# Sadece sayısal sütunları seçin
gd.trendAnalysis(df, "CURRENT ASSETS", symbol, 3, "quarterly", "itemDescEng", "pct")
