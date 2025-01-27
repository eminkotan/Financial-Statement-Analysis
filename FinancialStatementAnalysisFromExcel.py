import pandas as pd


# Read the data from the excel file
def getDataFromExcel(file):
    """
    Language English:
    This function reads the data from the excel file
    :param file: source of excel file /c:/Users/.../data.xlsx
    :return: returns readable data to use in other functions
    Language Turkish - Türkçe:
    Bu fonksiyon excel dosyasından verileri okur
    :param file: excel dosyasının kaynağı /c:/Users/.../data.xlsx
    :return: diğer fonksiyonlarda kullanmak için okunabilir veri döndürür
    """
    data = pd.read_excel(file)
    return data

## List of ratios
# Liquidty Ratios
def netWorkingCapital(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the net working capital of the company
    :param data: after reading the data from the excel file put it here
    :param firstColumn: define the current assets column in excel file as a string exp: "CURRENT ASSETS"
    :param secondColumn: define current liabilities column in excel file as a string exp: "CURRENT LIABILITIES"
    :return: reutrns the net working capital value
    Language Turkish - Türkçe:
    Şirketin net işletme sermayesini gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari varlıkları tanımlayın bir dize olarak örn: "CURRENT ASSETS"
    :param secondColumn: excel dosyasında cari borçları tanımlayın bir dize olarak örn: "CURRENT LIABILITIES"
    :return: net işletme sermayesi değerini döndürür
    """
    netWorkingCapital_value = data[firstColumn].values[0] - data[secondColumn].values[0]
    return netWorkingCapital_value

# Current Ratio
def currentRatio(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the current ratio of the company
    :param data: after reading the data from the excel file put it here
    :param firstColumn: define the current assets column in excel file as a string exp: "CURRENT ASSETS"
    :param secondColumn: define current liabilities column in excel file as a string exp: "CURRENT LIABILITIES"
    :return: returns the current ratio value

    Language Turkish - Türkçe:
    Şirketin cari oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari varlıkları tanımlayın bir dize olarak örn: "CURRENT ASSETS"
    :param secondColumn: excel dosyasında cari borçları tanımlayın bir dize olarak örn: "CURRENT LIABILITIES"
    :return: cari oran değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Quick Ratio
def quickRatio(data, firstColumn, secondColumn, thirdColumn):
    """
    Language English:
    Shows the quick ratio of the company
    :param data: after reading the data from the excel file put it here
    :param firstColumn: define the current assets column in excel file as a string exp: "CURRENT ASSETS"
    :param secondColumn: define current liabilities column in excel file as a string exp: "CURRENT LIABILITIES"
    :param thirdColumn: define the inventory column in excel file as a string exp: "INVENTORY"
    :return: returns the quick ratio value
    Language Turkish - Türkçe:
    Şirketin hızlı oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari varlıkları tanımlayın bir dize olarak örn: "CURRENT ASSETS"
    :param secondColumn: excel dosyasında cari borçları tanımlayın bir dize olarak örn: "CURRENT LIABILITIES"
    :param thirdColumn: excel dosyasında envanteri tanımlayın bir dize olarak örn: "INVENTORY"
    :return: hızlı oran değerini döndürür
    """
    ratio_value = (data[firstColumn].values[0] - data[thirdColumn].values[0]) / data[secondColumn].values[0]
    return ratio_value

# Cash Ratio
def cashRatio(data, firstColumn, secondColumn, thirdColumn, fourthColumn):
    """
    Language English:
    Shows the cash ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the current assets column in excel file as a string exp: "CURRENT ASSETS"
    :param secondColumn: define current liabilities column in excel file as a string exp: "CURRENT LIABILITIES"
    :param thirdColumn: define the inventory column in excel file as a string exp: "INVENTORY"
    :param fourthColumn: define the receivables column in excel file as a string exp: "RECEIVABLES"
    :return: returns the cash ratio value
    Language Turkish - Türkçe:
    Şirketin nakit oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari varlıkları tanımlayın bir dize olarak örn: "CURRENT ASSETS"
    :param secondColumn: excel dosyasında cari borçları tanımlayın bir dize olarak örn: "CURRENT LIABILITIES"
    :param thirdColumn: excel dosyasında envanteri tanımlayın bir dize olarak örn: "INVENTORY"
    :param fourthColumn: excel dosyasında alacakları tanımlayın bir dize olarak örn: "RECEIVABLES"
    :return: nakit oran değerini döndürür
    """
    ratio_value = (data[firstColumn].values[0] - data[thirdColumn].values[0] - data[fourthColumn].values[0]) / data[secondColumn].values[0]
    return ratio_value
# Defensive Interval
def defensiveInterval(data, firstColumn, secondColumn, thirdColumn, fourthColumn, fifthColumn):
    """
    Language English:
    Shows the defensive interval of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the current assets column in excel file as a string exp: "CURRENT ASSETS"
    :param secondColumn: define the inventory column in excel file as a string exp: "INVENTORY"
    :param thirdColumn: define the operating expenses column in excel file as a string exp: "OPERATING EXPENSES"
    :param fourthColumn: define the non-cash expenses column in excel file as a string exp: "NON-CASH EXPENSES"
    :param fifthColumn: define the cost of goods sold column in excel file as a string exp: "COST OF GOODS SOLD"
    :return: returns the defensive interval value
    Language Turkish - Türkçe:
    Şirketin savunma aralığını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari varlıkları tanımlayın bir dize olarak örn: "CURRENT ASSETS"
    :param secondColumn: excel dosyasında envanteri tanımlayın bir dize olarak örn: "INVENTORY"
    :param thirdColumn: excel dosyasında işletme giderlerini tanımlayın bir dize olarak örn: "OPERATING EXPENSES"
    :param fourthColumn: excel dosyasında nakit olmayan giderleri tanımlayın bir dize olarak örn: "NON-CASH EXPENSES"
    :param fifthColumn: excel dosyasında satılan mal maliyetini tanımlayın bir dize olarak örn: "COST OF GOODS SOLD"
    """
    averageDailyExpenses = (data[thirdColumn].values[0] - data[fourthColumn].values[0] +data[fifthColumn].values[0]) / 365
    ratio_value = (data[firstColumn].values[0] - data[secondColumn].values[0]) / averageDailyExpenses
    return ratio_value

# Solvency Ratios ( Capital Structure Ratios )
# Leverage Ratios
# debt to equity ratio
def debtToEquityRatio(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the debt to equity ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the total debt column in excel file as a string exp: "TOTAL DEBT"
    :param secondColumn: define the total equity column in excel file as a string exp: "TOTAL EQUITY"
    :return: returns the debt to equity ratio value
    Language Turkish - Türkçe:
    Şirketin borç / öz sermaye oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında toplam borcu bir dize olarak örn: "TOTAL DEBT"
    :param secondColumn: excel dosyasında toplam öz sermayeyi bir dize olarak örn: "TOTAL EQUITY"
    :return: borç / öz sermaye oranı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Long Term Debt to Equity Ratio
def longTermDebtToEquityRatio(data, firstColumn, secondColumn, thirdColumn):
    """
    Language English:
    Shows the long term debt to equity ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the non-current liabilities column in excel file as a string exp: "NON-CURRENT LIABILITIES"
    :param secondColumn: define the total debt column in excel file as a string exp: "TOTAL DEBT"
    :param thirdColumn: define the total equity column in excel file as a string exp: "TOTAL EQUITY"
    :return: returns the long term debt to equity ratio value
    Language Turkish - Türkçe:
    Şirketin uzun vadeli borç / öz sermaye oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında cari borçları bir dize olarak örn: "NON-CURRENT LIABILITIES"
    :param secondColumn: excel dosyasında toplam borcu bir dize olarak örn: "TOTAL DEBT"
    :param thirdColumn: excel dosyasında toplam öz sermayeyi bir dize olarak örn: "TOTAL EQUITY"
    :return: uzun vadeli borç / öz sermaye oranı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / (data[secondColumn].values[0] / data[thirdColumn].values[0])
    return ratio_value

# Debt to assets ratio
def debtToAssetsRatio(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the debt to assets ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the total debt column in excel file as a string exp: "TOTAL DEBT"
    :param secondColumn: define the total assets column in excel file as a string exp: "TOTAL ASSETS"
    :return: returns the debt to assets ratio value
    Language Turkish - Türkçe:
    Şirketin borç / varlık oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında toplam borcu bir dize olarak örn: "TOTAL DEBT"
    :param secondColumn: excel dosyasında toplam varlıkları bir dize olarak örn: "TOTAL ASSETS"
    :return: borç / varlık oranı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Equity Multiplier
def equityMultiplier(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the equity multiplier of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the total assets column in excel file as a string exp: "TOTAL ASSETS"
    :param secondColumn: define the total equity column in excel file as a string exp: "TOTAL EQUITY"
    :return: returns the equity multiplier value
    Language Turkish - Türkçe:
    Şirketin öz sermaye çarpanını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında toplam varlıkları bir dize olarak örn: "TOTAL ASSETS"
    :param secondColumn: excel dosyasında toplam öz sermayeyi bir dize olarak örn: "TOTAL EQUITY"
    :return: öz sermaye çarpanı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# coverage ratios

# Interest Coverage Ratio
def interestCoverageRatio(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the interest coverage ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the net operating income column in excel file as a string exp: "NET OPERATING INCOME"
    :param secondColumn: define the interest expense column in excel file as a string exp: "INTEREST EXPENSE"
    :return: returns the interest coverage ratio value
    Language Turkish - Türkçe:
    Şirketin faiz kapsama oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında net işletme gelirini bir dize olarak örn: "NET OPERATING INCOME"
    :param secondColumn: excel dosyasında faiz giderini bir dize olarak örn: "INTEREST EXPENSE"
    :return: faiz kapsama oranı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Fixed Charge Coverage Ratio
def fixedChargeCoverageRatio(data, firstColumn, secondColumn, thirdColumn):
    """
    Language English:
    Shows the fixed charge coverage ratio of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the net operating income column in excel file as a string exp: "NET OPERATING INCOME"
    :param secondColumn: define the interest expense column in excel file as a string exp: "INTEREST EXPENSE"
    :param thirdColumn: define the fixed charges column in excel file as a string exp: "FIXED CHARGES"
    :return: returns the fixed charge coverage ratio value
    Language Turkish - Türkçe:
    Şirketin sabit maliyet kapsama oranını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında net işletme gelirini bir dize olarak örn: "NET OPERATING INCOME"
    :param secondColumn: excel dosyasında faiz giderini bir dize olarak örn: "INTEREST EXPENSE"
    :param thirdColumn: excel dosyasında sabit maliyetleri bir dize olarak örn: "FIXED CHARGES"
    :return: sabit maliyet kapsama oranı değerini döndürür
    """
    ratio_value = (data[firstColumn].values[0] + data[thirdColumn].values[0]) / (data[secondColumn].values[0] + data[thirdColumn].values[0])
    return ratio_value

# Efficiency Ratios ( Turnovers )

# Recievables Turnover
def recievablesTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the recievables turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :param secondColumn: define the accounts recievables column in excel file as a string exp: "ACCOUNTS RECIEVABLES"
    :return: returns the recievables turnover ratio
    Language Turkish - Türkçe:
    Şirketin alacak devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :param secondColumn: excel dosyasında alacakları bir dize olarak örn: "ACCOUNTS RECIEVABLES"
    :return: alacak devir hızı oranını döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Inventory Turnover
def inventoryTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the inventory turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the cost of goods sold column in excel file as a string exp: "COST OF GOODS SOLD"
    :param secondColumn: define the inventory column in excel file as a string exp: "INVENTORY"
    :return: returns the inventory turnover ratio
    Language Turkish - Türkçe:
    Şirketin envanter devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında satılan mal maliyetini bir dize olarak örn: "COST OF GOODS SOLD"
    :param secondColumn: excel dosyasında envanteri bir dize olarak örn: "INVENTORY"
    :return: envanter devir hızı oranını döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Payables Turnover
def payablesTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the payables turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the purchases column in excel file as a string exp: "PURCHASES"
    :param secondColumn: define the accounts payables column in excel file as a string exp: "ACCOUNTS PAYABLES"
    :return: returns the payables turnover ratio
    Language Turkish - Türkçe:
    Şirketin borç devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında satın alınanları bir dize olarak örn: "PURCHASES"
    :param secondColumn: excel dosyasında borçları bir dize olarak örn: "ACCOUNTS PAYABLES"
    :return: borç devir hızı oranını döndürür
    """

# Assets Turnover
def assetsTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the assets turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :param secondColumn: define the total assets column in excel file as a string exp: "TOTAL ASSETS"
    :return: returns the assets turnover ratio
    Language Turkish - Türkçe:
    Şirketin varlık devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :param secondColumn: excel dosyasında toplam varlıkları bir dize olarak örn: "TOTAL ASSETS"
    :return: varlık devir hızı oranını döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Fixed Assets Turnover
def fixedAssetsTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the fixed assets turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :param secondColumn: define the PPE column in excel file as a string exp: "PPE" Net Property Plant and Equipment
    :return: returns the fixed assets turnover ratio
    Language Turkish - Türkçe:
    Şirketin sabit varlık devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :param secondColumn: excel dosyasında PPE'yi bir dize olarak örn: "PPE" Net Property Plant and Equipment
    :return: sabit varlık devir hızı oranını döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Equity Turnover
def equityTurnover(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the equity turnover of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :param secondColumn: define the total equity column in excel file as a string exp: "TOTAL EQUITY"
    :return: returns the equity turnover ratio
    Language Turkish - Türkçe:
    Şirketin öz sermaye devir hızını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :param secondColumn: excel dosyasında toplam öz sermayeyi bir dize olarak örn: "TOTAL EQUITY"
    :return: öz sermaye devir hızı oranını döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# day of sales outstanding DSO
def dayOfSalesOutstanding(reciviablesTurnover):
    """
    Language English:
    Shows the day of sales outstanding of the company
    :param reciviablesTurnover: put the recievables turnover value here
    :return: returns the day of sales outstanding value
    Language Turkish - Türkçe:
    Şirketin satışların tahsilat gününü gösterir
    :param reciviablesTurnover: alacak devir hızı değerini buraya koyun
    :return: satışların tahsilat günü değerini döndürür
    """
    ratio_value = 365 / reciviablesTurnover
    return ratio_value

# days of inventory outstanding DIO
def daysOfInventoryOutstanding(inventoryTurnover):
    """
    Language English:
    Shows the days of inventory outstanding of the company
    :param inventoryTurnover: put the inventory turnover value here
    :return: returns the days of inventory outstanding value
    Language Turkish - Türkçe:
    Şirketin envanterin tahsilat gününü gösterir
    :param inventoryTurnover: envanter devir hızı değerini buraya koyun
    :return: envanterin tahsilat günü değerini döndürür
    """
    ratio_value = 365 / inventoryTurnover
    return ratio_value

# days of payables outstanding DPO
def daysOfPayablesOutstanding(payablesTurnover):
    """
    Language English:
    Shows the days of payables outstanding of the company
    :param payablesTurnover: put the payables turnover value here
    :return: returns the days of payables outstanding value
    Language Turkish - Türkçe:
    Şirketin borçların tahsilat gününü gösterir
    :param payablesTurnover: borç devir hızı değerini buraya koyun
    :return: borçların tahsilat günü değerini döndürür
    """
    ratio_value = 365 / payablesTurnover
    return ratio_value

# cash convention cycle CCC
def cashConversionCycle(DSO, DIO, DPO):
    """
    Language English:
    Shows the cash conversion cycle of the company
    :param DSO: put the day of sales outstanding value here
    :param DIO: put the days of inventory outstanding value here
    :param DPO: put the days of payables outstanding value here
    :return: returns the cash conversion cycle value
    Language Turkish - Türkçe:
    Şirketin nakit dönüşüm döngüsünü gösterir
    :param DSO: satışların tahsilat günü değerini buraya koyun
    :param DIO: envanterin tahsilat günü değerini buraya koyun
    :param DPO: borçların tahsilat günü değerini buraya koyun
    :return: nakit dönüşüm döngüsü değerini döndürür
    """
    ratio_value = DSO + DIO - DPO
    return ratio_value

# Profitability Ratios

# Gross Profit Margin
def grossProfitMargin(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the gross profit margin of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the gross profit column in excel file as a string exp: "GROSS PROFIT"
    :param secondColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :return: returns the gross profit margin value
    Language Turkish - Türkçe:
    Şirketin brüt kar marjını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında brüt karı bir dize olarak örn: "GROSS PROFIT"
    :param secondColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :return: brüt kar marjı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Operating Profit Margin
def operatingProfitMargin(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the operating profit margin of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the operating profit column in excel file as a string exp: "OPERATING PROFIT"
    :param secondColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :return: returns the operating profit margin value
    Language Turkish - Türkçe:
    Şirketin işletme kar marjını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında işletme karını bir dize olarak örn: "OPER
    :param secondColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :return: işletme kar marjı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Net Profit Margin
def netProfitMargin(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the net profit margin of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the net profit column in excel file as a string exp: "NET PROFIT"
    :param secondColumn: define the revenue column in excel file as a string exp: "REVENUE"
    :return: returns the net profit margin value
    Language Turkish - Türkçe:
    Şirketin net kar marjını gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında net karı bir dize olarak örn: "NET PROFIT"
    :param secondColumn: excel dosyasında geliri bir dize olarak örn: "REVENUE"
    :return: net kar marjı değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Return on Assets
def returnOnAssets(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the return on assets of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the net profit column in excel file as a string exp: "NET PROFIT"
    :param secondColumn: define the total assets column in excel file as a string exp: "TOTAL ASSETS"
    :return: returns the return on assets value
    Language Turkish - Türkçe:
    Şirketin varlık getirisini gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında net karı bir dize olarak örn: "NET PROFIT"
    :param secondColumn: excel dosyasında toplam varlıkları bir dize olarak örn: "TOTAL ASSETS"
    :return: varlık getirisi değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

# Retırm on operating assets
def returnOnOperatingAssets(data, firstColumn, secondColumn):
    """
    Language English:
    Shows the return on operating assets of the company
    :param data: put the data after reading the data from the excel file
    :param firstColumn: define the net operating income column in excel file as a string exp: "NET OPERATING INCOME"
    :param secondColumn: define the total operating assets column in excel file as a string exp: "TOTAL OPERATING ASSETS"
    :return: returns the return on operating assets value
    Language Turkish - Türkçe:
    Şirketin işletme varlıklarındaki getirisini gösterir
    :param data: excel dosyasından verileri okuduktan sonra buraya koyun
    :param firstColumn: excel dosyasında net işletme gelirini bir dize olarak örn: "NET OPERATING INCOME"
    :param secondColumn: excel dosyasında toplam işletme varlıklarını bir dize olarak örn: "TOTAL OPERATING ASSETS"
    :return: işletme varlıklarındaki getiri değerini döndürür
    """
    ratio_value = data[firstColumn].values[0] / data[secondColumn].values[0]
    return ratio_value

        # Valuation Ratios ( Capital Market Metrics


