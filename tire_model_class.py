import numpy as np
from dataclasses import dataclass
ZeroVector = [0,0,0]
 @dataclass
 class Tire:
     weight: float
     radius: float
     width: float
     rotational_velocity: float
     rotational_inertia: float
     directional_velocity: np.zeros(3)
     heading: np.zeros(3)





    # PSI
    # Tyre radius
    # direction vector
    # velcocity vector
    # self aligning torque
    # Fn
    # Fw
    # Grip factor multiplier

    def compute(self, Fz, vel, heading, inclination_angle, ):

        return (Fx, Fy, align_torque)



