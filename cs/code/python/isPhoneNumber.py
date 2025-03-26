def isPhoneNumber(num):
    if len(num) != 12:
        return False
    for i in range(0, 3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
        return False
    for i in range(4, 7):
        if not num[i].isdecimal():
            return False
    if num[7] != '-':
        return False
    for i in range(8, 12):
        if not num[i].isdecimal():
            return False
    return True


num = '069-726-3764'
print(isPhoneNumber(num))
message = 'Is there a phone number contained in the text? 33vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;svE1231asdagbka;3vE1231asdagbka;s3vE1231asdagbka069-726-37643vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;s3vE1231asdagbka;ss'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
