import pytesseract
from gtts import gTTS
from PIL import Image
from colorama import init, Fore, Style
from datetime import datetime

init()  # Initialize colorama

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{image_path}' not found." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}" + Style.RESET_ALL)
    return ""

def get_filename_base(text):
    if not text:
        return "output"
    return '_'.join(text.split()[:3]) or "output"

def main():
    image_path = input(Fore.YELLOW + "Enter the path to your image file: " + Style.RESET_ALL).strip()
    text = extract_text_from_image(image_path)

    if not text:
        print(Fore.RED + "No text extracted. Exiting." + Style.RESET_ALL)
        return

    print("\n" + Fore.CYAN + "Extracted Text:\n" + Style.RESET_ALL + text + "\n")

    base_name = get_filename_base(text)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_name = f"{base_name}_{timestamp}"

    print(Fore.YELLOW + "Do you want to download the output?\n"
                        "1. Only Audio\n"
                        "2. Only Text\n"
                        "3. Both Audio and Text\n"
                        "4. None\n" + Style.RESET_ALL)

    choice = input("Enter your choice (1/2/3/4): ").strip()

    # Ask for language only if audio is chosen
    if choice in ['1', '3']:
        # lang = input("Enter language code for TTS (default is 'en'): ").strip()
        # if not lang:
        lang = "en"
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(final_name + ".mp3")
            print(Fore.GREEN + f"✅ Audio saved as: {final_name}.mp3" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Could not save audio: {e}" + Style.RESET_ALL)

    if choice in ['2', '3']:
        try:
            with open(final_name + ".txt", "w", encoding="utf-8") as f:
                f.write(text)
            print(Fore.GREEN + f"✅ Text saved as: {final_name}.txt" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"❌ Could not save text file: {e}" + Style.RESET_ALL)

    if choice == '4':
        print(Fore.BLUE + "🤝 Alright, no files saved. Just showing the result!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
