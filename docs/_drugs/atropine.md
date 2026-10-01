---
layout: default
title: Atropine
parent: Moderate Evidence (L3-L4)
nav_order: 428
evidence_level: L4
indication_count: 2
---

# Atropine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Atropine: From Marketed Muscarinic Antagonist to Migraine Disorder

## One-Sentence Summary

Atropine is a long-marketed non-selective muscarinic (anticholinergic) drug, with 20 US authorizations for injectable and solution forms.
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials** are registered and the literature is mostly **preclinical or mechanistic**.
This is a research question rather than a ready candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine is a non-selective muscarinic antagonist. Detailed mechanism-of-action data is not available in the source record, and the approved indication text for the listed authorizations is also empty. This analysis therefore relies on the known pharmacology of the drug class and the retrieved literature.

Several lines of preclinical work link cholinergic signaling to migraine biology:
- In rats, stimulating the parasympathetic sphenopalatine ganglion causes plasma protein extravasation in the dura mater, a model of neurogenic inflammation.
- A 2024 rat study implicates meningeal mast cell-mediated cholinergic modulation in neurogenic inflammation in the nitroglycerin-induced migraine model.
- Central cholinergic pathways are involved in sumatriptan-induced antinociception in rodents.
- In four patients with chronic paroxysmal hemicrania (a related headache disorder), systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion.

This supports a biologically plausible role for cholinergic pathways, but it does not show that blocking muscarinic receptors with atropine relieves or prevents migraine. No human study of atropine as a migraine treatment was found. Systemic anticholinergic effects (tachycardia, dry mouth, blurred vision, urinary retention, CNS effects) would also limit chronic use.

A second predicted indication, **migraine with brainstem aura** (score 99.42%, evidence level L5), rests on a single mouse study of cortical spreading depression. That study describes cholinergic *activation* inhibiting spreading depression, so the direction of effect for an antagonist like atropine is unclear. It is held.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Thirteen items were reported for migraine disorder, and 10 were provided for review. No RCTs were found. The table lists the items relevant to the cholinergic-migraine question.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical/Mechanistic | Eur J Neurosci | Cholinergic modulation and a mast cell stabilizer studied in the nitroglycerin migraine model in rats, supporting a meningeal mast cell–cholinergic mechanism in neurogenic inflammation |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical (animal) | Exp Neurol | Stimulating the parasympathetic sphenopalatine ganglion induced plasma protein extravasation in rat dura mater, consistent with a parasympathetic role in dural inflammation |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical observational | Cephalalgia | In 4 patients with chronic paroxysmal hemicrania, systemic atropine markedly reduced attack-related sweating, tearing and nasal secretion (autonomic features, not pain) |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical (animal) | J Pharmacol Exp Ther | Central cholinergic system is involved in the antinociception induced by sumatriptan in rodents and guinea pigs |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Not classified | Neurosci Lett | Examines the role of CGRP and nicotinic receptors in centrally evoked facial blood flow changes; CGRP is linked to migraine headache |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical (ex vivo) | Br J Pharmacol | Studied nicotine-evoked relaxation of guinea-pig basilar artery; atropine was only a background agent, not the tested treatment |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Pharmacology of anisodamine, an atropine derivative; not migraine-specific, so indirect support at most |

The following retrieved papers are not about atropine as an antimigraine treatment and were not counted as supporting evidence: PMIDs 40590589 (botulinum-induced dropped head syndrome), 27179636 (stunned myocardium after anesthesia), 18091300 and 18604026 (topiramate ocular adverse effects), 1786517 (ergotamine at 5-HT1C receptors), and 21252 (beta-phenethylamine).

For migraine with brainstem aura, the only item is [31945385](https://pubmed.ncbi.nlm.nih.gov/31945385/) (2020, Neuropharmacology). This mouse study shows cholinergic modulation inhibits cortical spreading depression through muscarinic receptor activation.

---

## US Market Information

Showing 5 of 20 authorizations. Approved indication text is not provided for these records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| ANDA215342 | atropine sulfate | Injection, solution | Amneal Pharmaceuticals LLC |
| ANDA213561 | Atropine Sulfate | Injection | Medical Purchasing Solutions, LLC |
| NDA208151 | Isopto Atropine | Solution | Alcon Laboratories, Inc. |
| NDA021146 | Atropine Sulfate | Injection, solution | Hospira, Inc. |
| ANDA215969 | Atropine Sulfate | Solution | Medical Purchasing Solutions, LLC |

Available forms are injectable solutions and other solutions/drops. No oral or other chronic-use form appears in these records, and route compatibility with a migraine indication has not been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found. As a class, systemic anticholinergic effects (tachycardia, dry mouth, blurred vision, urinary retention, CNS effects) would limit chronic use for a condition like migraine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.56%), but there are no registered clinical trials and no human evidence for atropine in migraine. The literature is mostly rodent and ex vivo work on cholinergic mechanisms, plus one small observational report in a related headache disorder. This is a research question, not a candidate ready for development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank to support the mechanistic-link analysis
- Preclinical evidence that muscarinic antagonism (not activation) is beneficial in migraine models
- Assessment of route and formulation fit, since current US forms are injectable or ophthalmic and chronic systemic anticholinergic effects are limiting
- Review of the 3 migraine literature items not provided in this pack

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

