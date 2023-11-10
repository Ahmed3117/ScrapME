import openpyxl

def read_excel_to_dict(file_path):
    try:
        # Load the Excel workbook
        workbook = openpyxl.load_workbook(file_path)
        # Select the first sheet (you may need to modify this if your data is in a different sheet)
        sheet = workbook.active
        # Create a dictionary from the first two columns
        result_dict = {}
        for row in sheet.iter_rows(min_row=1, max_col=2, values_only=True):
            value_list = []
            key, value = row
            value_list.append(key)
            if value == None:
                value_list.append('')
            else:
                value_list.append(value)
            result_dict[key] = value_list
        return result_dict
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

excel_file_path = 'C:/Users/SHHEKO/Downloads/datatest.xlsx'
result_dictionary = read_excel_to_dict(excel_file_path)
