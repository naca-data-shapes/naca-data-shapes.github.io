Overview
====

Researchers in agriculture seek to understand how factors such as weather, soil composition, and planting technique affect the quantity and quality of agricultural production.

Research typically starts with a problem, such as the relationship of growing conditions to the quality of a harvested product. 

To explore that problem, a researcher may need to pull data together from a variety of sources, such as sensors, smart phones, drones, or published statistics. That data may be available in a diversity of formats, such as databases, spreadsheets, instrument feeds, or even printed reports. The available data may use different units of measure, such as centimeters versus inches, or reflect different levels of granularity, such as state versus county. 

Researchers must decide which elements of the available sources will be required to support their planned queries or regression analyses. Through discussions and whiteboard diagrams (which we like to call ["boxologies"](https://www.youtube.com/watch?v=w1HTzAbCMDs&t=1491s)), researchers conceptualize the entities of interest for a given research problem, relationships among those entities, and the required properties for each entity. Each entity, along with its properties, is defined as a "data shape". 

In this project, data shapes are formalized as schemas using the Shape Expressions Language, or [ShEx](https://shex.io/shex-primer/). ShEx schemas are based, in turn, on Resource Description Framework, or [RDF](https://www.w3.org/TR/skos-primer/) -- a generalized and implementation-agnostic standard for expressing data in terms of sentence-like statements organized in flexible graph structures. RDF, in turn, is founded on the Uniform Resource Identifier, or URIs, most recognizable as the ubiquitous URL, or "Web address". 

The elements of data shapes are ideally identified with URIs from global "authorities" -- stable, persistent, institutionally backed repositories of well-defined URIs. It is the use of authoritative URIs that allow data shapes to serve as the basis for data interoperability not just in the here and now, but also in the future. For authoritative URIs related to concepts and properties in agriculture, the USDA research world looks to the [NALT Concept Space](https://agclass.nal.usda.gov/) of the National Agricultural Library. NALT, formerly known as the NAL Thesaurus, has extended its mission to support the creation of data shapes in support of research data interoperability.

A simple example: To address a given research problem, a researcher may need two data shapes: a "crop sample shape" with NALT URIs for harvest weight and color, and a "weather shape" with NALT URIs for precipitation and cloud cover. These shapes, or "target shapes", can serve as targets for converting, normalizing, and integrating selected data elements from a variety of sources and in a variety of formats. Precipitation might be pulled from a weather database by SQL query. Harvest weight might be extracted from a spreadsheet and converted into metric units using a Python script. (The implementation specifics of extraction and normalization are orthogonal to data shapes themselves.)

Data shapes can be published on the Web for use by other researchers or for adaptation to related research domains. To the extent that data shapes are based on authoritative URIs from NALT, data shapes serve to focus the efforts of agricultural researchers in the interest of improving data interoperability over the long term.
