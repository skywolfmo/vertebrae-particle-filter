<p align="center">
  <a href="" rel="noopener">
 <img src="https://i.imgur.com/g2VvNQM.png" alt="Project logo"></a>
</p>
<h3 align="center">Vertebrae Tracker - Particle Filter</h3>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/skywoflmo/vertebrae-particle-filter.svg)](https://github.com/skywolfmo/vertebrae-particle-filter/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/skywolfmo/vertebrae-particle-filter.svg)](https://github.com/skywolfmo/vertebrae-particle-filter/pulls)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center"> Vertebraes tracking using particle filter with polyroi package.
    <br> 
</p>

## 📝 Table of Contents
- [📝 Table of Contents](#-table-of-contents)
- [🧐 Problem Statement <a name = "problem_statement"></a>](#-problem-statement-)
- [⛓️ Dependencies / Limitations <a name = "limitations"></a>](#️-dependencies--limitations-)
- [🚀 Future Scope <a name = "future_scope"></a>](#-future-scope-)
- [🏁 Getting Started <a name = "getting_started"></a>](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🎈 Usage <a name="usage"></a>](#-usage-)
- [⛏️ Built With <a name = "tech_stack"></a>](#️-built-with-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)
- [🎉 Acknowledgments <a name = "acknowledgments"></a>](#-acknowledgments-)

## 🧐 Problem Statement <a name = "problem_statement"></a>

One of the main problems we face during our tries to track multiple vertebraes is the low quality of image sequences.

- IDEAL: We want to create an application to track multiple vertebraes at the same time. Export the image of each vertebrae during each iterations.

- REALITY: Currently we can track one vertebrae but working on a method to choose the best particle that maximize the likelihood.

- CONSEQUENCES: we will fail to export the best particle's vertebrae images.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- As you increase the instances of particles and trackers, the performence get affected.
- This is one of the setbacks of the particle filter method.

## 🚀 Future Scope <a name = "future_scope"></a>

Create a GUI to help configure the expirements before launch.

## 🏁 Getting Started <a name = "getting_started"></a>

Here are the thisngs you need to have up and ready before using this script.

### Prerequisites

What things you need to install the software and how to install them.

``` shell
pip install cv2
pip install numpy
pip install polyroi 
```

### Installing

You can launch the script using this command.

``` shell
python main.py -v tiw.avi -np 200 -vs 4 -vr 7
```

## 🎈 Usage <a name="usage"></a>

Parameters:

-v : Video

-np : particles number

-vs : Vertebraes speed

-vr : vertebraes rotation

## ⛏️ Built With <a name = "tech_stack"></a>

- [polyroi](https://pypi.org/project/polyroi/) - polyroi
- [opencv](https://opencv.org/) - OpenCV
- [Numpy](https://numpy.org/) - NumPy

## ✍️ Authors <a name = "authors"></a>

- [@skywolfmo](https://github.com/skywolfmo) - Idea & Initial work
- [@SaidiSouad](https://github.com/SaidiSouad) - Collaborator

See also the list of [contributors](https://github.com/skywolfmo/vertebrae-particle-filter/contributors) 
who participated in this project.

## 🎉 Acknowledgments <a name = "acknowledgments"></a>

- https://stackoverflow.com/a/30902423/6512445
- https://stackoverflow.com/questions/15341538/numpy-opencv-2-how-do-i-crop-non-rectangular-region/15343106#15343106
- https://github.com/hbenbel/VOIR
- https://pypi.org/project/polyroi/