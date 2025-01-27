import pandas as pd
import GetData as gd
import matplotlib.pyplot as plt

# Define the data

def data():
    data = pd.read_excel("financial_data.xlsx")
    return data
# Read the data from the excel file
def getDataFromExcel(file):
    data = pd.read_excel(file)
    return data


# Net Working Capital
def netWorkingCapital(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        current_assets = data.loc[data['itemDescEng'] == "CURRENT ASSETS", period].values[0]
        current_liabilities = data.loc[data['itemDescEng'] == "SHORT TERM LIABILITIES", period].values[0]
        values[period] = current_assets - current_liabilities
    return values


# Current Ratio
def currentRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        current_assets = data.loc[data['itemDescEng'] == "CURRENT ASSETS", period].values[0]
        current_liabilities = data.loc[data['itemDescEng'] == "SHORT TERM LIABILITIES", period].values[0]
        values[period] = current_assets / current_liabilities
    return values


# Quick Ratio
def quickRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        current_assets = data.loc[data['itemDescEng'] == "CURRENT ASSETS", period].values[0]
        inventories = data.loc[data['itemDescEng'] == "Inventories", period].values[0]
        current_liabilities = data.loc[data['itemDescEng'] == "SHORT TERM LIABILITIES", period].values[0]
        values[period] = (current_assets - inventories) / current_liabilities
    return values


# Cash Ratio
def cashRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        cash_equivalents = data.loc[data['itemDescEng'] == "Cash and Cash Equivalents", period].values[0]
        current_liabilities = data.loc[data['itemDescEng'] == "SHORT TERM LIABILITIES", period].values[0]
        values[period] = cash_equivalents / current_liabilities
    return values


# Defensive Interval
def defensiveInterval(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        current_assets = data.loc[data['itemDescEng'] == "CURRENT ASSETS", period].values[0]
        inventories = data.loc[data['itemDescEng'] == "Inventories", period].values[0]
        operating_expenses = data.loc[data['itemDescEng'] == "General Administrative Expenses (-)", period].values[0]
        non_cash_expenses = data.loc[data['itemDescEng'] == "Depreciation & Amortization", period].values[0]
        cost_of_sales = data.loc[data['itemDescEng'] == "Cost Of Sales", period].values[0]
        average_daily_expenses = (operating_expenses - non_cash_expenses + cost_of_sales) / 365
        values[period] = (current_assets - inventories) / average_daily_expenses
    return values


# Debt to Equity Ratio
def debtToEquityRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        total_debt = data.loc[data['itemDescEng'] == "TOTAL LIABILITIES AND S.HOLDERS EQUITY", period].values[0]
        total_equity = data.loc[data['itemDescEng'] == "SHAREHOLDERS EQUITY", period].values[0]
        values[period] = total_debt / total_equity
    return values


# Long Term Debt to Equity Ratio
def longTermDebtToEquityRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        long_term_liabilities = data.loc[data['itemDescEng'] == "LONG TERM LIABILITIES", period].values[0]
        total_debt = data.loc[data['itemDescEng'] == "TOTAL LIABILITIES AND S.HOLDERS EQUITY", period].values[0]
        total_equity = data.loc[data['itemDescEng'] == "SHAREHOLDERS EQUITY", period].values[0]
        values[period] = long_term_liabilities / (total_debt / total_equity)
    return values


# Debt to Assets Ratio
def debtToAssetsRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        total_debt = data.loc[data['itemDescEng'] == "TOTAL LIABILITIES AND S.HOLDERS EQUITY", period].values[0]
        total_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        values[period] = total_debt / total_assets
    return values


# Equity Multiplier
def equityMultiplier(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        total_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        total_equity = data.loc[data['itemDescEng'] == "SHAREHOLDERS EQUITY", period].values[0]
        values[period] = total_assets / total_equity
    return values


# Interest Coverage Ratio
def interestCoverageRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_operating_income = data.loc[data['itemDescEng'] == "Net Operating Profits", period].values[0]
        interest_expense = abs(data.loc[data['itemDescEng'] == "Financial Expenses", period].values[0])
        values[period] = net_operating_income / interest_expense
    return values


# Fixed Charge Coverage Ratio
def fixedChargeCoverageRatio(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_operating_income = data.loc[data['itemDescEng'] == "Net Operating Profits", period].values[0]
        interest_expense = abs(data.loc[data['itemDescEng'] == "Financial Expenses", period].values[0])
        fixed_charges = data.loc[data['itemDescEng'] == "Depreciation & Amortization", period].values[0]
        values[period] = (net_operating_income + fixed_charges) / (interest_expense + fixed_charges)
    return values


# Receivables Turnover
def receivablesTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        receivables = data.loc[data['itemDescEng'] == "Short-Term Trade Receivables", period].values[0]
        values[period] = net_sales / receivables
    return values


# Inventory Turnover
def inventoryTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        cost_of_sales = abs(data.loc[data['itemDescEng'] == "Cost Of Sales", period].values[0])
        inventories = data.loc[data['itemDescEng'] == "Inventories", period].values[0]
        values[period] = cost_of_sales / inventories
    return values


# Payables Turnover
def payablesTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        purchases = data.loc[data['itemDescEng'] == "Cost Of Sales", period].values[0]
        accounts_payables = data.loc[data['itemDescEng'] == "Short-Term Trade Payables", period].values[0]
        values[period] = purchases / accounts_payables
    return values


# Assets Turnover
def assetsTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        total_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        values[period] = net_sales / total_assets
    return values


# Fixed Assets Turnover
def fixedAssetsTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        ppe = data.loc[data['itemDescEng'] == "Tangible Fixed Assets", period].values[0]
        values[period] = net_sales / ppe
    return values


# Equity Turnover
def equityTurnover(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        total_equity = data.loc[data['itemDescEng'] == "SHAREHOLDERS EQUITY", period].values[0]
        values[period] = net_sales / total_equity
    return values


# Days of Sales Outstanding (DSO)
def dayOfSalesOutstanding(data):
    receivables_turnover = receivablesTurnover(data)
    values = {period: 365 / receivables_turnover[period] for period in receivables_turnover}
    return values


# Days of Inventory Outstanding (DIO)
def daysOfInventoryOutstanding(data):
    inventory_turnover = inventoryTurnover(data)
    values = {period: 365 / inventory_turnover[period] for period in inventory_turnover}
    return values


# Days of Payables Outstanding (DPO)
def daysOfPayablesOutstanding(data):
    payables_turnover = payablesTurnover(data)
    values = {period: 365 / payables_turnover[period] for period in payables_turnover}
    return values


# Cash Conversion Cycle (CCC)
def cashConversionCycle(data):
    dso = dayOfSalesOutstanding(data)
    dio = daysOfInventoryOutstanding(data)
    dpo = daysOfPayablesOutstanding(data)
    values = {period: dso[period] + dio[period] - dpo[period] for period in dso}
    return values


# Gross Profit Margin
def grossProfitMargin(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        gross_profit = data.loc[data['itemDescEng'] == "Gross Profit (Loss) from Trade Operations", period].values[0]
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        values[period] = gross_profit / net_sales
    return values


# Operating Profit Margin
def operatingProfitMargin(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        operating_profit = data.loc[data['itemDescEng'] == "OPERATING PROFITS", period].values[0]
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        values[period] = operating_profit / net_sales
    return values


# Net Profit Margin
def netProfitMargin(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_profit = data.loc[data['itemDescEng'] == "NET PROFIT AFTER TAXES", period].values[0]
        net_sales = data.loc[data['itemDescEng'] == "Net Sales", period].values[0]
        values[period] = net_profit / net_sales
    return values


# Return on Assets
def returnOnAssets(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_profit = data.loc[data['itemDescEng'] == "NET PROFIT AFTER TAXES", period].values[0]
        total_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        values[period] = net_profit / total_assets
    return values


# Return on Operating Assets
def returnOnOperatingAssets(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_operating_income = data.loc[data['itemDescEng'] == "Net Operating Profits", period].values[0]
        total_operating_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        values[period] = net_operating_income / total_operating_assets
    return values


# Economic Rantability
def economicRantability(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_operating_income = data.loc[data['itemDescEng'] == "Net Operating Profits", period].values[0]
        total_assets = data.loc[data['itemDescEng'] == "TOTAL ASSETS", period].values[0]
        values[period] = net_operating_income / total_assets
    return values


# Return on Equity
def returnOnEquity(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_profit = data.loc[data['itemDescEng'] == "NET PROFIT AFTER TAXES", period].values[0]
        total_equity = data.loc[data['itemDescEng'] == "SHAREHOLDERS EQUITY", period].values[0]
        values[period] = net_profit / total_equity
    return values


# Tax Burden
def taxBurden(data):
    periods = data.columns[3:]
    values = {}
    for period in periods:
        net_profit = data.loc[data['itemDescEng'] == "NET PROFIT AFTER TAXES", period].values[0]
        earnings_before_tax = \
        data.loc[data['itemDescEng'] == "PROFIT BEFORE TAX FROM CONTINUING OPERATIONS", period].values[0]
        values[period] = net_profit / earnings_before_tax
    return values


# Define the master function that calls all the ratio functions
def allRatios(file_path):
    # Read the data from the Excel file
    data = getDataFromExcel(file_path)

    # Calculate all ratios
    ratios = {
        "Net Working Capital": netWorkingCapital(data),
        "Current Ratio": currentRatio(data),
        "Quick Ratio": quickRatio(data),
        "Cash Ratio": cashRatio(data),
        "Defensive Interval": defensiveInterval(data),
        "Debt to Equity Ratio": debtToEquityRatio(data),
        "Long Term Debt to Equity Ratio": longTermDebtToEquityRatio(data),
        "Debt to Assets Ratio": debtToAssetsRatio(data),
        "Equity Multiplier": equityMultiplier(data),
        "Interest Coverage Ratio": interestCoverageRatio(data),
        "Fixed Charge Coverage Ratio": fixedChargeCoverageRatio(data),
        "Receivables Turnover": receivablesTurnover(data),
        "Inventory Turnover": inventoryTurnover(data),
        "Payables Turnover": payablesTurnover(data),
        "Assets Turnover": assetsTurnover(data),
        "Fixed Assets Turnover": fixedAssetsTurnover(data),
        "Equity Turnover": equityTurnover(data),
        "Days of Sales Outstanding": dayOfSalesOutstanding(data),
        "Days of Inventory Outstanding": daysOfInventoryOutstanding(data),
        "Days of Payables Outstanding": daysOfPayablesOutstanding(data),
        "Cash Conversion Cycle": cashConversionCycle(data),
        "Gross Profit Margin": grossProfitMargin(data),
        "Operating Profit Margin": operatingProfitMargin(data),
        "Net Profit Margin": netProfitMargin(data),
        "Return on Assets": returnOnAssets(data),
        "Return on Operating Assets": returnOnOperatingAssets(data),
        "Economic Rantability": economicRantability(data),
        "Return on Equity": returnOnEquity(data),
        "Tax Burden": taxBurden(data)
    }

    return ratios

def calcAll(symbol, begYear, endYear, exchange, financialGroup, print_ratios=False):
    gd.get_data(symbol, begYear, endYear, exchange, financialGroup, True)
    file_name = 'financial_data.xlsx'
    ratios = allRatios(file_name)
    df_ratios = pd.DataFrame(ratios)
    df_ratios.to_excel('ratios.xlsx')
    if print_ratios == True:
        for ratio, values in ratios.items():
            print(f"{ratio}:")
            for period, value in values.items():
                print(f"  {period}: {value}")
        return ratios
    else:
        return ratios


def plot_ratios(symbol, ratios, output_file='ratios_plot.png', selected_ratios=None):
    """
    Plots selected financial ratios over time and saves the plot to an image file.

    :param ratios: A dictionary containing financial ratios with periods as keys.
    :param output_file: The name of the output image file.
    :param selected_ratios: A list of ratio names to plot. If None, all ratios are plotted.
    """
    # If no specific ratios are selected, plot all ratios
    if selected_ratios is None:
        selected_ratios = list(ratios.keys())

    # Create a wider figure and axis
    fig, ax = plt.subplots(figsize=(18, 8))

    # Plot each selected ratio
    for ratio_name in selected_ratios:
        if ratio_name in ratios:
            periods = list(ratios[ratio_name].keys())
            ratio_values = list(ratios[ratio_name].values())
            ax.plot(periods, ratio_values, marker='o', label=ratio_name)
        else:
            print(f"Warning: Ratio '{ratio_name}' not found in the provided data.")

    # Set plot title and labels
    ax.set_title(f"{symbol} Financial Ratios Over Time")
    ax.set_xlabel('Period')
    ax.set_ylabel('Ratio Value')

    # Add legend
    ax.legend()

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Adjust layout to make room for x-axis labels
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig(output_file)

    # Show the plot
    plt.show()
