import re
from os import rename, path
from subprocess import PIPE, Popen


class BrandsDetector:
    """
    Класс для определения брендов на изображении
    """
    def __init__(
        self,
        prediction_file = 'predictions.jpg',
        darknet_path: str = 'bin/darknet',
        data_path: str = 'data/brands.data',
        cfg_path: str = 'cfg/brands.cfg',
        weights_path: str = 'cfg/brands.weights'
    ) -> None:
        """
        Args:
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

    def detect(self, image: str) -> dict:
        """
        По входному изображению определяет:
        - бренды, представленные на фото
        - точность, с которой был определен бренд

        Args:
            image (str): путь до файла

        Returns:
            dict: список изображений с данными о них
        
        Examples:
            >>> brands_detector.detect(image='test/3da2ba3337-4_1200x.jpg')
            {
                "coincidences": [
                    {
                        "brand": "Puma",
                        "precision": 1.0
                    },
                    {
                        "brand": "Puma",
                        "precision": 0.28
                    }
                ],
                "image": "/download/64559380_futbolka-mujskaya-puma-6555611-l/result.jpg"
            }
        """
        # файл, в который будет сохранена картинка с результатом
        filename = path.splitext(p=image)
        predicted = f"{path.dirname(image)}/result{filename[-1]}"

        # TODO: подумать над библиотекой на C
        # вызываем сеть
        proc = Popen(args=[
            self.darknet_path,
            'detector', 'test',
            self.data_path,
            self.cfg_path,
            self.weights_path,
            image
        ], stdout=PIPE)
        # список распознанных брендов
        # ищем строки формата Adidas: 73% и вытаскиваем из них нужные данные
        recognized = list(map(
            lambda pair: { 'brand': pair[0], 'precision': int(pair[1]) / 100 },
            re.findall(r'\\n(\w+): (\d+)%', str(proc.stdout.read()))
        ))

        # перемещаем результат работы сети в папку с результатами
        # при этом сохраняя исходное название файла
        rename(self.prediction_file, predicted)
        result_img = f"/download/{'/'.join(predicted.split('/')[-2:])}"

        return {
            'image': result_img,
            'coincidences': recognized
        }


if __name__ == '__main__':
    detector = BrandsDetector()
    detector.detect('test/3da2ba3337-4_1200x.jpg')
