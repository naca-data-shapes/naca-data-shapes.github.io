## Challenges for RDF Adoption

### RDF is mistakenly identified as a complex language.
Some people consider RDF as a theoretical, knowledge representation language which does not appeal to practical web developers. However, the RDF data model is very simple and can be understood by almost any person in less than an hour. In its simplicity lies its power and the advantages that we enumerated in previous sections. It is true that some of the technologies built on top of RDF, like OWL, have a more theoretical foundation based on description logics which diverge from this simplicity.

### Varying syntaxes
The RDF data model was defined along with an XML syntax in 1999. At that time XML was a popular syntax and that decision made sense. 
RDF/XML syntax was not human-readable i.e. it was difficult to write RDF/XML by hand and it was also difficult to process (it needed specialized libraries and parsers). The difference between the hierarchical, tree-based XML model and the graph-based RDF data model makes necessary to serialize the RDF graph to be represented in XML. The same RDF graph could be serialized in many ways making very difficult to use standard XML tools like XSLT or XPath to process RDF.
We consider that it is necessary to separate the RDF data model from its more powerful and complex relatives. This is not to say that these technologies are not useful or practical, but that the people who will manage them are different than the people who develop applications. Web developers are not so much interested in ontological discussions, they have more mundane concerns like what are the arcs expected to have for some node, what datatypes are allowed, which data structures can be used to represent some nodes, etc.

There were several attempts to define a more human-friendly syntax. Notation3 was proposed as a human-friendly language that was able to extend RDF and express other logical operations and rules. Turtle was later proposed as a subset of Notation3 for only expressing RDF. Turtle became popular in the semantic web community although not so much between web developers. Given that it is a special format, it requires a separate parser and tools.

In 2013, RDF 1.1 promotes also JSON-LD for developers who are familiar with JSON and RDFa which enables to embed RDF annotations along HTML content.

Although these efforts can help popularize RDF adoption between the developer community, some extra work is still needed to better understand the role of RDF in the Web development and publishing pipeline.

