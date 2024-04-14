import flwr as fl
from flwr.common import(
        Parameters,
        Weights,
        parameters_to_weights,
        weights_to_parameters,
)


if __name__ == "__main__":

    # Define strategy
    strategy = fl.server.strategy.FedPAQ(
        fraction_fit=1.00,
        fraction_eval=1.00,
        min_fit_clients=1,
        min_eval_clients=1,
        min_available_clients=1,
        sync_level=4,
        precision=3
    )

    # Start server
    fl.server.start_server(
        server_address="10.138.0.4:2222",
        config={"num_rounds": 30},
        strategy=strategy,
    )