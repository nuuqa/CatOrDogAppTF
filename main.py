import tkinter
import tkinter as tk
from repository import *

window = tk.Tk()
window.title("CatOrDogApp")
window.geometry("700x700")

# Title Label
titleLabel = tk.Label(master=window, text="Cat Or Dog?", font="Consolas 23 bold")
titleLabel.pack(pady=10)

# ImageFrame - tähän ilmestyy kuva mikä haetaan
imageFrame = tk.Frame(master=window)
detectImage = tk.Label(master=imageFrame)
detectImage.pack()
imageFrame.pack()

# InputFrame
inputFrame = tk.Frame(master=window)
entryString = tk.StringVar()
filePathEntry = tk.Entry(master=inputFrame, width=30, textvariable=entryString)

repo = Repository(entryString, filePathEntry, detectImage)

# Haetaan tiedostopolku...
filePathButton = tk.Button(master=inputFrame, width=5, text="File...", command=repo.BrowseFile)
filePathEntry.pack(side="left")
filePathButton.pack(side="left", padx=20)
inputFrame.pack(pady=10)

# DetectFrame 1
detectFrame = tk.Frame(master=window)
detectLabel = tk.Label(master=detectFrame, text="Detect:", font="Consolas 16 normal")
detectField = tk.Label(master=detectFrame, font="Consolas 16 normal")
detectLabel.pack(side="left")
detectField.pack(side="left")
detectFrame.pack()

repo.SetDetectField(detectField)

# DetectFrame 2
detectFrameTwo = tk.Frame(master=window)
detectButton = tk.Button(master=detectFrameTwo, width=20, text="Detect", command=repo.DetectCatOrDog)
detectButton.pack()
detectFrameTwo.pack(pady=10)



# Main loop
if __name__ == "__main__":
    window.mainloop()
