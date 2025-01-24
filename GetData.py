from isyatirimhisse import StockData, Financials
import pandas as pd

# Define the Func Var
financials = Financials()

# Define Func to get data of Financial Statement
def get_data(symbol: object, start_year: object, end_year: object, exchange: object, financial_group: object, save_to_excel: object) -> object:
    df = financials.get_data(
        symbols=[symbol],
        start_year=str(start_year),
        end_year=str(end_year),
        exchange=exchange,
        financial_group=str(financial_group),
        save_to_excel=True
    )
    dataFramed = pd.DataFrame(df[symbol])
    file_name = 'financial_data.xlsx'
    dataFramed.to_excel(file_name, index=False)
    return df

# Define Func to make DataFrame

def framed(data, symbol):
    df = pd.DataFrame(data[symbol])
    return df

# Define Func to make Graph Analysis

def trendAnalysis(df, categoryLabel, symbol, column, dateType, category, plotType):
    # Define the data
    # Year Sum
    # if statment for plotType

    if plotType == "numeric":
        if dateType == "quarterly":
            # Çeyrek sütunları seç
            quarterly_columns = df.columns[3:]  # İlk 3 sütunu atla

            # Yılları ayıkla
            years = sorted(set(col.split("/")[0] for col in quarterly_columns))

            # Kategori kontrolü
            if category not in df.columns:
                raise ValueError(f"'{category}' column not found in DataFrame.")

            # Yıllık veri hazırlığı
            annual_data = {category: df[category]}

            for year in years:
                cols = [col for col in quarterly_columns if col.startswith(year)]
                if not cols:
                    print(f"No columns found for year {year}. Skipping...")
                    continue

                # Sayısal veri kontrolü ve toplama
                df[cols] = df[cols].apply(pd.to_numeric, errors='coerce').fillna(0)
                annual_data[year] = df[cols].sum(axis=1)

            # Yıllık DataFrame oluştur
            df_annual = pd.DataFrame(annual_data)
            print(df_annual.head())  # Debugging output
            data1 = df_annual[df_annual[category] == categoryLabel].iloc[:,1:].values.flatten()

            plt.figure(figsize=(25, 10))
            plt.title(f"{categoryLabel} Annual Trend Analysis", fontsize=14)
            sns.lineplot(x= years, y=data1, marker="o", label=categoryLabel)
            plt.yticks(data1)
            plt.grid(True)
            plt.legend(loc='upper left')
            #plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x)}'))
            plt.xticks(rotation=45)
            plt.show()

        elif dateType == "yearly":
            data1 = df[df[category] == categoryLabel].iloc[:, 3:].values.flatten()
            numeric_columns = df.iloc[:, 3:]
            years = numeric_columns.columns
            plt.plot(years, data1, label=str(categoryLabel))
            plt.legend(loc='upper left')
            plt.show()

        else:
            print("Invalid date type")
            return
    elif plotType == "pct":
        if dateType == "quarterly":
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            # Çeyrek sütunları seç
            quarterly_columns = df.columns[3:]  # İlk 3 sütunu atla

            # Yılları ayıkla
            years = sorted(set(col.split("/")[0] for col in quarterly_columns))

            # Kategori kontrolü
            if category not in df.columns:
                raise ValueError(f"'{category}' column not found in DataFrame.")

            # Yıllık veri hazırlığı
            annual_data = {category: df[category]}

            for year in years:
                cols = [col for col in quarterly_columns if col.startswith(year)]
                if not cols:
                    print(f"No columns found for year {year}. Skipping...")
                    continue

                # Sayısal veri kontrolü ve toplama
                df[cols] = df[cols].apply(pd.to_numeric, errors='coerce').fillna(0)
                annual_data[year] = df[cols].sum(axis=1)

            # Yıllık DataFrame oluştur
            df_annual = pd.DataFrame(annual_data)
            print(df_annual.head())  # Debugging output

            # İlk veri için yıllık verileri al
            data1 = df_annual[df_annual[category] == categoryLabel].iloc[:, 1:].values.flatten()

            # İlk yılı 100 olarak belirle ve sonraki yılları CPI gibi hesapla
            base_year_value = data1[0]
            cpi_data = (data1 / base_year_value) * 100

            # Grafik oluştur
            plt.figure(figsize=(25, 10))
            plt.title(f"{categoryLabel} Annual Trend Analysis for {symbol}", fontsize=14)
            sns.lineplot(x=years, y=cpi_data, marker="o", label=f"{categoryLabel} ")
            #plt.yticks(cpi_data)
            plt.ylabel("Index (Base Year = 100)")
            plt.grid(True)
            plt.legend(loc='upper left')
            plt.xticks(rotation=45)
            plt.show()

            # Yıl bazında veri analizi (dateType == "yearly")
        elif dateType == "yearly":
            data1 = df[df[category] == categoryLabel].iloc[:, 3:].values.flatten()
            numeric_columns = df.iloc[:, 3:]
            years = numeric_columns.columns
            plt.plot(years, data1, label=str(categoryLabelcategoryLabel))
            plt.legend(loc='upper left')
            plt.show()
    else:
        print("Invalid plot type")

        return










