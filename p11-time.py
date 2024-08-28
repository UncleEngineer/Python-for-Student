"""
11- เขียนโปรแกรมแปลงเวลาจาก 24 ชั่วโมงเป็น A.M. หรือ P.M. เช่น กรอกตัวเลข 18.15 น. แปลงเป็น 6.15 P.M.
"""

text_time = input('กรุณากรอกเวลา เช่น 12.15 : ')

H,M = text_time.split('.')

cal = int(H) - 12 

if cal > 0:
    timetype = 'P.M.'
elif cal < 0:
    timetype = 'A.M.'
elif cal == 0 and M == '00' and H != '12':
    timetype = 'A.M.'
elif cal == 0 and int(M) > 0:
    timetype = 'P.M.'
elif H == '12' and M == '00':
    timetype = 'P.M.'
else:
    pass

if int(H) >= 12:
    print('เวลา: {}.{} {}'.format(cal,M,timetype))
else:
    print('เวลา: {} {}'.format(text_time,timetype))
