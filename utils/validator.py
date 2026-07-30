import pandas as pd

def validate(df):

    errors = []

    # Missing SKU
    missing_sku = df[df["SKU"].isna()]

    for i in missing_sku.index:
        errors.append({
            "Row": i+2,
            "Column":"SKU",
            "Error":"SKU Missing"
        })

    # Duplicate SKU
    duplicate = df[df["SKU"].duplicated()]

    for i in duplicate.index:
        errors.append({
            "Row": i+2,
            "Column":"SKU",
            "Error":"Duplicate SKU"
        })

    # Missing Brand
    missing_brand = df[df["Brand"].isna()]

    for i in missing_brand.index:
        errors.append({
            "Row": i+2,
            "Column":"Brand",
            "Error":"Brand Missing"
        })

    return pd.DataFrame(errors)
