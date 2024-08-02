from PyPDF2 import PdfReader
import pandas as pd

def extract_data(contact_no, name, address, shop_name, location):
    contact_no = []
    shop_name_list = []
    buyer_name = []
    buyer_address = []
    location_list = []

    for pdf_no in range(1,3):
        # Read the file
        file_name = f"{pdf_no}.pdf"
        reader = PdfReader(file_name)
        page = reader.pages[0]

        # Get the text
        text = page.extract_text().split("\n")

        # Get Contract No.
        index = [i+2 for i, x in enumerate(text) if x == "Contract No:"]
        contact_no.append(text[index[0]])

        # Get Shop Name
        shop_name_list.append(shop_name)

        # Get Buyer Name
        index = [i+1 for i, x in enumerate(text) if x == "Name:"]
        buyer_name.append(text[index[0]])

        # Get Buyer Address
        index = [i+1 for i, x in enumerate(text) if x == "Address:"]
        buyer_address.append(address)

        # Get Location
        location_list.append(location)

    data = pd.DataFrame({'Contract No.' : contact_no,
                                'Shop Name' : shop_name_list,
                                 'Buyer Name': buyer_name,
                                  'Buyer Address': buyer_address,
                                  'Location': location_list })
    data.to_excel("data.xlsx", index= False)

# Example usage:
extract_data('1234567890', 'John Doe', 'A.T Road, Opposite of Sanjeevani Hospital,KAMRUP, ASSAM-781011, India', 'My Shop', 'Kamrup')