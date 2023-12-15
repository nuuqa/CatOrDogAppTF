# Koodin luonnissa on käytetty ChatGPT:tä apuna.

from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import StringVar, Entry
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class Repository():
    # Konstruktori
    def __init__(self, entryString, filePathEntry, detectImage, detectField=None):
        self.file_path = ""
        self.entryString = entryString
        self.filePathEntry = filePathEntry
        self.detectImage = detectImage
        self.detectField = detectField

    # DetectField Setter.
    def SetDetectField(self, detectField):
        self.detectField = detectField

    # Tiedoston haku
    def BrowseFile(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.entryString.set(self.file_path)
            self.ShowImage()

    # Näyttää haetun kuvan sovelluksessa
    def ShowImage(self):
        if self.file_path:
            original_image = Image.open(self.file_path)
            width, height = original_image.size

            # Määritetään uusi leveys ja korkeus
            new_width = (int)(width / 2)
            new_height = (int)(height / 2)

            # Pienennä kuvaa
            resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

            # Luo PhotoImage muokatusta kuvasta
            photo = ImageTk.PhotoImage(resized_image)

            # Päivitä näytettävä kuva
            self.detectImage.config(image=photo)
            self.detectImage.photo = photo
        else:
            print("Tiedostoa ei ole valittu.")

    # Prosessoidaan kuva samalla tavalla kuin mallia kouluttaessa.
    def PreprocessImage(self):
        if self.file_path:
            img = image.load_img(self.file_path, target_size=(128, 128))
            imgArray = image.img_to_array(img)
            imgArray = np.expand_dims(imgArray, axis=0)
            imgArray = (imgArray / 255.0)  # Normalisoi pikseliarvot, tämän täytyy olla sama kuin mallia kouluttaessa.
            return imgArray
        else:
            print("Tiedostoa ei ole valittu.")
            return None

    # Tekee arvion onko kuvassa kissa vai koira.
    def DetectCatOrDog(self):
        modelPath = "C:/Temp/CatAndDogs_Final_91.h5"
        model = load_model(modelPath)
        user_image = self.PreprocessImage()
        if user_image is not None:
            prediction = model.predict(user_image)
            print(prediction)
            if prediction > 0.600:
                result = "Koira"
            if prediction >= 0.400 and prediction <= 0.600:
                result = "Ei ole varma"
            if prediction < 0.400:
                result = "Kissa"

            self.detectField.config(text=f"{result}")  # Teksti sovellukseen
