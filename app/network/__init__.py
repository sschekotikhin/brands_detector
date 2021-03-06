from typing import List
from pathlib import Path
from os import rename, path
from subprocess import call


class BrandsDetector:
    """
    Класс для определения брендов на изображении
    """
    def __init__(
        self,
        destination: str = 'app/public/images',
        prediction_file = 'predictions.jpg',
        darknet_path: str = 'bin/darknet',
        data_path: str = 'data/brands.data',
        cfg_path: str = 'cfg/brands.cfg',
        weights_path: str = 'cfg/brands.weights'
    ) -> None:
        """
        Args:
            destination (str, optional): Путь до директории, в которую
            будет сохранено изображение. Если директории не существует, то она
            будет создана. Defaults to 'app/public/images'
            prediction_file (str, optional): Путь до файла с результатом работы сети.
            Defaults to 'predictions.jpg'.
            darknet_path (str, optional): Путь до исполняемого файла.
            Defaults to 'bin/darknet'.
            data_path (str, optional): Путь до файла с данными для настройки нейронной сети.
            Defaults to 'data/brands.data'.
            cfg_path (str, optional): Путь до файла с конфигом нейронной сети.
            Defaults to 'cfg/brands.cfg'.
            weights_path (str, optional): Путь до файла с весами.
            Defaults to 'cfg/brands.weights'.
        """
        # создаем директорию, если ее не существует
        self.prediction_file = prediction_file

        self.darknet_path = darknet_path
        self.data_path = data_path
        self.cfg_path = cfg_path
        self.weights_path = weights_path

    def detect(self, image: str) -> List[hash]:
        """
        По входному изображению определяет:
        - бренды, представленные на фото
        - точность, с которой был определен бренд

        Args:
            image (str): путь до файла

        Returns:
            List[hash]: список изображений с данными о них
        
        Examples:
            >>> brands_detector.detect(image='/Users/sergei_schekotikhin/Studying/brands_detector/test/3da2ba3337-4_1200x.jpg')
            [
                {
                    'brand': 'Adidas',
                    'precision': 1.0,
                    'image': '/Users/sergei_schekotikhin/Studying/brands_detector/app/images/3da2ba3337-4_1200x.jpg'
                }
            ]
        """
        # файл, в который будет сохранена картинка с результатом
        filename = path.splitext(p=image)
        predicted = f"{path.dirname(image)}/result{filename[-1]}"

        # TODO: подумать над библиотекой на C
        # вызываем сеть
        call(args=[
            self.darknet_path,
            'detector', 'test',
            self.data_path,
            self.cfg_path,
            self.weights_path,
            image
        ])

        # перемещаем результат работы сети в папку с результатами
        # при этом сохраняя исходное название файла
        rename(self.prediction_file, predicted)

        return [{
            'brand': '',
            'precision': '',
            'image': predicted
        }]


if __name__ == '__main__':
    detector = BrandsDetector()
    detector.detect('test/3da2ba3337-4_1200x.jpg')
