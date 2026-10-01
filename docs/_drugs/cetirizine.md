---
layout: default
title: Cetirizine
parent: High Evidence (L1-L2)
nav_order: 515
evidence_level: L2
indication_count: 6
---

# Cetirizine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **6** 
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

# Cetirizine: From a Marketed H1 Antihistamine to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation H1 antihistamine, marketed in the United States in multiple oral and liquid forms.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **3 clinical trials** and **18 publications** currently supporting this direction.
This is closer to confirming a known use than to a novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 authorizations (NDA and ANDA) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Based on the pharmacology assessment, cetirizine is a peripheral H1-receptor inverse agonist.

In urticaria, histamine released from mast cells drives wheals, flare and itch. Blocking H1 receptors targets this effector pathway directly, so the prediction is mechanistically consistent. It also matches current practice, since second-generation antihistamines are the first-line treatment for urticaria.

The US authorization records supplied contain no indication text, so the original labelled indication could not be confirmed from this data. This is a data-completeness issue, not a sign of implausible biology.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Pilot study of IV cetirizine 10 mg vs IV diphenhydramine 50 mg in acute urticaria. It tests feasibility for a larger Phase 3 trial and does not establish efficacy. This is the most directly relevant trial. |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomized double-blind trial of adding a short corticosteroid burst to conventional H1 antihistamine treatment. Cetirizine is at most background therapy. |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Effect of levocetirizine (the active enantiomer of cetirizine) on skin inflammatory mediators in dermatographism and chronic idiopathic urticaria. Mechanistic design, terminated early, weak support. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Reviews efficacy and safety of up-dosing second-generation antihistamines (up to 4× licensed dose) in chronic spontaneous urticaria. Guideline recommendations rest mainly on expert opinion. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine is a potent H1 antagonist with antiallergic properties. It lacks CNS depressant effects at 10 mg daily. Covers allergic rhinitis, pollen-induced asthma and chronic urticaria. |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Review | Drugs | Clinical trial results indicate cetirizine is effective and well tolerated in chronic idiopathic urticaria in adults. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Review | Allergy | Clinical studies with cetirizine in allergic rhinitis and chronic urticaria. No abstract available. |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Review | Drugs | Comparative review of second-generation antihistamines, including cetirizine, focusing on sedation and anticholinergic effects. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine and levocetirizine in allergic rhinitis and chronic idiopathic urticaria. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Reviews levocetirizine's pharmacology, safety and effectiveness in allergic rhinitis and chronic idiopathic urticaria. |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Review | Drugs | Non-sedating antihistamines are the mainstay of treatment for most patients with chronic idiopathic urticaria. |

---

## US Market Information

Of the 20 authorizations, the 5 main ones are listed below. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| NDA021621 | Zyrtec (Kenvue Brands LLC) | Chewable tablet |
| ANDA204226 | Children's Allergy Relief (Rite Aid Corporation) | Solution |
| ANDA077829 | Allergy Relief (Pioneer Life Sciences, LLC) | Tablet |
| ANDA078870 | Cetirizine Hydrochloride Oral Solution (Preferred Pharmaceuticals Inc.) | Solution |
| ANDA078343 | Cetirizine Hydrochloride (Dr. Reddy's Laboratories Inc.) | Film-coated tablet |

Other marketed forms include orally disintegrating tablet, syrup and capsule.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried source.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is well established and the drug is widely marketed. The only Phase 3-labelled trial is a small feasibility pilot (n=36), and the other trials are indirect. L2 therefore reflects a plausible, well-known use rather than confirmed efficacy from a completed Phase 3 RCT.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved-indication text for the US authorizations, to confirm the original indication
- Efficacy data from a completed randomized trial of cetirizine in urticaria (the current pilot cannot support this)

**Other predicted indications (for reference):**
- Cold urticaria: research question (L3). Histamine-mediated, but some patients are refractory and may need dose escalation or add-on therapy.
- Nasal cavity disease: hold (L4). The disease term is too broad, and the only trial is methodological.
- Acute laryngopharyngitis, rosacea conjunctivitis and recalcitrant atopic dermatitis: hold (L5). These rest on model prediction only, with no supporting trials or literature and weak mechanistic rationale.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

