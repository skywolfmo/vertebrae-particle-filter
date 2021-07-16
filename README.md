<p align="center">
  <a href="" rel="noopener">
 <img src="https://i.imgur.com/AZ2iWek.png" alt="Project logo"></a>
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
- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Dependencies / Limitations](#limitations)
- [Future Scope](#future_scope)
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

One of the main problems we face during our tries to track multiple vertebraes is the low quality of image sequences.

The aim of this article is to tackle this problem by proposing a method for rigid object tracking based on the fragmentation of the tracked object. The proposed method is based on the particle filter using the calculation of the similarity between the respective fragments of objectsinstead of the whole objects.
The similarity measures used are the Jaccard index, the correlation coefficient, and the Bhattacharyya coefficient. The tracking starts with a semi-automatic initialization. The results show that the fragments-based object tracking method outperforms the classical method (without fragmentation) for each of the used similarity measures. The results show that the tracking based on the Jaccard index is more stable and outperforms methods based on other similarity measures.

- IDEAL: This section is used to describe the desired or “to be” state of the process or product. At large, this section should illustrate what the expected environment would look like once the solution is implemented.
- REALITY: This section is used to describe the current or “as is” state of the process or product.
- CONSEQUENCES: This section is used to describe the impacts on the business if the problem is not fixed or improved upon.
This includes costs associated with loss of money, time, productivity, competitive advantage, and so forth.

Following this format will result in a workable document that can be used to understand the problem and elicit
requirements that will lead to a winning solution. 

## 💡 Idea / Solution <a name = "idea"></a>

This section is used to describe potential solutions. 

Once the ideal, reality, and consequences sections have been.
completed, and understood, it becomes easier to provide a solution for solving the problem.

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>

- What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if 
appropriate, describe how these limitations could point to the need for further research.

## 🚀 Future Scope <a name = "future_scope"></a>

Write about what you could not develop during the course of the Hackathon; and about what your project can achieve 
in the future.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
pip install cv2
pip install numpy
pip install polyroi 
```

### Installing


``` shell
python main.py -v tiw.avi -np 200 -vs 4 -vr 7
```

## 🎈 Usage <a name="usage"></a>

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