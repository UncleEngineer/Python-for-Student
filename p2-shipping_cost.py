"""
2-รับน้ำหนักของพัสดุจากผู้ใช้ จากนั้นคำนวณค่าธรรมเนียมการส่งสินค้าตามเงื่อนไข:
น้ำหนัก <= 1 กิโลกรัม ค่าจัดส่ง 30 บาท; น้ำหนักมากกว่า 1 กิโลกรัม
แต่ไม่เกิน 5 กิโลกรัม ค่าจัดส่ง 50 บาท; น้ำหนักเกิน 5 กิโลกรัม ค่าจัดส่ง 100 บาท
"""

weight = float(input('สินค้าน้ำหนัก: '))
shipping_cost = 0

if weight <= 1:
    shipping_cost = 30
elif weight > 1 and weight <= 5:
    shipping_cost = 50
else:
    shipping_cost = 100

print('สินค้าหนัก: {:,.2f} กิโลกรัม รวมค่าธรรมเนียมการส่ง: {:,.2f} บาท'.format(weight,shipping_cost))
