# 🎮 Nvidia Clip Filter

A lightweight Python GUI tool for organizing and filtering **Nvidia ShadowPlay clips** based on folder name and file extension. Perfect for gamers who want to quickly locate highlight reels or gameplay recordings without digging through cluttered folders.

---

## 🚀 Features

- Browse and select a folder containing Nvidia clips
- Automatically uses folder name as keyword (e.g. game title)
- Filters `.mp4` or `.mov` files that match the keyword
- Displays how many matching clips were found
- Calls a built-in `filter()` function to process the clips

---

## 🛠 Requirements

- Python 3.6+
- `tkinter` (included with most Python installations)
- A `filter.py` file containing the `filter()` function

---

## 📁 Folder Structure

nvidia-clip-filter/ │ 
├── main.py  # GUI application
├── filter.py  # Contains filter() function used to process clips
└── README.md  # This file

## 📂 How It Works

1. Select a folder (e.g. `C:/Videos/Valorant`)
2. The app extracts `"Valorant"` as the keyword
3. Filters all `.mp4` or `.mov` files in that folder containing `"valorant"` in the filename
4. Displays the number of matching clips
5. Runs the `filter()` function to process them (e.g. move, rename, etc.)

---

## 🧪 Example

If your folder is:

C:/Users/Kacper/Videos/ApexLegends

The app will:
- Use `"ApexLegends"` as the keyword
- Find all `.mp4` or `.mov` files in that folder with `"apexlegends"` in the filename
- Display the count and run your filter logic

---

## 🧑‍💻 Author

**Kacper** — built for gamers, by a gamer.

---

## 📃 License

Open-source and free to use. Add a license if you plan to share or distribute.