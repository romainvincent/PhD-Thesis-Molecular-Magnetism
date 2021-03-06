from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.colors import LinearSegmentedColormap

#on regle le style des fleches
arrowpropsleft=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0.0",linewidth=3,color="black")
arrowpropsright=dict(arrowstyle='-|>',connectionstyle="arc3,rad=-0.0",linewidth=3,color="blue")
arrowpropsboth=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=-0.0",linewidth=2,color="black")

#colorscale
cdict = {'red': ((0.0, 1.0, 1.0),
                 (0.5,1.0, 1.0),
                 (1.0, 1.0, 1.0)),
         'green': ((0.0, 0.0, 0.0),
                   (0.5, 0.5, 0.5),
                   (1.0, 1.0, 1.0)),
         'blue': ((0.0, 0.0, 0.0),
                  (0.5, 0.5, 0.5),
                  (1.0, 1.0, 1.0))
         }

my_cmap = LinearSegmentedColormap('my_colormap',cdict)

#fermi function
def f(x):
	return 1/(1+exp(x))

def plotsquare(ax,x1,x2,y1,y2,color="black"):
  ax.plot([x1,x1,x2,x2,x1],[y1,y2,y2,y1,y1],color)


x = linspace(-2,10,1000)
y = f(x)

fermi= []
for X in x[:300]:
	fermi.append(y)
fermi = np.rot90(fermi)

fig = figure()
fig.set_size_inches(12,5.5)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)




#figure a

ax1.imshow(fermi, extent=[0.1,0.35,0.1,0.6],cmap=my_cmap)
ax1.imshow(fermi, extent=[0.65,0.9,0.1,0.6],cmap=my_cmap)
ax1.text(0.225,0.35,"source",fontsize=25,ha="center",va="bottom")
ax1.text(0.775,0.35,"drain",fontsize=25,ha="center",va="bottom")
#barriere tunnel
ax1.plot([0.65,0.65],[0.1,0.75],'--',color="blue",linewidth=5)
ax1.plot([0.35,0.35],[0.1,0.75],'--',color="blue",linewidth=5)
ax1.text(0.35,0.76,r"$\gamma_s/C_s$",fontweight="bold",fontsize=25,ha='center', va='bottom')
ax1.text(0.65,0.76,r"$\gamma_d/C_d$",fontweight="bold",fontsize=25,ha='center', va='bottom')

#grille
ax1.plot([0.4,0.6],[0.2,0.2], linewidth=4, color="black")
ax1.plot([0.5,0.5],[0.1,0.19], linewidth=4, color="black")
ax1.text(0.40,0.18,r"$C_g$",fontweight="bold",fontsize=25,ha='left', va='top')
#dot
r1 = Circle((0.5,0.4),0.12,edgecolor="black")
ax1.add_patch(r1)
ax1.plot([0.45,0.55],[0.35,0.35],linewidth=3,color="black")
ax1.plot([0.45,0.55],[0.45,0.45],linewidth=3,color="black")
ax1.annotate("",(0.46,0.35),(0.46, 0.45),ha="center",va="center",arrowprops=arrowpropsboth)
ax1.text(0.48,0.4,r"$\Delta E$",fontweight="bold",fontsize=25,ha='left', va='center')

#reglages
ax1.set_xlim(0,1)
ax1.set_ylim(0,1)


#figure b
ax2.plot([0.1,0.3],[0.8,0.8],color="red")
plotsquare(ax2,0.3,0.35,0.7,0.9)
plotsquare(ax2,0.35,0.4,0.7,0.9)
ax2.text(0.35,0.9,r"$\gamma_s/C_s$",fontweight="bold",fontsize=25,ha='center', va='bottom')


ax2.plot([0.4,0.6],[0.8,0.8],color="blue")
plotsquare(ax2,0.6,0.65,0.7,0.9)
plotsquare(ax2,0.65,0.7,0.7,0.9)
ax2.text(0.65,0.9,r"$\gamma_d/C_d$",fontweight="bold",fontsize=25,ha='center', va='bottom')


ax2.plot([0.5,0.5],[0.8,0.6],color="blue")
ax2.plot([0.4,0.6],[0.6,0.6],color="black")
ax2.plot([0.4,0.6],[0.56,0.56],color="black")
ax2.plot([0.5,0.5],[0.56,0.5],color="black")
ax2.text(0.4,0.54,r"$C_g$",fontweight="bold",fontsize=25,ha='center', va='top')
ax2.annotate("",(0.5,0.5),(0.5, 0.31),ha="center",va="center",arrowprops=arrowpropsleft)
ax2.text(0.52,0.4,r"$V_{g}$",fontweight="bold",fontsize=25,ha='left', va='center')


ax2.plot([0.7,0.9],[0.8,0.8],color="red")
ax2.plot([0.9,0.9],[0.8,0.3],color="red")
ax2.plot([0.9,0.1],[0.3,0.3],color="red")
ax2.annotate("",(0.1,0.8),(0.1, 0.31),ha="center",va="center",arrowprops=arrowpropsleft)
ax2.text(0.12,0.55,r"$V_{ds}$",fontweight="bold",fontsize=25,ha='left', va='center')

#reglagesa

ax2.set_xlim(0,1)
ax2.set_ylim(0.2,1.1)


ax1.set_axis_off()
ax2.set_axis_off()

#Mise en page du plot
#compute scale multiplicator
xmin= ax1.get_xlim()
ymin= ax1.get_ylim()
a1 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))

xmin= ax2.get_xlim()
ymin= ax2.get_ylim()
a2 = 1.0 * abs((xmin[0]-xmin[1])/(ymin[0]-ymin[1]))
#scale graphs
ax1.set_aspect(a1*0.9,)
ax2.set_aspect(a2*0.9,)
fig.subplots_adjust(left=0.00,right=1,wspace=0.0, bottom=0,top=1)
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold",backgroundcolor="pink")
fig.text(0.51,0.95,"b",fontsize=25,fontweight="bold",backgroundcolor="pink")
fig.savefig("/home/hukadan/These/Manuscript/Theorie/Transport/figure1/figure1.pdf")
#close(fig)
