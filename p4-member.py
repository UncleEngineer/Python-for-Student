"""
4-สร้างโปรแกรมเพื่อจัดการระบบสมาชิกของฟิตเนส โดยโปรแกรมจะ:

รับอายุผู้ใช้และประเภทของสมาชิก (เช่น รายเดือน รายปี)
หากผู้ใช้อายุต่ำกว่า 18 ปี ให้ส่วนลด 10% ของค่าสมาชิก
หากผู้ใช้สมัครสมาชิกแบบรายปี ให้ส่วนลด 20%
คำนวณและแสดงราคาสมาชิกสุดท้ายที่ต้องชำระ
"""

age = int(input("อายุ: "))
member_type = input('กรุณาเลือก:\n-รายเดือน A\n-รายปี B\n --> ')

discount_percent = 0 # %
package_price = 0

if age < 18:
    discount_percent += 10

if member_type == 'B' or member_type == 'b':
    discount_percent += 20
    package_price = 5000 # สมมติปีละ 5000 บาท
elif member_type == 'A' or member_type == 'a':
    discount_percent += 0
    package_price = 500

   
total = package_price - (package_price * (discount_percent/100))

if member_type == 'B' or member_type == 'b':
    print('คุณเลือก package B รายปี ชำระครั้งเดียว: {} บาท'.format(total))
    print('คุณได้รับส่วนลด: {}%'.format(discount_percent))
elif member_type == 'A' or member_type == 'a':
    print('คุณเลือก package A รายเดือน ชำระเดือนละ {} บาท'.format(total))