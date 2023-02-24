#!/usr/bin/env python
# coding: utf-8

# # Example workflow on Cotton shape

# In[1]:


import pandas as pd
from rdflib import Namespace, Graph, URIRef, Literal, BNode
from rdflib.namespace import DCTERMS, DC, XSD, RDFS, DCAT, RDF, FOAF, NamespaceManager, SKOS
import os
import urllib.parse
from datetime import datetime
import uuid
import graphviz
from ShExJSG import Schema, ShExC, ShExJ
from ShExJSG.ShExJ import Shape, IRIREF, TripleConstraint, NodeConstraint, ShapeOr, EachOf, ShapeExternal, ShapeDecl, Annotation, ObjectLiteral

symbol = dict()
symbol["class"] = "oval"
symbol["datatype"] = "octagon"
symbol["literal"] = "rectangle"
symbol["iri"]="diamond"
symbol["bnode"]='point'
symbol["oneof"]='record'

rdf = Graph()

AGSCHEMAS = Namespace("https://agschemas.org/")
AGUNITS = Namespace("https://agunits.org")
WD = Namespace("http://www.wikidata.org/entity/")
WDT = Namespace("http://www.wikidata.org/prop/direct/")
SUBJECT = Namespace("http://cottonexample.org/")
HARVESTLOCATION = Namespace("http://cottonexample.org/location/")
NALT = Namespace("https://lod.nal.usda.gov/nalt/")

OBO = Namespace("http://purl.obolibrary.org/obo/")
rdf.bind("obo", "http://purl.obolibrary.org/obo/")
SCHEMA = Namespace("https://schema.org/")
QUDT = Namespace("http://qudt.org/schema/qudt/")
UNIT = Namespace("http://qudt.org/schema/qudt/Unit/")
AGUNIT = Namespace("https://agschemas.org/units/")


rdf.bind("sio", "http://semanticscience.org/resource/")
rdf.bind("wd", "http://www.wikidata.org/entity/")
rdf.bind("wdt", "http://www.wikidata.org/prop/direct/")

def add2graphviz(command=None, arg1=None, arg2=None, shape=None, label=None):
    if command == "attr":
        localviz.attr(arg1, shape=shape)
        schema.attr(arg1, shape=shape)
    if command == "node":
        localviz.node(arg1,label=label)
        schema.node(arg1,label=label)
    if command == "edge":
        localviz.edge(arg1, arg2, label=label)
        schema.edge(arg1, arg2, label=label)


# In[2]:


filename = 'data/Legacy_Cotton_VT_data.csv'
fileURI = URIRef("https://www.protocols.io/file/jfwubrptx.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWSNCI5SNCPTWTQQ%2F20230111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230111T113315Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=dcd1bc448443105a322e54f10cc2f699f3dbba2d58e16f0525a72d3d9c32d673")


# # The original data
# In this chapter the tabular data from the previous chapter will be converted into linked data. As we discussed earlier, in linked data the data is mainly represented by using IRIs and placing those URIs in data shapes. 
# 
# This already starts with describing the data itself. 

# ## Schema of meta data on synthetic dataset 1
# Below is graph representation on the metadata on dataset 1. The following symbols are used.
# 

# In[3]:


md_schema = graphviz.Digraph(filename, filename=filename+'pda_cotton.gv')
md_schema.graph_attr['rankdir'] = 'LR'

for key in symbol.keys():
    md_schema.attr('node', shape=symbol[key])
    if key == "oneof":
        md_schema.node(key, label="{option 1|option ..|option n}")
    else:
        md_schema.node(key)
md_schema


# Below it the (proposed) shape for the metadata. 

# In[4]:



schema = graphviz.Digraph(filename, filename=filename+'.gv')
schema.graph_attr['rankdir'] = 'LR'
# graphviz
schema.attr('node', shape=symbol["iri"])
schema.node('fileURI')
schema.attr('node', shape=symbol["class"])
schema.node('dcatdataset', label='dcat:dataset')
schema.node('Q935809', label='wd:Q935809')
schema.attr('node', shape=symbol["literal"])
schema.node('comma-separated values@en')
schema.attr('node', shape='octagon')
schema.node('filename', label='xsd:string')
schema.node('filedatecreated', label='xsd:date')
schema.node('filedatemodified', label='xsd:date')
schema.edge('fileURI', 'dcatdataset', label='rdf:type')
schema.edge('fileURI', 'Q935809', label='dcterms:format')
schema.edge('Q935809', 'comma-separated values@en', label='skos:prefLabel')
schema.edge('fileURI', 'filename', label="skos:prefLabel")
schema.edge('fileURI', 'filedatecreated', label="dcterms:issued")
schema.edge('fileURI', 'filedatemodified', label="dcterms:modified")

# ShEx
dataexpressions = []
dataexpressions.append(TripleConstraint(predicate=IRIREF(RDF.type),valueExpr=NodeConstraint(values=[DCAT.Dataset])))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.format),valueExpr=NodeConstraint(values=[IRIREF(WD.Q63082925)]), annotations=[Annotation(RDFS.label,ObjectLiteral("Office Open XML Spreadsheet Document", language="en"))]))
dataexpressions.append(TripleConstraint(predicate=IRIREF(RDFS.label), valueExpr=NodeConstraint(datatype=XSD.string)))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.issued), valueExpr=NodeConstraint(datatype=XSD.dateTime)))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.modified), valueExpr=NodeConstraint(datatype=XSD.dateTime)))

# RDF
rdf = Graph()
rdf.add((fileURI, RDF.type, DCAT.Dataset))
rdf.add((fileURI, DCTERMS.format, WD.Q63082925))
rdf.add((WD.Q63082925, RDFS.label, Literal("Office Open XML Spreadsheet Document", lang="en")))
rdf.add((fileURI, RDFS.label, Literal(filename, datatype=XSD.string)))
datecreated = os.path.getctime(filename)
rdf.add((fileURI, DCTERMS.issued, Literal(datetime.fromtimestamp(datecreated).strftime('%Y-%m-%dT%H:%M:%SZ'), datatype=XSD.dateTime)))
datemodified = os.path.getmtime(filename)
rdf.add((fileURI, DCTERMS.modified, Literal(datetime.fromtimestamp(datemodified).strftime('%Y-%m-%dT%H:%M:%SZ'), datatype=XSD.dateTime)))

cotton = Schema()
shapesns = 'http://agschemas.org/'
startshape = shapesns + "#cotton"
cotton.shapes = [Shape(startshape, expression=EachOf(expressions=dataexpressions))]
cotton.start = startshape

# print(str(ShExC(gbm1, base=shapesns, namespaces=rdf.namespace_manager)))
schema


# ### Load (synthetic) data

# In[5]:


pd.set_option('display.max_columns', None)
subjects = pd.read_csv(filename,index_col=False)
subjects


# ## File
# 
# ## Production Shape
# * OBJECTID
# * Date of planting
# * Date of harvest
# * ValuePerac
# * SeedingRatePerAcre
# * PercentBallOpened
# 
# ## ProductionCrop
# * Staple (1/32 in.)
# * Length (in.)
# * Strength (g/tex)
# * Micronaire
# * Leaf
# * Ext
# * HVIColor
# * ColorRd
# * Color+b
# * TrashArea (%)
# * Length Uniformity (%)
# * LintTurnout (%)
# * LintYield (lb/ac)
# * ValuePerac ($/ac) StormTolerance
# ## ProductionLocation Shape
# * LocationName
# * LatLong
# * Latitude
# * Longitude
# * City
# * County
# * State
# ## Variety Shape
# * Yield (lb. lint/acre)
# * Elongation
# * HVIColor
# * Leaf
# * Staple (1/32 in.)
# * Length (in.)
# * LintFraction (%)
# * Strength (g/tex)
# * Micronaire
# * Length Uniformity (%)
# * StormTolerance
# ## Experiment Shape
# * Name
# * TestType
# * EntryNumber
# * Brand
# ## Soil Shape
# * Product
# * Trait
# * Soil
# * Date of Tillage
# ## Lot Shape
# * Date of irrigation
# * IrrigationType
# ## Weather Shape
# * Max and min temp
# * Precipitation
# * Cloud cover
# 

# # Schema modelling
# # Production Shape
# ## Production Shape
# * OBJECTID
# * Date of planting
# * Date of harvest
# * ValuePerac
# * SeedingRatePerAcre
# * PercentBallOpened

# In[6]:


localviz = graphviz.Digraph()
localviz.graph_attr['rankdir'] = 'LR'
# uri
add2graphviz(command='attr', arg1='node', shape=symbol["iri"])
# nodes
add2graphviz(command='node', arg1='production', label="Production")
# classes
add2graphviz(command='attr', arg1='node', shape=symbol["class"])
# nodes
add2graphviz(command='node', arg1= 'cotton', label='cotton (nalt:4418)')
# datatypes
add2graphviz(command='attr', arg1='node', shape=symbol["datatype"])
# nodes
add2graphviz(command='node', arg1= 'harvestid', label='xsd:integer')
add2graphviz(command='node', arg1= 'plantingdate', label="xsd:date")
add2graphviz(command='node', arg1= 'harvestdate', label="xsd:date")
# bnodes
add2graphviz(command='attr', arg1= 'node', shape=symbol["bnode"])
# nodes
add2graphviz(command='node', arg1= 'valueperac')
add2graphviz(command='node', arg1= 'seedingrate')
add2graphviz(command='node', arg1= 'ballopened')

# Measurements
#* ValuePerac
def quantities(source, quantity, unitName, unit, unitLabel, unitDatatype ):
    add2graphviz(command='edge', arg1=source, arg2=quantity, label='agschemas:'+unitName)
    add2graphviz(command='attr', arg1='node', shape=symbol["class"])
    add2graphviz(command='node', arg1=quantity+'Type', label="qudt:Quantity")
    add2graphviz(command='node', arg1=quantity+'Kind', label="agunits:"+unitName)
    add2graphviz(command='node', arg1=unit, label="agunits:"+unitLabel)
    add2graphviz(command='attr', arg1='node', shape=symbol["datatype"])
    add2graphviz(command='node', arg1=quantity+'Value', label=unitDatatype)
    add2graphviz(command='edge', arg1=quantity, arg2=quantity+'Type', label="rdf:type")
    add2graphviz(command='edge', arg1=quantity, arg2=quantity+'Kind', label="qudt:hasQuantityKind")
    add2graphviz(command='edge', arg1=quantity, arg2=quantity+'Value', label="qudt:value")
    add2graphviz(command='edge', arg1=quantity, arg2=unit, label="qudt:unit")

quantities(source='production', quantity='valueperac', unitName='ValuePerAcre', unit='usdperacre', unitLabel='UsdPerAcre', unitDatatype="xsd:float")
#* SeedingRatePerAcre
quantities(source='production', quantity='seedingrateperacre', unitName='SeedingRatePerAcre', unit='seedsperacre', unitLabel='SeedsPerAcre', unitDatatype="xsd:float")
#* PercentBallOpened
quantities(source='production', quantity='percentballopened', unitName='unitpercent', unit='openballpercentage', unitLabel='unit:PERCENT', unitDatatype="xsd:float")


#edges
add2graphviz(command='edge', arg1='production', arg2='fileURI',label="schema:isPartOf")
add2graphviz(command='edge', arg1='production', arg2='crop', label='agschemas:harvested')
add2graphviz(command='edge', arg1='crop', arg2='cotton', label='rdf:type')

add2graphviz(command='edge', arg1='production', arg2='harvestid', label='dcterms:identifier')
add2graphviz(command='edge', arg1='production', arg2='harvestdate', label="agschemas:harvestDate")
add2graphviz(command='edge', arg1='production', arg2='plantingdate', label="agschemas:plantingDate")

localviz


# ## ProductionCrop
# * Staple (1/32 in.)
# * Length (in.)
# * Strength (g/tex)
# * Micronaire
# * Leaf
# * Ext
# * HVIColor
# * ColorRd
# * Color+b
# * TrashArea (%)
# * Length Uniformity (%)
# * LintTurnout (%)
# * LintYield (lb/ac)
# * ValuePerac ($/ac) StormTolerance

# In[7]:


localviz = graphviz.Digraph()
localviz.graph_attr['rankdir'] = 'LR'
# uri
add2graphviz(command='attr', arg1='node', shape=symbol["iri"])
# nodes
add2graphviz(command='node', arg1='production', label="Production")
add2graphviz(command='node', arg1='productioncrop', label="Production Crop")
# one of
add2graphviz(command='attr', arg1='node', shape=symbol["oneof"])

# nodes
add2graphviz(command='node', arg1='administrationtype', label="{ schema:City | schema:County | schema:State }")
add2graphviz(command='edge', arg1='harvest', arg2='harvestlocation', label='agschemas:harvestedAt')
add2graphviz(command='edge', arg1='harvestlocation', arg2='latitude', label='schema:latitude')
add2graphviz(command='edge', arg1='harvestlocation', arg2='longitude', label='schema:longitude')
add2graphviz(command='edge', arg1='harvestlocation', arg2='harvestlocationname', label='skos:prefLabel')
add2graphviz(command='edge', arg1='harvestlocation', arg2='administration', label='schema:isPartOf')
add2graphviz(command='edge', arg1='administration', arg2='administrationtype', label='rdf:type')
add2graphviz(command='edge', arg1='harvestlocation', arg2='zipcode', label="schemapostalCode")

localviz


# ## Agricultural experiment

# In[8]:


localviz = graphviz.Digraph()

# uri
add2graphviz(command='attr', arg1='node', shape=symbol["iri"])
add2graphviz(command='node', arg1='test', label="experiment")
add2graphviz(command='node', arg1='sample', label="nalt:9555")

# datatypes
add2graphviz(command='attr', arg1='node', shape=symbol["datatype"])
# nodes
add2graphviz(command='node', arg1= 'triallabel', label='xsd:string')
add2graphviz(command='node', arg1= '')
# one of
add2graphviz(command='attr', arg1='node', shape=symbol["oneof"])

# nodes
add2graphviz(command='node', arg1='agriculturetrialdesign', label="{agschemas:CAST | agschemas:CottonIncorporated|agschemas:County|agschemas:Extension|agschemas:OVT|agschemas:Strip|agschemas:VertWilt}")

add2graphviz(command='edge', arg1='harvest', arg2='test', label="agschemas:trialPerformed")
add2graphviz(command='edge', arg1='test', arg2='agriculturetrialdesign', label="rdf:type")
add2graphviz(command='edge', arg1='test', arg2='triallabel', label='skos:prefLabel')

localviz


# # RDF generation

# In[9]:


rdf = Graph()
for index, row in subjects.iterrows():
    # Row Subject
    SubjectId = str(row["OBJECTID"])
    rdf.add((SUBJECT[SubjectId], DCTERMS.isPartOf, fileURI))
    rdf.add((SUBJECT[SubjectId], DCTERMS.identifier, Literal(row["OBJECTID"], datatype=XSD.string)))

    rdf.add((SUBJECT[SubjectId], AGSCHEMAS.harvested, NALT["4418"]))
    LocationUri = HARVESTLOCATION[row["LocationName"].replace(" ", "_").strip()]
    rdf.add((SUBJECT[SubjectId], AGSCHEMAS.harvestedAt, LocationUri))
    rdf.add((SUBJECT[SubjectId], AGSCHEMAS.harvestedIn, Literal(row["Year"])))
    rdf.add((LocationUri, SKOS.prefLabel, Literal(row["LocationName"].replace(" ", "_").strip(), datatype=XSD.string)))
    rdf.add((LocationUri, SCHEMA.postalCode, Literal(row["ZIP Code"], datatype=XSD.string)))
    rdf.add((LocationUri, SCHEMA.latitude, Literal(row["Latitude"])))
    rdf.add((LocationUri, SCHEMA.longitude, Literal(row["Longitude"])))
    if row["City"] != None:
        if row["City"] in placeqids["city"].keys():
            rdf.add((LocationUri, SCHEMA.isPartOf, WD[placeqids["city"][row["City"]]] ))
    else:
        rdf.add((LocationUri, SCHEMA.isPartOf, WD[placeqids["county"][row["County"]]]))

    rdf.add((SUBJECT[SubjectId], AGSCHEMAS.plantingDate, Literal(row["PlantingDate"])))
    rdf.add((SUBJECT[SubjectId], AGSCHEMAS.harvestDate, Literal(row["HarvestDate"])))
    valuePerAcre = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, valuePerAcre))
    rdf.add((valuePerAcre, RDF.type, QUDT.Quantity))
    rdf.add((valuePerAcre, QUDT.hasQuantityKind, AGUNITS["ValuePerac"]))
    rdf.add((valuePerAcre, QUDT.unit, AGUNITS["USD-PER-ACRE"]))
    rdf.add((valuePerAcre, QUDT.value, Literal(row["ValuePerac"])))
    seedingRatePerAcre = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, seedingRatePerAcre))
    rdf.add((seedingRatePerAcre, RDF.type, QUDT.Quantity))
    rdf.add((seedingRatePerAcre, QUDT.hasQuantityKind, AGUNITS["SeedingRatePerAcre"]))
    rdf.add((seedingRatePerAcre, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((seedingRatePerAcre, QUDT.value, Literal(row["SeedingRatePerAcre"])))
    percentBollOpened = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, percentBollOpened))
    rdf.add((percentBollOpened, RDF.type, QUDT.Quantity))
    rdf.add((percentBollOpened, QUDT.hasQuantityKind, AGUNITS["PercentBollOpened"]))
    rdf.add((percentBollOpened, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((percentBollOpened, QUDT.value, Literal(row["PercentBollOpened"])))
    stormTolerance = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, stormTolerance))
    rdf.add((stormTolerance, QUDT.hasQuantityKind, AGUNITS["StormTolerance"]))
    rdf.add((stormTolerance, RDF.type, QUDT.Quantity))
    rdf.add((stormTolerance, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((stormTolerance, QUDT.value, Literal(row["StormTolerance"])))
    cottonyield = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, cottonyield))
    rdf.add((cottonyield, RDF.type, QUDT.Quantity))
    rdf.add((cottonyield, QUDT.hasQuantityKind, AGUNITS["Yield"]))
    rdf.add((cottonyield, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((cottonyield, QUDT.value, Literal(row["Yield"])))
    elongation = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, elongation))
    rdf.add((elongation, RDF.type, QUDT.Quantity))
    rdf.add((elongation, QUDT.hasQuantityKind, AGUNITS["Elongation"]))
    rdf.add((elongation, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((elongation, QUDT.value, Literal(row["Elongation"])))
    hvicolor = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, hvicolor))
    rdf.add((hvicolor, QUDT.hasQuantityKind, AGUNITS["HVIColor"]))
    rdf.add((hvicolor, RDF.type, QUDT.Quantity))
    rdf.add((hvicolor, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((hvicolor, QUDT.value, Literal(row["HVIColor"])))
    leaf = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, leaf))
    rdf.add((leaf, QUDT.hasQuantityKind, AGUNITS["Leaf"]))
    rdf.add((leaf, RDF.type, QUDT.Quantity))
    rdf.add((leaf, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((leaf, QUDT.value, Literal(row["Leaf"])))

    length = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, length))
    rdf.add((length, QUDT.hasQuantityKind, AGUNITS["Length"]))
    rdf.add((length, RDF.type, QUDT.Quantity))
    rdf.add((length, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((length, QUDT.value, Literal(row["Length"])))

    lintfraction = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, lintfraction))
    rdf.add((lintfraction, RDF.type, QUDT.Quantity))
    rdf.add((lintfraction, QUDT.hasQuantityKind, AGUNITS["LintFraction"]))
    rdf.add((lintfraction, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((lintfraction, QUDT.value, Literal(row["LintFraction"])))

    loanvalue = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, loanvalue))
    rdf.add((loanvalue, RDF.type, QUDT.Quantity))
    rdf.add((loanvalue, QUDT.hasQuantityKind, AGUNITS["LoanValue"]))
    rdf.add((loanvalue, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((loanvalue, QUDT.value, Literal(row["LoanValue"])))

    mic = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, mic))
    rdf.add((mic, RDF.type, QUDT.Quantity))
    rdf.add((mic, QUDT.hasQuantityKind, AGUNITS["Mic"]))
    rdf.add((mic, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((mic, QUDT.value, Literal(row["Mic"])))

    strength = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, strength))
    rdf.add((strength, RDF.type, QUDT.Quantity))
    rdf.add((strength, QUDT.hasQuantityKind, AGUNITS["Strength"]))
    rdf.add((strength, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((strength, QUDT.value, Literal(row["Strength"])))

    ui = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, ui))
    rdf.add((ui, RDF.type, QUDT.Quantity))
    rdf.add((ui, QUDT.hasQuantityKind, AGUNITS["UI"]))
    rdf.add((ui, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((ui, QUDT.value, Literal(row["UI"])))

    turnout = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, turnout))
    rdf.add((turnout, RDF.type, QUDT.Quantity))
    rdf.add((turnout, QUDT.hasQuantityKind, AGUNITS["Turnout"]))
    rdf.add((turnout, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((turnout, QUDT.value, Literal(row["Turnout"])))

    grossincome = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, grossincome))
    rdf.add((grossincome, RDF.type, QUDT.Quantity))
    rdf.add((grossincome, QUDT.hasQuantityKind, AGUNITS["GrossIncome"]))
    rdf.add((grossincome, QUDT.unit, AGUNITS["TBD"]))
    rdf.add((grossincome, QUDT.value, Literal(row["GrossIncome"])))











    ui = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, ui))
    turnout = BNode()
    rdf.add((SUBJECT[SubjectId], SCHEMA.variableMeasured, turnout))



# In[78]:


print(rdf.serialize(destination=filename+".ttl", format="turtle"))


# In[59]:


subjects


# In[62]:


placedf = pd.read_csv("data/cottonplace.csv")
placeqids = {"city" : {}, "county" :{}}
for index, row in placedf.iterrows():
    placeqids["city"][row["City"]]=row["cityURI"]
    placeqids["county"][row["County"]]=row["countyQID"]
placeqids


# In[34]:


schema.view()
schema


# # ShEx design

# In[99]:


dataexpressions = []
dataexpressions.append(TripleConstraint(predicate=IRIREF(RDF.type),valueExpr=NodeConstraint(values=[DCAT.Dataset])))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.format),valueExpr=NodeConstraint(values=[IRIREF(WD.Q63082925)]), annotations=[Annotation(RDFS.label,ObjectLiteral("Office Open XML Spreadsheet Document", language="en"))]))
dataexpressions.append(TripleConstraint(predicate=IRIREF(RDFS.label), valueExpr=NodeConstraint(datatype=XSD.string)))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.issued), valueExpr=NodeConstraint(datatype=XSD.dateTime)))
dataexpressions.append(TripleConstraint(predicate=IRIREF(DCTERMS.modified), valueExpr=NodeConstraint(datatype=XSD.dateTime)))


# In[100]:


for node in rdf.all_nodes():
    if isinstance(node, URIRef):
        try:
            rdf.parse(node)
        except:
            print(node)


# # Extract schema

# In[101]:


from shexer.shaper import Shaper
from shexer.consts import NT, TURTLE

q = "select ?class where { ?item rdf:type ?class }"
target_classes = []
x = rdf.query(q)
for target_class in x:
  if str(target_class["class"]) not in target_classes:
    target_classes.append(str(target_class["class"]))

shex_target_file = filename+".shex"

shaper = Shaper(target_classes=target_classes,
                rdflib_graph=rdf,
                input_format=TURTLE,
                )  # Default rdf:type
            
shaper.shex_graph(output_file=shex_target_file)


# In[61]:


placedf


# In[ ]:




