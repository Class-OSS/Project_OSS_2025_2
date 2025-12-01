import csv
from datetime import datetime

def budget_as_csv(records, file_name=None):
    if not file_name:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        file_name = f"OSS_budget_export_{timestamp}.csv"

    if not records:
        return "No data. CSV export canceled."

    headers = ["category", "description", "amount"]

    value = []   
    for item in records:
        value.append([item.category, item.description, item.amount])

    final_rows = [headers] + value

    with open(file_name, "w", encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(final_rows)

    return f"CSV file created: {file_name}"
