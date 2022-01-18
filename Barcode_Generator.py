from barcode import Code128

username = 'Username'
password = 'dasIstMeinPasswort'

my_code = Code128(username + ' ' + password)

my_code.save('barcode')
