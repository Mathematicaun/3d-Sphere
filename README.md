# 3D Sphere Visualization

This project demonstrates the mathematical construction of a 3D sphere using Python's `matplotlib` and integrates it into a `customtkinter` interface. The code visualizes the sphere by plotting circular cross-sections in three dimensions.

## Mathematical Framework

### 1. Sphere Definition
A sphere in 3D space is defined as the set of all points that are equidistant from a central point $(X, Y, Z)$. The distance, or radius $r$, from any point on the surface of the sphere to the center is constant and can be expressed by the equation:
$x^2 + y^2 + z^2 = r^2$

### 2. Circle Parameterization
Each circular cross-section of the sphere can be parameterized using polar coordinates:

$x(\rho,\theta)=r\cos(\rho)\cos(\theta)+x_{i}$\
$y(\rho,\theta)=r\cos(\rho)\sin(\theta)+y_{i}$\
$z(\rho)=rsin(\rho)+z_{i}$\
where $\mu_{i}$ is the position on $\mu$ axis and ($\theta$, $\rho$) is a pair that in $[0$, $2\pi]^2$.

### 3. 3D Cross-Sections
The sphere is constructed by plotting circular cross-sections along each of the three axes:

- **Along the Z-axis**: Vary $z$ and compute corresponding $x$ and $y$ values.
$\sqrt{r^2 - z^2} = x(\theta) \quad \text{and} \quad y(\theta)$

- **Along the Y-axis**: Vary $y$ and compute corresponding $x$ and $z$ values.
$\sqrt{r^2 - y^2} = x(\theta) \quad \text{and} \quad z(\theta)$

- **Along the X-axis**: Vary $x$ and compute corresponding $y$ and $z$ values.
$\sqrt{r^2 - x^2} = y(\theta) \quad \text{and} \quad z(\theta)$

### 4. Sphere Construction
To represent the sphere visually, the code iterates through these cross-sections, plotting circles at incremental steps. The combined effect of these cross-sections gives the appearance of a solid sphere.

### 5. Projection
The 3D plot is visualized using a perspective projection, allowing for a more intuitive representation of the sphere. The view is initialized with specific elevation and aspect ratio settings to maintain the correct proportions.

## Integration with `customtkinter`
The `matplotlib` plot is embedded in a `customtkinter` window, providing a modern interface for visualizing the 3D sphere. This integration allows for an interactive display within a desktop application.

## Conclusion
This project offers a mathematical visualization of a 3D sphere, showcasing the power of combining mathematical concepts with Python's visualization libraries. The code serves as a practical example of applying geometry in a programmatic context.

## Author
AYOUB ZAHRAN
