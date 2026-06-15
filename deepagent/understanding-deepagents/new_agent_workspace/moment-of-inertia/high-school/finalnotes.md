# Rotational Mechanics: Moment of Inertia (Rotational Inertia)

## Learning Objectives

By the end of these study notes, students should be able to:
* Define **Moment of Inertia ($I$)** and explain its physical significance as the rotational analogue of mass.
* State and apply the formula for the moment of inertia of both discrete particle systems and continuous rigid bodies.
* State, prove, and apply the **Parallel Axis Theorem** and **Perpendicular Axis Theorem**.
* Calculate the moment of inertia for standard geometric bodies (thin rod, ring, disc, sphere, and cylinder) about different axes of rotation.
* Define and compute the **Radius of Gyration ($k$)**.
* Solve numerical and conceptual examination problems relating moment of inertia to torque, angular acceleration, and rotational kinetic energy.

---

## Introduction

In linear motion, we know that an object resists any change in its state of rest or uniform motion. This property is called **inertia**, and it is measured solely by the object's **mass ($m$)**. A heavier object requires a larger force to achieve the same linear acceleration as a lighter object ($F = ma$).

When we transition to rotational motion, a similar resistance is observed. A stationary wheel resists being spun, and a spinning wheel resists being stopped. This resistance to rotational change is called **Rotational Inertia** or, more formally, the **Moment of Inertia ($I$)**. 

Unlike mass, which is a constant property of a body (at non-relativistic speeds), the moment of inertia of a body is **not** constant. It depends not only on the mass of the body, but also on **how that mass is distributed** relative to the **axis of rotation**. Consequently, a single body can have infinitely many moments of inertia, depending on the axis about which it rotates. 

Mathematically, moment of inertia links torque ($\tau$) and angular acceleration ($\alpha$) through the rotational version of Newton's Second Law: 
$$\tau = I \alpha$$

---

## Key Terminology

| Term | Definition | S.I. Unit / Dimensions |
| :--- | :--- | :--- |
| **Moment of Inertia ($I$)** | The measure of a body's resistance to rotational acceleration about a specific axis. | $kg \cdot m^2$ <br> Dimensions: $[M L^2 T^0]$ |
| **Axis of Rotation** | The straight line about which all particles of a rigid body move in circular paths during rotation. | Dimensionless |
| **Rigid Body** | A body with a perfectly definite and unchanging shape, where the distances between all constituent particles remain constant. | N/A |
| **Radius of Gyration ($k$)** | The radial distance from the axis of rotation to a point where the entire mass of the body can be assumed to be concentrated, giving the same moment of inertia. | $m$ <br> Dimensions: $[M^0 L T^0]$ |
| **Torque ($\tau$)** | The turning or twisting action of a force that tends to cause rotation about an axis. | $N \cdot m$ or $J$ <br> Dimensions: $[M L^2 T^{-2}]$ |
| **Angular Acceleration ($\alpha$)** | The rate of change of angular velocity with respect to time. | $rad/s^2$ <br> Dimensions: $[M^0 L^0 T^{-2}]$ |

---

## Core Concepts

### Concept 1: Point Mass and Discrete Particle Systems

#### Explanation
For a single point mass $m$ moving in a circle of radius $r$ about a fixed axis of rotation, the moment of inertia is defined as:
$$I = m r^2$$

Where:
* $m$ = mass of the particle
* $r$ = **perpendicular distance** of the particle from the axis of rotation.

For a system consisting of multiple discrete particles of masses $m_1, m_2, m_3, \dots, m_n$ located at perpendicular distances $r_1, r_2, r_3, \dots, r_n$ from the axis of rotation, the total moment of inertia is the scalar sum of the individual moments of inertia:
$$I = m_1 r_1^2 + m_2 r_2^2 + m_3 r_3^2 + \dots + m_n r_n^2 = \sum_{i=1}^{n} m_i r_i^2$$

#### Factors Affecting Moment of Inertia
1. **Mass of the body ($M$):** Directly proportional ($I \propto M$).
2. **Distribution of mass:** Mass farther from the axis of rotation increases $I$ exponentially because of the $r^2$ term.
3. **Position and orientation of the axis of rotation:** Changing the axis changes the perpendicular distances ($r_i$), which changes $I$.

---

### Concept 2: Continuous Rigid Bodies

#### Explanation
A rigid body is composed of a continuous distribution of mass. To find its moment of inertia, we divide the body into infinitesimally small mass elements ($dm$) located at a perpendicular distance $r$ from the axis of rotation. The sum of the moments of inertia of these elements is found using integration:
$$I = \int r^2 dm$$

To perform this integration, we relate the mass element $dm$ to spatial dimensions using density:
* **Linear Mass Density ($\lambda = \frac{dm}{dx}$)** for 1D objects (thin rods, rings).
* **Surface Mass Density ($\sigma = \frac{dm}{dA}$)** for 2D objects (discs, flat plates).
* **Volume Mass Density ($\rho = \frac{dm}{dV}$)** for 3D objects (spheres, cylinders).

---

### Concept 3: Radius of Gyration ($k$)

#### Explanation
The **Radius of Gyration ($k$)** is the distance from the axis of rotation to a point where, if the entire mass $M$ of the body were concentrated, the moment of inertia would remain the same as the actual mass distribution.

Thus:
$$I = M k^2 \implies k = \sqrt{\frac{I}{M}}$$

#### Physical Significance
* It represents the "effective distance" of the mass of the rigid body from the rotation axis.
* A small $k$ means the mass is distributed close to the axis (easy to rotate).
* A large $k$ means the mass is distributed far from the axis (difficult to rotate).

---

### Concept 4: Important Theorems of Moment of Inertia

To find the moment of inertia of a body about an arbitrary axis, we use two fundamental theorems:

#### 1. Parallel Axis Theorem
* **Statement:** The moment of inertia of a body about any axis is equal to the sum of its moment of inertia about a parallel axis passing through its center of mass ($I_{cm}$) and the product of the total mass ($M$) of the body and the square of the perpendicular distance ($d$) between the two parallel axes.
* **Formula:** 
$$I = I_{cm} + M d^2$$

```
       Axis through CM         Parallel Axis
             |                      |
             |  <----- d ----->     |
             |                      |
         (o) |                      |
        /   \|                      |
       |  CM |                      |
        \___/                       |
             |                      |
             |                      |
```
* **Conditions:** 
  * The two axes must be strictly parallel.
  * One of the parallel axes **must** pass through the center of mass of the body.
  * Applicable to all types of bodies (1D, 2D, and 3D).

#### 2. Perpendicular Axis Theorem
* **Statement:** For a planar body (planar lamina), the moment of inertia about an axis perpendicular to its plane ($I_z$) is equal to the sum of its moments of inertia about two mutually perpendicular axes ($I_x$ and $I_y$) lying in its plane, all three axes intersecting at a common origin.
* **Formula:**
$$I_z = I_x + I_y$$

```
               Z-axis (Perpendicular to plane)
               ^
               |
               |     / Y-axis (In-plane)
               |    /
               |   / 
               |  /   . (Mass element dm)
               | /  
               |/__________> X-axis (In-plane)
               Origin (O)
```
* **Conditions:**
  * Only applicable to **two-dimensional (flat) objects** (laminas, rings, discs, thin sheets).
  * It **cannot** be applied to three-dimensional objects like spheres or cylinders.
  * The three axes must be mutually perpendicular and meet at a single point.

---

### Concept 5: Standard Shapes Reference Table

The following moments of inertia are standard results derived about specific axes and are essential for examinations:

| Body | Axis of Rotation | Moment of Inertia ($I$) | Radius of Gyration ($k$) |
| :--- | :--- | :---: | :---: |
| **Thin Uniform Rod** (Length $L$) | Through center, perpendicular to length | $\frac{1}{12} M L^2$ | $\frac{L}{\sqrt{12}}$ |
| **Thin Uniform Rod** (Length $L$) | Through one end, perpendicular to length | $\frac{1}{3} M L^2$ | $\frac{L}{\sqrt{3}}$ |
| **Circular Ring** (Radius $R$) | Central axis, perpendicular to plane | $M R^2$ | $R$ |
| **Circular Ring** (Radius $R$) | About any diameter | $\frac{1}{2} M R^2$ | $\frac{R}{\sqrt{2}}$ |
| **Circular Disc** (Radius $R$) | Central axis, perpendicular to plane | $\frac{1}{2} M R^2$ | $\frac{R}{\sqrt{2}}$ |
| **Circular Disc** (Radius $R$) | About any diameter | $\frac{1}{4} M R^2$ | $\frac{R}{2}$ |
| **Solid Cylinder** (Radius $R$) | Central longitudinal axis | $\frac{1}{2} M R^2$ | $\frac{R}{\sqrt{2}}$ |
| **Hollow Cylinder** (Radius $R$) | Central longitudinal axis | $M R^2$ | $R$ |
| **Solid Sphere** (Radius $R$) | About any diameter | $\frac{2}{5} M R^2$ | $\sqrt{\frac{2}{5}} R$ |
| **Spherical Shell** (Radius $R$) | About any diameter | $\frac{2}{3} M R^2$ | $\sqrt{\frac{2}{3}} R$ |

---

## Diagram Descriptions

When studying the moment of inertia, drawing the axis of rotation clearly is crucial. Here are visual descriptions of standard axes:

1. **Thin Rod Axis through Center vs. End:**
   * **Center Axis:** Imagine a long ruler spinning like a helicopter propeller around a pin pushed through its exact center. The mass is distributed symmetrically on both sides of the pin.
   * **End Axis:** Imagine swinging a baseball bat around your wrist. The axis is at one extreme end, and the rest of the mass is distributed far away, making it significantly harder to swing than spinning it through the center ($I_{end} = 4 \times I_{center}$).

2. **RingCentral Axis vs. Diameter Axis:**
   * **Central Axis (Perpendicular):** Imagine a bicycle wheel spinning on its axle. Every bit of mass in the rim is at the exact same distance ($R$) from the axle. Thus, $I = M R^2$.
   * **Diameter Axis (In-Plane):** Imagine spinning a coin on a table, or flipping a hula hoop. The axis cuts straight through the circle, dividing it in half. Some parts of the hoop are near the axis, and others are far, leading to a smaller moment of inertia ($I = \frac{1}{2} M R^2$).

---

## Important Formulas

### Rotational Dynamics Connections

#### 1. Rotational Kinetic Energy ($K_{rot}$)
$$K_{rot} = \frac{1}{2} I \omega^2$$
Where $\omega$ is the angular velocity ($rad/s$).

#### 2. Torque and Angular Acceleration
$$\tau = I \alpha$$
Where $\alpha$ is the angular acceleration ($rad/s^2$).

#### 3. Angular Momentum ($L$)
$$L = I \omega$$
Under zero external torque ($\tau_{ext} = 0$), angular momentum is conserved:
$$I_1 \omega_1 = I_2 \omega_2$$

---

## Worked Examples

### Example 1: Discrete System of Particles
**Problem:** Three point masses $m_1 = 1\,\text{kg}$, $m_2 = 2\,\text{kg}$, and $m_3 = 3\,\text{kg}$ are placed at the vertices of an equilateral triangle of side length $a = 2\,\text{m}$. Find the moment of inertia of this system about an axis passing through $m_1$ and perpendicular to the plane of the triangle.

**Step-by-Step Solution:**
1. **Identify the axis:** The axis is perpendicular to the plane, passing through the point mass $m_1$.
2. **Find the perpendicular distances ($r_i$) of each mass from the axis:**
   * For $m_1$: Since the axis passes through $m_1$, the distance $r_1 = 0\,\text{m}$.
   * For $m_2$: The distance is the length of the side of the equilateral triangle, so $r_2 = a = 2\,\text{m}$.
   * For $m_3$: Similarly, the distance is the length of the side of the triangle, so $r_3 = a = 2\,\text{m}$.
3. **Apply the formula for a discrete system:**
   $$I = m_1 r_1^2 + m_2 r_2^2 + m_3 r_3^2$$
   $$I = (1\,\text{kg})(0\,\text{m})^2 + (2\,\text{kg})(2\,\text{m})^2 + (3\,\text{kg})(2\,\text{m})^2$$
   $$I = 0 + (2 \times 4) + (3 \times 4)$$
   $$I = 8 + 12 = 20\,\text{kg}\cdot\text{m}^2$$

* **Answer:** The moment of inertia of the system is **$20\,\text{kg}\cdot\text{m}^2$**.

---

### Example 2: Deriving the Moment of Inertia of a Thin Rod (Central Axis)
**Problem:** Derive the moment of inertia of a uniform thin rod of mass $M$ and length $L$ about an axis passing through its center and perpendicular to its length.

```
                  Axis of Rotation (x = 0)
                            |
           <---- L/2 ---->  |  <---- L/2 ---->
       |====================|====================|
      -L/2                  |  dx                L/2
                            |<-- x --> [dm]
```

**Step-by-Step Solution:**
1. **Define mass density:** Since the rod is uniform and 1D, its linear mass density $\lambda$ is:
   $$\lambda = \frac{M}{L}$$
2. **Select an element:** Let us consider a small element of length $dx$ at a distance $x$ from the center (origin, $x = 0$).
   The mass of this element is:
   $$dm = \lambda dx = \frac{M}{L} dx$$
3. **Set up the integral:** The limits of integration will be from $x = -\frac{L}{2}$ to $x = \frac{L}{2}$ since the center is at $x=0$.
   $$I = \int r^2 dm = \int_{-L/2}^{L/2} x^2 \left(\frac{M}{L} dx\right)$$
4. **Evaluate the integral:**
   $$I = \frac{M}{L} \int_{-L/2}^{L/2} x^2 dx = \frac{M}{L} \left[ \frac{x^3}{3} \right]_{-L/2}^{L/2}$$
   $$I = \frac{M}{3L} \left[ \left(\frac{L}{2}\right)^3 - \left(-\frac{L}{2}\right)^3 \right]$$
   $$I = \frac{M}{3L} \left[ \frac{L^3}{8} - \left(-\frac{L^3}{8}\right) \right]$$
   $$I = \frac{M}{3L} \left[ \frac{2L^3}{8} \right] = \frac{M}{3L} \left[ \frac{L^3}{4} \right] = \frac{1}{12} M L^2$$

* **Answer:** **$I = \frac{1}{12} M L^2$**

---

### Example 3: Applying the Parallel Axis Theorem
**Problem:** Find the moment of inertia of the same uniform thin rod of mass $M$ and length $L$ about an axis passing through one of its ends and perpendicular to its length.

**Step-by-Step Solution:**
1. **Identify parameters for the Parallel Axis Theorem:**
   * The moment of inertia about the parallel axis through the center of mass is $I_{cm} = \frac{1}{12} M L^2$.
   * The perpendicular distance between the central axis and the end axis is $d = \frac{L}{2}$.
2. **Apply the theorem:**
   $$I_{end} = I_{cm} + M d^2$$
   $$I_{end} = \frac{1}{12} M L^2 + M \left(\frac{L}{2}\right)^2$$
   $$I_{end} = \frac{1}{12} M L^2 + \frac{1}{4} M L^2$$
3. **Find a common denominator:**
   $$I_{end} = \left(\frac{1}{12} + \frac{3}{12}\right) M L^2 = \frac{4}{12} M L^2 = \frac{1}{3} M L^2$$

* **Answer:** **$I_{end} = \frac{1}{3} M L^2$**
* **Common Student Mistake:** Forgetting to square the distance $d$, or choosing an incorrect $d$ value. Ensure $d$ is the perpendicular distance between parallel axes.

---

## Real-World Applications

Moment of inertia plays an essential role in technology, nature, and sports:

1. **The Figure Skater's Spin:**
   When a figure skater wants to spin faster (increase angular velocity $\omega$), they pull their arms and legs close to their body. This moves their mass closer to the rotation axis, decreasing their moment of inertia ($I$). Since there is no external torque, angular momentum ($L = I\omega$) must remain constant, causing them to spin rapidly. Extending their arms increases $I$, slowing them down instantly.

2. **Tightrope Walkers:**
   Tightrope walkers carry a long, heavy pole. By carrying a long pole, they distribute mass far from their body, which dramatically increases their moment of inertia ($I$). If they begin to tip, the large $I$ slows down their rotation (reduces angular acceleration $\alpha$ for any given torque), giving them plenty of time to make minor adjustments and maintain balance.

3. **Engine Flywheels:**
   Engines do not produce power continuously; instead, they deliver energy in pulses. A flywheel is a heavy, large-diameter wheel attached to the engine's driveshaft. Because of its large mass and radius, it has a very high moment of inertia. It stores rotational energy during power strokes and releases it smoothly during non-power phases, preventing jerky motions.

---

## Common Misconceptions

### Misconception 1: "A body has only one moment of inertia."
* **Correction:** False! A body has only one mass, but it has infinite moments of inertia. The value depends entirely on the location and orientation of the axis of rotation.

### Misconception 2: "Moment of Inertia is a vector quantity because it involves rotation."
* **Correction:** False. Moment of Inertia is a **scalar quantity** (strictly speaking, a tensor of rank 2, but at high school level, it is treated as a scalar). It has no specific direction, though it is defined relative to an axis.

### Misconception 3: "The Perpendicular Axis Theorem can be applied to any 3D body."
* **Correction:** No! This is a major source of lost marks in exams. The perpendicular axis theorem ($I_z = I_x + I_y$) is **only** valid for flat, planar laminas (2D objects). It cannot be used for solid spheres, cubes, or cylinders.

---

## Exam Focus

### Highly Tested Concepts
* **Derivations:** Deriving the moment of inertia of a thin rod (about center/end) or a ring/disc about its central axis.
* **Theorems:** Applying Parallel and Perpendicular axis theorems to find $I$ about tangents, diameters, or ends of shapes.
* **Ratio Problems:** Comparing the moments of inertia of two different shapes with the same mass and radius (e.g., $I_{ring} : I_{disc} = 2:1$).
* **Radius of Gyration:** Calculating $k$ for different objects and understanding how changing the axis affects $k$.

### Revision Formula Cheat Sheet for Exams

* **Ring (central axis):** $I = M R^2 \implies k = R$
* **Disc (central axis):** $I = \frac{1}{2} M R^2 \implies k = \frac{R}{\sqrt{2}}$
* **Thin Rod (center):** $I = \frac{1}{12} M L^2 \implies k = \frac{L}{\sqrt{12}}$
* **Solid Sphere (diameter):** $I = \frac{2}{5} M R^2 \implies k = \sqrt{\frac{2}{5}} R$
* **Hollow Sphere (diameter):** $I = \frac{2}{3} M R^2 \implies k = \sqrt{\frac{2}{3}} R$

---

## Key Points Summary

1. **Moment of Inertia ($I$)** measures a body's resistance to rotational acceleration, acting as the rotational counterpart to mass.
2. The S.I. unit of moment of inertia is **$kg \cdot m^2$** and its dimensional formula is **$[M L^2 T^0]$**.
3. For a discrete system of point masses, $I = \sum m_i r_i^2$, where $r_i$ is the perpendicular distance to the rotation axis.
4. For a continuous mass distribution, $I = \int r^2 dm$.
5. $I$ depends on the total mass, the distribution of mass relative to the axis, and the orientation of the axis of rotation.
6. The **Radius of Gyration ($k$)** is the distance where the entire mass can be concentrated to yield the same $I$ ($I = M k^2$).
7. The **Parallel Axis Theorem** states $I = I_{cm} + Md^2$ and applies to all rigid bodies.
8. The **Perpendicular Axis Theorem** states $I_z = I_x + I_y$ and applies **only** to flat, two-dimensional laminas.
9. A ring has a higher moment of inertia than a disc of the same mass and radius because all of the ring's mass is concentrated at its outermost edge.
10. Rotational kinetic energy is given by $K_{rot} = \frac{1}{2} I \omega^2$ and angular momentum is $L = I \omega$.

---

## Quick Revision Questions (Very Short Answer)

**Q1: What is the physical significance of the moment of inertia?**
* **A:** It measures a body's resistance to any change in its rotational state. It is the rotational analogue of mass.

**Q2: Why does a cycle wheel have spokes?**
* **A:** Spokes support the rim, allowing most of the wheel's mass to be concentrated at the outer rim. This increases the wheel's moment of inertia, ensuring a smoother ride by resisting sudden speed changes.

**Q3: State the unit and dimensions of the Radius of Gyration.**
* **A:** Unit: meter ($m$). Dimensions: $[M^0 L T^0]$.

**Q4: Can we apply the perpendicular axis theorem to find the moment of inertia of a solid sphere? Explain.**
* **A:** No. The perpendicular axis theorem is only applicable to 2D planar bodies, whereas a solid sphere is a 3D object.

**Q5: How does the moment of inertia of a body change if its mass is distributed closer to the axis of rotation?**
* **A:** The moment of inertia decreases because the perpendicular distances ($r$) of the mass elements decrease ($I \propto r^2$).

---

## Practice Questions

### Multiple Choice Questions

1. The moment of inertia of a solid cylinder of mass $M$ and radius $R$ about its central longitudinal axis is:
   * A) $M R^2$
   * B) $\frac{1}{2} M R^2$
   * C) $\frac{2}{5} M R^2$
   * D) $\frac{2}{3} M R^2$

2. If a ring and a disc have the same mass and same radius, which one has a larger moment of inertia about its central axis?
   * A) The disc
   * B) The ring
   * C) Both have the same
   * D) It depends on their material density

3. The radius of gyration of a uniform thin rod of length $L$ about an axis passing through its center and perpendicular to its length is:
   * A) $L/2$
   * B) $L/\sqrt{12}$
   * C) $L/\sqrt{3}$
   * D) $L/12$

4. A circular disc of mass $M$ and radius $R$ has a moment of inertia $I$ about its central axis. If its radius is doubled keeping the mass constant, its new moment of inertia about the same axis will be:
   * A) $2I$
   * B) $4I$
   * C) $I/2$
   * D) $I/4$

5. The parallel axis theorem formula is written as $I = I_{cm} + Md^2$. What does $d$ represent?
   * A) The diameter of the rotating body
   * B) The radius of gyration
   * C) The perpendicular distance between the two parallel axes
   * D) The distance from the center of mass to the outermost edge

---

### Fill in the Blanks

1. The rotational analogue of force is torque, and the rotational analogue of mass is __________.
2. The perpendicular axis theorem is applicable only to __________ bodies.
3. If no external torque acts on a rotating system, its __________ momentum remains conserved.
4. The moment of inertia of a solid sphere about its diameter is given by the formula __________.
5. The S.I. unit of the moment of inertia is __________.

---

### Short Answer Questions

1. Explain why flywheels are made heavy at the rim and thin at the center.
2. Two identical iron discs are taken. One is heated until it expands slightly in diameter. Which disc will have a larger moment of inertia about its central axis? Why?
3. State and explain the Parallel Axis Theorem with a suitable labeled diagram description.
4. Derive the relation between torque ($\tau$), moment of inertia ($I$), and angular acceleration ($\alpha$).

---

### Long Answer Questions

1. State the Perpendicular Axis Theorem. Use it to derive the moment of inertia of a thin circular disc about one of its diameters, given that its moment of inertia about its central axis is $\frac{1}{2} M R^2$.
2. (a) Define Radius of Gyration.
   (b) Derive the expression for the moment of inertia of a uniform circular ring of mass $M$ and radius $R$ about:
     * (i) A tangent perpendicular to its plane.
     * (ii) A tangent in its plane.

---

### Numerical Problems

**P1:** Four point masses, each of mass $m = 0.5\,\text{kg}$, are placed at the four corners of a square of side $a = 1.2\,\text{m}$. Calculate the moment of inertia of the system about an axis passing through the center of the square and perpendicular to its plane.

**P2:** A thin uniform rod of mass $2\,\text{kg}$ and length $1.5\,\text{m}$ is rotating about an axis passing through its center and perpendicular to its length at an angular speed of $10\,\text{rad/s}$. Calculate its rotational kinetic energy.

**P3:** Find the ratio of the radius of gyration of a solid sphere to that of a hollow sphere (spherical shell), both of same mass and radius, about their respective diameters.

**P4:** The moment of inertia of a uniform circular disc about its central axis is $0.8\,\text{kg}\cdot\text{m}^2$. What is its moment of inertia about a tangent parallel to its diameter?

---

### Higher-Order Thinking Questions (HOTS)

1. A cat falling from a height is famous for always landing on its feet. How does the cat utilize the conservation of angular momentum and variations in its moment of inertia to turn its body mid-air?
2. If the polar ice caps melt due to global warming, water will flow from the poles toward the equator. What effect will this redistribution of mass have on the duration of a day on Earth? Explain using physical principles.
3. Why is it easier to fold your legs while running fast? Relate this to the moment of inertia.

---

## Answers to Practice Material

### Multiple Choice Answers
1. **B) $\frac{1}{2} M R^2$** (Standard longitudinal axis formula).
2. **B) The ring** (The ring has all its mass at distance $R$, whereas the disc has mass distributed from $0$ to $R$, yielding $I_{ring} = M R^2 > I_{disc} = \frac{1}{2} M R^2$).
3. **B) $L/\sqrt{12}$** (Since $I = \frac{1}{12} M L^2 = M k^2 \implies k = \frac{L}{\sqrt{12}}$).
4. **B) $4I$** (Since $I \propto R^2$, doubling the radius increases the moment of inertia by $2^2 = 4$ times).
5. **C) The perpendicular distance between the two parallel axes**.

### Fill in the Blanks Answers
1. **moment of inertia** (or rotational inertia)
2. **planar** (or 2D / lamina)
3. **angular**
4. **$\frac{2}{5} M R^2$**
5. **$kg\cdot m^2$**

### Short Answer Answers (Key Points)
1. By placing the bulk of the mass at the outer rim, the perpendicular distance $r$ of the mass from the rotation axis is maximized. Since $I = \int r^2 dm$, this maximizes the moment of inertia for a given mass, allowing the flywheel to store maximum rotational energy ($K_{rot} = \frac{1}{2}I\omega^2$) and effectively smooth out fluctuations.
2. The expanded disc will have a larger moment of inertia. When the disc expands, its particles move farther away from the central axis of rotation. Since the mass remains constant but the distance $r$ increases, the term $\sum mr^2$ increases, resulting in a larger moment of inertia.
3. *Refer to Concept 4's Parallel Axis Theorem section for statement and formula.* The diagram shows two parallel lines, one running through the center of mass (labeled CM) and another running through an arbitrary point. The distance $d$ is shown as a perpendicular line bridging the two parallel axes.
4. Consider a rigid body rotating with angular acceleration $\alpha$. It consists of particles of masses $m_1, m_2, \dots$ at distances $r_1, r_2, \dots$ from the axis.
   The linear acceleration of particle $i$ is $a_i = r_i \alpha$.
   The force on this particle is $F_i = m_i a_i = m_i r_i \alpha$.
   The torque on this particle is $\tau_i = F_i r_i = m_i r_i^2 \alpha$.
   The total torque is the sum of individual torques:
   $$\tau = \sum \tau_i = \sum (m_i r_i^2 \alpha) = \left(\sum m_i r_i^2\right) \alpha$$
   Since $I = \sum m_i r_i^2$, we get **$\tau = I \alpha$**.

### Numerical Problem Solutions
**P1 Solution:**
* Distance of each corner from the center of a square of side $a$ is:
  $$r = \frac{\text{Diagonal}}{2} = \frac{\sqrt{2}a}{2} = \frac{a}{\sqrt{2}}$$
* For $a = 1.2\,\text{m}$, we have $r = \frac{1.2}{\sqrt{2}}\,\text{m}$.
* Total moment of inertia of 4 identical masses $m = 0.5\,\text{kg}$:
  $$I = 4 \times (m r^2) = 4 \times 0.5 \times \left(\frac{1.2}{\sqrt{2}}\right)^2$$
  $$I = 2 \times \frac{1.44}{2} = 1.44\,\text{kg}\cdot\text{m}^2$$
* **Answer:** **$1.44\,\text{kg}\cdot\text{m}^2$**

**P2 Solution:**
* Given: $M = 2\,\text{kg}$, $L = 1.5\,\text{m}$, $\omega = 10\,\text{rad/s}$.
* Moment of inertia about the center:
  $$I = \frac{1}{12} M L^2 = \frac{1}{12} (2) (1.5)^2 = \frac{1}{6} \times 2.25 = 0.375\,\text{kg}\cdot\text{m}^2$$
* Rotational Kinetic Energy:
  $$K_{rot} = \frac{1}{2} I \omega^2 = \frac{1}{2} (0.375) (10)^2 = \frac{1}{2} \times 0.375 \times 100 = 18.75\,\text{J}$$
* **Answer:** **$18.75\,\text{Joules}$**

**P3 Solution:**
* For a solid sphere: $I_{solid} = \frac{2}{5} M R^2 = M k_{solid}^2 \implies k_{solid} = \sqrt{\frac{2}{5}} R$
* For a hollow sphere: $I_{hollow} = \frac{2}{3} M R^2 = M k_{hollow}^2 \implies k_{hollow} = \sqrt{\frac{2}{3}} R$
* Ratio of radii of gyration:
  $$\frac{k_{solid}}{k_{hollow}} = \frac{\sqrt{2/5} R}{\sqrt{2/3} R} = \sqrt{\frac{2}{5} \times \frac{3}{2}} = \sqrt{\frac{3}{5}}$$
* **Answer:** **$\sqrt{3} : \sqrt{5}$** (or approximately $0.775 : 1$)

**P4 Solution:**
* Given $I_{cm} = 0.8\,\text{kg}\cdot\text{m}^2$ (about central perpendicular axis).
* Central central perpendicular axis $I_{cm} = \frac{1}{2} M R^2 = 0.8 \implies M R^2 = 1.6\,\text{kg}\cdot\text{m}^2$.
* We need the moment of inertia about a tangent parallel to its diameter.
* First, find $I$ about a diameter ($I_{dia}$):
  $$I_{dia} = \frac{1}{4} M R^2 = \frac{1.6}{4} = 0.4\,\text{kg}\cdot\text{m}^2$$
* Now apply Parallel Axis Theorem to find the moment of inertia about a parallel tangent at distance $d = R$:
  $$I_{tangent} = I_{dia} + M R^2$$
  $$I_{tangent} = 0.4 + 1.6 = 2.0\,\text{kg}\cdot\text{m}^2$$
* **Answer:** **$2.0\,\text{kg}\cdot\text{m}^2$**

### Higher-Order Thinking Solutions (HOTS)
1. A falling cat dynamically changes its shape to alter its moment of inertia in sections. By pulling in its front paws while extending its back legs, it reduces the moment of inertia of its front half relative to its back half. This allows it to twist its front body with very little torque. It then reverses the process (extends front paws and tucks back legs) to align its back half, resulting in a net rotation of 180 degrees while maintaining a total angular momentum of zero.
2. The melting of polar ice caps and the subsequent movement of water to the equator relocates mass farther from the Earth's rotational axis (as the equatorial radius is larger than the polar radius). This redistribution increases the Earth's moment of inertia ($I$). By conservation of angular momentum ($I\omega = \text{constant}$), an increase in $I$ results in a decrease in angular speed ($\omega$). A slower rotation means the Earth takes longer to complete one rotation, thereby **increasing the length of a day**.
3. Folding your legs during a run pulls the mass of your legs closer to your hip joints (the axis of rotation for the leg movement). This dramatically decreases the moment of inertia ($I$) of your legs about the hip. Since $I$ is reduced, the torque required from your hip muscles to swing your leg forward is much lower ($\tau = I\alpha$), reducing muscle fatigue and enabling a faster stride rate.

---

## Summary

The **Moment of Inertia ($I$)** represents the rotational inertia of a rigid body, serving as the rotational analogue to mass in linear motion. It quantifies a system's resistance to angular acceleration and depends fundamentally on the mass, the shape, and crucially, the spatial distribution of mass relative to the axis of rotation. 

Two powerful mathematical tools, the **Parallel Axis Theorem** ($I = I_{cm} + Md^2$) and the **Perpendicular Axis Theorem** ($I_z = I_x + I_y$), allow for the calculation of rotational inertia about any axis once the central moments of inertia are known. Understanding this concept is central to analyzing rotational dynamics, engineering stable machinery, and explaining everyday phenomena such as gyroscopes, athletic twists, and astronomical rotations.
