"""
9-คำนวณ BMI ในการหาค่าดัชนีมวลกาย = น้ำหนักตัว [กิโลกรัม] ÷ ส่วนสูง [เมตร] ยกกำลังสอง 
- น้อยกว่า 18.5 = ผอมเกินไป
-18.5 - 25.0 = น้ำหนักปกติ น้ำหนักเหมาะสม 
-มากกว่า 25.0 - 30.0 = เริ่มอ้วน
-มากกว่า 35.0 อ้วนมากผิดปกติ
"""

weight = float(input('กรอกน้ำหนักตัว(กิโลกรัม): '))
height = float(input('กรอกส่วนสูง(เมตร): '))
cal = weight / (height**2)

if cal < 18.5:
    print(f'BMI: {cal:.2f} --> ผอมเกินไป')
elif cal <= 25:
    print(f'BMI: {cal:.2f} --> น้ำหนักปกติ น้ำหนักเหมาะสม')
elif cal <= 30:
    print(f'BMI: {cal:.2f} --> เริ่มอ้วน')
else:
    print(f'BMI: {cal:.2f} --> อ้วนมากผิดปกติ')