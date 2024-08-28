'''
12- เขียนโปรแกรมให้ลานจอดรถของห้าง โดย 2 ชั่วโมงแรกจอดฟรี 
ชั่วโมงที่ 3-6 ชั่วโมงละ 20 บาท ชั่วโมงที่ 7 เป็นต้นไปชั่วโมงละ 40 บาท 
ถ้าจอดเกิน 15 นาทีให้นับเป็น 1 ชั่วโมง 
โดยให้ผู้ใช้กรอกเวลาเข้าและเวลาออกเช่น 19.15 น. 
'''

time_in = '9.05'
time_out = '20.21'

HI,MI = time_in.split('.')
HO,MO = time_out.split('.')

cal_h = int(HO)-int(HI) # 21-18 = 3
cal_m = int(MO)-int(MI) # 30-5 = 25

print('จอดไปทั้งหมด: {} ชั่วโมง {} นาที'.format(cal_h,cal_m))

if cal_m > 15:
    cal_h = cal_h + 1

if cal_h < 2:
    print('จอดฟรี')
elif cal_h == 2 and cal_m <= 15:
    print('จอดฟรี')
elif cal_h <= 6:
    print('A')
    cal = (cal_h - 2) * 20
    print('ค่าจอดทั้งหมด: {} บาท'.format(cal))
else:
    print('B')
    cal = ((cal_h - 6) * 40) + (4 * 20)
    print('ค่าจอดทั้งหมด: {} บาท'.format(cal))






