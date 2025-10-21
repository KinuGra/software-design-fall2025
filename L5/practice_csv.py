import pandas as pd

file_path = "c01.csv"
df = pd.read_csv(file_path, encoding="shift-jis")

# 00〜47 以外のコードを除外（正規表現で数字2桁だけ残す）
df = df[df["都道府県コード"].str.match(r"^\d\d$")]

res_df = pd.DataFrame(columns=["都道府県名", "人口(総数)合計"])
for i in range(1, 48):
    code = f"{i: 02d}"
    res_df = pd.concat(
        [
            res_df,
            pd.DataFrame(
                {
                    "都道府県名": [df[df["都道府県コード"] == code].iloc[0][1]],
                    "人口(総数)合計": [
                        df[df["都道府県コード"] == i]["人口（総数）"].sum()
                    ],
                }
            ),
        ],
        ignore_index=True,
    )

res_df.to_csv("test.csv")
