---
layout: default
title: Chlorpheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 522
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Chlorpheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis (other original indications include vasomotor rhini…"
monitor_inn: "CHLORPHENIRAMINE"
predicted_indications: ["nasal cavity disease"]
---

# Chlorpheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Chlorpheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Chlorpheniramine is a first-generation H1 antihistamine, originally used for allergic rhinitis, the common cold, and allergic skin conditions such as urticaria.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, but **no clinical trials** are registered for this prediction, and the **20 publications** retrieved are mostly reviews of other antihistamines or case reports.
Urticaria and angioedema are already among the drug's known indications, so this prediction largely overlaps with existing use rather than representing true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other original indications include vasomotor rhinitis, pharyngitis, common cold, conjunctivitis, urticaria and angioedema) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, chlorpheniramine is a first-generation H1-receptor antagonist (inverse agonist). In allergic urticaria, histamine released from mast cells causes the wheal-and-flare response, so blocking H1 receptors is a direct mechanistic fit.

The prediction is not a distant leap. Urticaria and angioedema are already listed among the drug's original indications, so the model is largely re-identifying a known use. The 2024 comprehensive review of chlorpheniramine and the comparative H1-antihistamine literature support the class effect. However, most retrieved papers examine other antihistamines (cetirizine, loratadine, acrivastine, ebastine), not chlorpheniramine-specific trials.

Other predictions in the data are weaker:
- **Cold urticaria** (score 99.13%, evidence L3): a small 1977 double-blind study compared chlorpheniramine, cyproheptadine and placebo. It is old, and modern guidelines favor second-generation antihistamines.
- **Nasal cavity disease** (score 99.53%, evidence L4): only animal models and mechanistic studies, and the term is too nonspecific to define an indication.
- **Acute laryngopharyngitis** (score 99.50%, evidence L5): model score only, with no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine, covering uses in allergic conditions, chronic urticaria, asthma and others |
| [1683523](https://pubmed.ncbi.nlm.nih.gov/1683523/) | 1991 | Review | Ann Allergy | Comparative efficacy of H1 antihistamines; second-generation agents are less sedating |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine in allergic rhinitis and urticaria (other drug, class-level support) |
| [14977391](https://pubmed.ncbi.nlm.nih.gov/14977391/) | 2004 | Review | Drugs | Cetirizine in allergic disorders including urticaria (other drug, class-level support) |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine was as effective as chlorpheniramine and other antihistamines in allergic disorders |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case report / pharmacovigilance | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus a pharmacovigilance database review |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Case report | Asia Pac Allergy | Chlorpheniramine-induced anaphylaxis diagnosed by basophil activation test |
| [21217928](https://pubmed.ncbi.nlm.nih.gov/21217928/) | 2011 | Case report | Allergy Asthma Immunol Res | Chlorpheniramine hypersensitivity with aspirin intolerance (rare) |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort | Asian Pac J Allergy Immunol | Epidemiology of urticaria in 142 Thai children |
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | RCT | Arch Dermatol | Cold urticaria, 8 patients: double-blind comparison of chlorpheniramine, cyproheptadine and placebo (relevant to the cold urticaria prediction) |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040829 | Chlorphen-12 | Extended-release film-coated tablet | Not listed (cancelled) |
| M012 | Pharbechlor | Tablet | Not listed (cancelled) |
| nan | ED CHLORPED JR | Liquid | Not listed (cancelled) |

All three authorizations are cancelled, so no valid single-ingredient or combination products are currently registered in the data compiled for this report.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: The knowledge graph links chlorpheniramine to a wide range of conditions as contraindications or cautions, including:
  - Cardiovascular: hypertension, hypotension
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Gastrointestinal: peptic and gastric ulcer, gastritis, inflammatory bowel disease, pancreatitis, gallbladder disease
  - Respiratory: COPD, bronchitis
  - Endocrine: hypothyroidism, myxedema, diabetes mellitus, diabetic ketoacidosis
  - Neurological and psychiatric: epilepsy, insomnia, psychotic disorders, schizophreniform disorder, schizoaffective disorder
  - Other: benign prostatic hyperplasia, thrombocytopenia, dermatitis herpetiformis

  These should be verified against the official label.
- **Drug Interactions**: 100 interactions were found. Major interactions are with **potassium chloride** and **potassium citrate**. Moderate interactions include anticholinergics (atropine, dicyclomine, glycopyrronium, methscopolamine, mepenzolate), opioids (morphine, opium, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), bupropion, metoclopramide, eliglustat, lorcaserin and glycerol phenylbutyrate.
- **Hypersensitivity**: Rare but documented reports of chlorpheniramine-induced anaphylaxis and urticaria exist, which matters when the drug is considered for an urticaria indication.
- **Class concerns**: The literature notes that sedation and anticholinergic burden of first-generation antihistamines lead modern guidelines to favor second-generation agents.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The H1-blockade mechanism fits allergic urticaria well, but the indication already overlaps with existing labeled use, so this is not genuine repurposing.
- There are no registered clinical trials, no chlorpheniramine-specific modern trials, and all US licenses are cancelled. The strongest direct evidence is a small 1977 study in cold urticaria, and safer second-generation antihistamines are generally preferred.

**To proceed, the following is needed:**
- Official US package insert data on warnings and contraindications
- Mechanism of action data from DrugBank
- Chlorpheniramine-specific controlled studies in urticaria (allergic or cold), ideally compared against second-generation antihistamines
- A defined rationale for reintroduction given that no US licenses are currently valid
- Review of the anticholinergic and sedation risks, the hypersensitivity reports, and the major potassium interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

