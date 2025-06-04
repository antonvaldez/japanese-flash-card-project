# 🇯🇵 Japanese Flashcard App

A beginner-friendly flashcard app built with Python and Tkinter to help users learn Japanese Kanji and vocabulary. It shows words in Japanese and flips to reveal the English meaning after a few seconds. Users can track and remove known words as they progress.

## 🚀 Features

- Flip cards automatically after 3 seconds  
- Learn Kanji and Japanese words with English translations  
- Track your progress — known words are saved and removed  
- Clean and simple UI using Tkinter  

## 🗂️ Project Structure
.
├── data/
│   ├── japanese_words.csv         # Full word list
│   └── words_to_learn.csv         # Tracks progress
├── images/
│   ├── card_front.png             # Front of the flashcard
│   ├── card_back.png              # Back of the flashcard
│   ├── right.png                  # Button icon (right/known)
│   └── wrong.png                  # Button icon (wrong/unknown)
└── main.py                        # Main application script
