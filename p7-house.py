"""
7-ให้เขียนโปรแกรมที่คำนวณอัตราการผ่อนบ้านรายเดือน โดยพิจารณาการเปลี่ยนแปลงอัตราดอกเบี้ยทุกๆ 5 ปี 
เช่น อัตราดอกเบี้ย 3% ในช่วง 5 ปีแรก, 4% ในช่วง 5 ปีต่อมา, และ 5% 
ในช่วงเวลาที่เหลือของระยะเวลาการผ่อน โดยให้รับค่าราคาบ้าน 
และกรอกระยะเวลาการผ่อน และจำนวนเปอร์เซ็นที่ต้องการผ่อนในแต่ละช่วง 5 ปี
"""

year = int(input('กรุณากรอกจำนวนปีที่ต้องการผ่อน: '))
house_price = int(input('กรุณากรอกราคาบ้าน: ')) 

if year <= 5:
    print('เงื่อนไข A')
    total = house_price + ((house_price * 0.03) * year)
    monthly_payment = total / (year * 12)
    print('ผ่อนบ้านทั้งหมด: {:,.2f} บาท ({:,.2f}/เดือน)'.format(total,monthly_payment)) 
elif year <= 10:
    print('เงื่อนไข B')
    year_5 = int(input('ต้องการผ่อนในช่วง 5 แรกกี่เปอร์เซ็น: '))
    year_10 = 100 - year_5

    print('คุณต้องการผ่อนในช่วง 5 ปีแรก: {}% และ {} ปีสุดท้าย {}%'.format(year_5,year-5,year_10))

    year_5_total = house_price * (year_5/100)
    year_10_total = house_price * (year_10/100)
    #####
    cal_year_5 = year_5_total + ((year_5_total * 0.03) * 5)
    monthly_payment_5 = cal_year_5 / 60 # 5 ปีแรก
    print('ผ่อนบ้านใน 5 ปีแรก: {:,.2f} บาท ({:,.2f}/เดือน)'.format(cal_year_5,monthly_payment_5))
    ######
    cal_year_10 = year_10_total + ((year_10_total * 0.04) * (year - 5))
    monthly_payment_10 = cal_year_10 / ((year-5)*12)
    print('ผ่อนบ้านใน {} ปีสุดท้าย: {:,.2f} บาท ({:,.2f}/เดือน)'.format(year-5,cal_year_10,monthly_payment_10))
else:
    print('เงื่อนไข C')
    year_5 = int(input('ต้องการผ่อนในช่วง 5 แรกกี่เปอร์เซ็น: '))
    year_10 = int(input('ต้องการผ่อนในช่วง 5 ปีต่อกี่เปอร์เซ็น: '))
    year_remaining = 100 - year_5 - year_10

    print('คุณต้องการผ่อนในช่วง 5 ปีแรก: {}% 5 ปีถัดมา: {}% และ {} ปีสุดท้าย {}%'.format(year_5,year_10,year-10,year_remaining))

    year_5_total = house_price * (year_5/100)
    year_10_total = house_price * (year_10/100)
    year_remaining_total = house_price * (year_remaining/100)

    #####
    cal_year_5 = year_5_total + ((year_5_total * 0.03) * 5)
    monthly_payment_5 = cal_year_5 / 60 # 5 ปีแรก
    print('ผ่อนบ้านใน 5 ปีแรก: {:,.2f} บาท ({:,.2f}/เดือน)'.format(cal_year_5,monthly_payment_5))
    ######
    cal_year_10 = year_10_total + ((year_10_total * 0.04) * 5)
    monthly_payment_10 = cal_year_10 / 60
    print('ผ่อนบ้านใน 5 ปีถัดมา {:,.2f} บาท ({:,.2f}/เดือน)'.format(cal_year_10,monthly_payment_10))

    ###remaining###
    cal_year_remaining = year_remaining_total + ((year_remaining_total * 0.05) * (year - 10))
    monthly_payment_remaining = cal_year_10 / ((year-10)*12)
    print('ผ่อนบ้านใน {} ปีสุดท้าย: {:,.2f} บาท ({:,.2f}/เดือน)'.format(year-10,cal_year_remaining,monthly_payment_remaining))


# elif year <= 10:


    
    
