# Définition du dictionnaire Morse
morse_dict = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
  'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
  'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
  '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

# Fonction pour convertir un texte en Morse
def text_to_morse(text):
  morse_code = ''
  for char in text:
    if char.upper() in morse_dict:
      morse_code += morse_dict[char.upper()] + ' '
    else:
      morse_code += char + ' '
  return morse_code.strip()

# Fonction pour convertir un Morse en texte
def morse_to_text(morse_code):
  text = ''
  morse_code = morse_code.split(' ')
  for code in morse_code:
    for key, value in morse_dict.items():
      if code == value:
        text += key
        break
    else:
      text += code
  return text

# Exemple d'utilisation
text = 'sos'
morse_code = text_to_morse(text)
print('Texte:', text)
print(f'Code Morse: {morse_code}')
decoded_text = morse_to_text(morse_code)
print(f'Texte décodé: {decoded_text}')
