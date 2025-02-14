import cv2
from image_loader import ImageLoader
from cartoon_effect import CartoonEffect


def main():
    # 1. Fotoğraf Seçimi
    image_loader = ImageLoader()
    image_path = image_loader.select_image()  # FONKSİYON GİBİ ÇAĞRILMALI
    if not image_path:
        return

    # 2. Karikatür Efekti Uygulama
    cartoon_effect = CartoonEffect(image_path)
    try:
        original_image = cartoon_effect.load_image()
        cartoon_image = cartoon_effect.apply_effect()
    except FileNotFoundError as e:
        print(f"Hata: {e}")
        return

    # 3. Görüntüleri Göster
    cv2.imshow("Orijinal Görüntü", original_image)
    cv2.imshow("El Çizimi Efekti", cartoon_image)

    # Çıkış için herhangi bir tuşa basmayı bekle
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 4. Görüntüyü Kaydetme
    save_choice = input("El çizimi görüntüsünü kaydetmek ister misiniz? (Evet/Hayır): ").strip().lower()
    if save_choice in ["evet", "e"]:
        file_name, file_ext = image_path.rsplit(".", 1)  # UZANTIYI DOĞRU AL
        save_path = f"{file_name}_sketch.{file_ext}"
        cv2.imwrite(save_path, cartoon_image)
        print(f"El çizimi görüntüsü {save_path} konumuna kaydedildi.")
    else:
        print("Görüntü kaydedilmedi.")


if __name__ == "__main__":  # DÜZGÜN YAZIM
    main()