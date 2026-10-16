---
layout: default
title: Zinc Gluconate
parent: Model Prediction Only (L5)
nav_order: 1307
evidence_level: L5
indication_count: 10
monitor_inn: "ZINC GLUCONATE"
predicted_indications: ["anemia of prematurity", "injury", "cell proliferation disorder", "perinatal disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "radiation or chemically induced disorder", "disease by subcellular system affected", "iatrogenic disease", "regional odontodysplasia"]
---

# Zinc Gluconate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Zinc Gluconate: From Ascorbic Acid Deficiency (Scurvy) to Anemia of Prematurity

## One-Sentence Summary

Zinc gluconate is a zinc salt. In the knowledge graph used for this analysis, its original indications are ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be useful for **anemia of prematurity**, but **no clinical trials and no publications** were retrieved for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency / scurvy (from the knowledge graph; no approved indication text appears in the US license record) |
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Zinc is an essential trace element involved in many enzyme systems. It also takes part in erythropoiesis and in iron and copper metabolism. That makes a link to anemia in preterm infants plausible in principle.

The link to the original indication is weak. Scurvy is a vitamin C deficiency, and the knowledge graph connects it to zinc gluconate mainly as a nutritional-deficiency association. The prediction therefore reflects graph-based similarity, not demonstrated clinical benefit in preterm anemia.

Zinc also has a known double-edged effect on blood. Excess zinc intake can cause copper deficiency and anemia (a case report of anemia from chronic high-dose zinc gluconate appears in the retrieved literature). Any use in infants would need very careful dosing.

## Clinical Trial Evidence

Currently no related clinical trials are registered for anemia of prematurity.

For reference, the second-ranked prediction ("injury") had one Phase 3 trial (NCT06290219). It tests platelet-rich plasma with hyaluronic acid nasal injection and does not involve zinc gluconate, so it gives no support for this drug.

## Literature Evidence

Currently no related literature is available for anemia of prematurity.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Not available | Zinc Cold Therapy (BETTER LIVING BRANDS LLC) | Chewable tablet | Not stated (status: cancelled) |

The only US license on record is cancelled. Other dosage forms in the data are oral tablets and lozenges.

## Safety Considerations

- **Knowledge-graph contraindication signals** (graph associations, not label text): hypertension and hypertensive disorder, rheumatoid arthritis, systemic lupus erythematosus (including pediatric), multiple sclerosis, allergic and vasomotor rhinitis, blood coagulation disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, diarrheal disease, asthma, HIV infection/AIDS, and leukemia.
- **Drug interactions**: 100 interactions were found, and the 20 shown here are mostly Minor. The Moderate ones are:
  - Alendronic acid
  - Risedronic acid
  - Ibandronate
  - Tetracycline
  - Baloxavir marboxil

  The Minor ones include immunosuppressants and biologics (such as abatacept, adalimumab, azathioprine) and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone).
- **Literature safety signals**: intranasal zinc gluconate has been linked to loss of smell (anosmia) in humans and animals. Chronic excessive zinc intake has caused copper-deficiency anemia.

Package insert warnings and contraindications were not available. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.94% TxGNN score is a graph-based prediction with no supporting trials or publications (L5). The drug has no active US license, and the knowledge graph lists blood-related contraindication signals (sickle cell anemia, iron metabolism disease, blood coagulation disease), which need clarification before any use in preterm infants.

**To proceed, the following is needed:**
- A literature and trial search specific to zinc and anemia of prematurity, including neonatal zinc, copper and iron status
- Mechanism of action data
- FDA package insert warnings and contraindications
- A neonatal dose and safety assessment, covering the risk of copper-deficiency anemia
- Review of the route and formulation, since current data covers only oral tablets and lozenges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

