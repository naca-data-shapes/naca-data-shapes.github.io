#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wikidataintegrator import wdi_core
from rdflib import Namespace, Graph, URIRef, Literal, BNode
from rdflib.namespace import DCTERMS, DC, XSD, RDFS, DCAT, RDF, FOAF, NamespaceManager, SKOS


# In[2]:


ontology = Graph()
ontologyName = "../codebook/nalt_full"
ontology.parse(ontologyName+".ttl", format="turtle")


# In[17]:


codelist = dict()
for uri, label in ontology.subject_objects(predicate=SKOS.prefLabel):
    if str(label) not in codelist.keys():
        codelist[str(label)] = []
    if uri not in codelist[str(label)]:
        codelist[str(label)].append(str(uri))

for uri, label in ontology.subject_objects(predicate=SKOS.altLabel):
    if str(label) not in codelist.keys():
        codelist[str(label)] = []
    if uri not in codelist[str(label)]:
        codelist[str(label)].append(str(uri))

for key in codelist.keys():
    codelist[key] = list(set(list(codelist[key])))


# In[18]:


codelist


# In[20]:


len(codelist.keys())


# In[25]:


urilist = {}
for key in codelist.keys():
    if codelist[key][0] not in urilist.keys():
        urilist[codelist[key][0]] = []
    urilist[codelist[key][0]].append(key)


# In[26]:


urilist


# In[31]:


wd_nalt = Graph()
query = """
SELECT * WHERE {
    ?wdnalt wdt:P2004 ?nalt
}
LIMIT 20
"""
for index, row in wdi_core.WDFunctionsEngine.execute_sparql_query(query, as_dataframe = True).iterrows():
    print(index, row["wdnalt"])
    wd_nalt.parse(row["wdnalt"]+".ttl")


# In[35]:


from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE

q = "select ?class where { {?item wdt:P31 ?class} UNION {?item wdt:P279* ?class} }"
target_classes = []
x = wd_nalt.query(q)
for target_class in x:
  if str(target_class["class"]) not in target_classes:
    target_classes.append(str(target_class["class"]))

shex_target_file = "wd_nalt.shex"

shaper = Shaper(target_classes=target_classes,
                rdflib_graph=wd_nalt,
                input_format=TURTLE,
                instantiation_property="http://www.wikidata.org/prop/direct/P31"
                )  # Default rdf:type

shaper.shex_graph(output_file=shex_target_file)


# In[36]:


get_ipython().system('cat wd_nalt.shex')


# In[ ]:




