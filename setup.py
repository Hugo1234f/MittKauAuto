import passwdManager

print("Mitt Kau setup: ")
print("----------")
print("Skapar krypteringsnyckel...")
passwdManager.generateKey()
print("Nyckel skapad (128 bitar)")
print("----------")
passwdManager.encrypt(input("Användarnamn: "), 'u')
passwdManager.encrypt(input("Lösenord: "), 'p')
print("----------")
print('\nKlar')