import random
import string

def generate_password(length, chars):
  password = ''.join(random.choice(chars) for i in range(length))
  return password

def main():
  while True:
    try:
      length = int(input("Enter desired password length: "))
      if length >= 8:
        break
      else:
        print("Password length must be at least 8 characters.")
    except ValueError:
      print("Invalid input. Please enter an integer.")

  chars = input("Enter desired character sets (letters, numbers, symbols, or any combination): ").lower()
  character_sets = {
    'letters': string.ascii_letters,
    'numbers': string.digits,
    'symbols': string.punctuation
  }
  allowed_chars = ''.join(character_sets[set_name] for set_name in chars.split())

  password = generate_password(length, allowed_chars)
  print("Generated password:", password)

if __name__ == "__main__":
  main()
