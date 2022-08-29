from sttevaluator.preprocessing import preprocessing_all
from sttevaluator.tokenization import tokenize_all, clean_genesys_tokens
from sttevaluator.wer import compute_wer
import pandas as pd


def main():
    # read the data
    df = pd.read_csv("data/transcripts_dlm.csv", encoding="utf-8")
    # df = df.iloc[:61, :] # numbers
    df = df.iloc[61:, :]  # general corpus

    nuance = df.loc[:, "nuance"].tolist()
    genesys = df.loc[:, "genesys"].tolist()
    reference = df.loc[:, "reference"].tolist()
    microsoft = df.loc[:, "microsoft"].tolist()
    microsoft_dlm = df.loc[:, "microsoft_dlm"].tolist()
    file_id = df.loc[:, "file_id"].tolist()
    # apply preprocessing
    referen_clean = list(map(preprocessing_all, reference))
    nuance_clean = list(map(preprocessing_all, nuance))
    genesys_clean = list(map(preprocessing_all, genesys))
    microsoft_clean = list(map(preprocessing_all, microsoft))
    microsoft_dlm_clean = list(map(preprocessing_all, microsoft_dlm))

    clean_transcriptions = pd.DataFrame(
        list(zip(file_id, referen_clean, nuance_clean, genesys_clean, microsoft_clean, microsoft_dlm_clean)),
        columns=["file_id", "reference", "nuance", "genesys", "microsoft", "microsoft_dlm"],
    )
    # clean_transcriptions.to_csv(
    #     "results/clean_transcriptions.csv", index=False, encoding="utf-8"
    # )

    # tokenization
    referen_tokens = list(map(tokenize_all, referen_clean))
    nuance_tokens = list(map(tokenize_all, nuance_clean))
    genesys_tokens = list(map(tokenize_all, genesys_clean))
    microsoft_tokens = list(map(tokenize_all, microsoft_clean))
    microsoft_dlm_tokens = list(map(tokenize_all, microsoft_dlm_clean))

    # compute wer
    wer_nuance, global_wer_nuance = compute_wer(referen_tokens, nuance_tokens)
    wer_genesys, global_wer_genesys = compute_wer(referen_tokens, genesys_tokens)
    wer_microsoft, global_wer_microsoft = compute_wer(referen_tokens, microsoft_tokens)
    wer_microsoft_dlm, global_wer_microsoft_dlm = compute_wer(referen_tokens, microsoft_dlm_tokens)

    df["wer_nuance"] = wer_nuance
    df["wer_genesys"] = wer_genesys
    df["wer_microsoft"] = wer_microsoft
    df["wer_microsoft_dlm"] = wer_microsoft_dlm

    df = df.reindex(
        columns=[
            "file_id",
            "reference",
            "nuance",
            "wer_nuance",
            "genesys",
            "wer_genesys",
            "microsoft",
            "wer_microsoft",
            "microsoft_dlm",
            "wer_microsoft_dlm"
        ]
    )

    df.to_excel("results/wer_corpusgen.xlsx", index=False, encoding="utf-8")


if __name__ == "__main__":
    main()
