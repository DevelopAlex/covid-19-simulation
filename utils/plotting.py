import matplotlib.pyplot as plt
plot.style.use('fivethirtyeight')
   
       
#from utils.plotting import bar_plot
#with sns.plotting_context("notebook", font_scale=2.5):
#    plot_diagram(simulation)
#    plt.savefig(os.path.join(DIR_FIGURES, "bar.png"), bbox_inches='tight')
#    plt.show()


def plot_diagram(simulation, **kwargs):
    fig, axes = plot.subplots(figsize=(16, 9))
    fig.subplots_adjust(bottom = 0.15)
    
    axes.grid(linestyle = ':', linewidth = 2.0, color = "#808080")
    
    t, x = zip(*simulation())
    S, E, I, R = zip(*x)
    
    axes.plot(t,S, color = "#0000cc")
    axes.plot(t,E, color = "#ffb000", linestyle = '--')
    axes.plot(t,I, color = "#a00060")
    axes.plot(t,R, color = "#008000", linestyle = '--')
    
    ax.legend()
    fig.tight_layout()
