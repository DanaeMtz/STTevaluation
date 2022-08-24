import pandas as pd

def main():
    # read the data 
    df = pd.read_csv("data/transcripts.csv", encoding="utf-8")
    #df = df.iloc[:61, :] # numbers 
    df = df.iloc[61:, :] # general corpus 

    print(df.head())
    print(df.tail())

if __name__ == '__main__':
    main()