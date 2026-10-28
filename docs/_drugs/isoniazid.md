---
layout: default
title: Isoniazid
parent: Model Prediction Only (L5)
nav_order: 814
evidence_level: L5
indication_count: 1
monitor_inn: "ISONIAZID"
predicted_indications: ["conjunctivitis"]
last_modified_at: 2026-10-14
description: "Isoniazid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Pulmonary tuberculosis"
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Isoniazid: From Pulmonary Tuberculosis to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Isoniazid is a long-established anti-tuberculosis drug, originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **Conjunctivitis**, but there are currently **0 registered clinical trials** and only **12 publications** (mostly case reports, reviews and older studies, several of them not directly about isoniazid treating conjunctivitis) behind this direction.
The evidence is weak and limited to tuberculosis-related eye disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| US Market Status | Marketed (valid licenses: 7 of 7) |
| Number of NDAs | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, isoniazid is an anti-mycobacterial agent that inhibits mycolic acid synthesis in the mycobacterial cell wall. Its efficacy in tuberculosis is well established.

The link to conjunctivitis is indirect and applies only to tuberculosis-related eye disease. Primary conjunctival tuberculosis is a true mycobacterial infection. Phlyctenular keratoconjunctivitis is a hypersensitivity reaction to mycobacterial antigens, often seen in people with tuberculosis infection or sensitization. In both cases, isoniazid would act on the underlying tuberculous process, not on conjunctivitis in general.

There is no evidence of benefit in common bacterial, viral or allergic conjunctivitis. The high TxGNN score (0.9936) is a computational prediction that is not backed by clinical trial data. It should be read as a hypothesis, not as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Cohort / field prophylaxis study | Am Rev Respir Dis | Isoniazid prophylaxis in phlyctenular keratoconjunctivitis among Eskimos in Alaska (no abstract available) |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Not classified | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 in children with primary tuberculosis, all tuberculin-positive |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Annales d'oculistique | Use of isoniazid in local treatment of ocular tuberculosis (no abstract available) |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva (no abstract available) |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report / series | Rev Rhum (Engl Ed) | Isoniazid used for refractory arthropathy after intravesical BCG therapy (not an eye indication) |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including drug-associated conjunctivitis (not about isoniazid as a treatment) |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Case report | Dtsch Med Wochenschr | BCG-associated reactive arthritis with conjunctivitis (not about isoniazid treating conjunctivitis) |

Several other retrieved publications (on toxic epidermal necrolysis, BCG-associated polyarthritis, and Munchausen syndrome by proxy) are not about isoniazid treatment of conjunctivitis and are omitted here.

## US Market Information

All seven authorizations are valid. No approved indication text is available for them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040090 | Isoniazid (Marlex Pharmaceuticals) | Tablet | Valid |
| ANDA080937 | Isoniazid (Aphena Pharma Solutions) | Tablet | Valid |
| ANDA088235 | Isoniazid (CMP Pharma) | Solution | Valid |
| ANDA080936 | Isoniazid (A-S Medication Solutions) | Tablet | Valid |
| ANDA081118 | Isoniazid (Chartwell RX) | Solution | Valid |

Two more cancelled authorizations are not shown: ANDA040648 (Sandoz, injection solution) and ANDA089776 (Chartwell RX, tablet).

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, acute liver failure, hepatitis, liver disease, gallbladder disease, porphyria (including inherited porphyria and porphyrin metabolism disease), diabetes mellitus, diabetic ketoacidosis, gout, peripheral neuropathy and other peripheral nervous system disease, substance abuse/dependence, and slow acetylator status.
- **Drug Interactions**: 100 interactions were found. The main ones listed are:
  - Moderate: acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, chlorpropamide, dapagliflozin (antidiabetic agents, which may reflect effects on blood glucose), as well as metronidazole, budesonide, alosetron, cholecalciferol, calcifediol, calcitriol and picosulfuric acid.
  - Minor: hydrocortisone, triamcinolone, dexamethasone and betamethasone.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score only. There are no registered clinical trials, and the literature is mostly old case reports and reviews limited to tuberculosis-related eye disease. Several retrieved papers are off-topic. Isoniazid is not expected to help common conjunctivitis. The drug is marketed in the US, with 7 of 7 licenses valid.

**To proceed, the following is needed:**
- Narrow the target indication to tuberculosis-associated ocular disease (e.g., phlyctenular keratoconjunctivitis, conjunctival tuberculosis) rather than conjunctivitis in general
- Manual review of the retrieved literature for relevance, and a search for controlled studies
- FDA package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Route compatibility assessment (systemic versus ocular delivery), since this is not yet defined
- Confirmation of current US market availability (7 of 7 licenses are valid)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

