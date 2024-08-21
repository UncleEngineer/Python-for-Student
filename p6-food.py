"""
6- ให้เขียนโปรแกรมคำนวณค่าอาหารในร้านอาหาร โดยให้กรอกจำนวนรายการ 
แล้วให้รับค่าราคาอาหารแต่ละจาน  + ค่า service charge 10% และภาษี 7% 
จากยอดรวม  จากนั้นให้โปรแกรมคำนวณค่าใช้จ่ายรวมที่ต้องจ่ายเมื่อสิ้นสุดการรับประทานอาหาร
"""

quantity = int(input('จำนวนรายการอาหารที่สั่ง: '))
total = 0
for i in range(quantity):
    price = float(input('ราคาอาหารจานที่ {} : '.format(i+1)))
    total += price

service = total * 0.1
total_service = total + service
grand_total = total_service * 1.07
print('ยอดที่ต้องชำระ: {:,.2f} บาท'.format(grand_total))
