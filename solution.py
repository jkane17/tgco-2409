
import pandas as pd
import requests
from typing import Any

def get_data(url : str, timeout=2) -> dict[str, list[dict[str, Any]]]:
    """Request data from server at given URL"""
    r = requests.get(url, timeout=timeout)
    if not r.ok: r.raise_for_status()
    return r.json()

def get_max_amount(invoices_df : pd.DataFrame) -> pd.DataFrame:
    """Returns rows from input df whose amount equals the maximum amount"""
    spent_df = invoices_df.groupby("customerId")["amount"].sum().reset_index()
    max_amount = spent_df["amount"].max()
    max_df = spent_df.loc[spent_df["amount"] == max_amount]
    return max_df

def get_customers_amounts(customers_df : pd.DataFrame, amounts_df : pd.DataFrame) -> pd.DataFrame:
    """Merge customer information with given amounts"""
    merged_df = pd.merge(
        right=customers_df,
        left=amounts_df,
        right_on="ID",
        left_on="customerId",
        how="inner"
    )

    return merged_df[["name", "surname", "amount"]]

def main():
    customers_url = "http://localhost:9090/"
    invoices_url = "http://localhost:9092/"

    customers = get_data(customers_url)["customers"]
    customers_df = pd.DataFrame(customers)

    invoices = get_data(invoices_url)["invoices"]
    invoices_df = pd.DataFrame(invoices)

    max_df = get_max_amount(invoices_df)
    merged_df = get_customers_amounts(customers_df, max_df)
    
    return merged_df

if __name__ == "__main__":
    result = main()
    print(result.to_string(index=False))
