from tkinter import Tk
from tkinter.filedialog import askopenfilename


class ImageLoader:
    """
    Görüntü seçme ve yükleme işlemlerinden sorumlu sınıf.
    """

    def _init_(self):
        self.file_path = None

    def select_image(self):
        """
        Kullanıcıdan bir görüntü seçmesini sağlar.
        """
        Tk().withdraw()  # Tkinter ana penceresini gizle
        self.file_path = askopenfilename(
            title="Bir fotoğraf seç",
            filetypes=[("Resim Dosyaları", ".jpg;.jpeg;.png;.bmp;*.tiff")]
        )
        if not self.file_path:
            print("Herhangi bir dosya seçilmedi.")
            return None
        print(f"Seçilen dosya: {self.file_path}")
        return self.file_path


# Kullanım örneği
if __name__ == "__main__":
    image_loader = ImageLoader()
    selected_file = image_loader.select_image()
    if selected_file:
        print(f"Seçilen dosyanın yolu: {selected_file}")