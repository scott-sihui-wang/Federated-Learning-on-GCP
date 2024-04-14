from .default import DefaultStrategy as DefaultStrategy
from .fast_and_slow import FastAndSlow as FastAndSlow
from .fault_tolerant_fedavg import FaultTolerantFedAvg as FaultTolerantFedAvg
from .fedadagrad import FedAdagrad as FedAdagrad
from .fedadam import FedAdam as FedAdam
from .fedavg import FedAvg as FedAvg
from .fedpaq import FedPAQ as FedPAQ
from .fedfs_v0 import FedFSv0 as FedFSv0
from .fedfs_v1 import FedFSv1 as FedFSv1
from .fedyogi import FedYogi as FedYogi
from .qfedavg import QFedAvg as QFedAvg
from .qfedavg import QffedAvg as QffedAvg  # Deprecated
from .strategy import Strategy as Strategy

__all__ = [
    "DefaultStrategy",
    "FastAndSlow",
    "FaultTolerantFedAvg",
    "FedAdagrad",
    "FedAdam",
    "FedAvg",
    "FedPAQ",
    "FedFSv0",
    "FedFSv1",
    "FedYogi",
    "QFedAvg",
    "QffedAvg",  # Deprecated
    "Strategy",
]