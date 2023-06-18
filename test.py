def palindrome():
    string_symbols = input().strip()
    return string_symbols == string_symbols[::-1]

if __name__ == "__main__":
    print(palindrome())