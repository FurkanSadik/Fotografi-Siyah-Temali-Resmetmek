import cv2

class CartoonEffect:
    """
    El çizimi tarzında karikatür efektini uygulayan sınıf.
    """

    def __init__(self, image_path):
        self.image_path = image_path
        self.original_image = None
        self.cartoon_image = None

    def load_image(self):
        """
        Görüntüyü dosya yolundan yükler ve yeniden boyutlandırır.
        """
        self.original_image = cv2.imread(self.image_path)
        if self.original_image is None:
            raise FileNotFoundError(f"Görüntü dosyası bulunamadı: {self.image_path}")

        self.original_image = cv2.resize(self.original_image, (800, 800))
        return self.original_image

    def apply_effect(self):
        """
        El çizimi tarzında karikatür efektini uygular.
        """
        if self.original_image is None:
            raise ValueError("Önce 'load_image()' metodunu çağırarak görüntüyü yükleyin.")

        # 1. Kenar Algılama
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 7)

        # Kenarları güçlü bir şekilde algıla
        edges = cv2.Laplacian(gray, cv2.CV_8U, ksize=5)
        _, edges = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY)

        # 2. Yumuşatma ve renkleri azaltma (daha çizim tarzı)
        color = cv2.bilateralFilter(self.original_image, 9, 300, 300)

        # 3. Kenarları çizim gibi gösterme
        self.cartoon_image = cv2.bitwise_and(color, color, mask=edges)

        # 4. Kurşun kalem efekti
        sketch = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        sketch = cv2.bitwise_not(sketch)  # Yalnızca ters çevirmek için bitwise_not kullanıyoruz
        sketch = cv2.GaussianBlur(sketch, (21, 21), 0)
        sketch = cv2.bitwise_not(sketch)  # Tekrar ters çeviriyoruz
        self.cartoon_image = cv2.bitwise_and(self.cartoon_image, self.cartoon_image, mask=sketch)

        return self.cartoon_image