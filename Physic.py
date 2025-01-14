# -*- coding: UTF-8 -*-
import math

class PhysicImpact:
    def Collision(self, body):
        raise Exception('Not implemented exception')
    def Force(self, force):
        raise Exception('Not implemented exception')
    g = 9.80665
    # Analytical and F~v solution isn't required.
    def GetVelocities(self, v_max, dt):
    # Takes initial coordinates, initial velocities, terminal velocity (!) and time step.
    # Returns numerical solution for velocities of body at t+dt.
        if(dt < 0 or v_max < 0):
            raise Exception("Wrong parameters")
        v = math.sqrt(self.VX*self.VX + self.VY*self.VY)
        self.VX = self.VX - self.g*(v*self.VX/(v_max*v_max))*dt
        self.VY = self.VY  + ( -self.g*v*self.VY/(v_max*v_max) - self.g ) * dt
        return [self.VX, self.VY]
    
    def Rotate(self, x0, y0, theta):
    # Rotate Z-X-Y coordinates by angle of theta.
        theta = theta/180.0*math.pi
        return [x0*math.sin(theta), y0, x0*math.cos(theta)]

    def GetRecoilVelocity(self, mu, v, dt):
    # Velocity of weapon after recoil.
        if(v < mu*self.g*dt):
            return 0
        else:
            return v - mu*self.g*dt

    def Move(self, x, y, z):
        self.Y = y
        self.X = x
        self.Z = z
    
class Body(PhysicImpact):
    X0 = 0
    Y0 = 0
    E = 1.0E3 # В будущем было бы неплохо варьировать энергию снаряда, т.е. его начальную скорость.
    Z = 0
    X = 0
    Y0 = 0
    Z0 = 0
    E = 1.0E3
    Z = 0
    X = 0
    Y = 0
    VX = 0
    VY = 0
    Width = 0
    Height = 0
    RVector = [0,0]
    Mass = 0
    Alpha = 0 # Regarding of the horison.
    VMax = 0
    V0 = 0
    #...
    def __init__(self, name, mass, alpha, x0, y0, z0):
        # alpha in degrees
        self.Name = name
        self.Mass = mass
        self.V0 = math.sqrt((2.0 * self.E) / mass)
        self.Alpha = alpha*180/math.pi
        self.VX = self.V0*math.cos(alpha)
        self.VY = self.V0*math.sin(alpha)

        self.X0 = x0
        self.Y0 = y0
        self.Z0 = z0
        self.X = x0
        self.Y = y0
class Scene:
    Bodies = []
    def __init__(self, name):
        self.Name = name

