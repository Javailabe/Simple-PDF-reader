import os
import fitz
import pandas as pd
import extractors

def read_data(file):
    try:
        pdf_document = fitz.open(file)
        page_ref = pdf_document.load_page[0]
        text = page_ref.get_text()

        date_of_order = get_date_of_order(text)
        part_number = get_part_number(text)
        price = get_price(text)
        effective_date = get_effective_date(text)
        ship_from_code = get_ship_from_code(text)
        plant = get_plant(text)

        extracted_values = {
            "File name":file,
            "Date of order":date_of_order,
            "Part number":part_number,
            "Price":price,
            "Effective date":effective_date,
            "Ship from code":ship_from_code,
            "Plant":plant
        }
        pdf_document.close()
        return extracted_values
    except Exception as e:
        extracted_values = {
            "File name":f"Error in opening file {file}; {e}",
            "Date of order":f"Error in opening file {file}; {e}",
            "Part number":f"Error in opening file {file}; {e}",
            "Price":f"Error in opening file {file}; {e}",
            "Effective date":f"Error in opening file {file}; {e}",
            "Ship from code":f"Error in opening file {file}; {e}",
            "Plant":f"Error in opening file {file}; {e}"
        }
        pdf_document.close()
        return extracted_values

if __name__ == "__main__":
    extracted_data = []
    for pdf_file in os.listdir():
        if pdf_file.endswith((".PDF", ".pdf")):
            data_from_pdf_file = read_data(pdf_file)
            extracted_data.append(data_from_pdf_file)
    df = pd.DataFrame(extracted_data)
    print(df)
    df.to_excel("POs data.xlsx", index=False)