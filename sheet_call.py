import gspread
gc=gspread.service_account(filename='Drive_api.json')
#sh=gc.open_by_key('1iiMJ0FinfpDwpKHBRlmYkq0zx3Tew2GEv-DNkBT_S5E')
sh=gc.open('Demo_data')
worksheet = sh.sheet1

res=worksheet.get_all_records()
print(res)
