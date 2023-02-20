from barcode import UPCA
from barcode.writer import ImageWriter
  
# Make sure to pass the number as string
system_digit = '0'
company_number = '95511'
color_code = 1

number = f'{system_digit}{company_number}0250{color_code}'
my_code = UPCA(number, writer=ImageWriter())
my_code.save(f"{color_code}Marie-Lou025")