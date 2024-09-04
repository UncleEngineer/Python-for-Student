'''
14- เขียนโปรแกรมเพื่อตรวจสอบว่าหมายเลขโทรศัพท์ที่ผู้ใช้ป้อนเข้ามา (รูปแบบ XXX-XXX-XXXX) 
ถูกต้องตามรูปแบบหรือไม่เงื่อนไข: ถ้าหมายเลขตรงตามรูปแบบที่กำหนด ให้แสดงว่า
 "หมายเลขถูกต้อง" นอกนั้นให้แสดงว่า "หมายเลขไม่ถูกต้อง"
'''
check = True

while check:
    tel = input('กรุณากรอกหมายเลขโทรศัพท์: ')
    digit_check = False
    digit_list = []
    for t in tel:
        if t == '-':
            pass
        elif t.isdigit():
            digit_list.append('t')
        else:
            digit_list.append('f')
            
    if 'f' in digit_list:
        digit_check = False
    else:
        digit_check = True


    if tel[3] == '-' and tel[7] == '-' and digit_check == True:
        print('หมายเลขถูกต้อง')
        check = False
    else:
        print('หมายเลขไม่ถูกต้อง กรุณากรอกใหม่ เช่น 081-234-5678')
        print('---------')

print('สิ้นสุดโปรแกรม')