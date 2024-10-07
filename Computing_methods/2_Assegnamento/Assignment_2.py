import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityDistribution(InterpolatedUnivariateSpline):
    def __init__(self, x, y):
        spline = InterpolatedUnivariateSpline(x, y)
        norm = spline.integral(x.min(), x.max())
        self._x = x
        self._y = y / norm
        super().__init__(self._x, self._y) #Importa tutti i metodi e gli attributi delle spline

    def plot(self):
        plt.plot(self._x, self._y, 'o', label='PDF')
        x = np.linspace(self._x.min(), self._x.max(), 250)
        plt.plot(x, self(x), label='PDF interpolata')

    def evaluate(self, x_of_evaluation):
        print(f'x of evaluation = {x_of_evaluation:.2f} \ny of evaluation = {self(x_of_evaluation):.2f}')

    def probability(self, x_in, x_fin):
        prob = self.integral(x_in, x_fin)
        print(f'The probability to be between {x_in} and {x_fin} is {prob:.2f}')


class CumulativeDensityFunction:
    def __init__(self, pdf: ProbabilityDensityDistribution):
        self._x_CDF = pdf._x
        # Calcoliamo la CDF come l'integrale della PDF
        self._y_CDF = np.array([pdf.integral(pdf._x.min(), xi) for xi in self._x_CDF])
        # Creiamo una spline interpolata per la CDF
        self.spline_CDF = InterpolatedUnivariateSpline(self._x_CDF, self._y_CDF)
        
    def plot(self):
        plt.plot(self._x_CDF, self._y_CDF, 'o', label='CDF')

    def invert(self, p):
        
        if not (0 <= p <= 1):
            raise ValueError("Probability p must be between 0 and 1.")
        
        # Usando la ricerca binaria per trovare x tale che CDF(x) = p
        low, high = self._x_CDF.min(), self._x_CDF.max()
        while low < high:
            mid = (low + high) / 2
            if self.spline_CDF(mid) < p:
                low = mid + 1e-3  # incrementa per non rimanere bloccato
            else:
                high = mid
        return low

def random_number_generator(cdf: CumulativeDensityFunction):
    num = random.uniform(0, 1)
    generated_random_number = cdf.invert(num)
    print(f'Numero generato random secondo la distribuzione fornita = {generated_random_number}')
    return generated_random_number


# Testing
if __name__ == '__main__':
    # Modifica i punti x per ottenere una PDF valida
    xx = np.linspace(-10., 10, 1001)
    yy = np.exp(-xx**2)  # Funzione gaussiana non normalizzata
    
    # Creiamo la PDF
    pdf = ProbabilityDensityDistribution(xx, yy)
    
    # Eseguiamo alcune valutazioni
    x0 = 0.5
    pdf.evaluate(0.5)
    
    start_x = -10
    end_x = 10
    pdf.probability(start_x, end_x)
    
    # Plottiamo la PDF
    pdf.plot()
    
    # Creiamo la CDF
    cdf = CumulativeDensityFunction(pdf)
    cdf.plot()
    
    # Inversione della CDF
    p = 0.6  # Esempio: vogliamo trovare x per p = 0.5
    x_inverted = cdf.invert(p)
    print(f'Value of x for CDF(x) = {p}: {x_inverted:.2f}')
    
    # Generiamo un numero casuale secondo la distribuzione fornita
    random_number_generator(cdf)
    
    plt.show()
