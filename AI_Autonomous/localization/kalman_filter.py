import numpy as np

class KalmanFilter:

    def __init__(self):

        self.x = np.array([[0],[0]])
        self.P = np.eye(2)

        self.F = np.eye(2)
        self.H = np.eye(2)

        self.R = np.eye(2)*0.1
        self.Q = np.eye(2)*0.01

    def predict(self):

        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self,z):

        y = z - self.H @ self.x

        S = self.H @ self.P @ self.H.T + self.R

        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ y

        I = np.eye(self.H.shape[1])

        self.P = (I - K @ self.H) @ self.P