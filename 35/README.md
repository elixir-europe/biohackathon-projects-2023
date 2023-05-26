# Project 35: Write once, run everywhere: exploring the use of Rust and WebAssembly to implement the Nanopublication signing protocol

## Abstract

We propose developing a cross-platform library for researchers to sign and publish Nanopublications. Nanopublication is a protocol to publish small pieces of information in a machine-readable format (the Resource Description Framework), Nanopublications are signed using a private key linked to the user's ORCID for authentication and traceability, then published to a decentralized network of Nanopublications servers.

Nanopublications are commonly used in biomedical and semantic web communities for publishing research-related data and metadata in a free, open, and trusted platform. There is currently an official implementation of the Nanopublication signing process in Java, and we have been working on a Python implementation, but there is is no JavaScript implementation that can perform signing in the browser yet, which would enable developers to implement the signing process on the web without the need for hosting a server.

We aim to solve this problem by developing a Rust library that can be compiled to work on any platform, including in the browser with WebAssembly. In addition, we will define bindings and publish libraries to packages registries for popular languages, such as JavaScript and Python.

This solution will enable developers to easily sign and publish Nanopublications from the browser, and will eliminate the need for maintaining and updating multiple versions for different languages, which requires extensive testing to ensure all cases are covered.

We believe that this project has the potential to improve access to technologies helping to build systems complying with the FAIR principles (Findable, Accessible, Interoperable, Reusable).

## More information

In the short-term, by the end of the Biohackathon, we hope to have a proof of concept of a Rust library that compiles to a JavaScript module, published to a public git repository with all the documentation required to reuse and maintain the project. In the long term, after the hackathon we plan to integrate this signing component to the nanopub-js web libraries, and create bindings for python and ruby.

A minimum of 2 to 3 people should be enough for the project to succeed, but it would gain from having more people joining and sharing their ideas and experiences.

People with experience in programming with any language are welcome to join us discovering the new tools and paradigms we will explore.

We will use a public git repository to collaborate and publish the code. We plan to use cargo with wasm-pack to compile the code and documentation.

## Lead(s)

Vincent Emonet, Shashank Chakravarthy

