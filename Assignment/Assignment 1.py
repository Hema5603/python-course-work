name = input("Enter your name: ")
phone = input("Enter your phone number: ")
about = input("Write something about yourself: ")
status = input("Enter your current status: ")
last_seen = input("Enter your last seen time: ")
profile_pic = input("Enter your profile picture filename: ")
country = input("Enter your country: ")
birthdate = input("Enter your birthdate (e.g., 12-08-2003): ")
email = input("Enter your email (optional): ")
theme = input("Enter your favorite theme color: ")

user_profile = {
    "name": name,
    "phone": phone,
    "about": about,
    "status": status,
    "last_seen": last_seen,
    "profile_picture": profile_pic,
    "country": country,
    "birthdate": birthdate,
    "email": email,
    "theme_color": theme
}
print(f"Name: {user_profile['name']}")
print(f"Phone: {user_profile['phone']}")
print(f"About: {user_profile['about']}")
print(f"Status: {user_profile['status']}")
print(f"Last Seen: {user_profile['last_seen']}")
print(f"Profile Picture: {user_profile['profile_picture']}")
print(f"Country: {user_profile['country']}")
print(f"Birthdate: {user_profile['birthdate']}")
print(f"Email: {user_profile['email']}")
print(f"Theme Color: {user_profile['theme_color']}")