A preamble into Nalt and related concept spaces
======================
In the previous chapter we introduced the concept of linked data and how it can be used to represent data in a standardized way.
Publishing linked-data requires the use of universally unique identifiers (URIs) to identify the concepts in the data. 
In this chapter we introduce the concept of concept spaces and how they can be used to identify concepts in linked-data, or
more specifically in RDF. 

# Concept spaces
A concept space is a collection of concepts that are related to each other, or are curated and maintained by a dedicated 
oragnisation. The concepts in a concept space are identified by a URI. Many concept spaces exist, as well as different (online)
tools to identify applicable concept spaces. 
In this project the NALT concept space is core, which absolves us from the need to search through different concept spaces.
However, it is good to know that other concept spaces exist and that they can be used to identify concepts in linked-data.

# Ontologies
Where a concept space is a collection of concepts, an ontology is a collection of concepts and the relationships between them. 
To put it differently, an ontology is a concept space with additional information on how the concepts are related to each other.
Currently, NALT is not a true ontology. This means that we need to rely on additional frameworks to express the relationships between 
the concepts expressed in NALT. Further study is needed to determine which ontologies are applicable and as such should be aligned to
the NALT concept space. Currently we have limited the scope of this project to the NALT concept space and the use of the SKOS framework and 
the Dublin Core metadata standard. Future modeling work will need to determine if additional ontologies are needed and how they can be
aligned to the NALT concept space.
