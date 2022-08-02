import json
from datetime import datetime
from cryptography.fernet import Fernet
from sample_python_binary.modules.settings import LICENSE_KEY, LICENSE_FILE, DEBUG


def _decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    f = Fernet(LICENSE_KEY)
    return f.decrypt(encrypted_message)

def _read_license(license_file: str):
    """
    Reads the license file
    """
    with open(license_file, "rb") as license_file:
        license = _decrypt_message(license_file.readline())
        license_json = json.loads(license)
    return license_json


def _check_expiry(license_expiry: datetime) -> bool:
    try:
        date_time_obj = datetime.strptime(license_expiry["LICENSE_EXPIRY"], '%Y/%m/%d')
    except:
        if DEBUG:
            print("Missing LICENSE_EXPIRY in license file.")
        return False
    delta = date_time_obj - datetime.now()
    if delta.days >= 0:
        return True
    else:
        return False

def _check_license() -> bool:
    license_checker = 0
    license_obj = _read_license(LICENSE_FILE)
    if _check_expiry(license_obj):
        license_checker += 1
    
    if license_checker == 1:
        return True
    return False