#on fait d'abord 3 subplot
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Polygon



gs1 = gridspec.GridSpec(1,1)
gs1.update(left=0.09,right=0.49,bottom=0.2)
ax1 = plt.subplot(gs1[:,:])

gs2 = gridspec.GridSpec(1,1)
gs2.update(left=0.51, right=0.98,hspace=0.1,bottom=0)
ax2 = plt.subplot(gs2[0,0])

fig = gcf()
fig.set_size_inches(12,5.5)









#ax3.set_axis_off()
##############################
#PANEL 1
#On commence par le pannel 1
tr0 = Polygon([[-1,0],[-1,1],[0,0]], color="#C0C0C0")
tr1 = Polygon([[0,0],[1,1],[1,0]], color="#C0C0C0")
poly1 = Polygon([[0,0],[0.25,0.25],[1,0.25],[1,0]],color='gray')
ax1.add_patch(tr0)
ax1.add_patch(tr1)
ax1.add_patch(poly1)
ax1.plot([0,1],[0,1],'b')#bord de diamant
ax1.plot([-1,0],[1,0],'b')#bord de diaman
ax1.plot([-0.5,0.25],[1,0.25],'r')#niveau excite
ax1.plot([0.25,0.5],[0.25,0],'r--')#sous l'etat fondamental


#delta Ez
ax1.plot([1,0.25],[0.25,0.25],color="red",linestyle='-')
ax1.annotate("",(0.5,0.25),(0.5,0),ha="center",va="center",arrowprops=dict(arrowstyle='<|-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))
ax1.text(0.620,0.125,r"$\Delta E_Z$",va="center",ha="center",fontsize=25, color='black')


ax1.set_xlim(-0.25,1)
ax1.xaxis.set_ticks([0,0.5])
ax1.xaxis.set_ticklabels(["$\mu_+(B)$","$\mu_{\minus}(B)$"], fontsize = 25)
ax1.yaxis.set_ticks([0,1])
ax1.set_xlabel(r"$V_{\rm{g}}(u.a)$")
ax1.set_ylabel(r"$V_{\rm{ds}}(u.a)$")
#une fleche pour l'influence du champ magnetique
#ax1.annotate("",(-0.5,0.5),(-0.7,0.5),ha="center",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=0",linewidth=4,color="b"))
#ax1.text(-0.6,0.45,"B",va="center",ha="center",fontsize=25,color = 'b')
#une deuxieme
ax1.annotate("",(0.0,0.5),(0.2,0.5),ha="center",va="center",arrowprops=dict(arrowstyle='<|-',connectionstyle="arc3,rad=0",linewidth=4,color="r"))
ax1.text(0.1,0.55,"B",va="center",ha="center",fontsize=25,color = 'r')



###############################
##PANEL 2 cotunneling inelastique
ax2.set_xlim(-0.1,1.5)
ax2.set_ylim(-0.1,1)
ax2.set_axis_off()

wl=2.5

#########
#premier potentiel elastique
xoffset=0
yoffset=0.1
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl)
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.075+xoffset,0.1+yoffset),(0.075+xoffset,0.2+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.00+yoffset),(0.225+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot


#premier potentiel inelastique
xoffset=0
yoffset=0.7
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.2+yoffset,0.2+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl)
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.075+xoffset,0.25+yoffset),(0.075+xoffset,0.15+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.00+yoffset),(0.225+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot


#elastique
xoffset=0.5
yoffset=0.1
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.2+yoffset,0.2+yoffset],'black',linewidth=wl,linestyle="--")
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.225+xoffset,0.15+yoffset),(0.225+xoffset,0.25+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=0",linewidth=2,color="black",linestyle='dashed'))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.00+yoffset),(0.225+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot



#inelastique
xoffset=0.5
yoffset=0.7
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.2+yoffset,0.2+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.25+yoffset,0.25+yoffset],'black',linewidth=wl,linestyle='--')
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.225+xoffset,0.3+yoffset),(0.225+xoffset,0.2+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=0",linewidth=2,color="black",linestyle='dashed'))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.00+yoffset),(0.225+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot



#final elastique
xoffset=1
yoffset=0.1
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl)
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.375+xoffset,0.2+yoffset),(0.375+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.+yoffset),(0.225+xoffset,0.1+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot


#final inelastique
xoffset=1
yoffset=0.7
#premier potentiel chimique
ax2.plot([0.15+xoffset,0.15+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0.3+xoffset,0.3+xoffset],[0+yoffset,0.25+yoffset],'black',linewidth=wl) #barriere tunnel
ax2.plot([0+xoffset,0.15+xoffset],[0.2+yoffset,0.2+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.10+yoffset,0.10+yoffset],'black',linewidth=wl)
ax2.plot([0.15+xoffset,0.3+xoffset],[0.05+yoffset,0.05+yoffset],'black',linewidth=wl*0.5,linestyle='--')
ax2.plot([0.3+xoffset,0.45+xoffset],[0.15+yoffset,0.15+yoffset],'black',linewidth=wl)
#on met les spins
ax2.annotate("",(0.375+xoffset,0.1+yoffset),(0.375+xoffset,0.2+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur l'electrode
ax2.annotate("",(0.225+xoffset,0.15+yoffset),(0.225+xoffset,0.05+yoffset),ha="right",va="center",arrowprops=dict(arrowstyle='-|>',connectionstyle="arc3,rad=0",linewidth=2,color="black"))#sur le dot


#un peu de legende
ax2.text(0.225,0.525,"Etat initial",va="center",ha="center",fontsize=20,color = 'black')
ax2.text(0.725,0.525,"Etat virtuel",va="center",ha="center",fontsize=20,color = 'black')
ax2.text(1.225,0.525,"Etat Final",va="center",ha="center",fontsize=20,color = 'black')


#quelques limites
ax2.plot([0.475,0.475],[0.,1.05],color='black',linestyle='-.')
ax2.plot([0.97,0.97],[0.,1.05],color='black',linestyle='-.')


#Mise en page du plot
fig.text(0.01,0.95,"a",fontsize=25,fontweight="bold")#,backgroundcolor="#FF0000")
fig.text(0.51,0.95,"b",fontsize=25,fontweight="bold")#,backgroundcolor="m")

#Et voila
fig.savefig("Theorie/Transport/figure5/figure5.pdf")

#close(fig)
