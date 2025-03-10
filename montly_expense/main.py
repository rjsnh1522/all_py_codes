import pdfplumber
import pandas as pd


def main():

    pdf_file = "input/february.pdf"
    excel_file = "output/february.xlsx"

    with pdfplumber.open(pdf_file) as pdf:
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)



    # Merge all DataFrames into a single DataFrame
    combined_df = pd.concat(all_tables, ignore_index=True)

    # Save to Excel (one sheet)
    combined_df.to_excel(excel_file, sheet_name="All_Data", index=False)

    print(f"Conversion completed! Saved as {excel_file}")




if __name__ == "__main__":
    main()
