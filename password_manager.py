from cryptography.fernet import Fernet
import pyperclip

key = Fernet.generate_key()

def encrypt_password(password):
	f = Fernet(key)
	encrypted_password = f.encrypt(password.encode())
	return encrypted_password

def decrypt_password(encrypted_password):
	f = Fernet(key)
	decrypted_password = f.decrypt(encrypted_password)
	return decrypted_password.decode()


def save_password(service, username, password):
	with open('password.txt','a') as f:
		encrypted_password = encrypt_password(password)
		f.write(f'{service}, {username}, {encrypted_password.decode()}\n')

def retrive_password(service, username):
	with open('passwords.txt','r') as f:
		lines = f.readlines()
		for line in lines:
			parts = line.split(', ')
			if part[0] == service and parts[1] == username:
				encrypted_password = parts[2].strip()
				return decrypt_password(encrypted_password.encode())
	return None

def copy_to_clipboard(password):
	pyperclip.copy(password)
	print('password copied to clipboard')


save_password('gmail', 'john doe', 'mysecretpasword')



