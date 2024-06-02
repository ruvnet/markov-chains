from setuptools import setup, find_packages

setup(
    name='markov-chains-cli',
    version='0.1.0',
    author='rUv',
    author_email='example@example.com',
    description='A CLI application for generating and refining text using Markov Chains and LLMs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ruvnet/markov-chains',
    packages=find_packages(),
    install_requires=[
        'markovify',
        'lionagi',
        'asyncio',
        'pytest',
        'spacy',
        'simple-term-menu'
    ],
    entry_points={
        'console_scripts': [
            'markov=src.main:main_menu',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.9',
    license='MIT License',
    keywords='markov chains text generation LLM CLI',
)
