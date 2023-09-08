## Integrate data with <<Shapes>>

Was: Linked data, RDF and the web of data

These days more and more devices generate data automatically and it is relatively easy to develop applications in different domains backed by databases and exposing data to the Web. The amount and diversity of data produced clearly exceeds our capacity to consume it.

Variety is a key concern which prevents data integration and generates lots of interoperability problems.

RDF was proposed as a graph-based data model which became part of the Semantic Web vision. 
Its reliance on the global nature of URIs offered a solution to the data integration problem as RDF datasets produced by different means can seamlessly be integrated with other data. 
Data integration using RDF can be done automatically and is more robust than traditional solutions in the face of schema changes.

RDF is also a key enabler of linked data. Linked data {cite}`heath2011linked` was proposed as a set of best practices to publish data on the Web. 
It was introduced by Tim Berners-Lee [8] and was based on four main principles. RDF is mentioned in the third principle as one of the standards that provides useful information. The goal is that information must be useful not only for humans navigating through browsers (for which HTML would be enough) but also for other agents that may automatically process that data.

The linked data principles became popular and several initiatives were created to publish data portals. The size of data on the Web increased significantly in the last years. For example, the LODStats project [36] aggregates around 150 billion triples from 2,973 datasets.

Material removed:
- [Two sentences on the Three Vs](../extra_files/three_vees.html). Removed because it raises issues about big data that we do not actually address in this simple demo, ie Volume and Velocity. Also, sources disagree on whether there are Three Vs, Four Vs, or Five Vs.
