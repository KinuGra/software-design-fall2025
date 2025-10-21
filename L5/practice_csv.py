import pandas as pd

file_path = "c01.csv"
df = pd.read_csv(file_path, encoding="shift-jis")

# 数字2桁の都道府県コードのみ（01〜47）
df = df[df["都道府県コード"].astype(str).str.match(r"^(0[1-9]|[1-4][0-7])$")]

# 人口（総数）を数値に変換（数値以外はNaNに）
df["人口（総数）"] = pd.to_numeric(df["人口（総数）"], errors="coerce")

# 都道府県ごとに合計
res_df = (
    df.groupby(["都道府県コード", "都道府県名"], as_index=False)["人口（総数）"]
    .sum()
    .rename(columns={"人口（総数）": "人口(総数)合計"})
)

# 整数化（欠損値がない前提ならこれでOK）
res_df["人口(総数)合計"] = res_df["人口(総数)合計"].astype(int)

# CSV出力（文字化け防止のためUTF-8-SIG推奨）
res_df.to_csv("test.csv", index=False, encoding="utf-8-sig")

print("✅ 正常に test.csv を出力しました。")
