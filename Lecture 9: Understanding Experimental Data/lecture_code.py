import pylab

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
    