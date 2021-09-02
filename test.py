from passlib.hash import pbkdf2_sha256


hash = pbkdf2_sha256.hash("1234")
print(hash)

result = pbkdf2_sha256.verify("12343333", hash)


print(result)