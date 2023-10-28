import openpyxl
import requests
import os
# file_path = 'scraped_data.xlsx'
def downloadimages(file_path,start_code):
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook.active  # or specify a sheet by name: workbook['SheetName']
    column_to_extract = 'I'
    column_data = []

    for row in worksheet.iter_rows(values_only=True):
        cell_value = row[ord(column_to_extract) - ord('A')]
        links_list = cell_value.split('\n')
        links_list = [link.strip() for link in links_list if link.strip()]
        column_data.append(links_list)

    corrected_links_list = []
    for links_list in column_data:
        for link in links_list:
            # print(link)
            corrected_links = link.replace("[", "").replace("]", "").replace("'", "").split(',')
            corrected_links_list.append(corrected_links)
    # print(corrected_links_list)
    for link_group in corrected_links_list[1:] :
        counter = 0
        # download_folder = 'downloaded_images/' + str(corrected_links_list.index(link_group)+1)
        download_folder = os.path.dirname(file_path) +'/downloaded_images/' + str(start_code)
        
        os.makedirs(download_folder, exist_ok=True)
        for link in link_group:
            # sub_folder = download_folder + '/' + download_folder +  f"({link_group.index(link) +1 })"
            # os.makedirs(sub_folder, exist_ok=True)
            print(link)
            try:
                response = requests.get(link)
                
                filename = os.path.join(download_folder, str(start_code) + " " + '(' + str(counter +1) + ')' + ".jpg")
                # Save the image to the specified folder
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print(f"Image downloaded and saved as {filename}")
                counter+=1
            except:
                print("not valid" + link)

        start_code += 1



# downloadimages(file_path)