import speech_recognition as sr
import pyttsx3
import openai

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

openai.api_key = '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'

def chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Adjust this as needed
    )
    return response.choices[0].text.strip()


todo_list = []

def add_to_do_item(item):
    todo_list.append(item)

def show_to_do_list():
    return todo_list


def main():
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for a command...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)

            command = recognizer.recognize_google(audio).lower()
                                    
            if "create a to-do" in command:
                print("What task would you like to add to the to-do list?")
                response = chat_gpt("Add a task to my to-do list: ")
                add_to_do_item(response)
                print(f"Added '{response}' to your to-do list.")

            elif "show my to-do list" in command:
                items = show_to_do_list()
                if items:
                    print("Your to-do list:")
                    for idx, item in enumerate(items, start=1):
                        print(f"{idx}. {item}")
                else:
                    print("Your to-do list is empty.")

            elif "search the web" in command:
                print("What would you like to search for?")
                response = chat_gpt("Search the web for: ")
                print(f"Searching the web for '{response}'...")  # You can implement web search logic here

            elif "exit" in command:
                print("Exiting the voice assistant.")
                break

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with the voice recognition service: {e}")

if __name__ == "__main__":
    main()

