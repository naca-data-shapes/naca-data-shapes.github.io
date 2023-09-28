Glossary
===

```{glossary}
Data Shape
  A description of the terms, modeling patterns, and constraints required or expected to be found in data - also known as a schema. Shape schemas are expressed in shape languages such as ShEx and are typically used to validate data consistency. In the NAL Shapes project, ShEx schemas specify a target form to which data from multiple sources can normalized and converted into RDF triples ("triplified"), using global identifiers (URIs, eg for properties from NALT), for the purpose of data integration.

Linked Data

NAL Shapes project
  NAL Shapes is a project of the USDA National Agricultural Library (NAL) in collaboration with the WESO Research Group of the University of Oviedo, Spain. The project goal is to illustrate and disseminate a method for integrating agricultural research data by normalizing the data to a common linked-data format on the basis of formally defined data shapes.

NALT Concept Space (NALT)
  NALT began in the 1980s as the National Agricultural Library Thesaurus, a hierarchically structured authority for keywords used for indexing agricultural research. Since then, NALT has evolved into the [NALT Concept Space](https://agclass.nal.usda.gov/) -- an authority for concepts, each of which has a globally unique web identifier (URI) and is annotated with a cloud of keywords in English and in Spanish. This concept space is subdivided into overlapping [concept schemes](https://www.w3.org/TR/skos-primer). In the NAL Shapes project, NALT concept URIs are used as properties for constructing data shapes in ShEx. NALT is expressed in <<SKOS>>, on the basis of <<RDF>>, and published as <<linked data>>. Many of its concepts are mapped to equivalent concepts in other authorities relevant to agriculture, such as [AGROVOC](http://fao.org/agrovoc/), [CABI Thesaurus](https://www.cabi.org/cabthesaurus/), and [Wikidata](https://www.wikidata.org/).

Resource Description Framework (RDF)

Shape Expressions Language (ShEx)

Simple Knowledge Organization System (SKOS)

Uniform Resource Identifier (URI)
  URIs are unique identifiers that are defined in the globally managed domain-name system of the Internet. URIs are commonly used to identify anything from webpage locations (URLs) to real-world things such as people (eg ORCID URIs), the RDF properties and classes of Linked Data, and the "concepts" of authority resources such as NALT Concept Space. Concept URIs may be used to denote purely conceptual things (eg "applied resource"), properties of things ("staple length"), or things in the real world ("apples"). URIs are made globally unique by using well-supported prefixes, or "schemes", such as "http" and "https". URIs maintained by organizations that guarantee their semantic stability and long-term availability, such as NALT URIs maintained by the National Agricultural Library, are referred to as persistent URIs. The use of persistent URIs in data can help ensure that data will remain useful in the longer-term future.
```
