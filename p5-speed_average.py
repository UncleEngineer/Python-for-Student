"""5-เขียนโปรแกรมเพื่อคำนวณความเร็วเฉลี่ยของการเดินทาง โดยโปรแกรมจะ:

-รับระยะทาง (กิโลเมตร) และเวลาที่ใช้ (ชั่วโมง) จากผู้ใช้
-คำนวณความเร็วเฉลี่ยจากระยะทางและเวลา
-ถ้าความเร็วเฉลี่ยเกิน 120 กิโลเมตรต่อชั่วโมง ให้เตือนว่า "ความเร็วเกินกำหนด" 
"""

distance = float(input('ระยะทาง (กิโลเมตร): '))
time = float(input('เวลา: (ชั่วโมง)'))

total = distance / time
print('ความเร็วเฉลี่ย: {:.0f} กิโลเมตร/ชั่วโมง'.format(total))
if total >= 120:
    print('คุณใช้ความเร็วเกินกำหนด')