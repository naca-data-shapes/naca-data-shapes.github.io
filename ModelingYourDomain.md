# Modeling Your Domain

The [overall model](index.md) is broken into sharable components:
1. Core model - Experimental data design and capture, shared environmental and geographic structures.
2. Cross-domain models - Elements shared between different Crop or Livestock domains.
3. Domain model - Elements specific to a particular domain, e.g. cotton crops.

Thse models are expressed as Shape Expressions (ShEx).
The core model defimes the model for a generic experimental sample.
The cross-domain model "Crop" extends that sample to include attributes common across crop products.
The Cotton model defines a `CottonSample` then extends `CropSample`.

Roughtly, the steps you will perform will be:
1. Familiarize yourself with the Core model; consider how it intersects with your data capture needs.
2. Pick a cross-domain model, e.g. Crop or Livestock, that encompasses your domain.
3. Develop a list of domain-specific entities. For an example, see the Cotton example in the [boxology](index.md).
4. Express your domain-model in ShEx; see the [Cotton.shex](https://github.com/agschemas/shapesdemo/blob/main/cotton-2023-05-10/schemas/Cotton.shex) for refernce.
5. Many properties in your domain model will already be defined in NALT. Use those NALT terms where possible.
6. Where no NALT terms exist, use descriptive property labels. e.g. `MeasuredMicronair`, as placeholders until theNALT curators can add them to NALT.

## Extension of cross-domain models
Modeling requires iteration and evaluation.
You may feel that your domain model includes attributes that should are common to other domains.
If they are commont to everything within e.g. Crops or Livestoc, propose the ammending that model.

### Creating new cross-domain models
If your domain attributes are shared with a small subsets of the other domains in your cross-domain model, you can develop new models to be shared between those domains.
For example, it is likely that the development of model for sheep farming and sheering will include factoring a fiber model with attributes shared with Cotton.
