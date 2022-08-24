from sttevaluator.preprocessing import preprocessing_all
from sttevaluator.tokenization import tokenize_all, clean_genesys_tokens
from sttevaluator.wer import compute_wer
import pandas as pd


def main():
    # read the data
    df = pd.read_csv("data/transcripts.csv", encoding="utf-8")
    # df = df.iloc[:61, :] # numbers
    df = df.iloc[61:, :]  # general corpus

    nuance = df.loc[:, "nuance"].tolist()
    genesys = df.loc[:, "genesys"].tolist()
    reference = df.loc[:, "reference"].tolist()
    microsoft = df.loc[:, "microsoft"].tolist()
    file_id = df.loc[:, "file_id"].tolist()
    # apply preprocessing
    referen_clean = list(map(preprocessing_all, reference))
    nuance_clean = list(map(preprocessing_all, nuance))
    genesys_clean = list(map(preprocessing_all, genesys))
    microsoft_clean = list(map(preprocessing_all, microsoft))

    # clean_transcriptions = pd.DataFrame(list(zip(file_id, referen_clean, nuance_clean, genesys_clean, microsoft_clean)),columns =["file_id", "reference", "nuance", "genesys", "microsoft"])
    # clean_transcriptions.to_csv("results/clean_transcriptions.csv", index=False, encoding='utf-8')

    # tokenization
    referen_tokens = list(map(tokenize_all, referen_clean))
    nuance_tokens = list(map(tokenize_all, nuance_clean))
    genesys_tokens = clean_genesys_tokens(list(map(tokenize_all, genesys_clean)))
    microsoft_tokens = list(map(tokenize_all, microsoft_clean))

    # compute wer
    wer_nuance, global_wer_nuance = compute_wer(referen_tokens, nuance_tokens)
    wer_genesys, global_wer_genesys = compute_wer(referen_tokens, genesys_tokens)
    wer_microsoft, global_wer_microsoft = compute_wer(referen_tokens, microsoft_tokens)

    wer_results = pd.DataFrame(
        list(
            zip(
                file_id,
                reference, 
                referen_clean,
                nuance, 
                nuance_clean,
                wer_nuance,
                genesys,
                genesys_clean,
                wer_genesys,
                microsoft, 
                microsoft_clean,
                wer_microsoft,
            )
        ),
        columns=[
            "file_id",
            "reference"
            "reference_clean",
            "nuance",
            "nuance_clean"
            "wer_nuance",
            "genesys",
            "genesys_clean"
            "wer_genesys",
            "microsoft",
            "microsoft_clean"
            "wer_microsoft",
        ],
    )
    wer_results.to_excel(
        "results/wer_results.xlsx", index=False, encoding="utf-8"
    )


if __name__ == "__main__":
    main()
