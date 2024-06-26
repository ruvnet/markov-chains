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

import lionagi as li
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def refine_text(generated_text):
    """
    Refines the generated text using LionAGI's LLMs to improve coherence and readability.

    :param generated_text: The text generated by the Markov Chain model.
    :return: The refined text after processing by LionAGI's LLMs.
    """
    system = "You are a helpful assistant designed to refine text."
    instruction = {"Refine": "Improve the coherence and readability of the following text."}
    context = {"text": generated_text}

    assistant = li.Session(system=system)
    result = await assistant.chat(instruction=instruction, context=context, model="gpt-4-1106-preview")
    return result

# Example usage
if __name__ == "__main__":
    sample_text = "This is a sample text generated by Markov Chain."
    refined_text = asyncio.run(refine_text(sample_text))
    print(f"Refined Text: {refined_text}")
