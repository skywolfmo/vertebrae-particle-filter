import cv2
import random
import numpy as np
from numpy import pi

from polyroi import Point, Shape
from .Particle import ParticleShape


class Tracker:
    def __init__(self, image, target_shape, nb_particles, object_speed, object_rotation):
        self.image = image
        self.target_shape = target_shape
        self.target_shape.to_rectangle()
        self.target_image = self.target_shape.extract_content(self.image)

        self.target_particle = ParticleShape(self.target_shape)
        self.target_histogram = self.target_particle.get_histogram(self.image)

        self.target_pty = None
        self.target_ptx = None

        self.particles_position = None
        self.partilces_rotation = None
        self.particles_likelihood = None

        self.nb_particles = 200 if nb_particles is None else nb_particles
        # ! expected translation speed
        # Used for generating particles around the current principle particle
        self.object_speed = 5 if object_speed is None else object_speed
        # ! expected rotation speed
        self.object_rotation_speed = 1 if object_rotation is None else object_rotation
        self.particles_weight = np.ones(self.nb_particles)

    # Compute the target BGR histogram
    def GetTargetHistogram(self):
        self.target_histogram = self.target_particle.get_histogram(self.image)

    # Initialize the particles with uniformely scatter position, uniform weight and 0 likelihood

    def ParticlesInitilization(self):

        self.base_particle = ParticleShape(self.target_shape)

        self.particles = np.array(
            [ParticleShape(Shape.copy(self.target_shape))
             for i in range(self.nb_particles)]
        )
        # Get the particles position
        self.get_particles_position()
        # Initialize the particles rotation with 0
        self.particles_rotation = np.zeros(self.nb_particles)
        # Uniform particle weights
        self.particles_weight = np.ones(self.nb_particles) / self.nb_particles
        # Update the particles objects weight
        self.update_particles_weights()
        # Initialize the particles likelihood to 0
        self.particles_likelihood = np.zeros(self.nb_particles)

    # Resample the particles according to their weights
    def ParticlesResampling(self):
        # Get the current particles weights
        self.get_particles_weights()
        # calculate the cumulated sum of the weights
        particles_weight_cumulated_sum = np.cumsum(self.particles_weight)
        # avoid round-off error
        particles_weight_cumulated_sum[-1] = 1.
        # Chosing the particles indexes
        indexes = np.searchsorted(
            particles_weight_cumulated_sum,
            np.random.rand(self.nb_particles)
        )
        # Resampling the particles according to the indexes above
        self.particles = np.array(
            [ParticleShape(Shape.copy(p.particle))
             for p in self.particles[indexes]]
        )
        # Uniform weights ?
        self.particles_weight.fill(1.0 / self.nb_particles)
        # Update the particles weigths
        self.update_particles_weights()

    # Apply the motion model and make sure that the new position are in the image boundaries
    def ParticlesMotionModel(self):
        # Updating the particles position
        rands = np.random.uniform(-self.object_speed,
                                  self.object_speed, self.particles_position.shape)
        rotats = np.random.uniform(-self.object_rotation_speed,
                                   self.object_rotation_speed,
                                   self.nb_particles)
        for i in range(self.nb_particles):
            # self.particles[i].particle.update(*rands[i], rotats[i])
            self.particles[i].update(rands[i][0], rands[i][1], rotats[i])
        # # ! BUG: sets all the positions to 0
        # self.particles_position[:, 0] = np.maximum(0, np.minimum(
        #     self.image.shape[0] , self.particles_position[:, 0]))
        # self.particles_position[:, 1] = np.maximum(0, np.minimum(
        #     self.image.shape[1] , self.particles_position[:, 1]))

    # Compute the likelihood of a particle with the Kullback-Lieber divergence
    # computed on the target BGR histogram and on the candidate target BGR histogram
    # of the current particle

    def ParticleAppearanceModel(self, frame, particle):
        particle.get_histogram(frame)
        candidate_target_histogram = particle.histogram
        # Calculating the Kullback-Lieber divergence
        kullback_lieber_divergence = cv2.compareHist(self.target_histogram.astype(
            np.float32), candidate_target_histogram.astype(np.float32), cv2.HISTCMP_BHATTACHARYYA)
        particle_likelihood = np.exp(-kullback_lieber_divergence)
        # Updating the current particle likelihood
        particle.likelihood = particle_likelihood
        # return it
        return particle_likelihood

    # Compute the likelihood of every particles
    def ParticlesAppearanceModel(self, frame):
        self.get_particles_likelihood()
        for i in range(self.nb_particles):
            self.particles_likelihood[i] = self.ParticleAppearanceModel(
                frame, self.particles[i])

    # Update all particles weights by multiplying them by their respective likelihood
    # and normalize the newly computed particles weights
    def UpdateParticlesWeight(self):
        self.get_particles_likelihood()
        self.particles_weight = self.particles_weight * self.particles_likelihood
        # keeping the weights under 1
        self.particles_weight = self.particles_weight / \
            np.sum(self.particles_weight)
        self.update_particles_weights()

    # Update target position by multiplying the old particle position
    # with the newly computed weight
    # TODO: Enhance this method
    def UpdateTargetPosition(self):
        self.get_particles_rotation()
        # Extracting the 10 best particles
        best_particles = self.particles[len(
            self.particles)-11: len(self.particles)-1]
        # extractring the rotation of the 10 best particles
        rotats = np.array(
            [p.rotation for p in best_particles]
        )
        # Creating a new particle
        particle = ParticleShape(Shape.copy(self.target_shape))
        # rotating the particle by the mean of rotations
        particle.rotate(np.mean(rotats))

        # getting the first point of each particle from the best particles
        first_points = np.array(
            [np.array(p.particle.points[0].to_tuple()) for p in best_particles])
        # calculating the mean of the points position
        self.particle_mean = np.mean(first_points, axis=0)
        # translating the target particle to the current best location
        particle.translate_to(*self.particle_mean)
        # Setting the target particle to the current target particle
        self.target_particle = particle
        print("particle mean ", self.particle_mean)
        print("Target Particle: ", self.target_particle.particle.center)

    def draw_target(self, frame):
        self.target_particle.particle.draw_shape(frame, thickness=2)
        Point(*self.particle_mean).draw_point(frame)

    def draw_particles(self, frame):
        for p in self.particles[-5:]:
            p.particle.draw_shape(frame, (125, 255, 0))

    def draw_particles_centroid(self, frame):
        for i in range(self.nb_particles):
            self.particles[i].particle.center.draw_point(frame)


# Secondary Methods
    def update_particles_rotation(self):
        for i in range(self.nb_particles):
            self.particles[i].rotate(self.particles_rotation[i])

    def update_particles_position(self):
        for i in range(self.nb_particles):
            self.particles[i].particle.update(
                self.particles_position[i, 0], self.particles_position[i, 1], 0)

    def update_particles_weights(self):
        for p, weight in zip(self.particles, self.particles_weight):
            p.weight = weight

    def get_particles_position(self):
        self.particles_position = np.array(
            [np.array(p.particle.center.to_tuple()) for p in self.particles], dtype=np.float64)

    def get_particles_weights(self):
        self.particles_weight = np.array([p.weight for p in self.particles])

    def get_particles_likelihood(self):
        self.particles_likelihood = np.array(
            [p.likelihood for p in self.particles])

    def get_particles_rotation(self):
        self.particles_rotation = np.array(
            [p.rotation for p in self.particles]
        )
