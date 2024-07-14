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

def fit_data(dist, mass, degree=1, file_name=None):
    x_vals, y_vals = get_data(file_name) if file_name else dist, mass
    x_vals = pylab.array(x_vals)
    y_vals = pylab.array(y_vals)
    plot_data(x_vals, y_vals)
    x_vals = x_vals*9.81
    model = pylab.polyfit(x_vals, y_vals, degree)
    
    est_y_vals = a*pylab.array(x_vals) + b
    print(f'a = {a} , b = {b}')
    pylab.plot(
        x_vals, 
        est_y_vals, 
        'r', 
        label=f'Linear Fit, k ={str(round(1/a, 5))}')
    pylab.legend(loc= 'best')
    