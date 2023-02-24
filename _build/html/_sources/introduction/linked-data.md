---
title: An Intro
datatable: true
---


A major challenge of any data-related endeavor is the integration of
disparate sources of information. German BioImaging (GerBI;
<https://gerbi-gmb.de/>) is currently involved in a project to link all German
research outputs at the national level in the National Research Data
Infrastructure ([NFDI](https://www.nfdi.de/)). ΔTissue has solicited GerBI to
provide a searchable, linked data graph for the program. Along with our
Belgium-based partner, Micelio (<https://micelio.be/>), we introduce below the
linked data framework as well as the proposed steps to bring the same
infrastructure to the ΔTissue program.

### What is Linked Data?

Linked data builds upon web technologies such as HTTP, RDF and URIs to connect
machine-readable representations of research outputs. A very straight-forward
introduction can be found at <https://ontola.io/what-is-linked-data/> .

The process of formatting one's data (here we do not differentiate between
"data" and "metadata") into linked data with well-defined identifiers and
semantics exposes inconsistencies early in the data acquisition process,
leaving one with cleaner, more interoperable *graphs* of data. Graphs produced
from a single research team can then be connected to others through common,
matching URIs, providing a single program-spanning, searchable resource. This
linked data graph:

-  provides a central clearing house for exposing inconsistencies and differences in naming;
-  drives the conversation of maximizing the FAIRness of data; and
-  serves as a portal through which disparate research areas can communicate

### Toy Example

To give a simple, toy example:

|            | Patient    | Observation    | Disease State |
| ---------- | ---------- | -------------- | ------------- |
| Sample\#1  | Patient\#A | N/A            | Early         |
| Sample\#2  | Patient\#A | Elevated count | Late          |
| Sample\#3  | Patient\#B | Prevalent      | Post-Mortem   |

A typical checklist that one would go through while trying to convert the above
spreadsheet into a linked data graph might contain:

1.  How will the local identifiers in each cell be converted into unique
    identifiers (URIs)? Is the same scheme used everywhere? Or are the
    identifiers only unique to the current spreadsheet table?
2.  What is the *exact* name of the property represented by the column heading?
    Again, is there a single URI for all uses of, e.g., "Disease State" or are
    there slight differences or perhaps restrictions between tables?
3.  What are the possible values for a given property? Do they come from an
    existing ontology? Is a new ontology needed?
4.  Are there any further semantics, limitations that can be captured? Is a
    given column of a type that is a sub-type or a super-type of another
    category?

Once this checklist has been applied to all spreadsheets, the table can be
written with clickable links (which is of course where the name "Linked Data"
comes from).

|                                                       | <https://wellcomeleap.org/delta-tissue/samples/acquired-from> |      |
|-------------------------------------------------------|---------------------------------------------------------------|------|
| <https://wellcomeleap.org/delta-tissue/samples/10584> | <https://wellcomeleap.org/delta-tissue/patients/49602>        | Etc. |
| <https://wellcomeleap.org/delta-tissue/samples/40592> | <https://wellcomeleap.org/delta-tissue/patients/49602>        | Etc. |
| <https://wellcomeleap.org/delta-tissue/samples/96049> | <https://wellcomeleap.org/delta-tissue/patients/99999>        | Etc. |

By using a namespace prefix, we can simplify this text and represent it
equivalently as statements in a graph:

```ttl
@prefix sample: <https://wellcomeleap.org/delta-tissue/samples/>.
@prefix patient: <https://wellcomeleap.org/delta-tissue/patients/>.
@prefix obs: <https://wellcomeleap.org/delta-tissue/observations/>.
sample:10584 sample:acquired-from patient:49602 .
sample:40592 sample:acquired-from patient:49602 .
sample:96049 sample:acquired-from patient:99999 .
sample:96049 obs:observed-with obj:prevalent .
sample:96049 obs:evidence https://wellcomeleap.org/delta-tissue/images/123 .
```

This process of cleaning the input data, assigning unique global identifiers,
and identifying or building ontologies also enables the use of a standardized
query language, SPARQL,
(<https://www.w3.org/TR/2013/REC-sparql11-overview-20130321/>):

```sparql
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX leap:  <http://wellcomeleap.org/vocabulary/0.1/>
SELECT ?patientName, ?sampleAge
	WHERE {
		?patient a leap:Patient .
		?patient foaf:name ?patientName .
		?sample leap:came_from ?patient .
		?sample leap:sample_age ?sampleAge .
	}
```

The sophistication of what is queryable is primarily limited by how well
the data is structured. See the example below from
[Wikidata for biomedical knowledge integration and curation (Gregory Stupp)](https://docs.google.com/presentation/d/1j5h5IwYM3ybRfU6T4E90UiqmNB23qQImQr5lvqRwP7g/edit#slide=id.g2dfcfa5dd2_0_107)
for a query which "finds drugs for cancers that target genes related to
cell proliferation":

<img src="{{site.baseurl}}/images/drugs-slide.png"
    alt="Slide titled 'What drugs interact with proteins that interact with other proteins that are known to be genetically associated to cancer?'"/>

## Questions
Please raise all your questions and issues [here]()


### Terminology
* Graph: or more formally, a labeled, directed, multi-graph, consists of a collection of RDF statements, or triples. 
* Linked Data: "LD", for "large scale integration of, and reasoning on, data on the web". See <https://www.w3.org/standards/semanticweb/data> .
* Ontology: For linked data, a vocabulary that defines concepts and relationships which describe and represent an area of concern. In general, "\[t\]here is no clear division between 'vocabularies' and 'ontologies'" though "the trend is to use the world 'ontology' for a more complex, and possibly quite formal collection of terms". See <https://www.w3.org/standards/semanticweb/ontology> .
* RDF: "Resource Description Framework", a standard model of data interchange and a W3C recommendation. See <https://www.w3.org/RDF/> 
* Sparql: specifications for languages and protocols for querying RDF graphs and a W3C recommendation. See <https://www.w3.org/TR/2013/REC-sparql11-overview-20130321/> 
* Triples: The basic unit of an RDF graph consisting of (resource, predicate, object).
* URI: universal resource identifier, a standardized representation of web resources. See <https://www.w3.org/Addressing/URL/uri-spec.html> 

{% include_relative navigation.md %}
