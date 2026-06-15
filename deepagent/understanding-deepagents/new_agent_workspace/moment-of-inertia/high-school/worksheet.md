# Moment of Inertia Practice Worksheet

**Subject:** Physics (Rotational Dynamics)  
**Grade Level:** High School (Grades 11-12)  
**Name:** ___________________________  
**Date:** ___________________________  

Show all your steps, coordinate systems, and formulas clearly in your answers.

---

## Section A: Conceptual & Derivation Challenges

### Question 1
Draw a thin uniform ring and a uniform disc of identical mass $M$ and radius $R$. Explain qualitatively (using words and physical reasoning) why the ring has a larger moment of inertia than the disc about their respective central perpendicular axes.

*Your Space for Answer / Sketch:*  
\
\
\
\
\


### Question 2
State the two primary conditions that must be satisfied for the **Parallel Axis Theorem** ($I = I_{cm} + Md^2$) to be valid.

*Your Space for Answer:*  
\
\
\
\


---

## Section B: Numerical Practice Problems

### Problem 1
Two point masses of $3\,\text{kg}$ and $5\,\text{kg}$ are attached to the opposite ends of a light, rigid rod of length $2.0\,\text{m}$ (the mass of the rod is negligible). Find the moment of inertia of this system about an axis perpendicular to the rod and passing through:
1. The midpoint of the rod.
2. The center of mass of the system.

*Your Steps & Calculations:*  
\
\
\
\
\
\


### Problem 2
A uniform solid sphere of mass $4.0\,\text{kg}$ and radius $0.5\,\text{m}$ is rotating about an axis tangent to its surface. 
1. State which theorem of moment of inertia you must use to solve this.
2. Calculate the moment of inertia of the sphere about this tangential axis.

*Your Steps & Calculations:*  
\
\
\
\
\
\


### Problem 3
The moment of inertia of a uniform circular disc of mass $M$ and radius $R$ about a central perpendicular axis is $\frac{1}{2} M R^2$. 
1. Use the Perpendicular Axis Theorem to find its moment of inertia about any diameter axis ($I_{dia}$).
2. Use the Parallel Axis Theorem to find its moment of inertia about a tangent lying in the plane of the disc ($I_{tangent, plane}$).

*Your Steps & Calculations:*  
\
\
\
\
\
\


---

## Section C: Exam-Style Long Question

### Question 3
An engine flywheel has a mass of $50\,\text{kg}$ and its mass is distributed such that its radius of gyration is $0.4\,\text{m}$. 
1. Find the moment of inertia of the flywheel about its axis of rotation.
2. If a constant torque of $20\,\text{N}\cdot\text{m}$ is applied to the flywheel, calculate the angular acceleration ($\alpha$) produced.
3. Determine the rotational kinetic energy of the flywheel when it reaches an angular velocity of $30\,\text{rad/s}$ from rest.

*Your Steps & Calculations:*  
\
\
\
\
\
\


---
---

## Teacher / Parent Answer Key

### Section A: Conceptual & Derivation Answers

#### Question 1 Solution:
The moment of inertia is defined as $I = \int r^2 dm$. It depends on the distance of the mass elements from the axis of rotation.
* In a **ring**, all the mass is concentrated at the outermost circumference (at the maximum distance $r = R$ from the central axis).
* In a **disc**, the mass is distributed continuously from the center ($r = 0$) out to the edge ($r = R$). Much of the disc's mass is closer to the axis, meaning its average perpendicular distance is smaller than $R$.
* Therefore, the ring resists rotation more than the disc of the same mass, making $I_{ring} = M R^2 > I_{disc} = \frac{1}{2} M R^2$.

#### Question 2 Solution:
The two primary conditions are:
1. The two axes must be strictly parallel to one another.
2. One of the two parallel axes must pass through the **center of mass** of the body.

---

### Section B: Numerical Solutions

#### Problem 1 Solution:
1. **About the midpoint of the rod ($d = 2.0\,\text{m}$, so distance to each mass is $1.0\,\text{m}$):**
   $$I = m_1 r_1^2 + m_2 r_2^2$$
   $$I = (3\,\text{kg})(1.0\,\text{m})^2 + (5\,\text{kg})(1.0\,\text{m})^2 = 3(1) + 5(1) = 8\,\text{kg}\cdot\text{m}^2$$

2. **About the center of mass of the system:**
   First, find the position of the center of mass ($x_{cm}$) measuring from the $3\,\text{kg}$ mass ($x=0$):
   $$x_{cm} = \frac{m_1 (0) + m_2 (2.0)}{m_1 + m_2} = \frac{3(0) + 5(2.0)}{3 + 5} = \frac{10}{8} = 1.25\,\text{m}$$
   So, the distance of $3\,\text{kg}$ mass is $r_1 = 1.25\,\text{m}$ and the distance of $5\,\text{kg}$ mass is $r_2 = 2.0 - 1.25 = 0.75\,\text{m}$.
   Now calculate $I_{cm}$:
   $$I_{cm} = m_1 r_1^2 + m_2 r_2^2$$
   $$I_{cm} = (3)(1.25)^2 + (5)(0.75)^2$$
   $$I_{cm} = 3(1.5625) + 5(0.5625) = 4.6875 + 2.8125 = 7.5\,\text{kg}\cdot\text{m}^2$$

#### Problem 2 Solution:
1. **Theorem to use:** Parallel Axis Theorem ($I = I_{cm} + M d^2$).
2. **Calculation:**
   * For a solid sphere about a diameter: $I_{cm} = \frac{2}{5} M R^2$.
   * Perpendicular distance to tangent: $d = R = 0.5\,\text{m}$.
   * Formula:
     $$I_{tangent} = I_{cm} + M d^2 = \frac{2}{5} M R^2 + M R^2 = \frac{7}{5} M R^2$$
     $$I_{tangent} = \frac{7}{5} (4.0\,\text{kg}) (0.5\,\text{m})^2$$
     $$I_{tangent} = 1.4 \times 4.0 \times 0.25 = 1.4 \times 1.0 = 1.4\,\text{kg}\cdot\text{m}^2$$
   * **Answer:** **$1.4\,\text{kg}\cdot\text{m}^2$**

#### Problem 3 Solution:
1. **Moment of inertia about a diameter ($I_{dia}$):**
   * By the Perpendicular Axis Theorem for a flat circular disc in the $xy$-plane: $I_z = I_x + I_y$.
   * By symmetry, the moment of inertia about any two perpendicular diameters is equal: $I_x = I_y = I_{dia}$.
   * Since $I_z = I_{cm} = \frac{1}{2} M R^2$:
     $$\frac{1}{2} M R^2 = I_{dia} + I_{dia} = 2 I_{dia} \implies I_{dia} = \frac{1}{4} M R^2$$

2. **Moment of inertia about a tangent in the plane of the disc ($I_{tangent, plane}$):**
   * This tangent is parallel to the diameter axis, and the perpendicular distance is $d = R$.
   * By the Parallel Axis Theorem:
     $$I_{tangent, plane} = I_{dia} + M R^2$$
     $$I_{tangent, plane} = \frac{1}{4} M R^2 + M R^2 = \frac{5}{4} M R^2$$

---

### Section C: Exam-Style Long Question Solution

#### Question 3 Solution:
1. **Moment of Inertia ($I$):**
   $$I = M k^2$$
   $$I = (50\,\text{kg}) (0.4\,\text{m})^2 = 50 \times 0.16 = 8.0\,\text{kg}\cdot\text{m}^2$$

2. **Angular Acceleration ($\alpha$):**
   Using Newton's second law for rotation:
   $$\tau = I \alpha \implies \alpha = \frac{\tau}{I}$$
   $$\alpha = \frac{20\,\text{N}\cdot\text{m}}{8.0\,\text{kg}\cdot\text{m}^2} = 2.5\,\text{rad/s}^2$$

3. **Rotational Kinetic Energy ($K_{rot}$):**
   $$K_{rot} = \frac{1}{2} I \omega^2$$
   $$K_{rot} = \frac{1}{2} (8.0\,\text{kg}\cdot\text{m}^2) (30\,\text{rad/s})^2$$
   $$K_{rot} = 4.0 \times 900 = 3600\,\text{J}$$
   * **Answer:** **$3600\,\text{Joules}$** (or $3.6\,\text{kJ}$)
