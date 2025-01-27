# Finansal Tablo Analizi

## Türkçe - Turkish explanation, English version is below


Bu proje, `FinancialStatementAnalysis` kullanarak finansal verileri nasıl çekeceğinizi, finansal oranları nasıl hesaplayacağınızı ve belirli bir sembol için belirli bir zaman diliminde seçilen finansal oranları nasıl grafikleştireceğinizi göstermektedir.

## Gereksinimler

- Python 3.x
- pandas kütüphanesi
- isyatirimhisse (özel teşekkürler github.com/urazakgul/isyatirimhisse)

## Kurulum

Kodu çalıştırmadan önce gerekli kütüphanelerin kurulu olduğundan emin olun. `pandas` kütüphanesini pip kullanarak kurabilirsiniz:

```bash
pip install pandas
pip install isyatirimhisse
```

## Kullanım

Aşağıdaki betik, finansal verileri nasıl çekeceğinizi, finansal oranları nasıl hesaplayacağınızı ve seçilen finansal oranları nasıl grafikleştireceğinizi göstermektedir.

### Betik

```python
import pandas as pd
import FinancialStatementAnalysis as fsa

# Verileri çek
data = fsa.data()

# Parametreleri tanımla
symbol = "TTRAK"
begYear = 2008
endYear = 2024
exchange = "TRY"
financialGroup = 1
selected_ratios = ["Current Ratio", "Quick Ratio"]

# Finansal oranları hesapla
ratios = fsa.calcAll(symbol, begYear, endYear, exchange, financialGroup)

# Grafik için çıktı dosya adını tanımla
output_file_name = 'selected_financial_ratios.png'

# Seçilen finansal oranları grafikleştir
fsa.plot_ratios(ratios, output_file_name, selected_ratios)
```

### Parametreler

- `symbol`: Finansal verilerin çekileceği hisse senedi sembolü (örneğin, "TTRAK").
- `begYear`: Veri aralığı için başlangıç yılı (örneğin, 2008).
- `endYear`: Veri aralığı için bitiş yılı (örneğin, 2024).
- `exchange`: Borsa kodu (örneğin, "TRY").
- `financialGroup`: Finansal grup tanımlayıcısı (örneğin, 1).
- `selected_ratios`: Grafikleştirilecek finansal oranların listesi (örneğin, `["Current Ratio", "Quick Ratio"]`).

### Çıktı

- Betik, belirtilen hisse senedi sembolü için belirli bir zaman diliminde finansal oranları hesaplar.
- Seçilen finansal oranlar grafikleştirilir ve bir resim dosyasına (`selected_financial_ratios.png`) kaydedilir.

## Örnek Kullanım

1. Hisse senedi sembolü, tarih aralığı, borsa ve finansal grup için parametreleri tanımlayın.
2. `calcAll` yöntemi ile finansal oranları hesaplayın.
3. `plot_ratios` yöntemi ile seçilen finansal oranları grafikleştirin ve grafiği bir resim dosyasına kaydedin.

## Notlar

- `FinancialStatementAnalysis` modülünün doğru şekilde kurulu ve erişilebilir olduğundan emin olun.
- Farklı hisse senedi sembolleri veya tarih aralıkları için verileri çekmek ve analiz etmek amacıyla parametreleri gerektiği gibi ayarlayın.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

README dosyasını, projenizin özel gereksinimleri ve detayları doğrultusunda daha fazla özelleştirmekten çekinmeyin.
# Financial Statement Analysis

This project demonstrates how to use the `FinancialStatementAnalysis` to fetch financial data, calculate financial ratios, and plot selected financial ratios for a specified symbol over a given time period.

## Prerequisites

- Python 3.x
- pandas library
- isyatirimhisse special thanks to github.com/urazakgul/isyatirimhisse

## Installation

Before running the code, make sure you have the necessary libraries installed. You can install `pandas` using pip:

```bash
pip install pandas
pip install isyatirimhisse

```


## Usage

The following script demonstrates how to fetch financial data, calculate financial ratios, and plot selected financial ratios.

### Script

```python
import pandas as pd
import FinancialStatementAnalysis as fsa

# Fetch data
data = fsa.data()

# Define parameters
symbol = "TTRAK"
begYear = 2008
endYear = 2024
exchange = "TRY"
financialGroup = 1
selected_ratios = ["Current Ratio", "Quick Ratio"]

# Calculate financial ratios
ratios = fsa.calcAll(symbol, begYear, endYear, exchange, financialGroup)

# Define output file name for the plot
output_file_name = 'selected_financial_ratios.png'

# Plot selected financial ratios
fsa.plot_ratios(ratios, output_file_name, selected_ratios)
```

### Parameters

- `symbol`: The stock symbol for which the financial data is to be fetched (e.g., "TTRAK").
- `begYear`: The beginning year for the data range (e.g., 2008).
- `endYear`: The ending year for the data range (e.g., 2024).
- `exchange`: The exchange code (e.g., "TRY").
- `financialGroup`: The financial group identifier (e.g., 1).
- `selected_ratios`: A list of financial ratios to be plotted (e.g., `["Current Ratio", "Quick Ratio"]`).

### Output

- The script calculates financial ratios for the specified stock symbol over the given time period.
- The selected financial ratios are plotted and saved to an image file (`selected_financial_ratios.png`).

## Example Usage

1. Define the parameters for the stock symbol, date range, exchange, and financial group.
2. Calculate the financial ratios using the `calcAll` method.
3. Plot the selected financial ratios using the `plot_ratios` method and save the plot to an image file.

## Notes

- Ensure that the `FinancialStatementAnalysis` module is properly installed and accessible.
- Adjust the parameters as needed to fetch and analyze data for different stock symbols or date ranges.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file further based on your project's specific requirements and details.
