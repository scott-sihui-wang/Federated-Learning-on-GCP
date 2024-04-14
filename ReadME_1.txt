GCP Project Address: https://console.cloud.google.com/compute/instances?authuser=1&project=mnist-distributed-332209

Implementation of FedAvg and FedPAQ:

On GCP: Virtual Machine: py-1, py-2, py-3, py-4
py-1 is the server, py-2, py-3, py-4 are the clients.

Usage:
Use SSH to open the 4 virtual machines: py-1 py-2 py-3 py-4
In each of the window, input:
cd flwr_sync
In the window for py-1 (the server), input:
python3 server.py
Afterward, in the other 3 windows, input
python3 client.py
Then we will see the training process, and the outcome of validation loss for each epoch, and the total training time.

Tweaking the Parameters:
In py-1's window, input:
cd flwr_sync
Then, input:
vim server.py
In server.start_server section, you can change "num_rounds"
In strategy section, you can change the strategy from FedAvg to FedPAQ
For FedAvg, you can change min_fit_client, min_eval_client, fraction_fit, fraction_eval to test different level of clients' participation:
The server requires min_fit_client number of clients to be available during training
The server requires fraction_fit percentage of clients to be available during training
And min_eval_client, fraction_eval's meanings are similar
For FedPAQ, there are two additional keywords: sync_level and precision
sync_level is the interval for 2 consecutive synchronizations
precision is for quantization of parameters

Acknowledgement:
The Flower Project: https://github.com/adap/flower
The Flower Package: https://github.com/adap/flower/tree/main/src/py/flwr
The Original Code for Federated Learning on MNIST: https://github.com/adap/flower/tree/main/examples/quickstart_pytorch