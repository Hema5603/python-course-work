name = input("Enter your name: ")
country = input("Enter your country: ")
birthdate = input("Enter your birthdate: ")
#using tuple
basic_information = (name, country, birthdate)
phone = input("Enter your phone number: ")
email = input("Enter your email: ")
theme = input("Enter your favorite theme color: ")
#using tuple
attributes = [phone, email, theme]
b1 = input("Enter business account username 1: ")
b2 = input("Enter business account username 2: ")
b3 = input("Enter business account username 3: ")
#using tuple
business_accounts = {b1, b2, b3}
about = input("Write something about yourself: ")
status = input("Enter your current status: ")
last_seen = input("Enter your last seen time: ")
profile_pic = input("Enter your profile picture filename: ")
#using dictionary
other_information = {
    "about": about,
    "status": status,
    "last_seen": last_seen,
    "profile_picture": profile_pic
}
print("Profile")
N, C, B = basic_information
print(f"Name: {N}, Country: {C}, Birthdate: {B}")
ph, em, th = attributes
print(f"Phone: {ph}, Email: {em}, Theme: {th}")
print(f"Business accounts (unique usernames): {business_accounts}")
a = other_information["about"]
st = other_information["status"]
ls = other_information["last_seen"]
pp = other_information["profile_picture"]
print(f"About: {a}, Status: {st}, Last seen: {ls}, Profile pic: {pp}")