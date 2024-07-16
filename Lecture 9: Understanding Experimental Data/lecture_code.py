import pylab
import numpy as np

def get_data():
    pass

def label_plot():
    pylab.title('Measured displacements of Spring')
    pylab.xlabel('|Force|(Newtons)')
    pylab.ylabel('Distance (Meters)')
    

def plot_data(dist, mass, file_name=None):
    x_vals, y_vals = get_data(file_name) if file_name else dist, mass
    
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)
    x_vals = x_vals*9.81 # acc. due to gravity
    pylab.plot(
        x_vals,
        y_vals,
        'bo',
        label= 'Measured displacements')
    label_plot()

def fit_data(dist, mass, degree=1, file_name=None, model_label='Linear Model'):
    x_vals, y_vals = get_data(file_name) if file_name else dist, mass
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)
    plot_data(x_vals, y_vals)
    x_vals = x_vals*9.81
    model = pylab.polyfit(x_vals, y_vals, degree)
    pylab.plot(
        x_vals, 
        pylab.polyval(model, x_vals),
        'r', 
        label=model_label)
    pylab.legend(loc= 'best')


def gen_fits(x_vals, y_vals, degrees):
    models = []
    for d in degrees:
        model = pylab.polyfit(x_vals, y_vals, d)
        models.append(model)
    return models


def test_fits(models, degrees, x_vals, y_vals, title):
    pylab.plot(x_vals, y_vals, 'o', label='Data')
    for i in range(len(models)):
        est_y_vals = pylab.polyval(models[i], x_vals)
        error = r_squared(y_vals, est_y_vals)
        pylab.plot(x_vals, est_y_vals,
            label=f'Fit of degree {str(degrees[i])}, R2={str(round(error, 5))}')
    pylab.legend(loc='best')
    pylab.title(title)


def r_squared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    mean_error = error/len(observed)
    return 1 - (mean_error/np.var(observed))


    