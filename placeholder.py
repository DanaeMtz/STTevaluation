import pandas as pd
from sttevaluator.preprocessing import preprocessing
import re 

def main():
    # read the data 
    df = pd.read_csv("data/transcripts.csv", encoding="utf-8")
    #df = df.iloc[:61, :] # numbers 
    df = df.iloc[61:, :] # general corpus 
    # nuance = df.loc[:, "nuance"].tolist()
    microsoft = df.loc[:, "microsoft"].tolist()
    # reference = df.loc[:, "reference"].tolist()
    # print(nuance[2])
    # print([re.findall(r"\d+\s\d{3}\s\$",sentence) for sentence in nuance])

    # nuance_new = re.sub(r"(?P<thousands>\d+)\s(?P<hundreds>\d{3}\s\$)", "\g<thousands>\g<hundreds>", nuance[2])
    # print(nuance_new)

    # print(reference[2])
    # print(preprocessing(nuance[2]))
    print([re.findall(r"celi|céli|reer|réer|nip|bnc|ferr",sentence) for sentence in microsoft])

if __name__ == '__main__':
    main()