from cryptography.fernet import Fernet

key = "4xsmn-fHh9xNUlDwtuip_qZ-tZORzIbvoHFkmlbMMBQ="

system_information_e = "C_UsersBryceDocumentsHACKSe_systeminfo.txt"
clipboard_information_e = "C_UsersBryceDocumentsHACKSe_clipboard.txt"
keys_information_e = ("C_UsersBryceDocumentsHACKSe_key_log.txt")

encrypted_files =[system_information_e, clipboard_information_e, keys_information_e]
count = 0


for decrypting_file in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count], 'wb') as f:
        f.write(decrypted)

    count += 1
