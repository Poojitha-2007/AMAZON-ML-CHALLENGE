import pandas as pd
from pathlib import Path

from preprocessing import normalize_name, normalize_address


# Dataset location
DATASET_ROOT = Path(
    r"C:\Users\pooji\Downloads\6ab10eb3b23ba_student_resource\student_resource\dataset"
)

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Output folder
OUTPUT_FOLDER = PROJECT_ROOT / "processed"
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


# Process all three training source files
for source in ["source1", "source2", "source3"]:

    input_file = DATASET_ROOT / "train" / f"train_{source}.tsv"
    output_file = OUTPUT_FOLDER / f"train_{source}_clean.tsv"

    print("\n========================================")
    print(f"Processing {source.upper()}")
    print("========================================")

    print("Reading:", input_file)

    # Read TSV
    df = pd.read_csv(input_file, sep="\t")

    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    # Normalize business name
    df["business_name_clean"] = df["business_name"].apply(
        normalize_name
    )

    # Normalize business address
    df["business_address_clean"] = df["business_address"].apply(
        normalize_address
    )

    # Save cleaned data
    df.to_csv(output_file, sep="\t", index=False)

    print("Preprocessing completed!")
    print("Saved to:", output_file)

    # Show sample
    print("\nSample results:")

    print(
        df[
            [
                "business_name",
                "business_name_clean",
                "business_address",
                "business_address_clean",
            ]
        ].head()
    )

print("\n========================================")
print("ALL THREE SOURCES PROCESSED SUCCESSFULLY!")
print("========================================")