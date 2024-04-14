Asynchronous Federated Learning:

On GCP: Virtual Machine: py-syft-1, py-syft-2, py-syft-3, py-syft-4
py-syft-2 is the "client"(this is the original programmer's wording, in our context, it is the server), py-syft-1, py-syft-3, py-syft-4 are "servers"

Usage:
Use SSH to open the 4 virtual machines: py-syft-1 py-syft-2 py-syft-3 py-syft-4
In each of the window, input:
cd syft-async
In the windows for syft-py-1, syft-py-3, syft-py-4, input:
python3 servers.py 1 0
The parameter 1 means that we need to start 1 "server" on each of these machines.
The parameter 0 means that we don't need the dataset to be unbalanced. (This is related to the original author's reseach interest, but it is not relevant to this project)
Afterward, in the window for syft-py-2 (the "client"), input:
python3 client.py 3 10000 fl_time.csv fl_epoch.csv yappi.csv
The parameter 3 means that this "client" will communicate with 3 "servers"
The parameter 10000 is the staleness tolerance for the model parameters in federated learning.
Set this parameter to 0 to simulate synchronous training. Set this parameter very high to simulate asynchronous training.
The last 3 parameters are for the loggings. You can choose the filenames for the logs as whatever you want
Then we will see the training process, the validation loss for each machine for each epoch, and the final results.
Currently the code is a simulation for asynchronous training under the situation that py-syft-1 is the straggler. 
py-syft-1 will sleep for random.random()*30 seconds for each epoch of training, you can see info in the window for py-syft-2

Acknowledgement:
Original Code for Single PC Simulation: https://github.com/diwangs/asynchronous-federated-learning