# Federated Learning on Google Cloud Platform (GCP)

**Topics:** _Cloud and Distributed Computing_, _Synchronous and Asynchronous Federated Learning_

**Skills:** _Google Cloud Platform_, _Federated Learning_, _Python_

## 1. Introduction

### 1.1 Motivation

This is the course project for CMPT 756: `Distributed and Cloud Systems`.

In this project, I implemented and evaluated some of `synchronous` and `asynchronous` `gradient aggregation algorithms` on a small cluster of computers deployed on `Google Cloud Platform` (GCP).

I also discussed how `clients' partial participation`, `reduced level of synchronization`, and `the presence of stragglers` might impact `communication efficiency` and `model accuracy` of `federated learning` algorithms.

For full technical details of this project, please refer to my [report](FinalReport.pdf).

### 1.2 Tasks

In this project, my contributions are:

- Implemented a variant of federated learning algorithm, `FedPAQ` [paper link](https://arxiv.org/pdf/1909.13014.pdf), based on `flower` [repository link](https://github.com/adap/flower);

- 

- Deployed the federated learning models to GCP;

- Evaluated and compared _synchronous_ federated learning algorithms, `FedAvg` and `FedPAQ`;

- Evaluated and compared _synchronous_ and _asynchronous_ federated learning algorithms, with a focus on `straggler's effect`.

### 1.3 Environment

## 2. Acknowledgement
