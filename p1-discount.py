"""
 1-เขียนโปรแกรมรับจำนวนสินค้าและราคาต่อหน่วย 
 จากนั้นคำนวณและแสดงราคาสินค้าทั้งหมดพร้อมส่วนลด 10% 
 หากซื้อเกิน 10 ชิ้น และลดเพิ่มอีก 5% หากราคารวมเกิน 1000 บาท
 """

quantity = float(input("จำนวนสินค้า: "))
price = float(input('ราคาต่อหน่วย: '))
print('จำนวนสินค้า: {:,.2f} หน่วย'.format(quantity))
print('ราคาต่อหน่วย: {:,.2f} บาท/หน่วย'.format(price))

total = quantity * price
discount = 0

if quantity >= 10:
    discount = discount + total * (10/100)

if total >= 1000:
    discount = discount + total * (5/100)

grand_total = total - discount

print('ยอดทั้งหมด: {} บาท (ได้รับส่วนลด: {} บาท) จากปกติ: {} บาท'.format(grand_total,discount,total))