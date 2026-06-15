# Derivations and Cheat Sheet: Moment of Inertia

This study resource contains step-by-step derivations of the most frequently tested Moment of Inertia formulas and theorems in High School physics examinations.

---

## 1. Derivation of Moment of Inertia of a Thin Uniform Ring
### Axis of Rotation: Passing through the center and perpendicular to its plane

Let us consider a thin uniform ring of mass $M$ and radius $R$.

```
                 __---""---__
              _-"            "-_
            /                    \
           |          .(O)        |  <-- Axis perpendicular to screen
           |                      |
            \                    /
             "-_              _-"   dm (mass element)
                ""---____---""
```

1. **Mass Distribution:**
   Since the ring is thin, its entire mass is distributed along its circumference of length $2\pi R$.
   Linear mass density ($\lambda$) is:
   $$\lambda = \frac{M}{2\pi R}$$

2. **Selecting a Small Element:**
   Consider an infinitesimal element of length $dl$ on the rim of the ring.
   The mass of this small element is:
   $$dm = \lambda \cdot dl = \frac{M}{2\pi R} dl$$

3. **Perpendicular Distance:**
   Every point on the circumference of the ring is at the same perpendicular distance $r = R$ from the central axis.

4. **Integration:**
   The moment of inertia $I$ of the ring is:
   $$I = \int r^2 dm = \int R^2 dm$$
   Since $R$ is constant for all elements of the ring, we can pull it out of the integral:
   $$I = R^2 \int dm$$
   The sum of all small mass elements $\int dm$ is simply the total mass $M$ of the ring.
   
   Therefore:
   $$I = M R^2$$

---

## 2. Derivation of Moment of Inertia of a Thin Uniform Disc
### Axis of Rotation: Passing through the center and perpendicular to its plane

Let us consider a circular uniform disc of mass $M$ and radius $R$.

```
                   ._________________
                .-'        |         `-.
              /            |            \
             |             | r           |
             |             |-->(dr)      |
             |            (O)            |
              \                         /
                `-._________________.-'
```

1. **Mass Distribution:**
   Since the mass of a disc is distributed over its surface area, we use surface mass density ($\sigma$):
   $$\sigma = \frac{M}{\text{Area}} = \frac{M}{\pi R^2}$$

2. **Selecting a Small Element:**
   We can think of the disc as being made up of many concentric thin rings. Let us select one elemental ring of radius $r$ and thickness $dr$.
   * The circumference of this elemental ring is $2\pi r$.
   * The area of this elemental ring is $dA = \text{circumference} \times \text{thickness} = 2\pi r \cdot dr$.
   * The mass $dm$ of this ring is:
     $$dm = \sigma \cdot dA = \left(\frac{M}{\pi R^2}\right) (2\pi r \cdot dr) = \frac{2M}{R^2} r \cdot dr$$

3. **Moment of Inertia of the Elemental Ring:**
   Using the result from Derivation 1, the moment of inertia of this thin elemental ring of mass $dm$ and radius $r$ is:
   $$dI = dm \cdot r^2 = \left(\frac{2M}{R^2} r \cdot dr\right) r^2 = \frac{2M}{R^2} r^3 dr$$

4. **Integration:**
   To find the total moment of inertia of the disc, we integrate $dI$ from $r = 0$ (the center) to $r = R$ (the outer edge):
   $$I = \int_{0}^{R} \frac{2M}{R^2} r^3 dr$$
   $$I = \frac{2M}{R^2} \int_{0}^{R} r^3 dr = \frac{2M}{R^2} \left[ \frac{r^4}{4} \right]_{0}^{R}$$
   $$I = \frac{2M}{R^2} \left( \frac{R^4}{4} - 0 \right) = \frac{2 M R^4}{4 R^2}$$
   $$I = \frac{1}{2} M R^2$$

---

## 3. Mathematical Proof of the Parallel Axis Theorem
### Theorem: $I = I_{cm} + Md^2$

Let us consider a rigid body of mass $M$. Let $I_{cm}$ be its moment of inertia about an axis passing through its center of mass ($C$), and let $I$ be the moment of inertia about a parallel axis passing through an arbitrary point $O$. The perpendicular distance between these parallel axes is $d$.

```
                  Axis through O        Axis through C (Center of Mass)
                        |                      |
                        | <------- d --------> |
                        |                      |
                     (O)|                      |(C) ----------> P (dm)
                        |                      |      x
                        |                      |
```

1. **Set Up Coordinate System:**
   Let us consider a small mass particle $dm$ at a point $P$. 
   Let the distance of $dm$ from the center of mass axis ($C$) be $x$.
   The distance of $dm$ from the parallel axis through $O$ is:
   $$r = d + x$$

2. **Express Moment of Inertia about O:**
   The moment of inertia $I$ about the axis through $O$ is:
   $$I = \int r^2 dm = \int (d + x)^2 dm$$
   Expand the squared term:
   $$I = \int (d^2 + 2dx + x^2) dm$$
   $$I = \int d^2 dm + \int 2dx dm + \int x^2 dm$$

3. **Analyze Each Integral Term:**
   * **Term 1:** $\int d^2 dm = d^2 \int dm = M d^2$ (since $d$ is constant).
   * **Term 2:** $\int x^2 dm = I_{cm}$ (by definition, since $x$ is the perpendicular distance of $dm$ from the axis passing through the center of mass $C$).
   * **Term 3:** $\int 2dx dm = 2d \int x dm$.
     Recall the definition of center of mass. The sum of the moments of mass about the center of mass is always zero:
     $$\int x dm = 0$$
     Therefore, the middle term $2d \int x dm = 0$.

4. **Combine the Terms:**
   $$I = M d^2 + 0 + I_{cm}$$
   $$I = I_{cm} + M d^2$$
   *(Hence Proved)*

---

## 4. Mathematical Proof of the Perpendicular Axis Theorem
### Theorem: $I_z = I_x + I_y$ (For a planar lamina)

Consider a flat, two-dimensional plate (lamina) lying in the $xy$-plane. 
Let us select an infinitesimal mass element $dm$ at coordinates $(x, y)$.

```
                            Y
                            ^
                            |       dm (x, y)
                            |      /|
                            |     / |
                            |  r /  | y
                            |   /   |
                            |  /    |
                            +-------> X
                            O   x
```

1. **Distances from Axes:**
   * The distance of the particle $dm$ from the $X$-axis is its $y$-coordinate. Thus, the moment of inertia about the $X$-axis is:
     $$I_x = \int y^2 dm$$
   * The distance of the particle $dm$ from the $Y$-axis is its $x$-coordinate. Thus, the moment of inertia about the $Y$-axis is:
     $$I_y = \int x^2 dm$$
   * The distance of the particle $dm$ from the $Z$-axis (which is perpendicular to the $xy$-plane and passes through the origin $O$) is $r$. By Pythagoras' Theorem:
     $$r^2 = x^2 + y^2$$

2. **Express Moment of Inertia about Z-axis:**
   The moment of inertia about the $Z$-axis is:
   $$I_z = \int r^2 dm$$
   Substitute $r^2 = x^2 + y^2$:
   $$I_z = \int (x^2 + y^2) dm$$
   Split the integral:
   $$I_z = \int x^2 dm + \int y^2 dm$$

3. **Substitute the individual moments of inertia:**
   $$I_z = I_y + I_x$$
   $$I_z = I_x + I_y$$
   *(Hence Proved)*
