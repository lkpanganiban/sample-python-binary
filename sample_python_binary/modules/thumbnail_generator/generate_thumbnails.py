import os
import multiprocessing
from typing import List
import cv2
from sample_python_binary.modules.utils.exec_timer import exec_time

class ThumbnailGenerator:
    def __init__(self, image_dir: str, thumbnail_dir: str="thumbnails"):
        self.name = "Thumbnail Generator"
        self.image_dir = image_dir
        self.thumbnail_dir = thumbnail_dir
        os.makedirs(self.thumbnail_dir, exist_ok=True)
        self.thumbnail_dimensions = (128,128)
        self.image_list = []
        self.supported_formats = [".png", ".jpg", ".bmp"]
    
    def _generate_thumbnails(self, image_path: str) -> str:
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        image_name = os.path.basename(image_path)
        image_resize = cv2.resize(image, self.thumbnail_dimensions, interpolation=cv2.INTER_LINEAR)
        output_image_path = f"{self.thumbnail_dir}/{image_name}"
        cv2.imwrite(output_image_path, image_resize)
        return output_image_path

    def _build_image_db(self) -> list:
        for root, dirs, files in os.walk(self.image_dir):
            for f in files:
                image_path = os.path.join(root, f)
                try:
                    if os.path.splitext(image_path)[1].lower() in self.supported_formats:
                        self.image_list.append(image_path)
                except:
                    print(f"skipped {image_path}")
        return self.image_list

    @exec_time
    def generate_thumbnails_from_dir(self) -> bool:
        image_list = self._build_image_db()
        try:
            pool = multiprocessing.Pool(processes=os.cpu_count())
            pool.map(self._generate_thumbnails, image_list)
            pool.close()
            return True
        except:
            return False
