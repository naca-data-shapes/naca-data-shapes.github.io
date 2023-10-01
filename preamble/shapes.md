Data shapes
===========
As we have discussed in previous chapters, when data is expressed as linked data, it is stored as a set of triples. Where the subject, predicate and object are identified by a URI. 
Sifting through these triples can be a daunting task, which involves following the connections provided by the URIs. 
To overcome this problem, Data Shapes can be used. Data shapes are a way to express the structure of the data. We have selected 
the Shape Expression language (ShEx) as the language to express these data shapes. ShEx is a formal language that is specifically
designed to formalize the structure of RDF data.
Both users and data publishers can benefit from the use of data shapes. Both data users and publishers can use data shapes to express their expectations. Which in a way
allows both stakeholders to compare notes. Data users can use data shapes to express their expectations on the data. Data publishers can use data shapes to express the contents of the 
offered data. 

We have started developing data shapes for the NACA project. A detailed description of the data shapes, which were developed in close collaboration with domain experts mandated by the USDA, will follow in a later chapter in this book.

The process of describing a data shape. The process is iterative and involves the following steps:
1. Bring together domain experts and data experts
2. Identify the available data
3. Identify the use cases
4. Draft a boxology (data model) in close collaboration with the domain experts and the data experts
5. Express the boxology in ShEx
6. Validate the ShEx against the data
7. Iterate over the boxology and the ShEx until the data is fully described
8. Provide some illustrative examples of the data and its use

