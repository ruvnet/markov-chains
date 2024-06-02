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
    Placeholder for configuration option functionality.
    """
    print("Configuration options will be implemented here.")

def installation_option():
    """
    Placeholder for installation option functionality.
    """
    print("Installation instructions will be provided here.")

def help_option():
    """
    Placeholder for help option functionality.
    """
    print("Help information will be provided here.")

def management_option():
    """
    Placeholder for management option functionality.
    """
    print("Management options will be implemented here.")

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
