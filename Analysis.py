import FinancialStatementAnalysis as fsa




# Define the symbol, beginning year, ending year, exchange, and financial group
symbol = "TTRAK"
begYear = 2008
endYear = 2024
exchange = "TRY"
financialGroup = 1

# Calculate the financial ratios
ratios = fsa.calcAll(symbol,begYear, endYear,exchange,financialGroup)


### PLOTTING

# Define the selected ratios
selected_ratios = ["Current Ratio", "Quick Ratio"]
# Ensure 'output_file' is a string
output_file_name = 'selected_financial_ratios.png'

#plot the selected ratios
fsa.plot_ratios(ratios, output_file_name, selected_ratios)



