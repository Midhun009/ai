import numpy as np

x=np.array(([2,9],[1,5],[3,6]),dtype=float)
y=np.array(([98],[86],[89]),dtype=float)
x=x/np.amax(x,axis=0)
y=y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivatives_sigmoid(x):
    return x*(1-x)

epoch=5000
lr=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
output_neurons=1

wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wo=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bo=np.random.uniform(size=(1,output_neurons))

for i in range(epoch):
    hinp1=np.dot(x,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    
    outinp1=np.dot(hlayer_act,wo)
    outinp=outinp1+bo
    output=sigmoid(outinp)
    
    EO=y-output
    outgrad=derivatives_sigmoid(output)
    d_output=EO*outgrad
    
    EH=d_output.dot(wo.T)
    hiddengrad=derivatives_sigmoid(hlayer_act)
    d_hiddenlayer=EH*hiddengrad
    
    wo += hlayer_act.T.dot(d_output)*lr
    wh += x.T.dot(d_hiddenlayer)*lr

print("Input: "+str(x))
print("Actual output: "+str(y))
print("Predicted output: ",output)

