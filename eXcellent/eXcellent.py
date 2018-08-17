import pandas as pd

headers = ["Category", "Brand", "Product_Name", "Shipping", "Price"]

xl = pd.ExcelFile("C:\\Users\\mmiller3\\Desktop\\products.xlsx")
df = xl.parse("products")
print(df)

df = df.sort_values(by=headers[4], axis='columns', na_position='last')

writer = pd.ExcelWriter('C:\\Users\\mmiller3\\Desktop\\output.xlsx')
df.to_excel(writer, sheet_name="Sheet1", columns=headers, index=False)
writer.save()

print("Done")

