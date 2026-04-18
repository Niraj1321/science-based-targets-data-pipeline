import pandas as pd
import json
import numpy as np

# 1. LOAD FILES
company_df = pd.read_excel("companies-excel.xlsx")
targets_df = pd.read_excel("targets-excel.xlsx")

# Normalize column names
company_df.columns = company_df.columns.str.strip().str.lower()
targets_df.columns = targets_df.columns.str.strip().str.lower()


# 2. REMOVE UNWANTED COMPANY COLUMNS
REMOVE_FROM_COMPANY = [
]

company_df = company_df.drop(
    columns=[c for c in REMOVE_FROM_COMPANY if c in company_df.columns],
    errors="ignore"
)


# 3. TARGET COLUMNS TO EXCLUDE FROM JSON (NOT DF)

EXCLUDE_FROM_TARGET_JSON = [
    "row_entry_id",
    "sbti_id",
    "company_name",
    "isin",
    "lei",
    "location",
    "region",
    "sector",
    "organization_type",
    "full_target_language",
]


# 4. JSON-SAFE CONVERSION
def make_json_safe(value):
    if pd.isna(value):
        return None
    if isinstance(value, (pd.Timestamp, np.datetime64)):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    return value


# 5. BUILD TARGET LIST PER COMPANY
targets_map = {}

for sbti_id, g in targets_df.groupby("sbti_id", dropna=True):
    target_list = []

    for _, row in g.iterrows():
        target_dict = {
            col: make_json_safe(row[col])
            for col in targets_df.columns
            if col not in EXCLUDE_FROM_TARGET_JSON
        }
        target_list.append(target_dict)

    targets_map[sbti_id] = json.dumps(
        target_list,
        ensure_ascii=False
    )


# 6. MERGE INTO COMPANY FILE
company_df["targets_commitments"] = company_df["sbti_id"].map(targets_map)


# 7. EXPORT FINAL FILE
company_df.to_excel(
    "output/sciencebasedtargets_data.xlsx",
    index=False
)

print("✅ SUCCESS")
print("Generated: sciencebasedtargets_data.xlsx")