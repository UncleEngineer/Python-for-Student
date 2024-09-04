'''
16- เขียนโปรแกรมเพื่อคำนวณเวลาที่ควรตื่นนอนหากคุณต้องการนอนหลับให้ครบ 8 ชั่วโมง
เงื่อนไข: ถ้าผู้ใช้ระบุเวลาที่ต้องตื่นนอน โปรแกรมจะแสดงเวลาที่ควรเข้านอนเพื่อให้นอนหลับครบ 8 ชั่วโมง
'''
sleep_hour = 8
text = input('คุณต้องการตื่นนอนเวลากี่โมง เช่น 8:30 : ')

wakeup_hour, wakeup_minute = map(int, text.split(':'))

bedtime_hour = wakeup_hour - sleep_hour
bedtime_minute = wakeup_minute

print(bedtime_minute)

if bedtime_hour < 0:
    bedtime_hour = bedtime_hour + 24

print(f'คุณต้องนอนเวลา: {bedtime_hour}:{bedtime_minute:02d}')