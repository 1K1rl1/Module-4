def info_polin(word):
    print(word)
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

print(info_polin('лепсспел')) 
print(info_polin('helloworld'))
