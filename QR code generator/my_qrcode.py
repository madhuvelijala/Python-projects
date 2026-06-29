import qrcode
print("qrcode")
data=input("enter text or URL:")
img=qrcode.make(data)
file_name =input("enter file name:")
img.save(file_name+".png")
print("QR code generated successfully")
print(f"saved as:{file_name}.py")