import argparse
from process.df_to_model import df2model
parser = argparse.ArgumentParser()
parser.add_argument("--datapath", "-d", help="path to paper file (must be json)",type = str)
args = parser.parse_args()

df = df2model(args.datapath)

df.to_csv('./data/df_to_model.csv',index=False)
