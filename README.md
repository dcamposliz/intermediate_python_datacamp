# Intermediate Python for Data Science

* Visualization
* Data Structures
* Control Structures
* Case Study

## Data Visualization

* Very important in Data Analysis
  * Explore data
  * Report insights

matplotlib

    import matplotlib.pyplot as plt

    year = [..., ...]
    pop = [..., ...]

    # shows plot (with lines connecting data points)
    plt.plot(year, pop)
    plt.show()

    # shows scatter plot (with dots)
    plt.scatter(year, pop)
    plt.show()
