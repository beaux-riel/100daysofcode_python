from barcode import UPCA
from barcode.writer import ImageWriter
  
# Make sure to pass the number as string
system_digit = '0'
company_number = '95511'
color_code = 1

# Initialize counter variables
product_counter = 0
color_counter = 0
  
# Now, let's create an object of UPCA class and pass the number
for product in range(0,100):

    product_counter += 1
    color_counter += 1
    
    if color_counter % 25 == 0:
        color_code += 1
        color_counter = 0
        product_counter = 1
        
    if product_counter < 10:
        product_code = f'00{product_counter}'
    else:
        product_code = f'0{product_counter}'
    
    number = f'{system_digit}{company_number}{product_code}0{color_code}'
    my_code = UPCA(number, writer=ImageWriter())
    my_code.save(f"{color_code}Marie-Lou{product_code}")
  
  
# from barcode import UPCA

# # Make sure to pass the number as string
# system_digit = '0'
# company_number = '95511'
# color_code = 1

# # Now, let's create an object of UPCA class and pass the number
# for product in range(1, 5):
#     if (product - 1) % 25 == 0 and product != 1:
#         color_code += 1

#     if product < 10:
#         product_code = f'00{product}'
#     else:
#         product_code = f'0{product}'

#     number = f'{system_digit}{company_number}{product_code}0{color_code}'
#     my_code = UPCA(number)
#     my_code.save(f"marie_lou{product_code}")
