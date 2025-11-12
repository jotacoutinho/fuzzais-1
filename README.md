# 🧠 Neural Networks and Fuzzy Systems practical exercise

This project implements a simple feedforward neural network from scratch in Python, using custom-built classes to represent neurons, layers, and synaptic connections.
It provides an educational foundation for understanding how neural networks are structured and how values propagate through the network.

## ⚙️ Overview

The code defines a modular NeuralNetwork class capable of:

- Dynamically creating input, hidden, and output layers

- Connecting neurons through weighted axons

- Propagating activations forward through the network

- Structuring neuron behavior via the external neuronio module

This implementation serves as a low-level educational framework, not dependent on libraries like TensorFlow or PyTorch.

## 🧩 Architecture Diagram

Below is a simplified representation of how neurons connect within your implementation:
```
Input Layer        Hidden Layers                   Output Layer
 ┌─────────┐        ┌─────────┐      ┌─────────┐      ┌─────────┐
 │ Input 1 │───┬───▶│Neuron H1│──┬──▶│Neuron H3│──┬──▶│Output 1 │
 └─────────┘   │    └─────────┘  │   └─────────┘  │   └─────────┘
               │                 │                │
               │    ┌─────────┐  │   ┌─────────┐  │
               └───▶│Neuron H2│──┴──▶│Neuron H4│──┘
                    └─────────┘      └─────────┘
```

Each connection represents an axon with an associated weight, defined in axonList.

Activations propagate forward from input → hidden → output neurons.

## 🧩 Key Components
**NeuralNetwork**: Responsible for constructing and managing the entire network:

**createNetwork()**: builds the network architecture (inputs, hidden layers, outputs)

**createListsForPropagation()**: gathers weights and activations for a given destination neuron

**propagateValues()**: performs forward propagation through all layers

**neuronio.Neuron**: External class that defines:
- Neuron activation value
- Axon list (weights)
- Activation computation logic

## 💻 Example Usage
```import redeneural

def neuralMain():
    # Create a simple neural network with 2 layers, 2 neurons, 1 input, and 1 output
    testNetwork = redeneural.NeuralNetwork(2, 2, 1, 1)
    testNetwork.createNetwork()

    # Print axon weights for inspection
    for i in range(0, 2):
        for j in range(0, 2):
            for weight in testNetwork.neuron[i][j].axonList:
                print(weight, i, j)

if __name__ == "__main__":
    neuralMain()
```

## 🔬 Educational Focus

This repository is designed for learning and experimentation. It’s ideal for:

- Understanding how neural networks are structured at a low level

- Exploring how activations and weights interact in propagation

- Extending the system with training algorithms such as backpropagation

## 📄 License

This project is released under the MIT License — feel free to modify, extend, and experiment with it.
