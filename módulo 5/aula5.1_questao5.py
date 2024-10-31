import emoji

emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

print("Emojis disponíveis:")
for emoji_char, emoji_code in emojis_disponiveis.items():
    print(f"{emoji_char} - {emoji_code}")

frase = input("Digite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase)

print("Frase emojizada:")
print(frase_emojizada)
