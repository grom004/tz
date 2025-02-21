import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_excel("data.xlsx")

# Преобразуем даты, игнорируя ошибки
df["receiving_date"] = pd.to_datetime(df["receiving_date"], format="%d.%m.%Y", errors='coerce')

# Заполняем пропуски в числовых столбцах
if "sum" in df.columns:
    df["sum"] = pd.to_numeric(df["sum"], errors='coerce').fillna(0)

# 1. Выручка за июль 2021 без просроченных сделок
july_revenue = df[(df["receiving_date"].notna()) &
                  (df["receiving_date"].dt.month == 7) &
                  (df["receiving_date"].dt.year == 2021) &
                  (df["status"] != "ПРОСРОЧЕНО")]["sum"].sum()
print(f"Выручка за июль 2021: {july_revenue}")

# 2. Динамика выручки по месяцам
if df["receiving_date"].notna().any():
    monthly_revenue = df.groupby(df["receiving_date"].dt.to_period("M"))["sum"].sum()
    if not monthly_revenue.empty:
        monthly_revenue.plot(kind="line", marker="o", title="Динамика выручки")
        plt.xlabel("Месяц")
        plt.ylabel("Выручка")
        plt.grid()
        plt.show()
    else:
        print("Нет данных для построения графика.")

# 3. Менеджер с наибольшей выручкой в сентябре 2021
september_sales = df[(df["receiving_date"].notna()) &
                     (df["receiving_date"].dt.month == 9) &
                     (df["receiving_date"].dt.year == 2021)]
if not september_sales.empty:
    best_manager = september_sales.groupby("sale")["sum"].sum()
    if not best_manager.empty:
        print(f"Лучший менеджер в сентябре 2021: {best_manager.idxmax()}")
    else:
        print("Нет данных по продажам за сентябрь 2021.")
else:
    print("Нет данных по продажам за сентябрь 2021.")

# 4. Преобладающий тип сделки в октябре 2021
october_deals = df[(df["receiving_date"].notna()) &
                   (df["receiving_date"].dt.month == 10) &
                   (df["receiving_date"].dt.year == 2021)]["new/current"].value_counts(dropna=False)
if not october_deals.empty:
    main_deal_type = october_deals.idxmax()
    print(f"Преобладающий тип сделки в октябре 2021: {main_deal_type}")
else:
    print("Нет данных по сделкам за октябрь 2021.")

# 5. Количество оригиналов договоров по майским сделкам, полученных в июне 2021
may_deals = df[(df["receiving_date"].notna()) &
               (df["receiving_date"].dt.month == 6) &
               (df["receiving_date"].dt.year == 2021) &
               (df["document"] == "оригинал")]
print(f"Оригиналов договоров по майским сделкам в июне: {may_deals.shape[0]}")

# 6-8. Расчет бонусов

def calculate_bonus(row):
    if pd.isna(row["sum"]):
        return 0
    if row["new/current"] == "новая" and row["status"] == "ОПЛАЧЕНО" and row["document"] == "оригинал":
        return row["sum"] * 0.07
    elif row["new/current"] == "текущая" and row["status"] != "ПРОСРОЧЕНО" and row["document"] == "оригинал":
        return row["sum"] * (0.05 if row["sum"] > 10000 else 0.03)
    return 0

df["bonus"] = df.apply(calculate_bonus, axis=1)
manager_bonus = df.groupby("sale")["bonus"].sum()
print("Бонусы менеджеров:")
print(manager_bonus)

# 8. Остаток на 01.07.2021
june_pending = df[(df["receiving_date"].notna()) &
                  (df["receiving_date"].dt.year == 2021) &
                  (df["receiving_date"].dt.month > 6)]
if not june_pending.empty:
    manager_pending = june_pending.groupby("sale")["bonus"].sum()
    print("Остаток на 01.07.2021:")
    print(manager_pending)
else:
    print("Нет данных по остаткам на 01.07.2021.")

