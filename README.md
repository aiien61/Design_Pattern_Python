# Design Patterns in Python

Welcome to the **Design Patterns Python** repository! This project is a comprehensive collection of various design patterns implemented in Python, with plenty of examples to help you understand and apply these patterns in your own projects.

## About

This repository is dedicated to showcasing and practicing different design patterns using Python. Design patterns are proven solutions to common problems that software developers face during development. By using these patterns, you can write code that is more flexible, reusable, and easier to maintain.


## SOLID Principles

The SOLID principles are a set of five design principles intended to make software designs more understandable, flexible, and maintainable:

- **Single Responsibility Principle (SRP)**: A class should have only one reason to change, meaning it should have only one job or responsibility.
- **Open/Closed Principle (OCP)**: Software entities should be open for extension but closed for modification.
- **Liskov Substitution Principle (LSP)**: Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.
- **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
- **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

## Patterns Covered

The repository includes examples and explanations for a wide range of design patterns, categorized into three main types:

### 1. Creational Patterns
- **Singleton**: Ensure a class has only one instance and provide a global point of access to it.
- **Factory Method**: Define an interface for creating an object, but let subclasses alter the type of objects that will be created.
- **Abstract Factory**: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
- **Builder**: Separate the construction of a complex object from its representation so that the same construction process can create different representations.
- **Prototype**: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

### 2. Structural Patterns
- **Adapter**: Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
- **Composite**: Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
- **Decorator**: Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
- **Facade**: Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
- **Flyweight**: Use sharing to support large numbers of fine-grained objects efficiently.
- **Proxy**: Provide a surrogate or placeholder for another object to control access to it.

### 3. Behavioral Patterns
- **Chain of Responsibility**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
- **Command**: Encapsulate a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
- **Iterator**: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- **Mediator**: Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
- **Memento**: Without violating encapsulation, capture and externalize an object’s internal state so that the object can be restored to this state later.
- **Observer**: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **State**: Allow an object to alter its behavior when its internal state changes. The object will appear to change its class.
- **Strategy**: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- **Template Method**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
- **Visitor**: Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.

## Getting Started

To get started with exploring the design patterns, simply clone this repository:

```bash
git clone https://github.com/aiien61/Design_Pattern_Python.git
cd Design_Pattern_Python
```

Each design pattern is implemented in its own directory with clear and concise examples. You can run the examples to see the patterns in action and modify them to deepen your understanding.

## Contributing

Contributions are welcome! If you have a new design pattern implementation, improvements, or bug fixes, feel free to submit a pull request. Please ensure your code adheres to the repository's coding standards and include relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to the open-source community and various resources that have contributed to the understanding and implementation of design patterns.
