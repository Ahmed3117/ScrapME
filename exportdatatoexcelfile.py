from openpyxl import Workbook
from scrapdata import scrapurl

def storescrapeddatatoexcel(urls,download_path):
    workbook = Workbook()
    sheet = workbook.active

    sheet['A1'] = 'urls'
    sheet['B1'] = 'Price'
    sheet['C1'] = 'Description'
    sheet['D1'] = 'images'

    for row, url in enumerate(urls, start=2):
        data = scrapurl(url)
        sheet.cell(row=row, column=1).value = data[0]
        sheet.cell(row=row, column=2).value = data[1]
        sheet.cell(row=row, column=3).value = data[2]
        sheet.cell(row=row, column=4).value = data[3]

    workbook.save(download_path + '/scraped_data.xlsx')

    print("done")

