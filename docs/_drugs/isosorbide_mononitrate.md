---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 816
evidence_level: L5
indication_count: 10
monitor_inn: "ISOSORBIDE MONONITRATE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "alopecia", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "pulmonary arterial hypertension"]
last_modified_at: 2026-10-30
description: "Isosorbide Mononitrate: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the compiled data (the drug is known as a nitrate vasod…"
---

# Isosorbide Mononitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Isosorbide Mononitrate: From Angina Pectoris to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Isosorbide mononitrate is an oral nitrate vasodilator. In the US it is sold as immediate-release and extended-release tablets, but the data compiled for this report contain no approved-indication text.
The TxGNN model's top-ranked prediction is **hypertrichosis**, with a score of 1.0000. There are **0 clinical trials** and **0 publications** supporting it, so this is a model prediction only.
The only prediction with any literature is **pulmonary arterial hypertension** (rank 10, 2 indirect publications), which is a better-grounded research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled data (the drug is known as a nitrate vasodilator; the label text was not captured) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses on record: at least 7) |
| Number of FDA Applications | 7 licences (1 NDA, 6 ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on general knowledge, isosorbide mononitrate is a nitric oxide (NO) donor. NO activates soluble guanylate cyclase, raises cGMP, and relaxes vascular smooth muscle.

For the top prediction, hypertrichosis (score 1.0000), the link is weak. The only plausible argument is that increased skin blood flow could influence hair growth, as with minoxidil. But hypertrichosis is a disorder of *excess* hair growth, so a vasodilator-like effect would be expected to worsen it rather than treat it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions are similarly unsupported:
- **Alopecia and diffuse alopecia areata:** a speculative perfusion argument for alopecia, and an autoimmune (JAK/IFN-γ-driven) disease for alopecia areata, with no supporting data.
- **Genetic and congenital conditions** (Ambras syndrome, hair shaft abnormalities, hypotrichosis simplex, congenital hypotrichosis milia, Dandy-Walker and odontal malformation syndromes): no known pathway links NO donation to these genetic causes.

The exception is **pulmonary arterial hypertension (PAH)**. Here the mechanism is biologically plausible, because the NO-sGC-cGMP pathway is the same one targeted by sildenafil and riociguat. Caveats include nitrate tolerance, possible V/Q mismatch, and a dangerous interaction with PDE5 inhibitors (severe hypotension).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (hypertrichosis). The only literature retrieved is for the rank-10 prediction, pulmonary arterial hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | J Sex Med | Hemodynamic effects of sildenafil and isosorbide mononitrate in men with coronary artery disease and erectile dysfunction (not a PAH population) |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical animal study | Life Sci | sGC stimulation in monocrotaline-induced pulmonary hypertensive rats; examined NO-enhancing drugs (not isosorbide mononitrate itself) |

## US Market Information

Seven licences are currently valid in the US market, and the drug is marketed. Approved-indication text was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA210822 | Isosorbide Mononitrate (Chartwell RX) | Tablet, extended release | Not available |
| ANDA210918 | Isosorbide Mononitrate (Ingenus) | Tablet, extended release | Not available |
| NDA020215 | Isosorbide Mononitrate (Proficient Rx) | Tablet | Not available |
| ANDA075522 | Isosorbide Mononitrate (NuCare) | Tablet, extended release | Not available |
| ANDA200270 | Isosorbide Mononitrate (American Health Packaging) | Tablet, extended release | Not available |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease links, not label text): hypotensive disorder, hypertrophic cardiomyopathy, myocardial infarction, coronary thrombosis, hemoglobinopathy, anaemia (including macrocytic anaemia), hyperthyroidism, Graves disease, thyrotoxicosis, and intracerebral haemorrhage.
- **Drug interactions:** 100 interactions were found in total. Examples of the 20 reviewed:
  - *Moderate:* bupropion, morphine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, dronabinol, nabilone, opium, sapropterin, rosiglitazone
  - *Minor:* omeprazole
  - *Unknown severity:* calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, clotrimazole, metformin, lansoprazole
- **Important class interaction:** nitrates combined with PDE5 inhibitors (e.g., sildenafil) can cause severe hypotension. This is highly relevant to the PAH hypothesis.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (hypertrichosis) and the other hair and genetic-disorder predictions rest only on TxGNN model (deep learning) scores, which may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature support them, and the vasodilator mechanism argues against benefit in hypertrichosis. Pulmonary arterial hypertension (L4) is biologically plausible, but its evidence is indirect and the nitrate-PDE5 inhibitor safety problem is significant. It should be treated as a research question only, not a go decision.

**To proceed, the following is needed:**
- FDA package insert data (warnings, contraindications, approved indications), the blocking data gap for safety screening
- Mechanism-of-action data from DrugBank
- For PAH: direct clinical or preclinical studies of isosorbide mononitrate in PAH models, and a review of nitrate tolerance and PDE5 inhibitor co-use risks
- Clarification of current US market status, since the facts list 7 valid licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

