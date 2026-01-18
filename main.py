import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow import keras

class CatDogClassifierApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Cat vs Dog Classifier")
        self.window.geometry("600x700")
        
        # Load model
        try:
            self.model = keras.models.load_model('cnn_model.keras')
        except:
            self.model = None
        
        # Title
        self.title_label = ctk.CTkLabel(
            self.window, 
            text="Cat vs Dog Classifier", 
            font=("Arial", 24, "bold")
        )
        self.title_label.pack(pady=20)
        
        # Image display frame
        self.image_frame = ctk.CTkFrame(self.window, width=400, height=400)
        self.image_frame.pack(pady=10)
        self.image_frame.pack_propagate(False)
        
        self.image_label = ctk.CTkLabel(self.image_frame, text="No image loaded")
        self.image_label.pack(expand=True)
        
        # Upload button
        self.upload_btn = ctk.CTkButton(
            self.window, 
            text="Upload Image", 
            command=self.upload_image,
            width=200,
            height=40
        )
        self.upload_btn.pack(pady=10)
        
        # Predict button
        self.predict_btn = ctk.CTkButton(
            self.window, 
            text="Predict", 
            command=self.predict,
            width=200,
            height=40,
            state="disabled"
        )
        self.predict_btn.pack(pady=10)
        
        # Result label
        self.result_label = ctk.CTkLabel(
            self.window, 
            text="", 
            font=("Arial", 18, "bold")
        )
        self.result_label.pack(pady=20)
        
        self.image_path = None
        
    def upload_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        
        if self.image_path:
            # Display image
            img = Image.open(self.image_path)
            img.thumbnail((380, 380))
            photo = ImageTk.PhotoImage(img)
            
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
            
            self.predict_btn.configure(state="normal")
            self.result_label.configure(text="")
    
    def predict(self):
        if not self.image_path or not self.model:
            return
        
        # Preprocess image
        img = Image.open(self.image_path)
        img = img.resize((128, 128))  # Adjust size based on your model
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        prediction = self.model.predict(img_array)
        
        if prediction[0][0] > 0.5:
            result = f"Dog ({prediction[0][0]*100:.2f}%)"
            color = "blue"
        else:
            result = f"Cat ({(1-prediction[0][0])*100:.2f}%)"
            color = "orange"
        
        self.result_label.configure(text=result, text_color=color)
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = CatDogClassifierApp()
    app.run()