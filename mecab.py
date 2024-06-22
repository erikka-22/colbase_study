import MeCab
# import csv
import pandas as pd

# with open('colbase_20240603_num_name_small.csv') as f:
#   reader = csv.reader(f)
#   l = [row for row in reader]

output = []
tagger = MeCab.Tagger("-Okana")

df = pd.read_csv('colbase_20240603_num_name_without_duplicate.csv')

for row in df.itertuples():
  id = row[0]
  output.append("JPS_ID:"+id)

  # tagger = MeCab.Tagger()
  # tagger = MeCab.Tagger("-Ounidic22")
  # tagger = MeCab.Tagger("-Overbose")
  # tagger = MeCab.Tagger("-Ochamame")
  # tagger = MeCab.Tagger("-Ochasen")

  # tagger = MeCab.Tagger('-d "{}"'.format(unidic.DICDIR))

  input = row[1]
  # input = "労務管理をめぐるトラブルと実践的解決法ケース別112"
  # input = "8月3日に放送された「中居正広の金曜日のスマイルたちへ」(TBS系)で、1日たった5分でぽっこりおなかを解消するというダイエット方法を紹介。キンタロー。のダイエットにも密着。"
  output.append(input+"\t\t[入力文]")

  input_yomi = row[2]
  output.append("\t"+input_yomi+"\t[入力 読み]")

  result = tagger.parse(input).split()

  hyoso = result[0:][::2] 
  yomi = result[1:][::2]

  # print(hyoso)
  # print(yomi)

  for i in range(len(yomi)):
    output_row = hyoso[i] + "\t" + yomi[i] + "\n"
    output.append(output_row)


w_file = "result.txt"
with open(w_file, "w", encoding="utf_8") as f:
  f.write("\n".join(output))