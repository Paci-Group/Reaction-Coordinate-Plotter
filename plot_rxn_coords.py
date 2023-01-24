import matplotlib.pyplot as plt
from matplotlib.colors import Colormap
from matplotlib import colormaps as cmap
import matplotlib
import numpy as np


def plot_rxn_coords(ax, energies, color, label, zero=None, linewidth=2, scale=0.32):
    energies = np.array(energies)
    if zero is not None:
        energies -= energies[zero]
    for j,l in enumerate(energies):
        ax.plot([(j+1-scale), (j+1+scale)], [l, l], color=color, linewidth=linewidth)
        if j <= len(energies)-2:
            ax.plot([(j+1+scale), (j+2-scale)], [l, energies[j+1]], linestyle=":", color=color, linewidth=linewidth)
    ax.plot([],[],color=color, linewidth=linewidth, label=label)
    
    
def plot_rxn_delta_es(ax, energies, color, label, width=0.25, shift=0, add_labels=False, fmt='%0.2f', 
                      label_padding=3, add_zero_line=True, linewidth=1, linestyle=':'):
    x = np.arange(len(energies) - 1) + 1  
    deltas = energies[1:] - energies[:-1]
    rects = ax.bar(x + shift, deltas, width, label=label, color=color)
    if add_labels:
        ax.bar_label(rects, padding=label_padding, fmt=fmt)
    if add_zero_line:
        ax.axhline(linewidth=linewidth, linestyle=linestyle, color='k')
        

if __name__ == "__main__":
    energies = np.array([6.0, 5.5, 5.7, 5.0, 4.3, 3.4, 3.0])
    
    ##########################################################################################
    # Plot Delta E's as Bar Grap
    ##########################################################################################
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    width=0.5
    plot_rxn_delta_es(ax, energies, 'red', 'Dummy Data', 
                      width=width, shift=0, label_padding=5, add_labels=True)
    
    ax.set_ylabel('$\Delta\Delta$ E (eV)', fontsize=16)
    ax.set_xlabel('Step', fontsize=16)
    x, labels = [1, 2, 3, 4, 5, 6], ["1-2", "2-3", "3-4", "4-5", "5-6", "6-7"]
    ax.set_xticks(x, labels)
    ax.tick_params(labelsize=14)
    ax.legend(loc="lower left", frameon=False, fontsize=14)
    plt.tight_layout()

    fig.savefig(f'delta_es.png', dpi=300)
    plt.close(fig)
    
    ##########################################################################################
    # Plot Standard Rxn Coordinate Diagram
    ##########################################################################################
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(111)
    width=0.5
    plot_rxn_coords(ax2, energies, 'red', 'Dummy Data', zero=0, linewidth=2, scale=0.32)
    
    ax2.set_ylabel('E (eV)', fontsize=16)
    ax2.set_xlabel('Reaction Coordinate', fontsize=16)
    x, labels = [1, 2, 3, 4, 5, 6, 7], ["1", "2", "3", "4", "5", "6", "7"]
    ax2.set_xticks(x, labels)
    ax2.tick_params(labelsize=14)
    ax2.legend(loc="lower left", frameon=False, fontsize=14)
    plt.tight_layout()

    fig2.savefig(f'es.png', dpi=300)
    plt.close(fig2)
    
    
    ##########################################################################################
    # Plot Rxn Coordinate Diagram with Delta E Inset
    ##########################################################################################
    fig3 = plt.figure(figsize=(8, 6))
    ax3 = fig3.add_subplot(111)
    width=0.5
    plot_rxn_coords(ax3, energies, 'red', 'Dummy Data', zero=0, linewidth=2, scale=0.32)
    
    ax3.set_ylabel('E (eV)', fontsize=16)
    ax3.set_xlabel('Reaction Coordinate', fontsize=16)
    x, labels = [1, 2, 3, 4, 5, 6, 7], ["1", "2", "3", "4", "5", "6", "7"]
    ax3.set_xticks(x, labels)
    ax3.tick_params(labelsize=14)
    ax3.legend(loc="lower left", frameon=False, fontsize=14)
    
    ax4 = ax3.inset_axes([0.6, 0.7, 0.35, 0.25])
    plot_rxn_delta_es(ax4, energies, 'red', 'Dummy Data', 
                      width=width, shift=0, label_padding=5, add_labels=False)
    ax4.tick_params(labelsize=12)
    ax4.locator_params(axis='y', nbins=6)
    ax4.set_xticks([1, 2, 3, 4, 5, 6], ["1-2", "2-3", "3-4", "4-5", "5-6", "6-7"])
    ax4.set_ylabel('$\Delta\Delta$ E (eV)', fontsize=12)
    ax4.set_xlabel('Step', fontsize=12)
    
    plt.tight_layout()

    fig3.savefig(f'es_delta_es_inset.png', dpi=300)
    plt.close(fig3)   
    