---
layout: default
title: Glycerin
parent: Model Prediction Only (L5)
nav_order: 756
evidence_level: L5
indication_count: 10
monitor_inn: "GLYCERIN"
predicted_indications: ["cauda equina syndrome", "open-angle glaucoma", "primary hereditary glaucoma", "alopecia", "congenital hypotrichosis milia", "irritable bowel syndrome", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "migraine disorder", "migraine with brainstem aura"]
---

# Glycerin
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

# Glycerin: From Constipation to Open-Angle Glaucoma

## One-Sentence Summary

Glycerin is an osmotic agent originally used to treat constipation (for example, as a rectal suppository).
Among its predicted new uses, the TxGNN model ranks **Cauda Equina Syndrome** first by score, but the best-supported candidate is **Open-Angle Glaucoma**, where there are **0 clinical trials** and only **3 indirect publications**.
Overall evidence is weak, and none of the top 10 predictions is supported by a direct clinical study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constipation disorder (from the knowledge graph; no approved indication text is available in the US license records) |
| Predicted New Indication | Cauda equina syndrome (rank 1 by score). Open-angle glaucoma (rank 2) has the most relevant mechanism and is the main focus below. |
| TxGNN Prediction Score | 99.60% (cauda equina syndrome); 99.59% (open-angle glaucoma) |
| Evidence Level | L5 for cauda equina syndrome; L4 for open-angle glaucoma |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known pharmacology, glycerin is a hyperosmotic agent. In the bowel it draws water into the lumen, which softens stool and stimulates evacuation. This explains its original use in constipation.

The same osmotic property gives a plausible link to **open-angle glaucoma**. Oral glycerin has historically been used to lower intraocular pressure (IOP), mainly in acute angle-closure episodes. However, the retrieved literature does not test glycerin as a treatment for open-angle glaucoma. The papers cover angle-closure pathogenesis, glycerin-preserved donor grafts used in drainage surgery, and osmoprotection for dry eye. The evidence is indirect only.

For the other top predictions, the rationale is weaker:
- **Cauda equina syndrome**, **primary hereditary glaucoma**, **congenital hypotrichosis milia**, **hypotrichosis simplex of the scalp**, **diffuse alopecia areata** and **migraine with brainstem aura**: no mechanism is identified, and no trials or papers support them. These appear to be network-similarity artifacts. An osmotic effect does not plausibly address a compressive or neurological injury, hereditary structural pathology, autoimmune hair loss or genetic hair-follicle disorders.
- **Alopecia**: the retrieved papers show only excipient or cosmetic safety use, and no therapeutic effect of glycerin.
- **Irritable bowel syndrome** (IBS): the osmotic laxative action is relevant to constipation-predominant IBS and is related to the original indication. The retrieved papers do not test glycerin in IBS, so this remains indirect.
- **Migraine disorder**: the single paper concerns glycerin injection for epistaxis and is not relevant to migraine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

Literature for the leading candidate, **open-angle glaucoma**:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1614157](https://pubmed.ncbi.nlm.nih.gov/1614157/) | 1992 | Review | Klinische Monatsblatter fur Augenheilkunde | Pathogenesis and treatment of primary angle-closure glaucoma. It is not about open-angle glaucoma or glycerin therapy. |
| [32890110](https://pubmed.ncbi.nlm.nih.gov/32890110/) | 2020 | Case series | Journal of Glaucoma | Glycerin-preserved human-donor corneoscleral patch grafts were effective and safe for glaucoma drainage devices. Glycerin served as a tissue preservative, not a therapeutic. |
| [20872359](https://pubmed.ncbi.nlm.nih.gov/20872359/) | 2011 | Clinical study | European Journal of Ophthalmology | Osmoprotective artificial tears and ocular surface damage in glaucoma patients on topical therapy. It concerns ocular surface disease, not IOP control. |

Literature for other predicted indications (all indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14215532](https://pubmed.ncbi.nlm.nih.gov/14215532/) | 1964 | Review / commentary | JAMA | "Irritable colon" (IBS). General commentary that does not test glycerin. |
| [29191058](https://pubmed.ncbi.nlm.nih.gov/29191058/) | 2017 | Preclinical | Drug Delivery | Nanoemulsion delivery of berberine hydrochloride (Caco-2 cells). Not about glycerin in IBS. |
| [3896179](https://pubmed.ncbi.nlm.nih.gov/3896179/) | 1985 | Clinical study (RCT) | Archives of Internal Medicine | Polysorbate 60 was ineffective for male pattern baldness. Glycerin was the control and showed no benefit. |
| [14555416](https://pubmed.ncbi.nlm.nih.gov/14555416/) | 2003 | Safety review | International Journal of Toxicology | Safety assessment of triacetin (a glycerin derivative) as a cosmetic ingredient. |
| [32227767](https://pubmed.ncbi.nlm.nih.gov/32227767/) | 2020 | Safety study | Journal of Traditional Chinese Medicine | Skin and eye safety of a bee venom hair essence in rabbits. Not a glycerin efficacy study. |
| [4666940](https://pubmed.ncbi.nlm.nih.gov/4666940/) | 1972 | Case series | Trans. Am. Acad. Ophthalmol. Otolaryngol. | Glycerin injection of the pterygopalatine fossa for posterior epistaxis. Not about migraine. |

---

## US Market Information

All six US licenses are cancelled, and no approved indication text is recorded for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| M006 | CLENZIDERM THERAPEUTIC MOISTURIZER | Cream | Not recorded |
| M018 | Clear Eyes Nighttime | Solution/drops | Not recorded |
| M016 | ANTIBACTERIAL FRUITY ZEST | Soap | Not recorded |
| M007 | Stratuscare Adult Glycerin | Suppository | Not recorded |
| M007.54 | Proctozone-G | Suppository | Not recorded |

A sixth license (M014, Optimel Manuka Forte Eye Gel, gel) is also cancelled.

---

## Safety Considerations

Please refer to the package insert for safety information. Package insert warnings and contraindications were not available in the data compiled for this report, and the knowledge graph lists no contraindicated diseases.

**Drug Interactions**: 100 interactions were found in the DDInter database. The 20 reviewed here are mostly **Moderate**, with one **Minor** (doxycycline). Examples of Moderate interactions:
- Abiraterone, tramadol, acetazolamide
- Hydrocortisone, triamcinolone
- Salbutamol, alfuzosin
- Hydrochlorothiazide, amiloride, benazepril
- Amiodarone, amisulpride, arsenic trioxide, lumefantrine, asenapine
- Anagrelide, propofol, apalutamide, apomorphine

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predictions have high model scores (about 99.2% to 99.6%), but none has a clinical trial or a direct study. The best-supported candidate, open-angle glaucoma, rests on an indirect osmotic IOP-lowering rationale. The US licenses are all cancelled, and the package insert safety data are missing.

**To proceed, the following is needed:**
- Obtain FDA package insert warnings and contraindications to allow safety screening.
- Obtain mechanism of action data from DrugBank.
- For open-angle glaucoma, search for studies of oral glycerin and IOP, and compare it with current glaucoma treatments, since osmotic agents lower IOP only transiently and are not standard in open-angle disease.
- For constipation-predominant IBS, search for direct clinical evidence of glycerin or osmotic laxatives.
- Confirm route and formulation compatibility for any indication pursued, since this has not yet been assessed.
- Deprioritize the genetic hair disorders, cauda equina syndrome and migraine predictions unless new supporting evidence appears.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

