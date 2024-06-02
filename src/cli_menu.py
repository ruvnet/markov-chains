# MIT License
# Copyright (c) 2024 rUv
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from simple_term_menu import TerminalMenu
import asyncio
from src.markov_chain import generate_markov_text
from src.text_refiner import refine_text

def show_menu(options, title="Menu"):
    """
    Displays a terminal menu with the given options and title.

    :param options: A list of strings representing menu options.
    :param title: A string representing the menu title.
    :return: The index of the selected menu option.
    """
    terminal_menu = TerminalMenu(options, title=title)
    menu_entry_index = terminal_menu.show()
    return menu_entry_index

async def use_option():
    """
    Handles the 'Use' menu option to generate and refine text.
    """
    generated_text = generate_markov_text("corpus/corpus.txt")
    refined_text = await refine_text(generated_text)
    print(f"Refined Text: {refined_text}")

def configuration_option():
    """
    Allows users to configure application settings.
    """
    print("Configuration options:")
    print("1. Set text generation model")
    print("2. Set refinement model")
    print("3. Set output verbosity")
    # Placeholder for actual configuration logic

def installation_option():
    """
    Provides instructions for installing the application.
    """
    print("Installation Instructions:")
    print("1. Ensure Python 3.9 or higher is installed.")
    print("2. Clone the repository from GitHub.")
    print("3. Run 'pip install -r requirements.txt' to install dependencies.")
    print("4. Run 'python src/main.py' to start the application.")

def help_option():
    """
    Offers guidance and usage instructions for the application.
    """
    print("Help Information:")
    print("Use: Generates and refines text using Markov Chains and LLMs.")
    print("Configuration: Allows setting various configuration options for text generation and refinement.")
    print("Installation: Provides step-by-step instructions for installing the application.")
    print("Management: Enables management of application resources or settings.")

def management_option():
    """
    Enables management of application resources or settings.
    """
    print("Management Options:")
    print("1. View current configuration")
    print("2. Reset to default configuration")
    # Placeholder for actual management logic

def main_menu():
    """
    Main function to display the menu and handle user input.
    """
    options = ["Use", "Configuration", "Installation", "Help", "Management", "Quit"]
    while True:
        choice = show_menu(options, title="Main Menu")
        if choice == 0:
            asyncio.run(use_option())
        elif choice == 1:
            configuration_option()
        elif choice == 2:
            installation_option()
        elif choice == 3:
            help_option()
        elif choice == 4:
            management_option()
        elif choice == 5:
            break

if __name__ == "__main__":
    main_menu()
