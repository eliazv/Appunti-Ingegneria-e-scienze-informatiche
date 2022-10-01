import numpy as np     
def iterazione(gname,x0,tolx,nmax):
        
        xk=[]
        xk.append(x0)
        x1=gname(x0)
        d=x1-x0
        xk.append(x1)
        it=1
        while it<nmax and  abs(d)>=tolx*abs(x1) :
            x0=x1
            x1=gname(x0)
            d=x1-x0
            it=it+1
            xk.append(x1)
           
    
        if it==nmax:
            print('Raggiunto numero max di iterazioni \n')
        
        return x1, it,xk
    

def stima_ordine(xk,iterazioni):
      p=[]

      for k in range(iterazioni-3):
         p.append(np.log(abs(xk[k+2]-xk[k+3])/abs(xk[k+1]-xk[k+2]))/np.log(abs(xk[k+1]-xk[k+2])/abs(xk[k]-xk[k+1])));
     
      ordine=p[-1]
      return ordine