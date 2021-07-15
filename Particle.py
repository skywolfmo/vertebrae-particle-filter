import cv2 as cv
import numpy as np

import abc


class Particle(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        self.weight = 1
        self.likelihood = 0
        self.rotation = 0

    def update(self, x, y, theta):
        self.rotation += theta * np.pi / 360
        self.particle.update(x, y,  theta * np.pi / 360)

    def rotate(self, theta):
        self.rotation += theta * np.pi / 360
        self.particle.rotate_around_center(theta * np.pi / 360)


class ParticlePoint(Particle):
    def __init__(self, point):
        super().__init__()
        self.particle = point
        self.histogram = None


class ParticleShape(Particle):
    def __init__(self, shape):
        super().__init__()
        self.particle = shape

    def translate_x(self, x):
        x = int(x)
        self.particle.translate_x(x)

    def translate_y(self, y):
        y = int(y)
        self.particle.translate_y(y)

    def translate_to(self, x, y):
        x = int(x)
        y = int(y)
        self.particle.translate_to(x, y)

    def get_histogram(self, frame):
        histogram = self.particle.get_histogram(frame)
        # because the extract_content of the Shape class returns an image where
        # everything is black except for the inner content of the image,
        # I had to ignore all the black in the image and set its histogram value of 0 to 0
        histogram[:, 0] = 0
        m = np.maximum(np.ones(np.sum(histogram).shape), np.sum(histogram))
        histogram = histogram / m

        self.histogram = histogram
        return histogram
