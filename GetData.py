from isyatirimhisse import StockData, Financials
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns

# Define the stock data
bist = ["AVOD", "ACSEL", "ADEL", "ADESE", "ADGYO", "AFYON", "AGHOL", "AGESA", "AGROT", "AHGAZ", "AKSFA", "AKFGY", "AKFYE", "AKSGY", "AKMGY", "AKBNK", "AKCNS", "AKENR", "AKGRT", "AKSA", "AKSEN", "AKYHO", "ALARK", "ALBRK", "ALCAR", "ALGYO", "ALKIM", "ALMAD", "ANELE", "ARCLK", "ARENA", "ARMDA", "ARSAN", "ARTI", "ASELS", "ASUZU", "ATAGY", "ATATP", "ATLAS", "ATSYH", "AVGYO", "AVISA", "AYCES", "AYDEM", "AYEN", "AYGAZ", "AZTEK", "BANVT", "BASCM", "BAYRK", "BERA", "BEYAZ", "BFREN", "BIMAS", "BIOEN", "BIZIM", "BJKAS", "BLCYT", "BMELK", "BMSCH", "BRISA", "BRKO", "BRMEN", "BRYAT", "BSOKE", "BTCIM", "BUCIM", "BURCE", "BURVA", "CANTE", "CASA", "CEMAS", "CEOEM", "CIMSA", "CMBTN", "COSMO", "CRDFA", "CRFSA", "CRISP", "CUSAN", "DAGHL", "DAGI", "DARDL", "DATAG", "DENGE", "DENIZ", "DERAS", "DERHL", "DESA", "DESPC", "DEVA", "DGATE", "DGKLB", "DGNMO", "DGRYO", "DIRIT", "DITAS", "DMSAS", "DOAS", "DOBUR", "DOCO", "DOGUB", "DOHOL", "DOKTA", "DURDO", "DYOBY", "ECILC", "ECZYT", "EDATA", "EDIP", "EGCEY", "EGEEN", "EGGUB", "EGPRO", "EGSER", "EGSUZ", "EKGYO", "EKIZ", "ENJSA", "ENKAI", "ERBOS", "EREGL", "ERSU", "ESCAR", "ESCOM", "ETILR", "EUHOL", "EUKYO", "EUREN", "EUYO", "FENER", "FONET", "FORMT", "FRIGO", "FROTO", "GARAN", "GEDIK", "GEDZA", "GENTS", "GEREL", "GLBMD", "GLRYH", "GLYHO", "GOLTS", "GOODY", "GOZDE", "GRNYO", "GSDDE", "GSDHO", "GSRAY", "GUBRF", "GUCLU", "GUSGR", "HALKB", "HALKS", "HATEK", "HDFGS", "HEDEF", "HEKTS", "HUBVC", "HUNER", "ICBCT", "IDEAS", "IDGYO", "IHEVA", "IHLAS", "IHYAY", "INDES", "INFO", "INTEM", "IPEKE", "ISCTR", "ISDMR", "ISFIN", "ISGYO", "ISKPL", "ISMEN", "ITTFH", "IZFAS", "IZINV", "IZMDC", "JANTS", "KAPLM", "KARSN", "KARTN", "KARYE", "KATMR", "KCHOL", "KENT", "KLKIM", "KLGYO", "KLMSN", "KMPUR", "KNFRT", "KONKA", "KORDS", "KOZAA", "KOZAL", "KRGYO", "KRONT", "KRTEK", "KUTPO", "KUYAS", "LIDFA", "LINK", "LKMNH", "LOGO", "MAALT", "MAGEN", "MAKTK", "MARKA", "MARTI", "MAVI", "MEGAP", "MERIT", "METRO", "METUR", "MIPAZ", "MMCAS", "MNDRS", "MPARK", "MRDIN", "MRSHL", "MSGYO", "MTRKS", "NATEN", "NIBAS", "NTHOL", "NUHCM", "ODAS", "OLMIP", "ORCAY", "ORGE", "OSTIM", "OTKAR", "OYAKC", "OYYAT", "PAGYO", "PAPIL", "PARSN", "PARSN", "PCILT", "PEGYO", "PENGD", "PETKM", "PGSUS", "POLHO", "PRKAB", "PRKME", "PSGYO", "PTOFS", "QUAGR", "RAYSG", "RALYH", "RHEAG", "ROYAL", "RYGYO", "SAHOL", "SANFM", "SANEL", "SANPA", "SARKY", "SASA", "SAHOL", "SAYAS", "SEKFK", "SEKUR", "SELEC", "SELGD", "SENKR", "SERVE", "SILVR", "SISE", "SKBNK", "SMART", "SNGYO", "SODSN", "SOFT", "SONME", "SRVGY", "SUMAS", "TACİRL", "TACTR", "TACTP", "TARDN", "TARFA", "TATGD", "TAVHL", "TBORG", "TCELL", "TDGYO", "TEKTU", "TGSAS", "THYAO", "TKFEN", "TMSN", "TMPOL", "TNPOL", "TNSFN", "TOASO", "TRCAS", "TRGYO", "TRILC", "TRKCM", "TRKHA", "TSGYO", "TSKB", "TTKOM", "TTRAK", "TUKAS", "TUNCM", "TUPRS", "TUREX", "TURGG", "TURKR", "TURSG", "ULAS", "ULKER", "ULUSE", "UNLU", "USAK", "UZEL", "UZKIP", "VAKBN", "VERTU", "VESTL", "VEYAL", "VKGYO", "YAPRK", "YATAS", "YAYLA", "YESIL", "YESYH", "YGGYO", "YKGYO", "YKSGR", "YOKFN", "YONGA", "YUNSA", "ZOREN"]
bist100All = ["ADER", "AEFES", "AGHOL", "AGROT", "AKBNK", "AKFGY", "AKFYE", "AKSA", "AKSEN", "ALARK","ALFAS", "ALTNY", "ANSGR", "ARCLK", "ARDYZ", "ASELS", "ASTOR", "BERA", "BIMAS", "BINHO","BJKAS", "BRSAN", "BRYAT", "BTCIM", "CANTE", "CCOLA", "CIMSA", "CLEBI", "CWENE", "DOAS","DOHOL", "ECILC", "EGEEN", "EKGYO", "ENERY", "ENJSA", "ENKAI", "EREGL", "EUPWR", "FENER","FROTO", "GARAN", "GESAN", "GOLTS", "GUBRF", "HALKB", "HEKTS", "ISCTR", "ISMEN", "KARSN","KCAER", "KCHOL", "KLSER", "KONTR", "KONYA", "KOZAA", "KOZAL", "KRDMD", "KTLEV", "LMKDC","MAVI", "MGROS", "MIATK", "MPARK", "OBAMS", "ODAS", "OTKAR", "OYAKC", "PAPIL", "PEKGY","PETKM", "PGSUS", "REEDR", "RGYAS", "SAHOL", "SASA", "SISE", "SKBNK", "SMRTG", "SOKM","TABGD", "TAVHL", "TCELL", "THYAO", "TKFEN", "TMSN", "TOASO", "TSKB", "TTKOM", "TTRAK","TUKAS", "TUPRS", "TURSG", "ULKER", "VAKBN", "VESBE", "VESTL", "YEOTK", "YKBNK", "ZOREN"]

# Defined and saved Excel Stock Lists
bistAllExBist100 = ['AVOD', 'ACSEL', 'ADEL', 'ADESE', 'ADGYO', 'AFYON', 'AGESA', 'AHGAZ', 'AKSFA', 'AKSGY', 'AKMGY', 'AKCNS', 'AKENR', 'AKGRT', 'AKYHO', 'ALBRK', 'ALCAR', 'ALGYO', 'ALKIM', 'ALMAD', 'ANELE', 'ARENA', 'ARMDA', 'ARSAN', 'ARTI', 'ASUZU', 'ATAGY', 'ATATP', 'ATLAS', 'ATSYH', 'AVGYO', 'AVISA', 'AYCES', 'AYDEM', 'AYEN', 'AYGAZ', 'AZTEK', 'BANVT', 'BASCM', 'BAYRK', 'BEYAZ', 'BFREN', 'BIOEN', 'BIZIM', 'BLCYT', 'BMELK', 'BMSCH', 'BRISA', 'BRKO', 'BRMEN', 'BSOKE', 'BUCIM', 'BURCE', 'BURVA', 'CASA', 'CEMAS', 'CEOEM', 'CMBTN', 'COSMO', 'CRDFA', 'CRFSA', 'CRISP', 'CUSAN', 'DAGHL', 'DAGI', 'DARDL', 'DATAG', 'DENGE', 'DENIZ', 'DERAS', 'DERHL', 'DESA', 'DESPC', 'DEVA', 'DGATE', 'DGKLB', 'DGNMO', 'DGRYO', 'DIRIT', 'DITAS', 'DMSAS', 'DOBUR', 'DOCO', 'DOGUB', 'DOKTA', 'DURDO', 'DYOBY', 'ECZYT', 'EDATA', 'EDIP', 'EGCEY', 'EGGUB', 'EGPRO', 'EGSER', 'EGSUZ', 'EKIZ', 'ERBOS', 'ERSU', 'ESCAR', 'ESCOM', 'ETILR', 'EUHOL', 'EUKYO', 'EUREN', 'EUYO', 'FONET', 'FORMT', 'FRIGO', 'GEDIK', 'GEDZA', 'GENTS', 'GEREL', 'GLBMD', 'GLRYH', 'GLYHO', 'GOODY', 'GOZDE', 'GRNYO', 'GSDDE', 'GSDHO', 'GSRAY', 'GUCLU', 'GUSGR', 'HALKS', 'HATEK', 'HDFGS', 'HEDEF', 'HUBVC', 'HUNER', 'ICBCT', 'IDEAS', 'IDGYO', 'IHEVA', 'IHLAS', 'IHYAY', 'INDES', 'INFO', 'INTEM', 'IPEKE', 'ISDMR', 'ISFIN', 'ISGYO', 'ISKPL', 'ITTFH', 'IZFAS', 'IZINV', 'IZMDC', 'JANTS', 'KAPLM', 'KARTN', 'KARYE', 'KATMR', 'KENT', 'KLKIM', 'KLGYO', 'KLMSN', 'KMPUR', 'KNFRT', 'KONKA', 'KORDS', 'KRGYO', 'KRONT', 'KRTEK', 'KUTPO', 'KUYAS', 'LIDFA', 'LINK', 'LKMNH', 'LOGO', 'MAALT', 'MAGEN', 'MAKTK', 'MARKA', 'MARTI', 'MEGAP', 'MERIT', 'METRO', 'METUR', 'MIPAZ', 'MMCAS', 'MNDRS', 'MRDIN', 'MRSHL', 'MSGYO', 'MTRKS', 'NATEN', 'NIBAS', 'NTHOL', 'NUHCM', 'OLMIP', 'ORCAY', 'ORGE', 'OSTIM', 'OYYAT', 'PAGYO', 'PARSN', 'PARSN', 'PCILT', 'PEGYO', 'PENGD', 'POLHO', 'PRKAB', 'PRKME', 'PSGYO', 'PTOFS', 'QUAGR', 'RAYSG', 'RALYH', 'RHEAG', 'ROYAL', 'RYGYO', 'SANFM', 'SANEL', 'SANPA', 'SARKY', 'SAHOL', 'SAYAS', 'SEKFK', 'SEKUR', 'SELEC', 'SELGD', 'SENKR', 'SERVE', 'SILVR', 'SMART', 'SNGYO', 'SODSN', 'SOFT', 'SONME', 'SRVGY', 'SUMAS', 'TACİRL', 'TACTR', 'TACTP', 'TARDN', 'TARFA', 'TATGD', 'TBORG', 'TDGYO', 'TEKTU', 'TGSAS', 'TMPOL', 'TNPOL', 'TNSFN', 'TRCAS', 'TRGYO', 'TRILC', 'TRKCM', 'TRKHA', 'TSGYO', 'TUNCM', 'TUREX', 'TURGG', 'TURKR', 'ULAS', 'ULUSE', 'UNLU', 'USAK', 'UZEL', 'UZKIP', 'VERTU', 'VEYAL', 'VKGYO', 'YAPRK', 'YATAS', 'YAYLA', 'YESIL', 'YESYH', 'YGGYO', 'YKGYO', 'YKSGR', 'YOKFN', 'YONGA', 'YUNSA']
bist100 = ['ADER', 'AEFES', 'AGHOL', 'AGROT', 'AKFGY', 'AKFYE', 'AKSA', 'AKSEN', 'ALFAS', 'ALTNY', 'ANSGR', 'ARCLK', 'ARDYZ', 'BERA', 'BINHO', 'BJKAS', 'BRSAN', 'BRYAT', 'BTCIM', 'CANTE', 'CCOLA', 'CIMSA', 'CLEBI', 'CWENE', 'DOHOL', 'ECILC', 'EGEEN', 'ENERY', 'ENJSA', 'EUPWR', 'FENER', 'GESAN', 'GOLTS', 'GUBRF', 'ISMEN', 'KARSN', 'KCAER', 'KLSER', 'KONYA', 'KOZAA', 'KTLEV', 'LMKDC', 'MAVI', 'MIATK', 'MPARK', 'OBAMS', 'ODAS', 'OTKAR', 'OYAKC', 'PAPIL', 'PEKGY', 'REEDR', 'RGYAS', 'SMRTG', 'SOKM', 'TABGD', 'TAVHL', 'TKFEN', 'TMSN', 'TTRAK', 'TUKAS', 'TURSG', 'VESBE', 'VESTL', 'YEOTK', 'ZOREN']
bist30ExBanks =["ALARK", "ASELS", "ASTOR", "BIMAS", "DOAS", "EKGYO", "ENKAI", "EREGL", "FROTO", "HEKTS", "KCHOL", "KONTR", "KOZAL", "KRDMD", "MGROS", "PETKM", "PGSUS", "SAHOL", "SASA", "SISE", "TCELL", "THYAO", "TOASO", "TTKOM", "TUPRS", "ULKER"]  #
banks = ["AKBNK", "GARAN", "ISCTR", "VAKBN", "YKBNK", "HALKB", "SKBNK", "ALBRK", "ICBCT", "QNBFL", "TKYAT", "TSKB"]

# Did not work
notWorked = ["ADER", "ANSGR", "KTLEV", "TURSG", "AGESA", "AKSFA", "AKGRT", "ALBRK", "ARMDA", "AVISA", "BMELK", "CRDFA", "CRISP", "DATAG","DENIZ", "DERAS", "DGKLB", "DGRYO", "DOCO", "EGSUZ", "GUCLU", "GUSGR", "HALKS", "ICBCT","IDEAS", "ISFIN", "ITTFH", "LIDFA", "MIPAZ", "MRDIN", "OLMIP", "PEGYO", "PTOFS", "RAYSG","RHEAG", "SANPA", "SEKFK", "SENKR", "SERVE", "SOFT", "TACİRL", "TACTR", "TACTP", "TARDN","TARFA", "TNPOL", "TNSFN", "TRKHA", "TUNCM", "TURKR", "UZEL", "UZKIP", "VEYAL", "YESYH","YKGYO", "YKSGR", "YOKFN"]

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










