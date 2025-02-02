import pdfplumber
import pandas as pd


def main():

    pdf_file = "input/january.pdf"
    excel_file = "output/january.xlsx"

    with pdfplumber.open(pdf_file) as pdf:
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table)
                all_tables.append(df)

    # Save to Excel
    with pd.ExcelWriter(excel_file) as writer:
        for idx, df in enumerate(all_tables):
            df.to_excel(writer, sheet_name=f"Page_{idx+1}", index=False)

    print(f"Conversion completed! Saved as {excel_file}")



if __name__ == "__main__":
    main()
