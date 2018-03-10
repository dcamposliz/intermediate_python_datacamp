# Intermediate Python for Data Science
A DataCamp Course (https://campus.datacamp.com/courses/intermediate-python-for-data-science)

* Visualization
* Data Structures
* Control Structures
* Case Study

## Data Visualization

* Very important in Data Analysis
  * Explore data
  * Report insights

We will be using the `matplotlib` package to generate our visualizations.

### Simple Plots

    # importing matplotlib
    import matplotlib.pyplot as plt

    # declaring some lists with numerical elements
    year = [..., ...]
    pop = [..., ...]

    # showing plot (with lines connecting data points)
    plt.plot(year, pop)
    plt.show()

    # showing scatter plot (with dots)
    plt.scatter(year, pop)
    plt.show()

---

Given a list:

    year = [1, 2, 3, 4]
    print(year[-1]) # prints 4

Line plots (`plt.plot()`) are useful when we have a time scale along the horizontal axis. Otherwise, it's probably worthy considering scatterplots.

### Histograms

    # importing matplotlib
    import matplotlib.pyplot as plt

    # 
