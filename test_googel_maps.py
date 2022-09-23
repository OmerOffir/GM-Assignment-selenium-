from Google_map import *


def test_maion_code():
    cities, zoom_num = load_csv()
    for ct,zn in zip(cities, zoom_num):
        print(colors.purple,f'----------------------{ct}-------------------------',colors.end)
        log_pdf(f'----------------------{ct}-------------------------')
        searchplace(ct)
        zoom_in(zn, ct)
        zoom_out(zn, ct)
    pdf.output("URL_list.pdf")                                                    # output file
    driver.close()
