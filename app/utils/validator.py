"""
In python3, [0-9] is not equivalent to \\d,
[0-9] matches only 0123456789 characters,
while \\d matches [0-9] and other digit characters,
for example, Eastern Arabic numerals ٠١٢٣٤٥٦٧٨٩.
So we use [0-9] for phone number validation here.
"""
cellphone_number_regex = r'^09+([0-9]{8})$'
telephone_number_regex = r'^(?=([0-9]{2,4}\-[0-9]{6,8})).{10,11}$'
email_regex = r'^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+$'
order_id_regex = r'^[2-9][0-9]{7}[0-9a-zA-Z]{6}$'
