# Complete Assignment Explanation — Roman Urdu

Yeh aapki learning guide hai. Is mein actual `sales_assignment.ipynb`, `run_assignment.py`, `build_assignment.py` aur saved CSV results ko samjhaya gaya hai. Pehle task aur pseudocode, phir implementation aur har code statement ka matlab diya gaya hai. Jo statement multiple lines mein hai, uski continuation lines bhi usi explanation mein covered hain. Blank lines sirf readability ke liye hain; woh koi operation nahi kartin.

## 1. Assignment mein task kya tha?

Humein raw sales data ko samajhna, clean karna, us se insights nikalna aur CSV editing demonstrate karni thi. Data provided `sales_raw.csv` se aata hai. Sales records khud se generate nahi kiye gaye.

**Part A — 70 marks:** CSV read aur inspect karo; missing values, invalid prices, inconsistent text aur duplicates handle karo; revenue calculate karo; grouped summary, do labelled charts aur do findings banao; cleaned CSV save karo. Original input preserve karo.

**Part B — 30 marks:** Part A ka output reload karo; revenue ka 5% tax add karo; Books prices 10% increase karo; dependent revenue/tax dobara calculate karo; existing transaction ID ki ek row delete karo; temporary review column add aur drop karo; separate updated CSV save/reload karke verify karo.

**Submission:** Dono parts ek runnable notebook mein; raw/cleaned/updated CSVs; README mein run instructions aur actual GitHub URL; sab required files ek ZIP mein, actual student name/training ID wale naam ke saath.

## 2. Pehle pseudocode: code likhne se pehle soch

Pseudocode normal zaban mein algorithm hota hai. Yeh executable Python nahi hota.

```text
PART A
1. Libraries load karo.
2. sales_raw.csv read karke table banao.
3. First 5 rows, dimensions, names, types, missing aur duplicate counts dikhao.
4. Raw table ki working copy banao; initial row count yaad rakho.
5. Exact duplicate rows remove karo.
6. Region/category ke spaces aur letter case standardize karo.
7. Missing region/category ko Unknown label do.
8. Date aur numeric conversion karo; invalid input missing ban jaye.
9. Missing/invalid date, missing/nonpositive quantity ya price wali rows identify karo.
10. Rejected rows dikhao, phir remove karo aur index reset karo.
11. Har remaining row: revenue = quantity * unit_price.
12. Before/after count aur missing values dobara dikhao.
13. Region/category ke groups ki revenue summary banao.
14. Region bar chart aur daily revenue line chart banao/save karo.
15. Actual totals se do findings likho; high price ka influence explain karo.
16. cleaned_sales.csv save karo, extra index column ke baghair.

PART B
1. cleaned_sales.csv dobara read karo.
2. Har row: tax_amount = revenue * 0.05; head dikhao.
3. Books select karo; price = old price * 1.10.
4. Revenue aur tax dobara calculate karo.
5. Transaction 1002 ki row remove karo.
6. review_status add karo; phir column drop karo.
7. sales_updated.csv save karo.
8. Saved CSV reload karke head, columns aur dimensions dikhao.
9. Assertions se formulas aur requested changes check karo.
```

## 3. Data ke columns ka matlab

| Column | Matlab | Example |
|---|---|---|
| transaction_id | Sale/transaction ki pehchan | 1001 |
| sale_date | Sale ki date | 10/1/2026 = October 1, 2026 |
| region | Sale ka region | North |
| category | Product ki category | Books |
| quantity | Kitne units sell hue | 2 |
| unit_price | Ek unit ki price | 120 |
| revenue | Quantity × unit price | 2 × 120 = 240 |
| tax_amount | Revenue ka 5% | 240 × 0.05 = 12 |

Source mein currency ka naam nahi diya gaya, is liye hum amounts ko rupees/dollars assume nahi karte. Revenue yahan tax se pehle ki sales amount hai; profit nahi. Profit nikalne ke liye cost chahiye jo source mein nahi hai.

## 4. Library, class, object, function, method aur attribute

| Term | Simple matlab | Hamare code mein |
|---|---|---|
| Library/package | Related tools ka collection | pandas, matplotlib |
| Module | Import ki ja sakne wali code unit | json, os, matplotlib.pyplot |
| Alias | Chhota local naam | pandas ko `pd`, pyplot ko `plt` |
| Class | Objects banane ka blueprint/type | DataFrame, Series, Path, NotebookClient |
| Object | Class ka actual instance | `raw`, `clean`, `fig`, `ax` |
| Function | Callable operation | `pd.read_csv(...)`, `len(...)` |
| Method | Object/type se attached callable | `raw.head()`, `clean.to_csv(...)` |
| Attribute/property | Object ki information; call nahi | `raw.shape`, `raw.dtypes` |
| Argument | Function/method ko diya input | `'sales_raw.csv'`, `index=False` |
| Variable | Value/object ko refer karne wala naam | `before`, `total`, `books` |

`pd.read_csv()` ek function hai jo **DataFrame object** return karta hai. Humne custom business class define nahi ki; library ke existing classes ke objects use kiye hain.

**DataFrame:** Rows/columns wali table, jaise Excel sheet. `raw` aur `clean` DataFrames hain.

**Series:** Ek dimension ki labelled values. `clean['quantity']` ek Series hai. `daily` bhi date-indexed Series hai.

**Figure/Axes:** Matplotlib mein Figure poori drawing canvas hai; Axes uske andar graph area hai. Variable `ax` graph area ko refer karta hai. `Axes` ka naam plural lagta hai magar yahan ek object hai.

**Path:** Files/folders ke paths handle karta hai. **NotebookClient:** Notebook ke code cells kernel se execute karwata hai. **ZipFile:** Archive read/write karta hai.

## 5. Syntax ki bunyaad

- `=` assignment hai: right side ka result left variable/column ko milta hai.
- `==` equality comparison hai; `*` multiplication; `-` subtraction; `/` division.
- `[]` list banana ya table se column/select karna; `{}` dictionary ya f-string placeholder.
- `()` function call, expression grouping ya tuple ho sakta hai, context par depend karta hai.
- `:` aur indentation loop/function/conditional ka block define karte hain.
- `#` comment hai; Python execute nahi karta.
- `'text'` aur `"text"` strings hain. `'''...'''` multiple lines wali string hai.
- `True` / `False` Boolean values hain.
- Pandas masks mein `|` elementwise OR aur `~` elementwise NOT hai. Yahan Python ka `or` lagana sahi replacement nahi.
- `f'...{value}...'` f-string hai: variable/formula ka result text mein insert hota hai.
- `\n` string mein new line hai; notebook JSON mein escaped representation alag dikh sakti hai.
- `.method1().method2()` chaining hai: pehle result par agla method apply hota hai.
- Pandas Series ki arithmetic har corresponding row par hoti hai; explicit row loop zaroori nahi. Isay vectorized operation kehte hain.

## 6. Part A: imports aur raw CSV inspection

Neeche exact notebook statements ke saath explanation hai.

### Libraries kyun?

```python
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
```

1. `from pathlib import Path`: Standard Python library ka Path class import karta hai. Aage `findings.md` file likhne ke kaam aata hai. Sirf CSV read karne ke liye yeh import zaroori nahi; findings export ke liye hai.
2. `import pandas as pd`: Tabular data read, clean, filter, group aur save karne ke tools. `pd` sirf alias hai.
3. `import matplotlib.pyplot as plt`: Graphs banane/save/display karne ke functions. `plt` alias hai.
4. `from IPython.display import display`: Notebook mein DataFrame ko readable table ki form mein dikhata hai. Yeh data cleaning nahi karta. Terminal runner isi display function ko terminal printing se temporarily replace karta hai.

### Load aur inspect

```python
raw = pd.read_csv('sales_raw.csv')
print('First five rows:')
display(raw.head())
print('Shape:', raw.shape)
print('Columns:', raw.columns.tolist())
print('Data types:')
print(raw.dtypes)
print('Missing values:')
print(raw.isna().sum())
print('Duplicate rows:', raw.duplicated().sum())
```

1. `raw = pd.read_csv(...)`: Actual CSV disk se read karke DataFrame `raw` banata hai. Relative filename hai, kisi personal absolute path par depend nahi karta. Default first line column headings banti hai.
2. `print('First five rows:')`: Sirf output label.
3. `display(raw.head())`: `head()` default pehli 5 rows return karta hai; `display` dikhata hai. Is se input structure ka sample samajh aata hai, poora dataset verify nahi hota.
4. `print('Shape:', raw.shape)`: Shape `(rows, columns)` tuple hai; input `(21, 6)` hai. Attribute hai, `shape()` nahi likhte.
5. `raw.columns` column-label Index hai; `.tolist()` ordinary Python list banata hai; `print` names dikhata hai.
6. `print('Data types:')`: Type output ka label.
7. `print(raw.dtypes)`: Har column ka inferred storage type. Raw `unit_price` mein `invalid` hai is liye use pehle numeric calculation ke laiq convert karna zaroori hai. Exact displayed type labels Pandas version se vary kar sakte hain.
8. `print('Missing values:')`: Missing-count output ka label.
9. `raw.isna()`: Har cell ka missing/nonmissing Boolean map; `.sum()` default har column mein True values count karta hai. Quantity, price aur region mein ek-ek original missing value milti hai. Literal `invalid` abhi missing nahi: conversion ke baad missing banega.
10. `raw.duplicated()`: Har exact repeated row par True, pehli occurrence par False. `.sum()` duplicate count **1** deta hai. Yeh poori row ka duplicate check hai, sirf transaction ID ka nahi.

## 7. Part A: cleaning ka har statement

### Working copy aur duplicates

```python
clean = raw.copy()
before = len(clean)
clean = clean.drop_duplicates().copy()
duplicates_removed = before - len(clean)
```

1. `.copy()` working DataFrame banata hai taake cleaning raw table par directly apply na ho. Original file preserve rehne ki doosri wajah yeh hai ke us filename par `to_csv` nahi chalaya gaya.
2. `len(clean)` rows count karta hai; `before = 21` initial audit number hai.
3. `.drop_duplicates()` exact duplicates remove karta hai, default first occurrence rakhta hai. Extra `.copy()` independent working object banata hai. Duplicate transaction 1003 ki repeated row remove hoti hai; 20 rows reh jati hain.
4. `before - len(clean)` se **1** duplicate removed count milta hai. Yeh logging/before-after explanation ke liye hai.

### Text cleaning

```python
for column in ['region', 'category']:
    clean[column] = clean[column].astype('string').str.strip().str.title()
    clean[column] = clean[column].replace('', pd.NA).fillna('Unknown')
```

1. `for column in [...]`: Wohi rules pehle region aur phir category par lagte hain; repeated code kam hota hai.
2. `clean[column]`: Current selected column. `.astype('string')` nullable text type banata hai. `.str` string methods ka accessor hai. `.strip()` start/end ke spaces hata deta hai. `.title()` capitalization standard karta hai. Example `' food '` → `'food'` → `'Food'`; `'SOUTH'` → `'South'`. Result usi column mein assign hota hai.
3. `.replace('', pd.NA)`: Whitespace trim ke baad agar empty text ho to missing marker banao. `pd.NA` Pandas missing-value marker hai. `.fillna('Unknown')` missing text ko label deta hai. Actual transaction 1018 ka region `Unknown` hota hai. Iska matlab region pata nahi; yeh naya actual geographical region nahi.

`Unknown` kyun? Is row ki quantity/price valid hain. Region invent kiye baghair sale retain karna reasonable choice hai. Missing region ki wajah se revenue discard karna zaroori nahi. Actual data mein category missing nahi, lekin same rule us column par bhi apply hai.

### Date aur number conversion

```python
clean['sale_date'] = pd.to_datetime(clean['sale_date'], format='%m/%d/%Y', errors='coerce')
for column in ['quantity', 'unit_price']:
    clean[column] = pd.to_numeric(clean[column], errors='coerce')
```

1. `pd.to_datetime` date strings ko datetime values mein convert karta hai. `%m` month, `%d` day, `%Y` four-digit year. Thus `10/1/2026` October 1 hai. `errors='coerce'` invalid date par crash karne ke bajaye `NaT` banata hai. Transaction 1014 ka `invalid-date` reject hone ke laiq missing date ban jata hai.
2. `for column ...`: Quantity aur unit_price dono numeric hone chahiye.
3. `pd.to_numeric(..., errors='coerce')`: Numeric text ko numbers mein, invalid text ko missing numeric value mein convert karta hai. Transaction 1011 ka price `invalid` → missing. Pehle se missing numbers bhi missing rehte hain.

`NaN` numeric missing marker, `NaT` datetime missing marker aur `pd.NA` nullable types ka missing marker hai. Hum checking ke liye `isna()` use karte hain; woh in sab ko handle karta hai.

### Invalid rows select karna

```python
invalid = (clean[['sale_date', 'quantity', 'unit_price']].isna().any(axis=1)
           | clean['quantity'].le(0) | clean['unit_price'].le(0))
print('Rejected transactions after duplicate removal:')
display(clean.loc[invalid])
rejected_count = int(invalid.sum())
```

1. `clean[[...]]` teen required columns ki subtable hai. Double square brackets is liye ke andar column names ki list hai.
2. `.isna().any(axis=1)`: Har row mein in teen fields mein se **koi ek bhi** missing ho to True. `axis=1` row ke across columns check karta hai.
3. Continuation line ka `.le(0)` means less than or equal to zero. Quantity **ya** price nonpositive ho to invalid. `|` teen conditions ko elementwise OR karta hai. Outer parentheses expression ko multiple lines mein likhne dete hain.
4. `invalid` Boolean Series/mask hai: kis row ko reject karna hai. Yeh data table se alag decision map hai.
5. `print(...)` rejection output ka label.
6. `.loc[invalid]` mask True wali rows return karta hai; `display` unko audit ke liye dikhata hai.
7. `.sum()` True values count karta hai; `int()` standard Python integer banata hai. `rejected_count = 5`.

### Actual rejected rows aur reasons

| Transaction | Reason |
|---|---|
| 1006 | Quantity missing |
| 1010 | Unit price missing |
| 1011 | Price `invalid`; numeric conversion ke baad missing |
| 1013 | Quantity -2; nonpositive quantity policy |
| 1014 | Invalid date |

Missing numeric values mein mean/median fill nahi kiya: woh imaginary quantity/price create karke total badal sakta tha. Negative quantity return ho sakti thi, magar dataset return semantics nahi deta; is solution mein documented rule ke mutabiq reject kiya. Yeh business choice hai, har sales system ke liye universal rule nahi.

### Valid rows, revenue aur audit

```python
clean = clean.loc[~invalid].reset_index(drop=True)
clean['quantity'] = clean['quantity'].astype(int)
clean['revenue'] = (clean['quantity'] * clean['unit_price']).round(2)
print(f'Rows before: {before}; duplicates removed: {duplicates_removed}; '
      f'invalid/incomplete rows removed: {rejected_count}; rows after: {len(clean)}')
print('Remaining missing values:')
print(clean.isna().sum())
display(clean)
```

1. `~invalid` mask invert karta hai: valid rows True. `.loc[...]` sirf valid rows rakhta hai. `.reset_index(drop=True)` row labels 0,1,2... bana deta hai; old index extra column nahi banta. Transaction IDs change nahi hote.
2. `.astype(int)` quantity ko integer banata hai. Is actual file ki valid quantities whole units hain. Agar future data mein fractional quantities hon to yeh conversion unko truncate kar sakti hai; yeh general-purpose validation rule nahi.
3. Quantity × price har row ka revenue hai. `.round(2)` two decimal places. Transaction 1001: `2 * 120 = 240`.
4. Dono adjacent f-strings ek print message banti hain: **21 before − 1 duplicate − 5 rejected = 15 after**. Doosri physical line pehle `print` ki continuation hai.
5. `print('Remaining missing values:')` label.
6. Missing counts dobara calculate hote hain; cleaned table ke har column mein zero.
7. `display(clean)` poori small cleaned table dikhata hai.

**10,000 price delete kyun nahi ki?** Transaction 1016 mein price high hai, magar valid positive numeric value hai. Source correct price nahi batata. Humne retain ki aur findings mein influence disclose kiya. Code automatic statistical outlier detection nahi karta; known 10,000 price ko explicitly select karta hai.

## 8. Part A: grouping aur summaries

```python
region_summary = (clean.groupby('region', as_index=False)
                  .agg(total_revenue=('revenue', 'sum'), transactions=('transaction_id', 'count'))
                  .sort_values('total_revenue', ascending=False))
category_summary = (clean.groupby('category', as_index=False)['revenue'].sum()
                    .sort_values('revenue', ascending=False))
print('Revenue by region:')
display(region_summary)
print('Revenue by category:')
display(category_summary)
region_summary.to_csv('revenue_by_region.csv', index=False)
category_summary.to_csv('revenue_by_category.csv', index=False)
print('Total revenue:', f"{clean['revenue'].sum():,.2f}")
```

1. `groupby('region', as_index=False)`: Same region ki rows ek group. `as_index=False` region ko normal column rakhta hai. GroupBy intermediate object khud final summary nahi; aggregation chahiye.
2. `.agg(...)`: Named aggregations. `total_revenue=('revenue','sum')` revenue add karta hai. `transactions=('transaction_id','count')` nonmissing IDs count karta hai. Actual cleaned IDs nonmissing hain is liye yeh transaction count hai.
3. `.sort_values(..., ascending=False)`: Sabse zyada revenue upar. First 3 physical lines ek assignment statement hain.
4. Category statement same grouping karta hai; `['revenue']` sirf revenue aggregate karta hai; `.sum()` total, phir descending sort. Next physical line uski continuation hai.
5. `print('Revenue by region:')`: Label.
6. `display(region_summary)`: Region summary table.
7. `print('Revenue by category:')`: Label.
8. `display(category_summary)`: Category summary table.
9. First `.to_csv` region summary separate CSV save karta hai. `index=False` DataFrame index ko extra unnamed column banne se rokta hai.
10. Second `.to_csv` category summary save karta hai. Ye extra helpful exports hain; brief mein ek grouped summary minimum thi.
11. `clean['revenue'].sum()` total sales. Format `:,.2f` comma thousands separator aur 2 decimal digits deta hai: `14,175.00`.

### Actual region summary

| Region | Revenue | Transactions |
|---|---:|---:|
| North | 11,470 | 6 |
| South | 1,035 | 3 |
| East | 740 | 3 |
| West | 530 | 2 |
| Unknown | 400 | 1 |

### Actual category summary

| Category | Revenue |
|---|---:|
| Stationery | 10,460 |
| Food | 1,945 |
| Books | 1,770 |

## 9. Part A: chart 1 ki har line

```python
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(region_summary['region'], region_summary['total_revenue'], color='#2563eb')
ax.bar_label(bars, fmt='%.0f', padding=3)
ax.set(title='Revenue by Region', xlabel='Region', ylabel='Revenue (currency units)')
ax.set_ylim(0, region_summary['total_revenue'].max() * 1.15)
fig.tight_layout()
fig.savefig('revenue_by_region.png', dpi=160)
plt.show()
```

1. `.style.use(...)` readable white-grid styling apply karta hai. Yeh Matplotlib ka supplied style hai; separate seaborn import use nahi hui. Styling calculation ke liye zaroori nahi.
2. `.subplots(figsize=(8,5))` 8×5 inches Figure aur ek Axes return karta hai; tuple unpacking se `fig`, `ax` milte hain.
3. `.bar(x,y,...)` region names ke against revenue bars banata hai. `bars` BarContainer object hai. Hex color graph ki appearance set karta hai.
4. `.bar_label(...)` bars par amount labels. `fmt='%.0f'` zero decimal places; `padding=3` text aur bar mein space.
5. `.set(...)` title aur dono axes labels deta hai; labelled chart requirement cover hoti hai.
6. `.set_ylim(...)` y-axis zero se highest value ke 115% tak: labels ke liye headroom. `.max()` biggest regional revenue return karta hai.
7. `.tight_layout()` spacing adjust karta hai taake titles/labels overlap ya cut na hon.
8. `.savefig(...)` PNG disk par likhta hai; `dpi=160` image resolution. DataFrame ya CSV nahi banta.
9. `plt.show()` notebook mein chart display karta hai. Terminal runner isko no-op karta hai; saved PNG phir bhi banti hai.

Bar chart kyun? Discrete categories/regions ki amounts compare karna easy hota hai.

## 10. Part A: chart 2 ki har line

```python
daily = clean.groupby('sale_date')['revenue'].sum().sort_index()
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(daily.index, daily.values, marker='o', color='#0f766e', linewidth=2)
ax.set(title='Daily Sales Revenue', xlabel='Sale date (October 2026)', ylabel='Revenue (currency units)')
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig('daily_revenue.png', dpi=160)
plt.show()
```

1. `groupby('sale_date')` same day ki sales group; revenue `.sum()` daily total; `.sort_index()` dates ascending. `daily` date-indexed Series hai. October 7 ki valid transaction nahi bachi; code missing date ke liye zero row insert nahi karta.
2. Nayi Figure/Axes 9×5 inches; purani variables replace hoti hain, pehli saved PNG delete nahi hoti.
3. `.plot(...)` dates on x-axis, amounts on y-axis. `.index` dates, `.values` amounts. `marker='o'` dots, color aur line width display options hain. Line observed dates ko join karti hai; unobserved date ka exact revenue infer nahi hota.
4. Chart title aur axes names. October 2026 label current dataset ke liye hai; future data ke months badlein to yeh label bhi update hona chahiye.
5. `matplotlib.dates` date-formatting module import; alias `mdates`.
6. `mdates.DateFormatter('%b %d')` formatter object banata hai: abbreviated month + day, jaise `Oct 08`. `.set_major_formatter(...)` x-axis tick labels par apply karta hai.
7. `.autofmt_xdate()` dates ke label rotation/alignment ko readable banata hai.
8. `.tight_layout()` spacing adjust.
9. `.savefig(...)` second PNG export.
10. `.show()` notebook display.

Line chart kyun? Date/time ke saath amount ka change aur spike dikhata hai. Sirf 10 din ke sample se long-term trend prove nahi hota.

## 11. Part A: findings aur cleaned CSV export

```python
total = clean['revenue'].sum()
leader = region_summary.iloc[0]
unusual = clean.loc[clean['unit_price'].eq(10000)].iloc[0]
peak_date = daily.idxmax()
findings = (
    f"1. {leader['region']} leads regional revenue with {leader['total_revenue']:,.2f} "
    f"({leader['total_revenue'] / total:.1%} of the {total:,.2f} total). "
    f"Transaction {int(unusual['transaction_id'])} alone contributes {unusual['revenue']:,.2f} "
    f"({unusual['revenue'] / total:.1%} of total), so this lead depends heavily on an unverified high price.\n\n"
    f"2. Daily revenue peaks on {peak_date:%Y-%m-%d} at {daily.max():,.2f}. "
    f"Excluding that high-price transaction would reduce that day's revenue to "
    f"{daily.loc[unusual['sale_date']] - unusual['revenue']:,.2f}; "
    "the peak should not be interpreted as a sustained sales trend."
)
print(findings)
Path('findings.md').write_text('# Two evidence-based findings\n\n' + findings + '\n', encoding='utf-8')
clean.to_csv('cleaned_sales.csv', index=False, date_format='%Y-%m-%d')
print('Saved cleaned_sales.csv')
```

1. `total` cleaned revenue ka total **14,175**.
2. `.iloc[0]` integer position se first regional row leta hai. Summary pehle descending sort hui thi, is liye leader North hai. `.loc` labels/masks ke liye; `.iloc` positions ke liye.
3. `.eq(10000)` price equal-to-10000 mask. `.loc[...]` matching rows select karta hai; `.iloc[0]` pehli match ka Series. Actual record 1016 hai. Yeh dataset-specific selection hai; agar future file mein matching price na ho to `.iloc[0]` error dega.
4. `.idxmax()` maximum revenue ki index label/date deta hai, value nahi. Peak date **2026-10-08**.
5. `findings = (` multiple adjacent strings ko ek variable mein collect karta hai. Parentheses grouping hain, list nahi.
6. Pehli f-string leader ka region aur revenue insert karti hai: North, 11,470.00.
7. Next line regional share calculate karti hai: `11470 / 14175`; `:.1%` ratio ko percentage bana kar one decimal dikhata hai: **80.9%**. Total bhi insert hota hai.
8. Next line transaction ID `int()` se whole number aur uska revenue insert karti hai: **1016**, **10,000**.
9. Next line outlier share `10000 / 14175` → **70.5%**, aur caveat/newlines add karti hai.
10. Next line peak date format aur `.max()` daily amount insert karti hai: **10,240.00**.
11. Next string second finding ka explanatory text hai; is particular line mein f-prefix hai magar placeholder nahi, is liye ordinary literal text jaisa output hai.
12. Next line same date ka total minus unusual sale: `10240 - 10000 = 240`. `.loc[date]` Series ki date label se lookup hai.
13. Last plain string sustained-trend claim se bachne ka interpretation hai. Closing `)` findings expression complete karta hai.
14. `print(findings)` notebook/terminal mein actual findings show karta hai.
15. `Path(...).write_text(...)` UTF-8 Markdown file save karta hai. `+` text concatenate karta hai; `\n` lines separate karta hai. `encoding='utf-8'` text encoding explicitly set karta hai.
16. `.to_csv('cleaned_sales.csv', index=False, date_format='%Y-%m-%d')`: Part A ka main output; extra index nahi; dates ISO-like year-month-day strings. CSV format actual Python datetime types preserve nahi karta.
17. Last `print` saved-file confirmation; real write previous line karti hai.

## 12. Part B: add tax aur update prices

```python
updated = pd.read_csv('cleaned_sales.csv')
updated['tax_amount'] = (updated['revenue'] * 0.05).round(2)
print('First five rows after adding tax:')
display(updated.head())

books = updated['category'].eq('Books')
updated.loc[books, 'unit_price'] = (updated.loc[books, 'unit_price'] * 1.10).round(2)
updated['revenue'] = (updated['quantity'] * updated['unit_price']).round(2)
updated['tax_amount'] = (updated['revenue'] * 0.05).round(2)
print('Books after the 10% price increase:')
display(updated.loc[books])
```

1. Actual Part A saved CSV reload hoti hai; sirf memory ka `clean.copy()` use nahi kiya. Brief ne CSV read karna maanga tha. Dates yahan default strings read hoti hain; Part B ko date arithmetic nahi chahiye.
2. Naya column `tax_amount`; `0.05 = 5/100`; revenue × 5%, two decimals. Tax revenue ka 5% hai, unit_price ka nahi.
3. Label print.
4. `head()` pehli 5 rows with initial tax show karta hai.
5. `books` Boolean mask: category exact `Books` ho to True. Part A case standardization ki wajah se original `books` bhi match hota hai.
6. `.loc[books, 'unit_price']`: Rows filter + specific column select. Right side old price × **1.10**, yani old 100% + 10% increase. Assignment same selected cells update karta hai. Non-Books prices unchanged rehti hain.
7. Revenue updated price se recalculate hota hai. Sirf price change karke old revenue chhorna inconsistent hota.
8. Tax new revenue se recalculate hota hai; old tax ab Books ke liye correct nahi rehta.
9. Label.
10. Updated Books rows display. Abhi transaction 1002 bhi maujood hai; deletion next step mein hoti hai.

Example transaction **1005**:

```text
Part A: quantity 2; price 250; revenue 500
Part B updated price: 250 * 1.10 = 275
Updated revenue: 2 * 275 = 550
Updated tax: 550 * 0.05 = 27.50
```

Har run Part A ko raw CSV se recreate aur Part B ko fresh cleaned output se start karta hai; repeated full runs Books price ko 10% compounded increase nahi dete.

## 13. Part B: row aur column remove; save/reload

```python
selected_id = 1002
assert updated['transaction_id'].eq(selected_id).sum() == 1
updated = updated.drop(index=updated.index[updated['transaction_id'].eq(selected_id)])
updated['review_status'] = 'Reviewed'
print('Temporary columns:', updated.columns.tolist())
updated = updated.drop(columns=['review_status']).reset_index(drop=True)
updated.to_csv('sales_updated.csv', index=False)

verified = pd.read_csv('sales_updated.csv')
print('Saved file, first five rows:')
display(verified.head())
print('Final column names:', verified.columns.tolist())
print('Final shape:', verified.shape)
```

1. `selected_id = 1002`: Existing row choose ki; arbitrary deliberate demo choice. Is transaction ko invalid declare nahi kiya.
2. `assert ... == 1`: Check ke ID exactly ek row mein exist karti hai. False ho to `AssertionError` aur execution stop; wrong/missing selection silently pass nahi hoti.
3. `.eq(selected_id)` mask; `updated.index[mask]` matching row labels; `.drop(index=...)` un labels ki rows remove karta hai. Default returned DataFrame ko `updated` mein reassign kiya. Transaction ID ko row-number samajh kar `.drop(1002)` nahi kiya.
4. New `review_status` column; scalar `'Reviewed'` har remaining row mein broadcast hota hai. Yeh real manual review ka evidence nahi, temporary column-operation demo hai.
5. Column names print; temporary column is stage par list mein nazar aata hai.
6. `.drop(columns=['review_status'])` column removes; `.reset_index(drop=True)` row labels reset; assignment result retain karta hai. `.drop(index=...)` rows aur `.drop(columns=...)` columns handle karte hain.
7. Updated CSV new filename mein save hoti hai; cleaned file overwrite nahi hoti; `index=False` extra index avoid.
8. Saved file disk se reload karke `verified` table. In-memory values ke bajaye persisted file check hoti hai.
9. Label.
10. Saved output ki pehli 5 rows.
11. Final column names; review_status absent.
12. Final dimensions **(14, 8)**.

Final columns:

```text
transaction_id, sale_date, region, category,
quantity, unit_price, revenue, tax_amount
```

## 14. Verification cell: har assertion ka matlab

```python
# Verify the saved results and the requested manipulations.
pd.testing.assert_frame_equal(verified, updated)
assert len(clean) == before - duplicates_removed - rejected_count
assert not clean.isna().any().any() and not clean.duplicated().any()
assert not clean['transaction_id'].duplicated().any()
assert len(verified) == len(clean) - 1
assert selected_id not in verified['transaction_id'].values
assert 'review_status' not in verified.columns
pd.testing.assert_series_equal(verified['revenue'],
    (verified['quantity'] * verified['unit_price']).round(2), check_names=False)
pd.testing.assert_series_equal(verified['tax_amount'],
    (verified['revenue'] * 0.05).round(2), check_names=False)
original_books = clean.set_index('transaction_id').loc[
    verified.loc[verified['category'].eq('Books'), 'transaction_id'], 'unit_price']
assert (verified.loc[verified['category'].eq('Books'), 'unit_price'].to_numpy()
        == (original_books * 1.10).round(2).to_numpy()).all()
print('All output and manipulation checks passed.')
```

1. `# ...` comment cell ka purpose batata hai, execute nahi hota.
2. `pd.testing.assert_frame_equal`: Reloaded file ki table aur saved in-memory table equal hon; values, columns, index/types waghera library defaults ke mutabiq compare hote hain. Iska pass hona correct revenue formula ka alag proof nahi; formula checks neeche hain.
3. Row accounting: **15 == 21 − 1 − 5**.
4. `clean.isna().any().any()`: First `.any()` per column missing existence, second overall existence. `not` demands no missing. `clean.duplicated().any()` any exact duplicate; `not` demands none. `and` dono overall Boolean conditions ko join karta hai.
5. Transaction IDs ka separate duplicate check; complete-row duplicate test se stronger ID-specific check hai.
6. Exactly one row remove hui: **14 == 15 − 1**.
7. Selected ID final values mein nahi honi chahiye.
8. Temporary column final columns mein nahi hona chahiye.
9. Revenue Series ko independently quantity × updated price ke formula se compare karta hai. Next line statement ki continuation hai. `check_names=False` Series ke name difference ignore karta hai; formula/values ignore nahi.
10. Next two-line assertion tax ko revenue × 0.05 se compare karta hai, names ignore karke.
11. `clean.set_index('transaction_id')`: Original cleaned prices ko transaction-ID lookup ke liye indexed view banata hai. Existing `clean` variable overwrite nahi hota.
12. Continuation line surviving Books IDs verified file se leti hai; `.loc[IDs,'unit_price']` unhi IDs ki old prices same order mein select karta hai. Transaction 1002 already deleted hai is liye surviving IDs hi compare hote hain.
13. Last two-line `assert`: Surviving Books updated prices ko old prices × 1.10 se compare. `.to_numpy()` positional arrays deta hai taake different Series indexes ki automatic alignment comparison ko disturb na kare. `==` elementwise; `.all()` demands every comparison True.
14. Last `print` tabhi aata hai jab previous checks pass hon. Yeh universal guarantee nahi ke har possible future dataset valid hoga; current assertions ka success hai. Python `-O` optimization mode mein ordinary `assert` statements disable ho sakte hain, is liye normal run command use karein.

## 15. Verified results: kya output aaya?

| Check | Actual result |
|---|---|
| Raw shape | 21 rows × 6 columns |
| Exact duplicates | 1 |
| Invalid/incomplete rows after deduplication | 5 |
| Cleaned shape | 15 rows × 7 columns |
| Cleaned missing values | All columns zero |
| Cleaned revenue | 14,175.00 |
| Highest region | North, 11,470.00 (80.9%) |
| High-price transaction | 1016; revenue 10,000.00 (70.5% of total) |
| Highest daily revenue | October 8, 2026: 10,240.00 |
| Same day without transaction 1016 | 240.00 |
| Updated shape | 14 rows × 8 columns |
| Removed transaction | 1002 |
| Final temporary review column | Absent |
| Final test message | All output and manipulation checks passed. |

Verification ke waqt notebook code fresh execute karke CSV exports ko memory mein capture kiya gaya aur existing saved CSVs se compare kiya gaya; dono main output files aur dono summary CSVs match hui thin. Original Downloads CSV aur working raw CSV byte-for-byte identical mile. Is guide mein business results unhi calculations se liye gaye hain.

## 16. Har project file ka role

| File | Role |
|---|---|
| sales_raw.csv | Original supplied sales input |
| sales_assignment.ipynb | Main mandatory notebook: explanations, Part A/B code aur saved outputs |
| cleaned_sales.csv | Part A output |
| sales_updated.csv | Part B output |
| revenue_by_region.csv | Extra exported region summary |
| revenue_by_category.csv | Extra exported category summary |
| revenue_by_region.png | Bar chart |
| daily_revenue.png | Daily line chart |
| findings.md | Notebook run generate karta hai; standalone two findings |
| README.md | Running instructions aur submission details |
| requirements.txt | Runtime dependencies ki version ranges |
| run_assignment.py | Same notebook code terminal mein execute/show karta hai |
| build_assignment.py | Notebook construct, execute aur ZIP package karne ka helper |
| .gitignore | Local environment/cache files Git se exclude karta hai |
| ASSIGNMENT_EXPLAINED_ROMAN_URDU.md | Yeh separate learning guide |

Notebook Markdown cells explanatory text hain; executable Python cells alag hain. `.ipynb` internally JSON document hai jisme cells, metadata aur outputs store hote hain. Notebook submit karna brief ki requirement hai, chahe aap personally terminal use karein.

## 17. Terminal runner: pehle pseudocode

```text
Script ke folder mein working directory set karo.
Matplotlib ko screen window ke baghair chart save karne wala backend do.
Notebook JSON read karo.
Display ko temporarily terminal printer se replace karo.
Har code cell order mein same shared namespace mein execute karo.
Markdown cells skip karo.
Charts ki windows suppress karo; PNG saves chalti rahen.
End par figures close aur success message show karo.
```

## 18. run_assignment.py: har line/statement

```python
"""Run the notebook's code cells and show results in the terminal."""
import json
import os
from pathlib import Path
from unittest.mock import patch
```

1. Triple-quoted first text module docstring hai: script ka purpose describe karta hai.
2. `json`: Notebook JSON ko Python dictionary/list mein parse karta hai.
3. `os`: Current directory/environment handle.
4. `Path`: Script aur notebook paths.
5. `patch`: Temporary function replacement ka context manager. Naam `unittest.mock` hone ke bawajood yahan sirf test nahi, display adaptation ke liye use hai. Context finish par original functions restore ho jate hain.

```python
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
os.environ.setdefault('MPLCONFIGDIR', str(ROOT / '.jupyter' / 'matplotlib'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

1. `__file__` running script filename; `Path(...)` path object; `.resolve()` absolute resolved path; `.parent` containing folder. `ROOT` script directory hai.
2. `os.chdir(ROOT)` process ki working directory badalta hai taake relative CSV paths script ke folder se resolve hon, chahe command doosre folder se chalai ho.
3. `os.environ` environment-variable mapping. `.setdefault(...)` MPL config directory tab set karta hai jab pehle set na ho. `ROOT / ...` Path joining hai, numeric division nahi. `str` path ko text banata hai. Workspace-local chart config/cache location milti hai.
4. Matplotlib package import.
5. `.use('Agg')` noninteractive rendering backend choose: chart PNG bana sakta hai, desktop graph window nahi kholta. Pyplot import se pehle backend select kiya.
6. Pyplot module alias; figures/show/close functions.

```python
def terminal_display(*objects, **kwargs):
    for obj in objects:
        print(obj.to_string(index=False) if hasattr(obj, 'to_string') else obj)
        print()
```

1. Function definition. `*objects` multiple positional display arguments tuple mein leta hai. `**kwargs` keyword arguments accept karta hai; is helper mein use nahi kiye.
2. Har supplied object par loop.
3. `hasattr(obj,'to_string')` check ke printable table conversion supported hai. True ho to `.to_string(index=False)` readable table without row index, warna object directly print. `A if condition else B` conditional expression hai. Actual object/data modify nahi hota.
4. Empty `print()` table ke baad blank line.

```python
def main():
    notebook = json.loads((ROOT / 'sales_assignment.ipynb').read_text(encoding='utf-8'))
    namespace = {'__name__': '__main__'}
    step = 0
    with patch('IPython.display.display', terminal_display), patch.object(plt, 'show', lambda: None):
        for cell in notebook['cells']:
            if cell['cell_type'] != 'code':
                continue
            step += 1
            print(f'\n========== Step {step} ==========\n')
            source = cell['source']
            exec(compile(''.join(source) if isinstance(source, list) else source,
                         f'notebook_step_{step}', 'exec'), namespace)
    plt.close('all')
    print('\nSUCCESS: Both parts completed. CSV files and charts were regenerated.')

if __name__ == '__main__':
    main()
```

1. `def main()` main workflow function banata hai; define karna execute karna nahi.
2. Path notebook file ka text read karta hai; `json.loads` parsed dictionary return karta hai. Notebook absent ho to runner fail karega; yeh independent duplicate analysis script nahi.
3. `namespace` shared variables dictionary. Har cell same dictionary mein run hota hai, is liye first cell ka `raw` next cells use kar sakte hain. `__name__` execution context set hai.
4. Step counter zero se start.
5. `with` context manager temporary patches active karta hai: notebook ka imported `display` terminal printer ban jata hai; `.show()` zero-argument `lambda: None` ban kar windows suppress karta hai. `None` no meaningful result hai. `savefig` patch nahi hua, is liye images save hoti hain.
6. Parsed notebook ki cell list par loop.
7. `!= 'code'`: Markdown/other cells code nahi.
8. `continue` current cell skip karke next loop iteration par jata hai. Is se Markdown Python samajh kar execute nahi hoti.
9. `step += 1` counter increment, same as `step = step + 1`.
10. F-string heading aur blank lines print.
11. Current cell ka source retrieve.
12. `isinstance(source,list)` format check; JSON source list ho to `''.join(source)` all fragments concatenate; already string ho to same source. `compile(..., label, 'exec')` Python code object banata hai; next physical line filename-style label `notebook_step_N` aur statement mode provide karti hai. Yeh label traceback mein help karta hai, actual new file create nahi karta.
13. Outer `exec(..., namespace)` compiled statements execute karta hai; variables shared dictionary mein rehte hain. Yeh aapke apne trusted assignment notebook ko run karne ke liye hai; arbitrary untrusted notebook run karna safe sandboxing nahi.
14. `plt.close('all')` open figure objects release karta hai, PNG files delete nahi.
15. Final success print. Runner CSVs/charts/findings regenerate karta hai; notebook ke saved cell outputs aur ZIP update nahi karta.
16. `if __name__ == '__main__'`: Direct script run hui ho to condition True; import hui ho to normal module name hota hai.
17. `main()` actual runner workflow call.

## 19. build_assignment.py: task aur pseudocode

Yeh support/build helper hai, data analysis ka alag source nahi. Is mein notebook cells ka code strings ki form mein stored hai. Isne notebook construct karke execute aur archive banana tha.

```text
Notebook helper libraries import karo.
Script directory select karo.
Markdown/code cells ki empty list banao.
Har explanation ko Markdown cell; har analysis block ko code cell banao.
Cell list se notebook object banao.
Current Python interpreter ke liye local kernel spec likho.
Jupyter/Matplotlib folders workspace mein point karo.
Notebook execute karo, outputs ke saath .ipynb save karo.
Required output filenames collect karo aur ZIP mein write karo.
```

### Imports aur helper functions

```python
from pathlib import Path
import json
import os
import sys
import nbformat as nbf
from nbclient import NotebookClient
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
cells = []

def md(text):
    cells.append(nbf.v4.new_markdown_cell(text))

def code(text):
    cells.append(nbf.v4.new_code_cell(text))
```

1. `Path` file/folder handling.
2. `json` kernel configuration serialize karta hai.
3. `os` working directory/environment settings.
4. `sys` current Python interpreter path provide karta hai.
5. `nbformat as nbf` Jupyter notebook structure construct/save karne ki library. Main notebook ke CSV analysis ke liye yeh library import nahi hoti; builder ke liye hai.
6. `NotebookClient` class import; notebook execution manage karta hai. Yeh custom student-defined class nahi.
7. `ROOT` script folder; same Path chain runner mein explain hui.
8. Working directory set.
9. `cells = []` empty ordered Python list; notebook cells yahan collect hongi.
10. `def md(text)` helper definition.
11. `nbf.v4.new_markdown_cell(text)` notebook format version 4 ka Markdown cell object; `.append(...)` list ke end par add.
12. `def code(text)` executable-cell helper.
13. `new_code_cell(text)` executable code ka cell object; list mein append.

### Beech ke md(...) aur code(...) blocks

Builder ke har `md('''...''')` block mein headings/cleaning explanation hai. Har `code('''...''')` block mein upar sections 6–14 wala exact analysis code hai, isi order mein:

| Builder block | Content | Har code line ki explanation |
|---|---|---|
| First `md(...)` | Title, Part A, date/currency notes | Sections 1–3 |
| First `code(...)` | Imports, raw CSV inspection | Section 6 |
| Cleaning `md(...)` | Cleaning choices | Section 7 |
| Second `code(...)` | Cleaning/revenue | Section 7 |
| Third `code(...)` | Group summaries | Section 8 |
| Fourth `code(...)` | Both charts | Sections 9–10 |
| Fifth `code(...)` | Findings/cleaned export | Section 11 |
| Part B `md(...)` | Part B instructions/selected ID | Sections 12–13 |
| Sixth `code(...)` | Tax/update/delete/save | Sections 12–13 |
| Seventh `code(...)` | Assertions | Section 14 |

Triple quotes ke andar code builder ke point of view se **text** hai. `code(...)` call us text ko notebook cell banati hai; actual execution baad mein `NotebookClient.execute()` karta hai. Is liye nested analysis lines ko duplicate explanation ke bajaye upar individually explain kiya gaya hai. Text-string construction mein `\\n` likhna generated cell ke source mein `\n` rakhne ke liye hota hai; generated cell execute hone par new line banti hai.

### Notebook object aur kernel specification

```python
nb = nbf.v4.new_notebook(cells=cells, metadata={'kernelspec': {
    'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}})
kernel_dir = ROOT / '.jupyter' / 'kernels' / 'assignment'
kernel_dir.mkdir(parents=True, exist_ok=True)
(kernel_dir / 'kernel.json').write_text(json.dumps({
    'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
    'display_name': 'Assignment', 'language': 'python'}))
```

1. `nbf.v4.new_notebook` collected cells se notebook object banata hai; `metadata` dictionary runtime/editor information deti hai.
2. Continuation line: display label Python 3, language python, standard kernel name python3. Saved notebook ko doosre environments mein open karne mein help.
3. `kernel_dir` local custom kernel configuration path.
4. `.mkdir(parents=True, exist_ok=True)` missing parent directories bhi create; already directory ho to sirf us wajah se error nahi.
5. `kernel.json` path aur `.write_text(json.dumps(...))`: Python dictionary ko JSON text banakar config save. Next do lines isi statement ke inputs hain.
6. `argv` kernel launch command list. `sys.executable` current `.venv` Python; `-m ipykernel_launcher` module run; `-f` connection file argument; `{connection_file}` kernel manager replace karta hai. Yeh f-string nahi, template string hai.
7. `display_name='Assignment'` custom kernel label; language python. Final braces/parentheses dictionary aur calls close karti hain.

Kernel ka matlab Python process hai jo notebook cells execute karta hai. Notebook editor aur kernel different cheezen hain; builder background kernel use karta hai, aapko Jupyter browser interface kholna zaroori nahi.

### Environment settings aur execution

```python
os.environ['JUPYTER_PATH'] = str(ROOT / '.jupyter')
os.environ['IPYTHONDIR'] = str(ROOT / '.jupyter' / 'ipython')
os.environ['JUPYTER_CONFIG_DIR'] = str(ROOT / '.jupyter' / 'config')
os.environ['MPLCONFIGDIR'] = str(ROOT / '.jupyter' / 'matplotlib')
os.environ['JUPYTER_RUNTIME_DIR'] = str(ROOT / '.jupyter' / 'runtime')
NotebookClient(nb, timeout=180, kernel_name='assignment', resources={'metadata': {'path': str(ROOT)}}).execute()
nbf.write(nb, ROOT / 'sales_assignment.ipynb')
```

1. `JUPYTER_PATH` local data/kernel discovery location add karta hai.
2. `IPYTHONDIR` IPython working config/profile data ki local location.
3. `JUPYTER_CONFIG_DIR` Jupyter config location.
4. `MPLCONFIGDIR` Matplotlib config/cache location.
5. `JUPYTER_RUNTIME_DIR` runtime/connection-related files ki location. Yeh environment settings analysis formulas ko nahi badaltin.
6. `NotebookClient(...)` object create; `nb` notebook input; `timeout=180` code-cell execution time limit seconds mein; `kernel_name='assignment'` local selected kernel; resources metadata path working directory. `.execute()` cells order mein run karke notebook outputs populate karta hai.
7. `nbf.write(...)` executed notebook ko .ipynb format mein save karta hai.

### ZIP packaging

```python
files = ['sales_assignment.ipynb', 'sales_raw.csv', 'cleaned_sales.csv', 'sales_updated.csv',
         'revenue_by_region.png', 'daily_revenue.png', 'revenue_by_region.csv',
         'revenue_by_category.csv', 'findings.md', 'README.md', 'requirements.txt']
with zipfile.ZipFile('StudentName_TrainingID.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for name in files:
        archive.write(ROOT / name, arcname=name)
print('Executed notebook and created StudentName_TrainingID.zip')
```

1. `files = [...]` archive mein include hone wale filenames ki ordered list; three physical lines ek statement. Learning guide aur terminal runner is current list mein include nahi hain. Notebook submission minimum cover karne ke liye terminal runner required nahi.
2. `ZipFile` class archive object kholta hai; `'w'` write mode existing same-name ZIP replace kar sakta hai; `ZIP_DEFLATED` compression. `with ... as archive` context manager end par archive properly close karta hai.
3. Har selected filename par loop.
4. `.write(ROOT/name, arcname=name)` local file archive mein copy; `arcname` plain filename rakhta hai, personal absolute folder path nahi.
5. Final confirmation successful preceding operations ke baad.

**Current builder file ka verified issue:** Is guide banane ke waqt `build_assignment.py` mein `import zipfile` line maujood nahi thi, jabke neeche `zipfile.ZipFile` use ho raha hai. Is exact current version ko run karne par packaging line par `NameError` aa sakta hai. Isko sahi karne ke liye imports mein `import zipfile` hona chahiye. Yeh guide actual code explain karti hai; is request mein builder change nahi kiya gaya. Main notebook aur `run_assignment.py` ko `zipfile` ki zaroorat nahi. Pehle ke successful run ko current file ke identical hone ka proof nahi maana gaya.

## 20. requirements.txt aur .gitignore

Current requirements:

```text
pandas>=2.2,<4
matplotlib>=3.9,<4
ipykernel>=6,<8
```

- First line Pandas 2.2 ya newer, major version 4 se pehle.
- Second Matplotlib 3.9 ya newer, 4 se pehle.
- Third ipykernel 6 ya newer, 8 se pehle. IPython/IPython display is dependency chain ke through available hota hai.
- Yeh version ranges hain, exact installed-version lock nahi.
- Builder ke liye **nbformat aur nbclient bhi chahiye**; current requirements mein woh explicitly listed nahi. Local environment mein installed hain. Notebook/terminal analysis chalana aur notebook builder chalana different dependency scopes hain.
- `pypdf` sirf provided PDF inspect karne ke liye environment mein install hua tha; main analysis ko PDF read karne ki zaroorat nahi.

`.gitignore` ki har line:

| Pattern | Kyun ignore? |
|---|---|
| `.venv/` | Local Python environment; bahut saari machine-specific dependencies |
| `.uv-cache/` | Package manager download/build cache |
| `.jupyter/` | Local kernel/config/runtime/cache data |
| `__pycache__/` | Python auto-generated bytecode cache |
| `.ipynb_checkpoints/` | Notebook editor ke auto-checkpoints |

Gitignore input/output assignment CSVs ko ignore nahi karta; woh repository mein aa sakte hain. Gitignore already-tracked file ko automatically untrack nahi karta.

## 21. Khud kaise run aur manually verify karein?

Windows CMD mein project folder par:

```cmd
.venv\Scripts\activate.bat
python run_assignment.py
```

Activation project environment ka Python select karti hai. Runner same main notebook code terminal par execute karta hai. Last output:

```text
All output and manipulation checks passed.
SUCCESS: Both parts completed. CSV files and charts were regenerated.
```

Manual verification:

1. Raw file ki original rows compare: 21 data rows, header extra. Duplicate 1003 twice.
2. Cleaned file mein 1006, 1010, 1011, 1013, 1014 absent; 1003 once.
3. Transaction 1018 region Unknown; text `Food`, `Books`, `South` standardized.
4. Transaction 1001 revenue 240; updated tax 12.
5. Books 1005 updated price 275, revenue 550, tax 27.50.
6. Updated file mein 1002 absent aur review_status absent.
7. PNGs open karke labels, North bar aur October 8 spike dekhein.
8. Cleaned revenue sum 14,175 verify karein; high-price sale ki wajah findings ke saath samjhein.

`run_assignment.py` notebook outputs ko .ipynb ke andar rewrite nahi karta aur ZIP nahi banata. Code/edit ke baad notebook ke embedded saved results refresh karne ke liye notebook execution/save ya working builder workflow chahiye.

## 22. Submission aur limitations ki clear distinction

Technical analysis complete hona aur submission ready hona alag checks hain. Last inspection mein README ka training ID/GitHub URL placeholder tha aur folder mein ZIP nahi thi. Yeh file un details ko assume karke fill nahi karti. Actual name/training ID, repository URL aur portal deadline aapko apni information se confirm karni hain.

Current solution small supplied dataset ke liye hai. `unusual` selection exact price 10,000 aur chart month label October 2026 par depend karte hain. Fractional quantities ke liye integer cast reconsider karna hoga. Monetary amounts floating-point + rounding se handle hue, production accounting ke Decimal/minor-unit design se nahi. Brief ke beginner-level scope mein SQL, Streamlit, machine learning, database ya custom business classes required nahi the aur implement nahi kiye.

## 23. Viva mein simple jawab

**Data kahan se aaya?** `pd.read_csv('sales_raw.csv')` se provided input read hua. Part B `cleaned_sales.csv` read karta hai.

**Cleaning kyun?** Missing/invalid amounts reliable revenue calculation rok sakte hain; duplicates double-count karte hain; text inconsistencies same category ko separate groups bana deti hain.

**Revenue kya?** Quantity × unit price; profit nahi.

**Unknown kyun?** Valid sale retain karni thi, unknown region invent nahi karna tha.

**High price kyun retain?** Error prove nahi hua aur correct value source mein nahi; influence explicitly disclose kiya.

**.loc kyun?** Condition-matching rows ke specific column ko safely/directly update karna tha aur brief ne explicitly .loc maanga.

**Tax dobara kyun?** Price change se revenue badla; tax usi new revenue ka 5% hona chahiye.

**index=False kyun?** Internal DataFrame row labels ko unwanted CSV column nahi banana.

**CSV reload kyun?** Disk par saved actual output verify karna, sirf memory table nahi.

**Notebook aur terminal script dono kyun?** Notebook brief ki submission requirement; terminal script aapki preferred execution/display convenience. Same analysis code notebook se run hota hai.

**Sabse important finding?** North 80.9% revenue lead karta hai, lekin ek 10,000 sale total ka 70.5% hai. Is liye apparent lead aur daily spike ko high-price record verify kiye baghair business growth ka proof nahi kehna chahiye.
