Semantic Modelling
=======

The proposed semantic model includes experimental design and data captured for those experiments.
It is designed for optimal re-use, allowing all experiments to reuse the <span style="background-color: #cfe2f3">experiment shapes</span>, all experiments on <span style="background-color: #fff2cc">crops</span> (vs. e.g. livestock) to reuse soil and harvest methods shapes, and specific products, e.g. <span style="background-color: #ffffff">cotton</span>, to extend the crop shapes.
This image is intended to orient readers as to the current model, inspire further development, and orient developers of other crop products with its inclusion of the cotton exemplar.

![experiment model with cotton](boxology-lot-to-location.svg)

This model exploits inheritance, allowing the base <span style="background-color: #cfe2f3">experiments</span> to reference abstract `Sample`s.
<span style="background-color: #cfe2f3">Crop Samples</span> add attributes common to (hopefully) all crops.
<span style="background-color: #ffffff">Cotton Samples</span> include the remaining attributes common to measurements of cotton growth and harvest.
A similar hierarchy captures the expected yield with the cotton-specific <span style="background-color: #ffffff">VarietySpec</span> extending <span style="background-color: #fff2cc">CropSpec</span>, which in turn extends the base notion of a <span style="background-color: #cfe2f3">ReferenceSpec</span>.
The <span style="background-color: #ffffff">cotton shapes</span> include two enumerations for ginning and cleaning methods, as well as additional harvest methods.

Each Test includes a set of Blocks, each of which collects a set of TestDescriptions.
TestDescriptions capture both test constraints and study variables.
The latter are distinguished by having fixed value that constraints the intentions of the study.
The `var` attribute identifies attributes from e.g. Samples or Weather.
In the image, this is represented by a green line pointing at an attribute.

* <span style="background-color: #cfe2f3">experiments</span>
* <span style="background-color: #fff2cc">crops</span>
* <span style="background-color: #ffffff">cotton</span>
