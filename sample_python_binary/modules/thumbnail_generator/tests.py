import os
import unittest
import shutil
from sample_python_binary.modules import thumbnail_generator
from sample_python_binary.modules.thumbnail_generator.generate_thumbnails import ThumbnailGenerator

class TestThumbnailGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.image_dir = "data_dir/test_data/logos"
        self.thumbnail_dir = "thumbnail_test"
        return super().setUp()

    def tearDown(self) -> None:
        shutil.rmtree(self.thumbnail_dir)
        return super().tearDown()

    def test_generate_thumbnails(self):
        raw_image_count = len([name for name in os.listdir(self.image_dir) if os.path.isfile(os.path.join(self.image_dir, name))])
        thumbnail_generator = ThumbnailGenerator(self.image_dir, self.thumbnail_dir)
        thumbnail_generator.generate_thumbnails_from_dir()
        thumbnail_generated_count = len([name for name in os.listdir(self.thumbnail_dir) if os.path.isfile(os.path.join(self.thumbnail_dir, name))])
        self.assertEqual(raw_image_count, thumbnail_generated_count)


if __name__ == '__main__':
    unittest.main()