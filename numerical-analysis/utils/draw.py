from matplotlib.patches import Patch
from matplotlib.pyplot import plot, show, legend, savefig, title

from typing import Sequence


colors = ['red', 'green', 'blue', 'black']


def draw(xs: Sequence, arr, t, f, show_plots=True, save_plots=False) -> None:
    # legend(loc='upper center', shadow=True, fontsize='x-large')
    for (func, _), color in zip(arr, colors):
        plot(xs, func, color=color)
    legend(handles=[
        Patch(color=color, label='${}$'.format(name))
        for (_, name), color in zip(arr, colors)
    ])
    title(t)
    if show_plots:
        show()
    if save_plots:
        savefig(f + '.png')
